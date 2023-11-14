import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < T; i++) {
			int x = 0;
			int y = 0;
			int n = 0;
			String line = br.readLine();
			StringTokenizer st = new StringTokenizer(line, " ");
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			n = Integer.parseInt(st.nextToken());
			
			int sum = Math.abs(x) + Math.abs(y);
		
			if(sum > n) {
				System.out.println("NO");
				continue;
			} else if(sum == n) {
				System.out.println("YES");
				continue;
			} else {
				if((sum - n) % 2 == 0) {
					System.out.println("YES");
					continue;
				}
				System.out.println("NO");
			}
		}
		
		
		
	}
}
