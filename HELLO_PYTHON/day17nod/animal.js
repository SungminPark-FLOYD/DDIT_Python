class Animal {
	constructor () {
        this.x = 0;
        this.y = 0;
    }
    
    moveX(x) {
		this.x += x;
	}
	moveY(y) {
		this.y += y; 
	}
}

module.exports = Animal;
	if (require.main === module) {
		let ani = new Animal();
		console.log(ani)
		
		
		ani.moveX(5);
		ani.moveY(-3);
		
		console.log(ani)
	}


