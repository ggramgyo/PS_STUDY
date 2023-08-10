import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
	static int[] cards;
	static int win;
	static ArrayList<Integer> opp;
	static boolean[] chk;
	static int[] li; 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int testcase = 1; testcase <= T; testcase++) {
            chk = new boolean[18];
            cards = new int[9];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 9; i++) {
                cards[i] = Integer.parseInt(st.nextToken());
                chk[cards[i] - 1] = true;
            }

            opp = new ArrayList<>();
            for (int i = 0; i < 18; i++) {
                if (!chk[i]) {
                    opp.add(i + 1);
                }
            }

            win = 0;
            li = new int[9];
            permuteAndCheck(0);

            sb.append("#").append(testcase).append(" ").append(362880 - win).append(" ").append(win).append("\n");
        }

        System.out.println(sb.toString());
    }

    public static void permuteAndCheck(int index) {
        if (index == 9) {
            if (check(li)) {
                win++;
            }
            return;
        }

        for (int i = 0; i < opp.size(); i++) {
            if (!chk[opp.get(i) - 1]) {
                li[index] = opp.get(i);
                chk[opp.get(i) - 1] = true;
                permuteAndCheck(index + 1);
                chk[opp.get(i) - 1] = false;
            }
        }
    }

    public static boolean check(int[] arr) {
        int a = 0, b = 0;
        for (int i = 0; i < 9; i++) {
            if (arr[i] > cards[i]) {
                b += arr[i] + cards[i];
            } else {
                a += arr[i] + cards[i];
            }
        }
        return a < b;
    }
}
