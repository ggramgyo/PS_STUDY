import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        String dna = br.readLine().trim();

        int[] tmp = new int[4];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            tmp[i] = Integer.parseInt(st.nextToken());
        }

        char[] chk = {'A', 'C', 'G', 'T'};
        Map<Character, Integer> chkCount = new HashMap<>();
        for (int i = 0; i < 4; i++) {
            chkCount.put(chk[i], tmp[i]);
        }

        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < p; i++) {
            char w = dna.charAt(i);
            count.put(w, count.getOrDefault(w, 0) + 1);
        }

        int start = 0;
        int answer = 0;
        while (start <= dna.length() - p) {
            // Check if the current substring contains enough occurrences of each nucleotide
            if (count.getOrDefault('A', 0) >= chkCount.getOrDefault('A', 0) &&
                    count.getOrDefault('C', 0) >= chkCount.getOrDefault('C', 0) &&
                    count.getOrDefault('G', 0) >= chkCount.getOrDefault('G', 0) &&
                    count.getOrDefault('T', 0) >= chkCount.getOrDefault('T', 0)) {
                answer++;
            }
            // Move the window by decreasing the count of the character at the start and adding the count at the end
            char startChar = dna.charAt(start);
            count.put(startChar, count.get(startChar) - 1);
            if (start + p < s) {
                char endChar = dna.charAt(start + p);
                count.put(endChar, count.getOrDefault(endChar, 0) + 1);
            }
            start++;
        }

        System.out.println(answer);
    }
}