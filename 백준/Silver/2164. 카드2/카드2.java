import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        LinkedList<Integer> q = new LinkedList<>();
        for (int x = 1; x <= n; x++) {
            q.add(x);
        }

        while (q.size() > 1) {
            q.removeFirst();
            q.add(q.removeFirst());
        }

        for (int num : q) {
            System.out.print(num + " ");
        }
        System.out.println();
        sc.close();
    }
}
