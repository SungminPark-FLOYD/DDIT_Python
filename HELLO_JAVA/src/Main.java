import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		//3kg 봉지 5kg 봉지
		//n kg의 설탕을 배달해야할때 가장 적은 수의 봉지 개수 구하기
		//정확하게 n을 만들수 없으면 -1
		
		Scanner sc = new Scanner(System.in);
		int t = 0,f = 0,n = 0;
		n = sc.nextInt();
		
		f = n / 5;
		t = (n%5)/3;
		
		if((n%5)%3 != 0) System.out.println(-1);
		else System.out.println(f+t);
			

	}
}
