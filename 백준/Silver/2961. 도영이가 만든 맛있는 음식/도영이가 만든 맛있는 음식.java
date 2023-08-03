import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
	static int n;
    static int[][] li;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        li = new int[n][2];
        answer = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            li[i][0] = Integer.parseInt(st.nextToken());
            li[i][1] = Integer.parseInt(st.nextToken());
        }

        dfs(0, 1, 0);
        System.out.print(answer);
    }

    static void dfs(int i, int s, int b) {
        if (i > 0 && b > 0) {
            answer = Math.min(answer, Math.abs(s - b));
        }
        if (i >= n) {
            return;
        }
        dfs(i + 1, s * li[i][0], b + li[i][1]);
        dfs(i + 1, s, b);
    }
}
