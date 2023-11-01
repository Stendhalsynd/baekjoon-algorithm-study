import java.util.Map;
import java.util.Scanner;

import com.sun.tools.javac.util.List;

class Bingo {
    public class Point {
        public int x, y; // 좌표
        public List<String> lineList; // 좌표를 포함하는 라인 목록

        public Point(int x, int y, List<String> lineList) {
            this.x = x;
            this.y = y;
            this.lineList = lineList;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<Point> points = new ArrayList();

        Map<String, Integer> LineMap = new Map(); // 라인이름, Hit횟수
        LineMap.put("row0", 0); // 0, 0-4 라인
        LineMap.put("row1", 0); // 1, 0-4 라인
        LineMap.put("row2", 0);
        LineMap.put("row3", 0);
        LineMap.put("row4", 0);
        LineMap.put("col0", 0); // 0-4, 0 라인
        LineMap.put("col1", 0); // 0-4, 1 라인
        LineMap.put("col2", 0);
        LineMap.put("col3", 0);
        LineMap.put("col4", 0);
        LineMap.put("RD", 0); // 오른쪽 대각선
        LineMap.put("LD", 0); // 왼쪽 대각선

        for(int i = 0; i < 5; i++) {
            for(int j = 0; j < 5; j ++) {
                List<String> lineList = new List<String>();
                lineList.append("row"+i);
                lineList.append("col"+j);
                if(i == j) lineList.append("RD");
                if(i + j == 4) lineList.append("LD");

                Point p = new Point(i, j, lineList);
                int index = scanner.nextInt();
                points[index] = p;
                // System.out.println("["+ (i+1)*(j+1) +"] Insert Point - index : " + index + ", point : " + points[index]);
            }
        }

        int bingo = 0; // 맞춘 라인 수
        for(int count = 0; count < 25; count++) { // 숫자 호출 횟수
            int callNum = scanner.nextInt(); // 호출한 숫자

            // List에서 해당 인덱스의 Point를 얻어온다.
            Point point = points[callNum];

            // System.out.println("["+ count +"] Get Point - callNum : " + callNum + ", point : " + points[callNum]);

            // point를 포함하는 라인 확인
            List<String> hitLines = new List<String>();
            for(String lineName : hitLines) {

                int hitCount = LineMap.get(lineName);

                // System.out.println("LineName : " + lineName + ", hitCount : " + hitCount);

                if(hitCount == 4) // 라인의 체크횟수가 5가 되면 bingo +1
                {
                    bingo += 1;
                    // System.out.println("BINGO! "+ count);
                    if(bingo >= 3){
                        // bingo가 3이면 호출횟수 출력
                        // System.out.println("WIN!! "+ (count+1));
                        break;
                    }
                }
                LineMap.put(lineName, hitCount + 1);
            }
        }
    }
}