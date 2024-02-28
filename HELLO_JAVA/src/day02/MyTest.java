package day02;

import java.util.Scanner;

public class MyTest {
	public static void main(String[] args) {
		//첫수를 입력하시오 4
		//끝수를 입력하시오 5
		//4와 5의 합은 9입니다
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("첫수를 입력하시오");
		int f = sc.nextInt();
		System.out.println("끝수를 입력하시오");
		int l = sc.nextInt();
		
		System.out.println(f + "와 " + l + "의 합은 " + (f+l) + "입니다" );
		
		
	}
}
