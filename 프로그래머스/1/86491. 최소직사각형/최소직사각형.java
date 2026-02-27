class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int x1 = 0;
        int x2 = 0;
        for(int i=0; i < sizes.length; i++) {
            if(sizes[i][0] > sizes[i][1]) {
                if(sizes[i][0] > x1) x1 = sizes[i][0];
                if(sizes[i][1] > x2) x2 = sizes[i][1];
            } else {
                if(sizes[i][1] > x1) x1 = sizes[i][1];
                if(sizes[i][0] > x2) x2 = sizes[i][0];
            }
        }
        
        answer = x1 * x2;
        return answer;
    }
}