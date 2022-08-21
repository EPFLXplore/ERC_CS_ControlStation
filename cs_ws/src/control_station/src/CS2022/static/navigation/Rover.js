// Wheels
var canvas = document.getElementById("W1");
var canvas2 = document.getElementById("W2");
var canvas3 = document.getElementById("W3");
var canvas4 = document.getElementById("W4");
//Wheels

//Rover's Body
var Body = document.getElementById("Body");

//Rover's body


var ctx = canvas.getContext("2d");
var ctx2 = canvas2.getContext("2d");
var ctx3 = canvas3.getContext("2d");
var ctx4 = canvas4.getContext("2d");

var BodyContext = Body.getContext("2d");




var Input1 = document.getElementById("input1");
var Input2 = document.getElementById("input2");
var Input3 = document.getElementById("input3");
var Input4 = document.getElementById("input4");
var SButton = document.getElementById("SUB");



ctx.fillStyle = "#ffffff";
ctx2.fillStyle = "#ffffff";
ctx3.fillStyle = "#ffffff";
ctx4.fillStyle ="#ffffff";

BodyContext.fillStyle = "#0016db";






//Wheels
ctx.fillRect(0, 0, canvas.width, canvas.height)
ctx2.fillRect(0, 0, canvas2.width, canvas2.height);
ctx3.fillRect(0, 0, canvas3.width, canvas3.height)
ctx4.fillRect(0,0,canvas4.width, canvas4.height);
//Wheels

//Rover
BodyContext.lineWidth = 8;
BodyContext.strokeStyle = "blue";
BodyContext.beginPath();
BodyContext.rect(57,60,Body.width-113, Body.height-110);
BodyContext.rotate(-7.606*Math.PI/180);
BodyContext.lineWidth = 6;

// first arm

BodyContext.moveTo(40,140);
BodyContext.lineTo(0,0);
// first arm

//second arm
BodyContext.moveTo(40,140);
BodyContext.lineTo(-33,265)
// second arm

//third arm
BodyContext.moveTo(220,160);
BodyContext.lineTo(315,0);
//third arm


//fourth arm
BodyContext.moveTo(220,160);
BodyContext.lineTo(335,700);
//fourth arm

//top square
BodyContext.rotate(7.606*Math.PI/180);
BodyContext.rect(130,30,30,30);
// top square

// bottom circle

BodyContext.moveTo(158,220);
BodyContext.arc(143, 244, 25, 0, 2 * Math.PI);
//bottom circle


BodyContext.stroke();
// Rover




// BodyContext.clearRect(0,0,Body.width, Body.height);

// Event listener
SButton.onclick = function() {


canvas.style.transform = "rotate("+ String(Input1.value) +"deg)";
canvas2.style.transform = "rotate("+ String(Input2.value) +"deg)";
canvas3.style.transform = "rotate("+ String(Input3.value) +"deg)";
canvas4.style.transform = "rotate("+ String(Input4.value) +"deg)";

}
// Event listener



