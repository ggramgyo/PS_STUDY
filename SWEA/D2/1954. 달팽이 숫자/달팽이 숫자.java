import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static boolean[][] chk;
	static int n;
	static int[][] result;
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for (int testcase = 1; testcase <= T; testcase++) {
			n = sc.nextInt();
			chk = new boolean[n][n];
			result = new int[n][n];
			result[0][0] = 1;
			chk[0][0] = true;
			dfs(0, 0, 1, 0);
			System.out.println("#" + testcase);
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					System.out.print(result[i][j] + " ");
				}
				System.out.println();
			}
		}
	}

	private static void dfs(int x, int y, int value, int dir) {
		// TODO Auto-generated method stub
		if(value >= Math.pow(n, 2))	return;
		int nx = x + dx[dir];
		int ny = y + dy[dir];
		if(0 > nx || n <= nx || 0 > ny || n <= ny || chk[nx][ny]) {
			dir = (dir + 1) % 4;
			dfs(x, y, value, dir);
		}
		else {
			result[nx][ny] = value+1;
			chk[nx][ny] = true;
			dfs(nx, ny, value+1, dir);
		}
	}
}