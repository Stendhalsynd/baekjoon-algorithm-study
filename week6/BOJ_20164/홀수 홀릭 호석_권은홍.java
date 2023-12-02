import java.util.Scanner;

public class 홀수홀릭호석_20164_골드5 {

    static int maxOddCnt = 0; // 최대 홀수 개수
    static int minOddCnt = Integer.MAX_VALUE; // 최소 홀수 개수

    // 최대/최소 갱신
    public static void getMinMax(int oddCnt)
    {
        if(oddCnt > maxOddCnt)
        {
            maxOddCnt = oddCnt;
        }
        if(oddCnt < minOddCnt)
        {
            minOddCnt = oddCnt;
        }
    }

    // target의 부분(part)을 받아 최대/최소 홀수 값을 계산하는 재귀함수
    public static void getOdd(String part, int oddCnt)
    {
        // 각 자리의 홀수 개수 count
        for(int i = 0; i < part.length(); i++)
        {
            if(Character.getNumericValue(part.charAt(i))%2 == 1)
            {
                oddCnt++;
            }
        }

        // part가 1자리수) 지금까지 계산한 홀수개수로 min/max를 갱신하고 종료
        if(part.length() == 1)
        {
            getMinMax(oddCnt);
        }
        // part가 2자리수) 둘을 더한 수로 getOdd를 다시 돌려서 홀수개수 계산
        else if(part.length() == 2)
        {
            part = String.valueOf(Character.getNumericValue(part.charAt(0))
                    + Character.getNumericValue(part.charAt(1)));
            getOdd(part, oddCnt);
        }
        // part가 3자리수 이상) 구분자를 나눠 모든 case에 대하여 합에 대한 getOdd를 구하는 getPart 수행
        else
        {
            getPart(part, 1, 3, oddCnt);
        }
    }

    // part를 나눠 모든 case들을 만들기 위한 재귀함수
    // p는 첫번째 구분자 인덱스, 1부터 n-2까지
    // q는 두번째 구분자 인덱스, 3부터 n까지
    // ex. 8 | 1 9 0 | 5  --> 8, 190, 5 세 부분으로 나뉨
    public static void getPart(String part, int p, int q, int oddCnt)
    {
        int n = part.length();
        // p 인덱스(첫번째 구분자)가 최대범위를 넘어가면 모든 경우 다 본 것이므로 return
        if(p > n-2) return;

        StringBuilder tmpStr = new StringBuilder();
        tmpStr.append(part);
        tmpStr.insert(p, ","); // p 인덱스에 구분자1 추가
        tmpStr.insert(q, ","); // q 인덱스에 구분자2 추가
        String[] parts = tmpStr.toString().split(",");

        // 구분자로 구분한 각 정수들을 합친 값으로 다시 홀수 개수를 구함
        int sum = Integer.parseInt(parts[0]) + Integer.parseInt(parts[1]) + Integer.parseInt(parts[2]);
        getOdd(String.valueOf(sum), oddCnt);

        // q 인덱스(두번째 구분자)가 최대범위를 넘어가면 p 추가, 아니면 q 추가
        if(q >= n)
        {
            p++;
            q = p + 2;
        }
        else q++;

        // 다음 구분자 case 탐색
        getPart(part, p, q, oddCnt);
    }

    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        String target = scanner.next();
        getOdd(target, 0);

        if(maxOddCnt == 0) minOddCnt = maxOddCnt;
        System.out.println(minOddCnt + " " + maxOddCnt);
    }
}
