import java.io.*;
import java.util.*;

public class Main {
	static int N, M, graph[][], distances[][];
	static List<int[]> chicken, house;
	static int answer = Integer.MAX_VALUE;
	static boolean[] selected;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		graph = new int[N][N];
		chicken = new ArrayList<>();
		house = new ArrayList<>();

		for (int x = 0; x < N; x++) {
			st = new StringTokenizer(br.readLine());
			for (int y = 0; y < N; y++) {
				graph[x][y] = Integer.parseInt(st.nextToken());
				if (graph[x][y] == 2) {
					chicken.add(new int[] { x, y });
				} else if (graph[x][y] == 1) {
					house.add(new int[] { x, y });
				}
			}
		}
		// 각 집에서 치킨집까지의 거리를 저장할 배열
		distances = new int[house.size()][chicken.size()];

		for (int i = 0; i < house.size(); i++) {
		    int[] h = house.get(i);
		    for (int j = 0; j < chicken.size(); j++) {
		        int[] c = chicken.get(j);
		        distances[i][j] = Math.abs(c[0] - h[0]) + Math.abs(c[1] - h[1]);
		    }
		}

		selected = new boolean[chicken.size()];
		combination(0, 0, selected);

		System.out.println(answer);
	}

	static void combination(int start, int count, boolean[] selected) {
	    if (count == M) {
	        int temp = 0;
	        for (int i = 0; i < house.size(); i++) {
	            int diff = Integer.MAX_VALUE;
	            for (int j = 0; j < selected.length; j++) {
	                if (selected[j]) {
	                    diff = Math.min(distances[i][j], diff);
	                }
	            }
	            temp += diff;
	        }
	        answer = Math.min(answer, temp);
	        return;
	    }

		for (int i = start; i < chicken.size(); i++) {
			selected[i] = true;
			combination(i + 1, count + 1, selected);
			selected[i] = false;
		}
	}
}

