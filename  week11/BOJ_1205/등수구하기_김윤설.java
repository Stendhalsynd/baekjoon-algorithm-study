import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        //1. 입력 받기
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int new_score = sc.nextInt();
        int p = sc.nextInt();

        int[] arr = new int[n];

        for(int i =0; i<n;i++){
            arr[i] = sc.nextInt();
        }

        //2.
        int rank = 1;

        if(n==p && arr[n-1]>= new_score){
            System.out.println(-1);
        }else{
            for(int i=0;i<n; i++){
                if(new_score < arr[i]){
                    rank++;
                }else{
                    break;
                }

            }
            System.out.println(rank);
        }
    }
}
