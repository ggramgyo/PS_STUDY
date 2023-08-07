import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] tops = new int[N];
        String[] input = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            tops[i] = Integer.parseInt(input[i]);
        }

        Stack<int[]> stack = new Stack<>();
        int[] answer = new int[N];

        for (int ix = N - 1; ix >= 0; ix--) {
            int target = tops[ix];
            if (stack.isEmpty() || stack.peek()[0] > target) {
                stack.push(new int[]{target, ix});
            } else {
                while (!stack.isEmpty() && stack.peek()[0] < target) {
                    int[] temp = stack.pop();
                    answer[temp[1]] = ix + 1;
                }
                stack.push(new int[]{target, ix});
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int a : answer) {
            sb.append(a).append(" ");
        }
        System.out.println(sb.toString());
    }
}
