class Solution {
    public int[] solution(int n) {
    
        int[][] triangle = new int[n][n];
        int v = 1;  // triangle에 기록한 숫자의 수
        int x = 0; int y = 0;  // 움직일 좌표
        
        while(true) {
            // 아래로 이동
            while(true) {
                triangle[y][x] = v++;
                if(y + 1 == n || triangle[y+1][x] != 0) break;
                y += 1;
            }
            
            if(x + 1 == n || triangle[y][x+1] != 0) break;
            x += 1;
            
            // 오른쪽으로 이동
            while(true) {
                triangle[y][x] = v++;
                if (x + 1 == n || triangle[y][x+1] != 0) break;
                x += 1;
            }
            if(triangle[y-1][x-1] != 0) break;
            x -= 1;
            y -= 1;
            
            // 왼쪽 위로 이동
            while(true) {
                triangle[y][x] = v++;
                if(triangle[y-1][x-1] != 0) break;
                x -= 1;
                y -= 1;
            }
            
             if(y + 1 == n || triangle[y+1][x] != 0) break;
            y += 1;
        }
        
        int[] answer = new int[v-1];
        int index = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j <= i; j++) {
                answer[index++] = triangle[i][j];
            }
        }
        
        return answer;
    }
}
