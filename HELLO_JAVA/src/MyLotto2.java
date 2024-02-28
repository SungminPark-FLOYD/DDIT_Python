

public class MyLotto2 {
	public static void main(String[] args) {
		int arr[] = new int[6];
	
		
		for(int i = 0; i < arr.length; i++) {
			int ran = (int)((Math.random()*45)+1);
			arr[i] = ran;
			for(int j = 0; j < i; j++) {
				if(arr[i] == arr[j]) {
					i--;
					break;
				}
			}
			System.out.print(arr[i] + " ");
		}
		
		System.out.println();
		
		int[] aa = {
				1,2,3,4,5, 6,7,8,9,10,
				11,12,13,14,15, 16,17,18,19,20,
				21,22,23,24,25, 26,27,28,29,30,
				31,32,33,34,35, 36,37,38,39,40,
				41,42,43,44,45
		};
		
		for(int i = 0; i < 1000; i++) {
			int ran = (int)(Math.random()*45);
			int a = aa[0];
			aa[0] = aa[ran];
			aa[ran] = a;
		}
		System.out.print(aa[0] + " ");
		System.out.print(aa[1] + " ");
		System.out.print(aa[2] + " ");
		System.out.print(aa[3] + " ");
		System.out.print(aa[4] + " ");
		System.out.print(aa[5] + " ");
		
		
		
		
		
	}
}
