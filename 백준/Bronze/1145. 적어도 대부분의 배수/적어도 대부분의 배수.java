import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);

        int[] arr = new int[5];
        for(int i=0; i<5; i++) {
             arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int num=1; num<1000000; num++) {
            int count = 0;
            for(int i : arr) {
                if(num % i == 0) count++;
            }
            if(count >= 3) {
                System.out.println(num);
                return;
            }
        }
    }
}