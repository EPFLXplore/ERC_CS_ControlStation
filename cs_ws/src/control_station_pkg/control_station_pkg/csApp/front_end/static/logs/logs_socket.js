const tabName = JSON.parse(document.getElementById('tab-name').textContent);
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/CS2022/'
    + tabName
    + '/'
);


chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data)
    //console.log("debug")

    document.getElementById("dialog").value = data.exceptions.join("\n - ")


};

// chatSocket.onclose = function(e) {
// 	console.log('Switched Tab');
// };

// // -----------------------------------------------------------------------------
// // TimeSocket
const timeSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/CS2022/'
    + 'time'
    + '/'
);

timeSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    console.log("debug timer");
    var time = `${data.hor} : ${data.min} : ${data.sec}`;
    document.getElementById('elapsed').innerHTML = time;

};