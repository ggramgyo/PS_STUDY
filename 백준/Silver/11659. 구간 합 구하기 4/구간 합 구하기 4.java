import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N];
		int[] dp = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
			if (i >= 1)
				dp[i] = arr[i] + dp[i - 1];
			else
				dp[i] = arr[i];
		}

		for (int i = 0; i < M; i++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			System.out.println(dp[end - 1] - dp[start - 1] + arr[start - 1]);
		}

	}

}
