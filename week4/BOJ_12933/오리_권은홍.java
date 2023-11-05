package week4.BOJ_12933;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
class Main {
    public static void main(String[] args) throws Exception {

        // 오리 울음소리 맵 - 들어온 문자 : 이전 문자
        HashMap<Character, Character> quack = new HashMap<>();
        quack.put('q','k');
        quack.put('u','q');
        quack.put('a','u');
        quack.put('c','a');
        quack.put('k','c');

        int result = 0; // 오리의 최소 수

        ArrayList<Character> ducks = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        char[] soundArr = (reader.readLine()).toCharArray();

        for(char x : soundArr) {
            if(ducks.isEmpty()) {
                if(x == 'q') ducks.add('q');
                else {
                    // System.out.println("duck이 비었는데 q가 아닌 값 들어옴 x : " + x);
                    result = -1;
                    System.out.println(result);
                    return;
                }
            }
            else {
                char target = quack.get(x); // 현재 문자 이전 문자
                boolean flag = false; // ducks 안에 찾는 문자가 있는지
                for(int i = 0; i < ducks.size(); i++) {
                    if(ducks.get(i) == target) {
                        ducks.set(i, x); // 찾는 문자가 있으면 현재 문자로 변경한다
                        flag = true;
                        break;
                    }
                }
                if(!flag) { // 찾는 문자가 없을 경우
                    if(x == 'q') ducks.add('q'); // q이면 ducks에 새 오리를 추가
                    else {
                        // System.out.println("찾는 이전 문자가 없는데 q도 아님 x : "+ x + ", target : " + target);
                        result = -1;
                        System.out.println(result);
                        return;
                    }
                }
            }
        }

        for(char k : ducks) { // 모두 k 로 끝나는지 확인, 오리 수 계산
            if(k == 'k') result += 1;
            else {
                // System.out.println("k로 끝나지 않음 k : " + k);
                result = -1;
                System.out.println(result);
                return;
            }
        }
        System.out.println(result);
    }

    public static void printDuck(ArrayList<Character> ducks) {
        System.out.println("--ducks--");
        for(char d : ducks) System.out.println(d);
    }
}
