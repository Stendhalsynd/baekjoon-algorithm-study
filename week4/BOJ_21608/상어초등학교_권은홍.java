package week4.BOJ_21608;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Shark { // 돌릴 때 Main으로 바꾸기
    public static void main(String[] args) throws Exception{

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        int[][] room = new int[n][n];

        int result = 0; // 만족도 총합
        Map<Integer, Set> likeMap = new HashMap<>();

        for(int i = 0; i < Math.pow(n,2); i++) {
            String[] studentInfo = (reader.readLine()).split("\\s+"); // 공백 기준으로 자름
            int stdNum = Integer.parseInt(studentInfo[0]);

            // 현재 학생이 좋아하는 학생 리스트
            HashSet<Integer> likeList = new HashSet<>();
            for(int j = 0; j < 4; j++) {
                int std = Integer.parseInt(studentInfo[j+1]);
                likeList.add(std);
            }
            likeMap.put(stdNum, likeList);

            if(i == 0) {
                // 첫 번째 학생은 항상 1,1에 앉는다.
                room[1][1] = stdNum;
                continue;
            }

            // 후보자리 : x, y, 인접한 좋아하는 학생 수, 인접한 빈 자리 수
            String bestSeat = "0,0,0,0";

            // 자리 탐색
            for (int x = 0; x < n; x++) {
                for (int y = 0; y < n; y++) {
                    int likeCnt = 0; // 해당 자리의 인접한 좋아하는 학생 수
                    int emptyCnt = 0; // 해당 자리의 인접한 빈 자리 수
                    int seat = 0;

                    if(room[x][y] != 0) continue; // 이미 자리가 차있으면 넘긴다.

                    if(x > 0) {
                        seat = room[x-1][y];
                        if(seat == 0) emptyCnt += 1;
                        else {
                            for(int likeGuy : likeList) {
                                if(seat == likeGuy) {
                                    likeCnt += 1;
                                    break;
                                }
                            }
                        }
                    }
                    if(x < n-1) {
                        seat = room[x+1][y];
                        if(seat == 0) emptyCnt += 1;
                        else {
                            for(int likeGuy : likeList) {
                                if(seat == likeGuy) {
                                    likeCnt += 1;
                                    break;
                                }
                            }
                        }
                    }
                    if(y > 0) {
                        seat = room[x][y-1];
                        if(seat == 0) emptyCnt += 1;
                        else {
                            for(int likeGuy : likeList) {
                                if(seat == likeGuy) {
                                    likeCnt += 1;
                                    break;
                                }
                            }
                        }
                    }
                    if(y < n-1) {
                        seat = room[x][y+1];
                        if(seat == 0) emptyCnt += 1;
                        else {
                            for(int likeGuy : likeList) {
                                if(seat == likeGuy) {
                                    likeCnt += 1;
                                    break;
                                }
                            }
                        }
                    }

                    String[] parts = bestSeat.split(",");
                    int bestX = Integer.parseInt(parts[0]);
                    int bestY = Integer.parseInt(parts[1]);
                    int bestLike = Integer.parseInt(parts[2]);
                    int bestEmpty = Integer.parseInt(parts[3]);
                    String curSeat = x + "," + y + "," + likeCnt + "," + emptyCnt;
                    if(room[bestX][bestY] != 0 ) {
                        bestSeat = curSeat;
                        continue;
                    }
                    if(likeCnt > bestLike)
                    {
                        bestSeat = curSeat;
                        continue;
                    }
                    else if(likeCnt == bestLike && emptyCnt >= bestEmpty) {
                        if(emptyCnt > bestEmpty) {
                            bestSeat = curSeat;
                            continue;
                        }
                        else if(emptyCnt == bestEmpty && x <= bestX) {
                            if(x < bestX) {
                                bestSeat = curSeat;
                                continue;
                            }
                            else if (x == bestX && y < bestY) {
                                bestSeat = curSeat;
                                continue;
                            }
                            else continue;
                        }
                    }
                    else continue;
                }
            }

            String[] parts = bestSeat.split(",");
            int bestX = Integer.parseInt(parts[0]);
            int bestY = Integer.parseInt(parts[1]);
            int bestLike = Integer.parseInt(parts[2]);
            int bestEmpty = Integer.parseInt(parts[3]);
            room[bestX][bestY] = stdNum;
        }

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                int score = 0; // 해당 자리의 인접한 좋아하는 학생 수
                int num = room[x][y];
                HashSet<Integer> likeList = (HashSet<Integer>) likeMap.get(num);
                int seat;

                if (x > 0) {
                    seat = room[x - 1][y];
                    for (int likeGuy : likeList) {
                        if (seat == likeGuy) {
                            score += 1;
                            break;
                        }
                    }
                }
                if (x < n - 1) {
                    seat = room[x + 1][y];
                    for (int likeGuy : likeList) {
                        if (seat == likeGuy) {
                            score += 1;
                            break;
                        }
                    }
                }
                if (y > 0) {
                    seat = room[x][y - 1];
                    for (int likeGuy : likeList) {
                        if (seat == likeGuy) {
                            score += 1;
                            break;
                        }
                    }
                }
                if (y < n - 1) {
                    seat = room[x][y + 1];
                    for (int likeGuy : likeList) {
                        if (seat == likeGuy) {
                            score += 1;
                            break;
                        }
                    }
                }
                if(score > 0) {
                    result += (score == 1 ? 1 : (int) Math.pow(10, score-1)); // 1, 10, 100, 1000
                }
            }
        }

        // 만족도 출력
        System.out.println(result);

    }
}