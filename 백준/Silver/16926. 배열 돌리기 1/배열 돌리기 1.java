import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int r = 0; r < R; r++) {
            boolean[][] chk = new boolean[N][M];
            for (int start = 0; start < Math.min(N, M); start++) {
                if (!chk[start][start]) {
                    chk[start][start] = true;
                    rotate(start, start, 0, graph[start][start], graph, chk);
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(graph[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }

    static void rotate(int x, int y, int direction, int temp, int[][] graph, boolean[][] chk) {
        while (direction < 4) {
            x += dx[direction];
            y += dy[direction];
            if (0 <= x && x < graph.length && 0 <= y && y < graph[0].length) {
                if (!chk[x][y]) {
                    int next_temp = graph[x][y];
                    graph[x][y] = temp;
                    temp = next_temp;
                    chk[x][y] = true;
                } else {
                    x -= dx[direction];
                    y -= dy[direction];
                    direction++;
                }
            } else {
                x -= dx[direction];
                y -= dy[direction];
                direction++;
            }
        }
        graph[x + dx[direction - 1]][y + dy[direction - 1]] = temp;
    }
}
