package day03;

public class Animal {
	int x = 0;
	int y = 0;
	
	void moveX(int x) {
		this.x += x; 
	}
	void moveY(int y) {
		this.y += y; 
	}
	
	public static void main(String[] args) {
		Animal ani = new Animal();
		System.out.println(ani.x);
		System.out.println(ani.y);
		
		ani.moveX(5);
		ani.moveY(-3);
		
		System.out.println(ani.x);
		System.out.println(ani.y);
	}
}
