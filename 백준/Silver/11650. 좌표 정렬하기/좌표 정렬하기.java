import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static StringBuilder sb;
    static StringTokenizer st;
    static int N;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        List<Pair> arr = new ArrayList<Pair>();
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            arr.add(new Pair(x, y));
        }

        Collections.sort(arr, new Comparator<Pair>() {
            @Override
            public int compare(Pair p1, Pair p2) {
                if (p1.x == p2.x) {
                    return Integer.compare(p1.y, p2.y);
                } else {
                    return Integer.compare(p1.x, p2.x);
                }
            }
        });

        for(Pair p : arr) {
            System.out.println(p.x + " " + p.y);
        }

    }

    public static class Pair{
        int x;
        int y;

        public Pair(int x, int y){
            this.x = x;
            this.y=  y;
        }
    }

}
