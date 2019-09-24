var socket = io.connect(location.origin + '/led');

document.getElementById("on").onclick = function on(){
    socket.emit('on');
    console.log("On command sent");
}

document.getElementById("off").onclick = function off(){
    socket.emit('off');
    console.log("Off command sent");
}

document.getElementById("submit").onclick = function rgb(){
    red = document.getElementById("red").value;
    green = document.getElementById("green").value;
    blue = document.getElementById("blue").value;
    socket.emit('rgb', {'red':red,'green':green,'blue':blue});
}
