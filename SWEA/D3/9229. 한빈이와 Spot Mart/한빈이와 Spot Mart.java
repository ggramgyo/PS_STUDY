import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int testcase = 1; testcase <= T; testcase++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[] bags = new int[N];
            for (int i = 0; i < N; i++) {
                bags[i] = sc.nextInt();
            }
            int answer = -1;

            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    int s = bags[i] + bags[j];
                    if (s <= M) {
                        answer = Math.max(answer, s);
                    }
                }
            }

            System.out.println("#" + testcase + " " + answer);
        }
    }
}
