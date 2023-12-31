import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        //1. 입력 받기
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];
        boolean[] visit = new boolean[n]; //false

//        자기보다 큰 사람이 왼쪽에 몇 명 있었는지만
        for(int i =0; i<n;i++){
            int p = sc.nextInt();
            int cnt = 0;
            for(int j=0;j<n;j++){
                if(!visit[j]){
                    if(cnt == p){
                        visit[j] = true;
                        arr[j] = i+1;
                        break;
                    }
                    cnt++;
                }
            }
        }

        //3.정답출력
        for(int a:arr){
            System.out.print(a+" ");
        }
    }
}
