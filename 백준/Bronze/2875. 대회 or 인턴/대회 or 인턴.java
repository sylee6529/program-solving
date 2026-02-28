import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);

        int fCount = Integer.parseInt(st.nextToken());
        int mCount = Integer.parseInt(st.nextToken());
        int iCount = Integer.parseInt(st.nextToken());

        int answer = 0;
        int nextF = fCount;
        int nextM = mCount;

        while(nextF >= 2 && nextM >= 1 && (nextF + nextM - 3) >= iCount) {
            nextF -= 2;
            nextM--;
            answer++;
//            System.out.println(nextF + " " + nextM + " " + iCount + " " + answer);
        }

        System.out.print(answer);

    }
}