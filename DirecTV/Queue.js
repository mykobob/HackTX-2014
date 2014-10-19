//code.stephenmorley.org
function Queue(){
	var a=[],b=0;
	isEmpty=true;
	this.getLength=function(){
		return a.length-b;
	};
	this.isEmpty=function(){
		return isEmpty;
	};
	this.enqueue=function(b){
		a.push(b);
		isEmpty = false;
	};
	this.dequeue=function(){
		if(0!=a.length){
			var c=a[b];
			2*++b>=a.length&&(a=a.slice(b),b=0);
			isEmpty = a.length == 0;
			return c;
		}
	};
	this.peek=function(){
		return 0<a.length?a[b]:void 0;
	}
};