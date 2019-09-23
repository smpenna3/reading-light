var socket = io.connect('http://localhost:5000/led');

function on(){
    socket.emit('on', led);
}

function off(){
    socket.emit('off', led);
}