import rclpy

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from custom_msg.srv import ChangeModeSystem
from custom_msg.action import DrillTerrain, HDManipulation, NAVReachGoal

from concurrent.futures import Future

channel_layer = get_channel_layer()

class Controller():
    '''
        Controller (Model View Controller (MVC) template)
    '''

    def __init__(self, cs):
        self.cs = cs

        self.nav_action = False
        self.drill_action = False
        self.hd_action = False
    
    # ===========================================================================
    # CHANGE MODE SYSTEM SERVICE   
    # ===========================================================================
    
    def send_request_system(self, system, mode, queue):
        while not self.cs.change_mode_system.wait_for_service(timeout_sec=1.0):
            self.cs.node.get_logger().info('Service ChangeModeSystem not available, waiting again...')

        self.cs.node.get_logger().info('Service ChangeModeSystem is available')            
        req = ChangeModeSystem.Request()
        req.system = system
        req.mode = mode
        
        future = self.cs.change_mode_system.call_async(req)
        future.add_done_callback(lambda f: self.service_callback(f, queue))
        return self.result_future
    
    def service_callback(self, future, result):
        try:
            response = future.result()
            result.put((response.systems_state, response.error_type, response.error_message))
                
        except Exception as e:
            result.put(("", 1, "exception {e}"))

    # ===========================================================================
    # HANDLING DEVICE MANIPULATION ACTION
    # ===========================================================================
    
    def send_handling_device_manipulation_goal(self, task_type, task_id):
        if not self.hd_action:

            goal = HDManipulation.Goal()
            
            goal.task_type = task_type
            goal.task_id = task_id
            
            self.cs.handling_device_manipulation.wait_for_server()

            self.hd_action = self.cs.handling_device_manipulation.send_goal_async(goal, feedback_callback=self.handling_device_manipulation_feedback)
            self.hd_action.add_done_callback(self.handling_device_manipulation_callback)
        
            # CHANGE WITH FUTURES LIKE WITH DRILL ACTION

        else:
            self.cs.node.get_logger("A HD action is already running")
        
    def handling_device_manipulation_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.cs.node.get_logger().info('Goal HD rejected')
            return ("goal rejected", 1, "the goal was rejected by the subsystem")

        self.cs.node.get_logger().info('Goal accepted for HD Manipulation')
        self.hd_action = True

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.handling_device_manipulation_result_callback)
        
    def handling_device_manipulation_result_callback(self, future):
        result = future.result().result

        result = result.result
        error_type = result.error_type
        error_message = result.error_message
        self.hd_action = False
        return (result, error_type, error_message)
    
    def handling_device_manipulation_feedback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.cs.node.get_logger().info(f"Feedback HDManipulation action: {feedback.current_status}, {feedback.warning_type}, {feedback.warning_message}")


    # ===========================================================================
    # NAVIGATION REACH ACTION
    # ===========================================================================

    def send_navigation_reach_goal(self, mode, goal):
        if not self.nav_action:

            goal_ = NAVReachGoal.Goal()
            
            goal_.mode = mode
            goal_.task_id = goal
            
            self.cs.navigation_reach.wait_for_server()

            self.nav_action = self.cs.navigation_reach.send_goal_async(goal_, feedback_callback=self.navigation_reach_feedback)
            self.nav_action.add_done_callback(self.navigation_reach_callback)
        
            # CHANGE WITH FUTURES LIKE WITH DRILL ACTION

        else:
            self.cs.node.get_logger("A NAV action is already running")
        
    def navigation_reach_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.cs.node.get_logger().info('Goal NAV rejected')
            return ("goal rejected", "", 1, "the goal was rejected by the subsystem")

        self.cs.node.get_logger().info('Goal accepted for Navigation Reach')
        self.nav_action = True

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.navigation_reach_result_callback)
        
    def navigation_reach_result_callback(self, future):
        result = future.result().result

        result = result.result
        final_pos = result.final_pos
        error_type = result.error_type
        error_message = result.error_message
        self.nav_action = False

        return (result, final_pos, error_type, error_message)
    
    def navigation_reach_feedback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.cs.node.get_logger().info(f"Feedback Navigation Reach action {feedback.current_status}, {feedback.current_pos}, {feedback.distance_to_goal}, {feedback.warning_type}, {feedback.warning_message}")

    # ===========================================================================
    # DRILL TERRAIN ACTION
    # ===========================================================================

    def send_drill_terrain_goal(self):
        if not self.drill_action:

            goal = DrillTerrain.Goal()
            self.cs.drill_terrain.wait_for_server()

            self.drill_action = self.cs.drill_terrain.send_goal_async(goal, feedback_callback=self.drill_terrain_feedback)
            self.drill_action.add_done_callback(self.drill_terrain_callback)
            self.future_drill = Future()
            return self.future_drill
        else:
            future = Future()
            future.set_result(("goal rejected", 1, "A DRILL action is already running"))
            return future
        
    def drill_terrain_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.cs.node.get_logger().info('Goal Drill rejected')
            self.future_drill.set_result(("goal rejected", 1, "the goal was rejected by the subsystem"))
            return

        self.cs.node.get_logger().info('Goal accepted for Drill')
        self.drill_action = True

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.drill_terrain_result_callback)
        
    def drill_terrain_result_callback(self, future):
        result = future.result().result

        result = result.result
        error_type = result.error_type
        error_message = result.error_message
        self.drill_action = False

        self.future_drill.set_result((result, error_type, error_message))
        #return (result, error_type, error_message)
    
    def drill_terrain_feedback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.cs.node.get_logger().info(f"Feedback Drill action: {feedback.current_status}, {feedback.warning_type}, {feedback.warning_message}")

    # ===========================================================================
    # ===========================================================================

    def rover_state(self, data):
        print(data.data)
        async_to_sync(channel_layer.group_send)("rover", {"type": "rover_message",
                                                            'rover_state': data.data
                                                            })
