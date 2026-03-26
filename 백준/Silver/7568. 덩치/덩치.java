
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int[] xArr = new int[n];
        int[] yArr = new int[n];
        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            xArr[i]=Integer.parseInt(st.nextToken());
            yArr[i]=Integer.parseInt(st.nextToken());
        }

        for(int i=0; i<n; i++) {
            int count = 0;
            for(int j=0; j<n; j++) {
                if(i != j && xArr[i] < xArr[j] && yArr[i] < yArr[j]) {
                    count++;
                }
            }
            count++;
            sb.append(count + " ");
        }
        System.out.println(sb);
    }
}