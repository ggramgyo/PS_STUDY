import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
	static int N, M;
	static List<Integer> data = new ArrayList();
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		nm(1, 0);
	}

	private static void nm(int value, int count) {
		if (count == M) {
			for (Integer i : data) {
				System.out.print(i + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = value; i <= N; i++) {
			if (!data.contains(i)) {
				data.add(i);
				nm(i, count + 1);
				data.remove(data.size()-1);
			}
		}
	}

}
