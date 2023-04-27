/* Prevents a prompt from appearing if you refresh after entering values*/
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

// -----------------------------------------------------------------------------
// DataSocket
const tabName = JSON.parse(document.getElementById('tab-name').textContent);
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/csApp/'
    + tabName
    + '/'
);
//const YARD_WIDTH_M = 39
//const YARD_LENGTH_M = 47
const START_X_PX = X_START_PX
const START_Y_PX = Y_START_PX
// on receiving a json message from the back-end
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    // UPDATING VALUES COMING FROM ROVER/BACK-END
    document.getElementById('Z_coord').innerHTML = Math.round((data.z + Number.EPSILON) * 100) / 100
    document.getElementById('YAW_coord').innerHTML = Math.round((data.yaw + Number.EPSILON) * 100) / 100
    document.getElementById('linVel').innerHTML = Math.round((data.linVel + Number.EPSILON) * 100) / 100
    document.getElementById('angVel').innerHTML = Math.round((data.angVel + Number.EPSILON) * 100) / 100
    document.getElementById('distToGoal').innerHTML = Math.round((data.distance + Number.EPSILON) * 100) / 100

    // draw on nav map canvas (meters to navmap_size proportions)
    var width_meters = 47
    var height_meters = 39
    // ======== CODE FOR THE TRIANGLE ON THE MAP + THE PATH IT TOOK ========
    // html divs of x and y coordinates
    var x_coord_meters = document.getElementById('X_coord');
    var y_coord_meters = document.getElementById('Y_coord');
    // previous values before receiving update from back-end
    let x_prev = x_coord_meters.innerHTML;
    let y_prev = y_coord_meters.innerHTML;
    // new current coordinates received from back-end
    let x_next = Math.round((data.x + Number.EPSILON) * 100) / 100
    let y_next = Math.round((data.y + Number.EPSILON) * 100) / 100
    // update only if coordinates changed 
    //TODO yaw_prev != yaw_next
    if (x_prev != x_next || y_prev != y_next) {
        x_coord_meters.innerHTML = x_next
        y_coord_meters.innerHTML = y_next
        // ??????????? ASK EMMA
        posContext.clearRect(0, 0, width_map, height_map);
        posContext.fillStyle = 'rgba(0, 255, 0, 0.5)';

        // new yaw value from back-end
        let yaw = -(document.getElementById('YAW_coord').innerHTML) - Math.PI / 2;

        // transform the (x,y) coordinates from meters to distance in pixels (to display on screen)
        let x_px = START_X_PX - y_next * width_map / YARD_WIDTH_M;
        let y_px = START_Y_PX - x_next * height_map / YARD_LENGTH_M;
        posContext.beginPath();
        // ======= code of the triangle representing the rover on the map =======
        // the triangle is isosceles with two sides of length 15 and third side of length 10
        let p1 = [0, 0]
        let p2 = [0, 0]
        // top point of the triangle
        // here and later on, adding x_px and y_px is done to reposition the triangle correctly on the map (shifting)
        posContext.moveTo(15 * Math.cos(yaw) + x_px, 15 * Math.sin(yaw) + y_px);
        // p1 and p2 are the points of the two other angles of the triangle
        if (Math.abs(yaw) == Math.PI / 2) {
            p1 = [x_px - 5, y_px]
            p2 = [x_px + 5, y_px]
        } else {
            let tan = Math.round(Math.tan(yaw) * 100) / 100 // two decimal precision
            let factor = Math.round(5 / (Math.sqrt(tan * tan + 1)) * 100) / 100

            p1 = [factor * (-tan) + x_px, factor + y_px]
            p2 = [factor * tan + x_px, -factor + y_px]
        }
        // draw triangle 
        // JS draws two lines from the moveTo() method (see above) to the points p1 and p2 and then fills up the drawn object
        posContext.lineTo(p1[0], p1[1]);
        posContext.lineTo(p2[0], p2[1]);
        posContext.fill();
        // draw new segment of the path 
        pathContext.lineTo(x_px, y_px);
        pathContext.strokeStyle = "#008000";
        pathContext.stroke();
    }

    /*myContext.lineTo((x_coord_meters * width_map) / width_meters, (y_coord_meters * height_map) / height_meters); 
    myContext.strokeStyle = "#008000"; 
    myContext.stroke();*/
};
chatSocket.onclose = function (e) {
    console.log('Switched Tab');
};




////timer

const timeSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/csApp/'
    + 'time'
    + '/'
);

var time = 0;
var isrunning = false;

document.querySelector("#pause_button").addEventListener("click", event => {

    chatSocket.send(JSON.stringify({
        'launch': False,
        'duration': time
    }));

})

timeSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var launch = data.launch;
    var duration = data.duration;
    console.log(launch + "  " + duration);
    time = data.duration;
    if(launch){
        console.log("launch");
    }else{
        console.log("pause");
    }
};

////gamepad

let controllers = {};


function disconnecthandler(e) {
    removegamepad(e.gamepad);
  }

window.addEventListener("gamepadconnected", event => {
    controllers[event.gamepad.index] = event.gamepad;
    console.log("gamepad connected");
    });
window.addEventListener("gamepaddisconnected", event => {
    delete controllers[event.gamepad.index];
    console.log("gamepad disconnected");
    });

if (!haveEvents) {
 setInterval(scangamepads, 500);
}
