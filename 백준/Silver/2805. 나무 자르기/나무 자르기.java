import java.io.*;
import java.util.*;

public class Main
{
	public static void main(String[] args) throws IOException {
	    
	    Scanner sc = new Scanner(System.in);
	    int N = sc.nextInt();
	    long M = sc.nextInt();
	    
	    int[] arr = new int[N];
	    int max = 0;
	    for (int i=0; i<N; i++) {
	        arr[i] = sc.nextInt();
	        if(max < arr[i]) max = arr[i];
	    }
	    
		int low = 0;
		int high = max;
		int ans = 0;
		while(low <= high) {
		    int mid = (low + high) / 2;
		    if(check(mid, arr, M)) {
		        ans = mid;
		        low = mid + 1;
		    } else {
		        high = mid-1;
	    	}
		
		} 
		System.out.print(ans);
	}
	
	public static boolean check(int mid, int[] arr, long M) {
	    long sum = 0;
	    for(int item : arr) {
	        if(item - mid > 0) sum += ((long)item - mid);
	    }
	    return (sum - M >= 0);
	}
}