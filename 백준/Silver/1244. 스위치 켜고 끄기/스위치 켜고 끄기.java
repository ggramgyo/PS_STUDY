import java.util.Scanner;

public class Main {
    public static void change(int[] switchArr, int num) {
        if (switchArr[num] == 0) {
            switchArr[num] = 1;
        } else {
            switchArr[num] = 0;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] switchArr = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            switchArr[i] = scanner.nextInt();
        }

        int students = scanner.nextInt();
        for (int s = 0; s < students; s++) {
            int sx = scanner.nextInt();
            int num = scanner.nextInt();

            // 남자
            if (sx == 1) {
                for (int i = num; i <= N; i += num) {
                    change(switchArr, i);
                }
            }
            // 여자
            else {
                change(switchArr, num);
                for (int k = 1; k <= N / 2; k++) {
                    if (num + k > N || num - k < 1) break;
                    if (switchArr[num + k] == switchArr[num - k]) {
                        change(switchArr, num + k);
                        change(switchArr, num - k);
                    } else {
                        break;
                    }
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.print(switchArr[i] + " ");
            if (i % 20 == 0) {
                System.out.println();
            }
        }
    }
}
