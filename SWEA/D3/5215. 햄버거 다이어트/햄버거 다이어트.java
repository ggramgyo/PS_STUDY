import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static int N, L;
    static int[][] k;
    static int answer, maximum;

    public static void bt(int i, int taste, int calorie, int cur) {
        // 종료조건 1
        if (calorie > L) {
            return;
        }
        // 종료조건 2
        if (taste + maximum - cur < answer) {
            return;
        }
        // 종료조건 3
        if (i >= N) {
            answer = Math.max(answer, taste);
            return;
        }
        bt(i + 1, taste + k[i][0], calorie + k[i][1], cur + k[i][0]);
        bt(i + 1, taste, calorie, cur + k[i][0]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int testcase = 1; testcase <= T; testcase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());
            answer = Integer.MIN_VALUE;
            k = new int[N][2];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                k[i][0] = Integer.parseInt(st.nextToken());
                k[i][1] = Integer.parseInt(st.nextToken());
            }

            maximum = 0;
            for (int i = 0; i < N; i++) {
                maximum += k[i][0];
            }

            bt(0, 0, 0, 0);
            System.out.println("#" + testcase + " " + answer);
        }
    }
}
