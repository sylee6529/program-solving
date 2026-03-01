import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {

        int n = scan.nextInt();
        double[] nArr = new double[n+1];
        int max = -1;
        for(int i = 0 ; i < n; i++) {
            int score = scan.nextInt();
            nArr[i] = score;

            if(max < score) {
                max = score;
            }
        }

        double sum = 0;
        for(int i = 0; i < n; i++) {
            nArr[i] = nArr[i]/max;
            nArr[i] *= 100;
            sum += nArr[i];
        }
        System.out.println(sum / n);

    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
