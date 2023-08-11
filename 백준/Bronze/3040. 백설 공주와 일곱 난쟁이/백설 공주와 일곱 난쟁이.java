import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[] numbers;
    static int total;
    static List<Integer> pick = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 아홉 개의 정수 입력받기
        numbers = new int[9];
        for (int i = 0; i < 9; i++) {
            numbers[i] = Integer.parseInt(br.readLine());
        }
        total = 0;
        for (int num : numbers) {
            total += num;
        }

        bt(0, 0, 0, new ArrayList<>());
    }

    static void bt(int i, int value, int cur, List<Integer> pick) {
        if (value == 100 && pick.size() == 7) {
            StringBuilder sb = new StringBuilder();
            for (int p : pick) {
                sb.append(numbers[p]).append('\n');
            }
            System.out.print(sb.toString());
            return;
        }
        if (total - cur + value < 100) {
            return;
        }
        if (9 - i < 7 - pick.size()) {
            return;
        }
        if (i >= 9) {
            return;
        }

        pick.add(i);
        bt(i + 1, value + numbers[i], cur + numbers[i], new ArrayList<>(pick));
        pick.remove(pick.size() - 1);
        bt(i + 1, value, cur + numbers[i], new ArrayList<>(pick));
    }
}
