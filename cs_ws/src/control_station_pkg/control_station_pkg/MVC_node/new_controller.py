import rclpy

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from custom_msg.srv import ChangeModeSystem
from custom_msg.action import DrillTerrain, HDManipulation, NAVReachGoal

channel_layer = get_channel_layer()

class Controller():
    '''
        Controller (Model View Controller (MVC) template)
    '''

    def __init__(self, cs):
        self.cs = cs
    
    # ===========================================================================
    # CHANGE MODE SYSTEM SERVICE   
    # ===========================================================================
    
    def send_request_system(self, system, mode):
        while not self.cs.change_mode_system.wait_for_service(timeout_sec=1.0):
            self.cs.node.get_logger().info('Service ChangeModeSystem not available, waiting again...')

        self.cs.node.get_logger().info('Service ChangeModeSystem is available')            
        req = ChangeModeSystem.Request()
        req.system = system
        req.mode = mode
        
        future = self.cs.change_mode_system.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        result = future.result()
        
        return (result.systems_state, result.error_type, result.error_message)
    
    # ===========================================================================
    # HANDLING DEVICE MANIPULATION ACTION
    # ===========================================================================
    
    def send_handling_device_manipulation_goal(self, task_type, task_id):
        goal = HDManipulation.Goal()
        
        goal.task_type = task_type
        goal.task_id = task_id
        
        self.cs.handling_device_manipulation.wait_for_server()

        future = self.cs.handling_device_manipulation.send_goal_async(goal, feedback_callback=self.handling_device_manipulation_feedback)
        future.add_done_callback(self.handling_device_manipulation_callback)
        
    def handling_device_manipulation_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.cs.node.get_logger().info('Goal HD rejected')
            return

        self.cs.node.get_logger().info('Goal accepted for HD Manipulation')

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.handling_device_manipulation_result_callback)
        
    def handling_device_manipulation_result_callback(self, future):
        result = future.result().result

        result = result.result
        error_type = result.error_type
        error_message = result.error_message

        return (result, error_type, error_message)
    
    def handling_device_manipulation_feedback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.cs.node.get_logger().info(f"Feedback HDManipulation action: {feedback.current_status}, {feedback.warning_type}, {feedback.warning_message}")


    # ===========================================================================
    # NAVIGATION REACH ACTION
    # ===========================================================================

    def send_navigation_reach_goal(self, mode, goal):
        goal = NAVReachGoal.Goal()
        
        goal.mode = mode
        goal.task_id = goal
        
        self.cs.navigation_reach.wait_for_server()

        future = self.cs.navigation_reach.send_goal_async(goal, feedback_callback=self.navigation_reach_feedback)
        future.add_done_callback(self.navigation_reach_callback)
        
    def navigation_reach_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.cs.node.get_logger().info('Goal NAV rejected')
            return

        self.cs.node.get_logger().info('Goal accepted for Navigation Reach')

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.navigation_reach_result_callback)
        
    def navigation_reach_result_callback(self, future):
        result = future.result().result

        result = result.result
        final_pos = result.final_pos
        error_type = result.error_type
        error_message = result.error_message

        return (result, final_pos, error_type, error_message)
    
    def navigation_reach_feedback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.cs.node.get_logger().info(f"Feedback Navigation Reach action {feedback.current_status}, {feedback.current_pos}, {feedback.distance_to_goal}, {feedback.warning_type}, {feedback.warning_message}")

    # ===========================================================================
    # DRILL TERRAIN ACTION
    # ===========================================================================

    def send_drill_terrain_goal(self):
        goal = DrillTerrain.Goal()
                
        self.cs.drill_terrain.wait_for_server()

        future = self.cs.drill_terrain.send_goal_async(goal, feedback_callback=self.drill_terrain_feedback)
        future.add_done_callback(self.drill_terrain_callback)
        
    def drill_terrain_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.cs.node.get_logger().info('Goal Drill rejected')
            return

        self.cs.node.get_logger().info('Goal accepted for Drill')

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.drill_terrain_result_callback)
        
    def drill_terrain_result_callback(self, future):
        result = future.result().result

        result = result.result
        error_type = result.error_type
        error_message = result.error_message

        return (result, error_type, error_message)
    
    def drill_terrain_feedback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.cs.node.get_logger().info(f"Feedback Drill action: {feedback.current_status}, {feedback.warning_type}, {feedback.warning_message}")


    # ===========================================================================
    # ===========================================================================

    def rover_state(self, data):
        async_to_sync(channel_layer.group_send)("rover", {"type": "rover_message",
                                                            'rover_state': data.data
                                                            })
