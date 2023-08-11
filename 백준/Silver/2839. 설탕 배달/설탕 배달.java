import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	static int sugar, cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        sugar = Integer.parseInt(st.nextToken());
        cnt = 0;

        while (sugar >= 0) {
            if (sugar % 5 == 0) {
                cnt += sugar / 5;
                System.out.println(cnt);
                break;
            }
            sugar -= 3;
            cnt++;
        }

        if (sugar < 0) {
            System.out.println(-1);
        }
    }
}
