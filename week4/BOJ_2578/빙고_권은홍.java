package week4.BOJ_2578;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        // 숫자가 위치한 2차원 배열의 좌표를 가지는 맵 ex) 11 : "0,0"
        HashMap<String, String> locationMap = new HashMap<>();
        for(int x = 0; x < 5; x++) {
            String[] row = reader.readLine().split("\\s+");
            for(int y = 0; y < 5; y++) {
                locationMap.put(row[y], x+","+y);
            }
        }

        // 각 좌표의 숫자가 체크되었는지 여부를 담는 2차원 배열
        boolean[][] checkArr = new boolean[5][5];
        // 각 라인이 빙고인지 여부를 담음
        boolean[] rowBingo = new boolean[5];
        boolean[] colBingo = new boolean[5];
        boolean ldBingo = false;
        boolean rdBingo = false;

        int bingo = 0; // 빙고된 라인 수

        String str = "";
        for(int x = 0; x < 5; x++) {
            String temp = reader.readLine();
            str += temp + " ";
        }
        String[] callArr = str.split("\\s+"); // 호출 숫자 배열

        for(int i = 0; i < 25; i++) { // 숫자 호출
            String[] point = locationMap.get(callArr[i]).split(",");
            int x = Integer.parseInt(point[0]);
            int y = Integer.parseInt(point[1]);
            checkArr[x][y] = true; // 해당 숫자가 있는 좌표 체크

            // 포함 행이 빙고인지?
            boolean hit = true;
            for(int c = 0; c < 5; c++) {
                if(!checkArr[x][c]) {
                    hit = false;
                    break;
                }
            }
            if(hit) {
                if(!rowBingo[x]) {
                    bingo += 1;
                    rowBingo[x] = true;
                    if(bingo >= 3) {
                        System.out.println(i+1);
                        return;
                    }
                }
            }

            // 포함 열이 빙고인지?
            hit = true;
            for(int r = 0; r < 5; r++) {
                if(!checkArr[r][y]) {
                    hit = false;
                    break;
                }
            }
            if(hit) {
                if(!colBingo[y]) {
                    bingo += 1;
                    colBingo[y] = true;
                    if(bingo >= 3) {
                        System.out.println(i+1);
                        return;
                    }
                }
            }

            // 포함 대각선(오른쪽, 왼쪽)이 빙고인지?
            hit = true;
            for(int dr = 0; dr < 5; dr++) {
                if(!checkArr[dr][dr]) {
                    hit = false;
                    break;
                }
            }
            if(hit) {
                if(!rdBingo) {
                    bingo += 1;
                    rdBingo = true;
                    if(bingo >= 3) {
                        System.out.println(i+1);
                        return;
                    }
                }
            }

            hit = true;
                for(int dl = 0; dl < 5; dl++) {
                    if(!checkArr[dl][4-dl]) {
                        hit = false;
                        break;
                    }
                }
            if(hit) {
                if(!ldBingo) {
                    bingo += 1;
                    ldBingo = true;
                    if(bingo >= 3) {
                        System.out.println(i+1);
                        return;
                    }
                }
            }
        }
    }
}
