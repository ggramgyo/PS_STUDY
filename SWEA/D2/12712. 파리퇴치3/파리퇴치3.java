/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
static int[] ri = {1, 1, 0, 1, -1, -1, 0, -1};
    static int[] rj = {0, -1, 1, 1, 0, 1, -1, -1};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int tc = 0; tc < T; tc++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int[][] g = new int[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    g[i][j] = scanner.nextInt();
                }
            }

            int res = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int pv = g[i][j];
                    int mv = g[i][j];
                    for (int k = 0; k < 8; k += 2) {
                        for (int w = 1; w < m; w++) {
                            int ni = i + ri[k] * w;
                            int nj = j + rj[k] * w;
                            int nni = i + ri[k + 1] * w;
                            int nnj = j + rj[k + 1] * w;
                            pv += (0 <= ni && ni < n && 0 <= nj && nj < n) ? g[ni][nj] : 0;
                            mv += (0 <= nni && nni < n && 0 <= nnj && nnj < n) ? g[nni][nnj] : 0;
                        }
                    }
                    res = Math.max(res, Math.max(pv, mv));
                }
            }
            System.out.println("#" + (tc + 1) + " " + res);
        }
    }
}