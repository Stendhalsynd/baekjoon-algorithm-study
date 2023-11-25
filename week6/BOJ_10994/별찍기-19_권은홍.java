import java.util.Scanner;
import java.util.HashMap;

// TODO : 재귀로 구현해보기
public class 별_찍기_19_10994_실버4 {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        // size는 총 줄 개수이고, 각 문자열의 크기이다.
        int size = (n-1)*4 + 1; // 위아래 대칭 2줄씩 총 4줄 + 가운데 1줄

        HashMap<Integer, String> rowStrMap = new HashMap<>();

        int half = (int)size/2 + 1; // 중간줄이 몇 번째인지
        for(int i = 0; i < half; i++)
        {
            String rowStr = "";
            if(i % 2 == 0) // i가 짝수이면
            {
                rowStr += "* ".repeat((int)(i / 2)); // String 클래스의 repeat은 Java11버전부터 사용 가능
                rowStr += "*".repeat(size - (i * 2));
                rowStr += " *".repeat((int)(i / 2));
            }
            else
            {
                rowStr += "* ".repeat((int)(i / 2) + 1);
                rowStr += " ".repeat(size - ((i + 1) * 2));
                rowStr += " *".repeat((int)(i / 2) + 1);
            }
            rowStrMap.put(i, rowStr);
        }

        for(int j = 0; j < rowStrMap.size(); j++)
        {
            System.out.println(rowStrMap.get(j));
        }
        for(int k = rowStrMap.size()-2; k >= 0; k--)
        {
            System.out.println(rowStrMap.get(k));
        }

    }
}
