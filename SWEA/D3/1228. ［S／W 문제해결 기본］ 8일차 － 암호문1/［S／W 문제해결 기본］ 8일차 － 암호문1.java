import java.util.*;
class Solution
{
        public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int testcase = 1; testcase <= 10; testcase++) {
            int N = Integer.parseInt(scanner.nextLine());
            LinkedList<String> origin = new LinkedList<>(Arrays.asList(scanner.nextLine().split(" ")));
            int M = Integer.parseInt(scanner.nextLine());
            String[] query = scanner.nextLine().split("I");

            for (String q : query) {
                if (!q.isEmpty()) {
                    String[] li = q.split(" ");
                    int index = Integer.parseInt(li[1]);
                    for (int i = 3; i < li.length; i++) {
                        origin.add(index++, li[i]);
                    }
                }
            }

            System.out.print("#" + testcase + " ");
            for (int i = 0; i < 10; i++) {
                System.out.print(origin.get(i) + " ");
            }
            System.out.println();
        }
    }
}