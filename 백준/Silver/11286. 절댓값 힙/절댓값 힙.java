import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) {
                return -Integer.compare(b[1], a[1]);
            } else {
                return -Integer.compare(b[0], a[0]);
            }
        });
        int numQueries = Integer.parseInt(br.readLine());

        for (int i = 0; i < numQueries; i++) {
            int target = Integer.parseInt(br.readLine());

            if (target != 0) {
                heap.offer(new int[]{Math.abs(target), target});
            } else {
                try {
                    sb.append(heap.poll()[1]).append("\n");
                } catch (NullPointerException e) {
                    sb.append("0\n");
                }
            }
        }

        System.out.print(sb.toString());
    }
}
