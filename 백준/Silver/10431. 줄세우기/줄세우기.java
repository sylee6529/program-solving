
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int p = Integer.parseInt(st.nextToken());
        for(int i=0; i<p; i++) {
            st = new StringTokenizer(br.readLine());
            int[] arr = new int[20];
            int t = Integer.parseInt(st.nextToken());
            for(int j=0; j<20; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
            }

            int count = 0;
            for(int j=1; j<20; j++) {
                for(int k=j-1; k>=0; k--) {
                    if(arr[k] > arr[j]) {
                        count++;
                    }
                }
            }

            sb.append(t + " " + count + "\n");
        }

        System.out.print(sb);
    }
}

