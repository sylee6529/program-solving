import java.io.*;
import java.util.*;
import java.awt.Point;

class Main {
	static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] visited = new boolean[2001][2001];

    public static int bfs(int x, int y, int[][] pMap, int n, int m) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(x, y));
        visited[x][y] = true;
        int cnt = 0;
        int val = pMap[x][y];
        if(val == 2) {
            cnt -= 2;
        }
        else if(val == 0) {
            cnt++;
        }

        while(queue.peek() != null) {
            Point p = queue.poll();

            for(int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if(nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                    if(pMap[nx][ny] == 1) {
                        continue;
                    }

                    queue.add(new Point(nx, ny));
                    visited[nx][ny] = true;

                    val = pMap[nx][ny];
                    if(val == 2) {
                        cnt -= 2;
                    }
                    else if(val == 0) {
                        cnt++;
                    }
                }

            }
        }
        return cnt;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] st = br.readLine().split(" ");
        int n = Integer.parseInt(st[0]);
        int m = Integer.parseInt(st[1]);


        int[][] parkingMap = new int[n+1][m+1];
        for(int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for(int j = 0; j < m; j++) {
                parkingMap[i][j] = Integer.parseInt(s[j]);
            }
        }

        int maxCount = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(!visited[i][j] && parkingMap[i][j] != 1) {
                    int result = bfs(i, j, parkingMap, n, m);
                    if(result > maxCount) {
                        maxCount = result;
                    }
                }
            }
        }

        System.out.print(maxCount);

    }
}
