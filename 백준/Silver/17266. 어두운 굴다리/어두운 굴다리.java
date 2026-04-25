
import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] positions;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        positions = new int[M];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            positions[i] = Integer.parseInt(st.nextToken());
        }

        // TODO: 이분 탐색 로직 작성
        int left = 0;
        int right = N;

        while(left < right) {
            int mid = (left + right) / 2;

            if(possible(mid)) right = mid;
            else left = mid+1;
        }

        // TODO: 정답 출력
        System.out.println(left);
    }

    static boolean possible(int h) {
        // TODO: 시작 구간 확인
        if(positions[0] - h > 0) return false;

        // TODO: 가로등 사이 확인
        for(int i=0; i < M-1; i++) {
            if(positions[i] + h < positions[i+1] - h)
                return false;
        }

        // TODO: 끝 구간 확인
        if(positions[M-1] + h < N) return false;

        return true;
    }
}
