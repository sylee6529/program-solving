class Solution {
    // 상+하=3, 좌+우=3 => {하, 좌, 우, 상}
    private static final int dx[] = {0, -1, 1, 0};
    private static final int dy[] = {-1, 0, 0, 1};
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        
        // places를 각 place로 쪼개고, 그 place를 String[]=>char[][]로 변환
        for (int i = 0; i < answer.length; i++) {
            String[] place = places[i];
            char[][] room = new char[place.length][];
            for (int j = 0; j < room.length; j++) {
                room[j] = place[j].toCharArray();
            }
            
            if(isDistanced(room)) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        
        return answer;
    }
    
    // 해당 대기실이 거리두기를 모두 지키고 있는지 체크
    private boolean isDistanced(char[][] room) {
        for(int y = 0; y < room.length; y++) {
            for(int x = 0; x < room[y].length; x++) {
                if(room[y][x] != 'P') continue;
                if(!isDistanced(room, x, y)) return false;
            }
        }
        return true;
    }
    
    // 해당 대기실에서 x,y 위치의 사람이 거리두기를 지키고 있는지 체크
    private boolean isDistanced(char[][] room, int x, int y) {
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(ny < 0 || ny >= room.length || nx < 0 || nx >= room[ny].length) continue;
            
            switch(room[ny][nx]) {
                case 'P': return false;
                case 'O':
                    if(isNextToVolunteer(room, nx, ny, 3-d)) return false;
                    break;
            }
        }
        return true;
    }
    
    // 한 방향(기존 사람 자리)를 제외하고 3방향을 탐색
    private boolean isNextToVolunteer(char[][] room ,int x, int y, int exclude) {
        for (int d = 0; d < 4; d++) {
            if (d == exclude) continue;
            
            int nx = x + dx[d];
            int ny = y + dy[d];
            if (ny < 0 || ny >= room.length || nx < 0 || nx >= room[ny].length) continue;
            if(room[ny][nx] == 'P') return true;
        }
        return false;
    }
}