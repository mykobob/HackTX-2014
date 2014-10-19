var LeapObject = {
	notification:null,

	isHorizontal:function (dx, dy, dz) {
		return Math.abs(dx) > .75;
	},

	getDirection:function(dx, dy, dz) {
		if(dy < -.8) {
			return "down";
		}
		else if(isHorizontal(dx, dy, dz)) {
			return dx > 0 ? "right" : "left";
		} else {
			return "invalid direction";
		}
	},

	runLeapMotion:function(notification) {
		var options = {enableGestures: true};
		var epsilon = .1;
		var time = performance.now();

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
		  				if(isHorizontal(dx, dy, dz)) {
		  					if(timeout != null) {
		  						clearTimeout(timeout);
		  						notification.innerHTML = "";
		  					}
		  				}
		  				else if (getDirection(dx, dy, dz) === "down") {
		  					clearTimeout(timeout);
		  					//notification.innerHTML = expanded_email;
		  				}
					}
				}
			}); 
		}
	}
};