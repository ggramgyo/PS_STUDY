import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Solution
{
	    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        for (int testcase = 1; testcase <= T; testcase++) {
            int N = Integer.parseInt(br.readLine());
            int[][] graph = new int[N][N];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            ArrayList<int[]> result = new ArrayList<>();
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    int answer = Integer.MIN_VALUE;
                    ArrayDeque<int[]> q = new ArrayDeque<>();
                    q.offer(new int[]{x, y, 0});
                    while (!q.isEmpty()) {
                        int[] point = q.poll();
                        int sx = point[0];
                        int sy = point[1];
                        int value = point[2];
                        answer = Math.max(answer, value);
                        for (int i = 0; i < 4; i++) {
                            int nx = sx + dx[i];
                            int ny = sy + dy[i];
                            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                                if (graph[nx][ny] - graph[sx][sy] == 1) {
                                    q.offer(new int[]{nx, ny, value + 1});
                                }
                            }
                        }
                    }
                    result.add(new int[]{answer, graph[x][y]});
                }
            }

            Collections.sort(result, (a, b) -> {
                if (a[0] == b[0]) {
                    return Integer.compare(a[1], b[1]);
                }
                return Integer.compare(b[0], a[0]);
            });

            sb.append("#").append(testcase).append(" ").append(result.get(0)[1])
              .append(" ").append(result.get(0)[0] + 1).append("\n");
        }

        System.out.print(sb.toString());
    }
}