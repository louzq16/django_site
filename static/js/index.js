//----------//
/*The QR code display */
// if(...){
// document.getElementById("code").value="";
//}

var imagesource = "http://" + window.location.hostname + ":8000/camera/test1/?id=1";
document.getElementById('imagesource').src = imagesource;
/*set the image source for clicked camera button  */
document.getElementById("camera_1").addEventListener('click', function () {
    var imagesource = "http://" + window.location.hostname + ":8000/camera/test1/?id=1";
    document.getElementById('imagesource').src=imagesource;
});
document.getElementById("camera_2").addEventListener('click', function () {
    var imagesource = "http://" + window.location.hostname + ":8000/camera/test2/?id=2";
    document.getElementById('imagesource').src=imagesource;
});
document.getElementById("camera_3").addEventListener('click', function () {
    var imagesource = "http://" + window.location.hostname + ":8000/camera/test3/?id=3";
    document.getElementById('imagesource').src=imagesource;
});
document.getElementById("camera_4").addEventListener('click', function () {
    var imagesource = "http://" + window.location.hostname + ":8000/camera/test4/?id=4";
    document.getElementById('imagesource').src=imagesource;
});
//------------//
var draw = document.getElementById("draws");
var two = new Two({
    width: 400,
    height: 500
}).appendTo(draw);
var offset = Two.Vector(0, 0);
var circle = two.makeCircle(200, 200, 10);
circle.fill = "#ff0"
var circle2 = two.makeCircle(200, 200, 10);
var x = document.getElementById("test");
two.update(); //document.getElementById("test").innerHTML="fsfs";
socket = new WebSocket("ws://" + window.location.hostname + ":8888/chat/");
socket.onmessage = function (e) {
    var data = JSON.parse(e.data)
    var x = data.quaposi[0]
    var y = data.quaposi[1]
    circle.translation.set(200 + x, 200 + y)
    two.update()
    x.innerHTML = data.quaposi[0].toFixed(2); //data.quaposi[0].toFixed(2);
    socket.send("ok"); //window.setTimeout(socket.onopen,100);
}
socket.onopen = function () {
    socket.send("ok");
}
if (socket.readyState == WebSocket.OPEN) socket.onopen();

