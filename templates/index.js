//----------//
/*The QR code display */
// if(...){
// document.getElementById("code").value="";
//}

var imagesource = "http://" + window.location.hostname + ":8000/camera/test/";

/*set the image source for clicked camera button  */
document.getElementById("camera_1").addEventListener('click', function () {
    // document.getElementById('imagesource').src = imagesource;
});
document.getElementById("camera_2").addEventListener('click', function () {
    // document.getElementById('imagesource').src = imagesource;

});
document.getElementById("camera_3").addEventListener('click', function () {
    // document.getElementById('imagesource').src = imagesource;

});
document.getElementById("camera_4").addEventListener('click', function () {
    // document.getElementById('imagesource').src = imagesource;

});
//------------//
var draw = document.getElementById("draws");
var two = new Two({
    width: 400,
    height: 500
}).appendTo(draw);
var offset = Two.Vector(0, 0);
//offset.set(2,4);
var circle = two.makeCircle(200, 200, 10);
circle.fill = "#ff0"
var circle2 = two.makeCircle(200, 200, 10);
//circle.translation.set(100,100)
var x = document.getElementById("test");
alert(JSON.stringify(circle.translation))
two.update(); //document.getElementById("test").innerHTML="fsfs";
socket = new WebSocket("ws://" + window.location.hostname + ":8888/chat/");
socket.onmessage = function (e) {
    //var data=JSON.parse(e.data.text)
    //alert(data.quaposi[0]);
    //alert(e.data)
    var data = JSON.parse(e.data)
    var x = data.quaposi[0]
    var y = data.quaposi[1]
    //x.innerText="wanna"
    //alert(e.data)
    circle.translation.set(200 + x, 200 + y)
    two.update()
    x.innerHTML = data.quaposi[0].toFixed(2); //data.quaposi[0].toFixed(2);
    socket.send("ok"); //window.setTimeout(socket.onopen,100);
}
socket.onopen = function () {
    socket.send("ok");
}
if (socket.readyState == WebSocket.OPEN) socket.onopen();

