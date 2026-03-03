import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return; 
        
        int N = sc.nextInt();
        int[] arr = new int[N];
        
        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        
        Arrays.sort(arr);
        
        System.out.print(arr[(N - 1) / 2]);
    }
}