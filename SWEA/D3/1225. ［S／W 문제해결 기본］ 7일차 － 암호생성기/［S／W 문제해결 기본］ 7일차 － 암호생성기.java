import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
public class Solution {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int testcase = 1; testcase <= 10; testcase++) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[8];
            String[] c = br.readLine().split(" ");
            for (int i = 0; i < 8; i++) {
                arr[i] = Integer.parseInt(c[i]);
            }
            int count = 0;
            int index = 0;
            int value = 1;
            while (true) {
            	if(arr[index] - value <= 0) {
            		arr[index] = 0;
            		break;
            	}else {
            		arr[index] -= value;
            	}
                index = (index + 1) % 8;
                value = (value + 1) % 6;
                if (value == 0) {
                	value ++;
                }
                count ++;
            }
            int remain = count % 8;
            
            bw.write("#");
            bw.write(String.valueOf(testcase));
            bw.write(" ");
            for (int i = (remain + 1) % 8; i < 8; i++) {
            	bw.write(String.valueOf((arr[i])));
                bw.write(" ");
			}
            for (int i = 0; i <= remain % 8; i++) {
            	bw.write(String.valueOf((arr[i])));
                bw.write(" ");
			}

            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}