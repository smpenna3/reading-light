var socket = io.connect(location.origin + '/led');

document.getElementById("on").onclick = function on(){
    socket.emit('on');
    console.log("On command sent");
}

document.getElementById("off").onclick = function off(){
    socket.emit('off');
    console.log("Off command sent");
}