package day02;

import java.util.Scanner;

public class MyHoll {
	public static void main(String[] args) {
		//홀짝 선택 홀
		//나 : 홀
		//컴 : 홀
		//결과 : 이김
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("홀, 짝을 선택하시오");
		String user = sc.next();
		String com;
		double ran = Math.random();
		if(ran > 0.5) com = "홀";
		else com = "짝";
		
		System.out.println("유저 : " + user);
		System.out.println("컴퓨터 : " + com);
		
		if(user.equals(com)) {
			System.out.println("결과 : 유저 승");
		}
		else System.out.println("결과 : 컴퓨터 승");
		
	}
}
