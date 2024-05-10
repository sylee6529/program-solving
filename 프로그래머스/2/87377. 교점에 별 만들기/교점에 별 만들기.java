import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        
        // 직선들을 2개씩 비교하여 교점이 있으면 배열에 추가
        for (int i = 0; i < line.length; i++) {
            for(int j = 0; j < line.length; j++) {
                Point intersection = intersection(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                
                if(intersection != null) {
                    points.add(intersection);
                }
            }
        }
        
        // 교점들의 최소/최대 좌표 값을 구함
        Point minPoint = getMinimumPoint(points);
        Point maxPoint = getMaximumPoint(points);
        
        // 2차원 배열의 길이 구함
        int width = (int) (maxPoint.x - minPoint.x + 1);
        int height = (int) (maxPoint.y - minPoint.y + 1);
        
        char[][] arr = new char[height][width];
        
        // . 으로 초기화
        for(char[] row : arr) {
            Arrays.fill(row, '.');
        }
        
        // 별 표시
        for(Point p : points) {
            int x = (int) (p.x - minPoint.x);
            int y = (int) (maxPoint.y - p.y);
            
            arr[y][x] = '*';
        }
        
        // char 배열을 String 배열로 변환
        String[] answer = new String[arr.length];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = new String(arr[i]);
        }        
        
        return answer;
    }
    
    // List<Point>에서 가장 작은 값의 각 x, y 값을 Point로 반환
    private Point getMinimumPoint(List<Point> points) {
        long minX = Long.MAX_VALUE;
        long minY = Long.MAX_VALUE;
        
        for(Point p : points) {
            if(p.x < minX) minX = p.x;
            if(p.y < minY) minY = p.y;
        }
        return new Point(minX, minY);
    }
    
    // List<Point>에서 가장 큰 값의 각 x, y 값을 Point로 반환
    private Point getMaximumPoint(List<Point> points) {
        long maxX = Long.MIN_VALUE;
        long maxY = Long.MIN_VALUE;
        
        for(Point p : points) {
            if(p.x > maxX) maxX = p.x;
            if(p.y > maxY) maxY = p.y;
        }
        return new Point(maxX, maxY);
    }
    
    // a1x + b1y + c1 = 0과 a2x + b2y + c2 = 0의 교점 반환
    private Point intersection(long a1, long b1, long c1, long a2, long b2, long c2) {
        double x = (double) (b1 * c2 - c1 * b2) / (a1 * b2 - a2 * b1);
        double y = (double) (c1 * a2 - a1 * c2) / (a1 * b2 - a2 * b1);
        
        if(x % 1 != 0 || y % 1 != 0) return null;
        
        return new Point((long) x, (long) y);
    }
    
    private static class Point {
	  public final long x, y;
	  private Point(long x, long y) {
		  this.x = x;
		  this.y = y;
	  }
  }
}