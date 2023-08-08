import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int testcase = 1; testcase <= 10; testcase++) {
            int N = Integer.parseInt(br.readLine());
            boolean flag = true;

            for (int i = 0; i < N; i++) {
                String[] query = br.readLine().split(" ");
                if (query.length == 2) {
                    String value = query[1];
                    if (value.equals("+") || value.equals("-") || value.equals("*") || value.equals("/")) {
                        flag = false;
                    }
                } else {
                    String value = query[1];
                    if (value.equals("+") && value.equals("-") && value.equals("*") && value.equals("/")) {
                        flag = false;
                    }
                }
            }

            System.out.println("#" + testcase + " " + (flag ? 1 : 0));
        }
    }
}
