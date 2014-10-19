var output = document.getElementById("element");
var options = {enableGestures: true};
var epsilon = .1;

function isHorizontal(dx, dy, dz) {
  return Math.abs(dx) > .75;
}

function getDirection(dx, dy, dz) {
  if(dy < -.8) {
    return "down";
  }
  else if(isHorizontal(dx, dy, dz)) {
    return dx > 0 ? "right" : "left";
  } else {
    return "invalid direction";
  }
}

Leap.loop(options, function(frame) {
  // There exists some gestures
  if(frame.gestures.length > 0) {
    for (var i = frame.gestures.length - 1; i >= 0; i--) {
      var gesture = frame.gestures[i];
      var out = "";
      if(gesture.type === "swipe") {
        var dx = gesture.direction[0];
        var dy = gesture.direction[1];
        var dz = gesture.direction[2];
        out += dx + ", " + dy + ", " + dx;
        out = "<" + out + ">";
        // output.innerHTML = out;
        output.innerHTML = "";
        output.innerHTML += "going " + getDirection(dx, dy, dz);
      }
    };
  } else {
    console.log("no gestures exist");
  }
}); 