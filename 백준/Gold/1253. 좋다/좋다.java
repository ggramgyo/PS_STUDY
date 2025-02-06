import java.util.*;
import java.io.*;

public class Main {
    static int[] arr;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        String[] input = br.readLine().split(" ");
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(arr);

        int answer = 0;

        for (int i = 0; i < N; i++) {
            if (isGoodNumber(i)) {
                answer++;
            }
        }

        System.out.println(answer);
    }

    public static boolean isGoodNumber(int index) {
        int target = arr[index];
        int left = 0, right = N - 1;

        while (left < right) {
            if (left == index) { // 자기 자신 제외
                left++;
                continue;
            }
            if (right == index) { // 자기 자신 제외
                right--;
                continue;
            }

            int sum = arr[left] + arr[right];
            if (sum == target) return true;
            if (sum < target) left++;
            else right--;
        }
        return false;
    }
}
