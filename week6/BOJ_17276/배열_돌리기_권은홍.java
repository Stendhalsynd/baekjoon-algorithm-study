import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

// TODO : 각도는 360도면 처음과 같은 위치에 온다는 것을 고려하여 리팩토링하기
public class 배열_돌리기_17276_실버2 {
    public static void main(String[] args) throws Exception
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(reader.readLine()); // 테스트 케이스
        for(int t = 0; t < T; t++)
        {
            String[] info = reader.readLine().split(" ");
            int n = Integer.parseInt(info[0]);
            int d = Integer.parseInt(info[1]);
            int mid = (n+1)/2 - 1;
            boolean isClock = d > 0; // 시계방향인지?
            d = Math.abs(d/45);
            if(d == 8) d = 0; // 360도이면 처음과 같다

            int[][] arr = new int[n][n]; // 기존 배열
            int[][] newArr = new int[n][n]; // 새 배열

            // 배열 입력받기
            for(int i = 0; i < n; i++)
            {
                String[] nums = reader.readLine().split(" ");
                for(int j = 0; j < n; j++)
                {
                    arr[i][j] = Integer.parseInt(nums[j]);
                }
            }

            int newX, newY;

            // 배열 돌리기
            for(int k = 0; k < d; k++)
            {
                for(int x = 0; x < n; x++)
                {
                    for(int y = 0; y < n; y++)
                    {
                        if(x == y) // 주 대각선
                        {
                            if(isClock)
                            {
                                newX = x;
                                newY = mid;
                            }
                            else
                            {
                                newX = mid;
                                newY = y;
                            }
                        }
                        else if(y == mid) // 가운데 열
                        {
                            if(isClock)
                            {
                                newX = x;
                                newY = n-1-x;
                            }
                            else
                            {
                                newX = x;
                                newY = x;
                            }
                        }
                        else if(x + y == (n-1)) // 부 대각선
                        {
                            if(isClock)
                            {
                                newX = mid;
                                newY = y;
                            }
                            else
                            {
                                newX = x;
                                newY = mid;
                            }
                        }
                        else if(x == mid) // 가운데 행
                        {
                            if(isClock)
                            {
                                newX = y;
                                newY = y;
                            }
                            else
                            {
                                newX = n-1-y;
                                newY = y;
                            }
                        }
                        else // 무소속
                        {
                            newX = x;
                            newY = y;
                        }

                        newArr[newX][newY] = arr[x][y];
                    }
                }
                for(int c = 0; c < n; c++)
                {
                    arr[c] = Arrays.copyOf(newArr[c], newArr[c].length);
                }
            }

            if(d == 0) newArr = arr;

            // 2차원 배열 출력
            for(int p = 0; p < n; p++)
            {
                StringBuilder printStr = new StringBuilder();
                for(int q = 0; q < n; q++)
                {
                    printStr.append(newArr[p][q]).append(" ");
                }
                System.out.println(printStr);
            }
        }
    }
}