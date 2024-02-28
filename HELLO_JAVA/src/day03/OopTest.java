package day03;

public class OopTest {
	public static void main(String[] args) {
		Human ani = new Human();
		System.out.println("X :" + ani.x);
		System.out.println("Y :" + ani.y);
		System.out.println("skill_cook :" + ani.skill_cook);
		
		ani.moveX(3);
		ani.moveY(-5);
		ani.element();
		System.out.println("X :" + ani.x);
		System.out.println("Y :" + ani.y);
		System.out.println("skill_cook :" + ani.skill_cook);
	}
	
}
