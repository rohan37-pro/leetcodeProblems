/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
   this.stack = [];
   this.size = maxSize
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    var n = this.stack.length
    if (this.size > n){
        this.stack.push(x)
    }
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    var n = this.stack.length
    if (n==0){
        return -1
    }
    return this.stack.pop()
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    var n = this.stack.length
    if (k>n){
        k = n
    }
    for (let index = 0; index < k; index++) {
        this.stack[index] += val
    }
};

/** 
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */