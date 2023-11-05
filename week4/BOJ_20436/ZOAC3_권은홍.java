package week4.BOJ_20436;

import java.util.HashMap;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. 키보드 배열 정보를 가진 맵 생성
        HashMap<Character, String> keyMap = new HashMap<>();
        String[] keyboard = { // 문자, 좌/우, x좌표, y좌표
                "q,L,0,0", "w,L,0,1", "e,L,0,2", "r,L,0,3", "t,L,0,4", "y,R,0,5", "u,R,0,6", "i,R,0,7", "o,R,0,8", "p,R,0,9",
                "a,L,1,0" , "s,L,1,1", "d,L,1,2", "f,L,1,3", "g,L,1,4", "h,R,1,5", "j,R,1,6", "k,R,1,7", "l,R,1,8",
                "z,L,2,0",  "x,L,2,1", "c,L,2,2", "v,L,2,3", "b,R,2,4", "n,R,2,5", "m,R,2,6"
        };
        for(String key : keyboard)
        {
            // key : 'q', value : "L,0,0" 형식
            keyMap.put(key.charAt(0), key.substring(2));
        }

        // 2. 결과변수, 현재 왼쪽 키 좌표, 오른쪽 키 좌표 세팅
        int result = 0;
        String leftKey = keyMap.get(scanner.next().charAt(0));
        String rightKey = keyMap.get(scanner.next().charAt(0));
        int curLX = Integer.parseInt(leftKey.substring(2,3));
        int curLY = Integer.parseInt(leftKey.substring(4));
        int curRX = Integer.parseInt(rightKey.substring(2,3));
        int curRY = Integer.parseInt(rightKey.substring(4));

        // 3. 문자열 타이핑 거리 계산하기
        char[] target = scanner.next().toCharArray();
        int LX = 0;
        int LY = 0;
        int RX = 0;
        int RY = 0;
        int distance = 0;
        for(char c : target)
        {
            String key = keyMap.get(c);
            if(key.charAt(0) == 'L')
            {
                LX = Integer.parseInt(key.substring(2,3));
                LY = Integer.parseInt(key.substring(4));
                distance = Math.abs(curLX-LX)+Math.abs(curLY-LY);
                result += (distance + 1);
                curLX = LX;
                curLY = LY;
            }
            else
            {
                RX = Integer.parseInt(key.substring(2,3));
                RY = Integer.parseInt(key.substring(4));
                distance = Math.abs(curRX-RX)+Math.abs(curRY-RY);
                result += (distance + 1);
                curRX = RX;
                curRY = RY;
            }
        }
        System.out.println(result);
    }
}