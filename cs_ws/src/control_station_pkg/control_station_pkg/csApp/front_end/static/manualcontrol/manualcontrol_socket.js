const tabName = JSON.parse(document.getElementById('tab-name').textContent);

// ----------------------------------------------------------------------
// Data
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/csApp/'
    + tabName
    + '/'
);

// on receiving json message from back-end
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    console.log("debug")
    // update x and y coordinates + linear and angular velocities
    document.getElementById('X_coord').innerHTML = Math.round((data.x + Number.EPSILON) * 100) / 100
    document.getElementById('Y_coord').innerHTML = Math.round((data.y + Number.EPSILON) * 100) / 100
    document.getElementById('linVel').innerHTML = Math.round((data.linVel + Number.EPSILON) * 100) / 100
    document.getElementById('angVel').innerHTML = Math.round((data.angVel + Number.EPSILON) * 100) / 100

    // update hd mode
    document.getElementById('hd_man_mode').innerHTML = data.hd_mode

    /* display joint velocities */
    let velocities = document.querySelectorAll('#joint1_vel, #joint2_vel, #joint3_vel, #joint4_vel, #joint5_vel, #joint6_vel, #joint7_vel');
    let j = 0;
    velocities.forEach(vel => {
        document.getElementById(vel.id).innerHTML = Math.round((data.joint_vel[j] + Number.EPSILON) * 100) / 100;
        j += 1;
    })

    /* display joint coordinates */
    let coordinates = document.querySelectorAll('#joint1_coord, #joint2_coord, #joint3_coord, #joint4_coord, #joint5_coord, #joint6_coord, #joint7_coord');
    let i = 0;
    coordinates.forEach(coord => {
        document.getElementById(coord.id).innerHTML = (Math.round((data.joint_pos[i] + Number.EPSILON) * 180 / Math.PI * 100) / 100);
        i += 1;

    })

    /* sliders to illustrate the joints' angle openings*/
    let sliders = document.querySelectorAll('#joint1_slider, #joint2_slider, #joint3_slider, #joint4_slider, #joint5_slider, #joint6_slider');
    let f = 0;
    sliders.forEach(slider => {
        document.getElementById(slider.id).value = (Math.round((data.joint_pos[f] + Number.EPSILON) * 180 / Math.PI * 100) / 100);
        f += 1;
    })

};

chatSocket.onclose = function (e) {
    console.log('Switched Tab');
};

// --------------------------------------------------------------------------
// Cameras
let ws = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/cameras/'
    + 'video6/'
    // + 'wms'
    // + '/'
);

let ws2 = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/cameras/'
    + 'video2/'
    // + 'wms'
    // + '/'
);
let ws3 = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/cameras/'
    + 'video/'
    // + 'wms'
    // + '/'
);


ws.onmessage = function (evt) {
    v_data = JSON.parse(evt.data);
    // $("#camera_1").attr("src", v_data.message);
    document.getElementById('camera_1').src = v_data.message;



};

ws2.onmessage = function (evt) {
    v_data = JSON.parse(evt.data);
    document.getElementById('camera_2').src = v_data.message;



};
ws3.onmessage = function (evt) {
    v_data = JSON.parse(evt.data);
    document.getElementById('camera_3').src = v_data.message;



};

ws.onclose = function (evt) {
    console.log("Connection closed.");
};

const timeSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/csApp/'
    + 'time'
    + '/'
);

timeSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    console.log("debug timer");
    var time = `${data.hor} : ${data.min} : ${data.sec}`;
    document.getElementById('elapsed').innerHTML = time;

};