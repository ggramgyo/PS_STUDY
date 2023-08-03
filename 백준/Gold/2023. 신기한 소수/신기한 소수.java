import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int start : new int[]{2, 3, 5, 7}) {
            bt(start);
        }
    }

    static boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    static void bt(int num) {
        if (String.valueOf(num).length() == N) {
            System.out.println(num);
        }

        for (int i = 1; i < 10; i+=2) {
            int temp = num * 10 + i;
            if (isPrime(temp)) {
                bt(temp);
            }
        }
    }
}