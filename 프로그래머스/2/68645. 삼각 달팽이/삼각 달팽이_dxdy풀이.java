class Solution {
    private static final int[] dx = {0, 1, -1};
    private static final int[] dy = {1, 0, -1};
    
    public int[] solution(int n) {
        int [][] triangle = new int[n][n];
        int v = 1; int x = 0; int y = 0; int d = 0;  // d는 진행방향
        
        while(true) {
            triangle[y][x] = v++;
            // nx, ny는 미리 진행해보는 좌표
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            // 미리 진행한 좌표가 범위 밖이거나 이미 작성된 칸이라면,
            // 진행방향을 바꾸고 nx, ny를 업데이트 && nx, ny가 범위 밖이거나 이미 작성된 칸이면 끝
            if(nx == n || ny == n || nx == -1 || ny == -1 || triangle[ny][nx] != 0) {
                d = (d + 1) % 3;
                nx = x + dx[d];
                ny = y + dy[d];
                if(nx == n || ny == n || nx == -1 || ny == -1 || triangle[ny][nx] != 0) break;
            }
            x = nx;
            y = ny;
        }
        
        // n, n-1, ..., 1번 triangle의 요소를 1차원 배열로 변환
        int[] result = new int[v-1];
            int index = 0;
            for(int i = 0; i < n; i++) {
                for(int j = 0; j <= i; j++) {
                    result[index++] = triangle[i][j];
                }
            }
        return result;
    }
}
