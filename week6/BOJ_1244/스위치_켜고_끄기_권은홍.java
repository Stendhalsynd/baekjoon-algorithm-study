import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 스위치_켜고_끄기_1244_실버4 {
    public static int toggleSwitch(int value)
    {
        return (value == 0) ? 1 : 0;
    }
    public static void main(String[] args) throws Exception
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String printStr = ""; // 프린트할 결과 문자열

        int N = Integer.parseInt(reader.readLine()); // 스위치 총 개수
        int[] switches = new int[N+1]; // 스위치 배열
        String[] switchStrArr = reader.readLine().split(" ");
        for(int i = 1; i < N+1; i++)
        {
            switches[i] = Integer.parseInt(switchStrArr[i-1]);
        }

        int M = Integer.parseInt(reader.readLine()); // 학생 수
        for(int j = 0; j < M; j++)
        {
            String[] info = reader.readLine().split(" ");
            int gender = Integer.parseInt(info[0]); // 성별
            int num = Integer.parseInt(info[1]); // 받은 숫자
            if(gender == 1) // 남학생
            {
                if(num == N) // 받은 수가 스위치 개수와 같으면 배수가 자기자신뿐이므로 토글 후 넘어가기
                {
                    switches[N] = toggleSwitch(switches[N]);
                    continue;
                }
                for(int n = 1; n*num < N; n++)
                {
                    switches[n*num] = toggleSwitch(switches[n*num]); // 각 배수 토글
                }
            }
            else // 여학생
            {
                switches[num] = toggleSwitch(switches[num]); // 자기 자신은 항상 토글
                int left = num - 1;
                int right = num + 1;
                while(left > 0 && right < N+1) // 왼쪽, 오른쪽이 인덱스 바운더리를 넘어가지 않도록 조건주기
                {
                    if(switches[left] == switches[right]) // 양 옆이 같다면 각각 토글 후 각자 옆에 확인
                    {
                        switches[left] = toggleSwitch(switches[left]);
                        switches[right] = toggleSwitch(switches[right]);
                        left -= 1;
                        right += 1;
                    }
                    else break;
                }
            }
        }

        for(int i = 1; i < N+1; i++) // 20줄마다 줄바꿈해서 프린트
        {
            printStr += switches[i] + " ";
            if(i % 20  == 0) printStr += "\n";
        }

        System.out.println(printStr.substring(0, printStr.length()-1));
    }
}
