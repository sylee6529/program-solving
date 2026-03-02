
import java.io.*;
import java.util.Scanner;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		long[] arr = new long[N];
		int[] cumArr = new int[N];
		int[] cntArr = new int[M];
		
		for(int i=0; i<N; i++) {
		    arr[i] = sc.nextLong();
		    if(i == 0) cumArr[0] = (int)(arr[0] % M);
		    else cumArr[i] = (int)((cumArr[i-1] + arr[i]) % M);
		    cntArr[cumArr[i]]++;
		}
		
		long answer = 0;
		answer += cntArr[0];
		for(int i=0; i<M; i++) {
		    answer += ((long)cntArr[i] * (cntArr[i]-1)) / 2;
		}
	    System.out.print(answer);
	}
}