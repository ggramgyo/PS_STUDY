import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        boolean[][] graph = new boolean[100][100];
        int answer = 0;

        for (int k = 0; k < N; k++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            for (int i = x - 1; i < x + 9; i++) {
                for (int j = y - 1; j < y + 9; j++) {
                    if (!graph[i][j]) {
                        graph[i][j] = true;
                        answer++;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
