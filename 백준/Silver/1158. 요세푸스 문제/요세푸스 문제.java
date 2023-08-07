import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        List<String> arr = new ArrayList<>();
        for (int x = 1; x <= n; x++) {
            arr.add(String.valueOf(x));
        }
        List<String> res = new ArrayList<>();
        int index = m - 1;
        for (int i = 0; i < n; i++) {
            res.add(arr.remove(index));
            if (!arr.isEmpty()) {
                index = (index + m - 1) % arr.size();
            }
        }
        System.out.print("<" + String.join(", ", res) + ">");
    }
}
