
import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i<N; i++) {
            arr[i] = sc.nextInt();
        }
        int b = sc.nextInt();
        int c = sc.nextInt();

        long answer = N;
        for(int i=0; i<N; i++) {
            if(arr[i] >= b) arr[i] = arr[i] - b;
            else arr[i] = 0;
        }

        for(int i=0; i<N; i++) {
            if(arr[i] > 0) {
                answer += (long)(arr[i] + c - 1) / c;
            }
        }
        System.out.print(answer);

    }
}