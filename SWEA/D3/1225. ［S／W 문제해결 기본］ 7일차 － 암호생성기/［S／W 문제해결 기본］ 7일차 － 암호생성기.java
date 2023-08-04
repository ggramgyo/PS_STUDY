import java.util.Scanner;
import java.io.FileInputStream;
import java.util.ArrayDeque;

class Solution
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int testcase = 1; testcase <= 10; testcase++) {
            int n = sc.nextInt();
            int[] arr = new int[8];
            int[] result = new int[8];
            for (int i = 0; i < 8; i++) {
                arr[i] = sc.nextInt();
            }
            int count = 0;
            int index = 0;
            int value = 1;
            while (true) {
                if (arr[index] - value <= 0) {
                    arr[index] = 0;
                    break;
                } else {
                    arr[index] -= value;
                }
                index = (index + 1) % 8;
                value = (value + 1) % 6;
                if (value == 0) {
                    value++;
                }
                count++;
            }
            int remain = count % 8;

            System.out.print("#" + testcase + " ");
            for (int i = (remain + 1) % 8; i < 8; i++) {
                System.out.print(arr[i] + " ");
            }
            for (int i = 0; i <= remain % 8; i++) {
                System.out.print(arr[i] + " ");
            }

            System.out.println();
        }
    }
}