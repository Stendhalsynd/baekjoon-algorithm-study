package week4.BOJ_22858;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); // 카드 갯수
        int K = scanner.nextInt(); // 셔플 횟수
        scanner.nextLine(); // 엔터 흡수용
        int sArr[] = new int[N];
        int dArr[] = new int[N];
        int pArr[] = new int[N];

        String[] sLine = scanner.nextLine().split("\\s+");
        for(int i = 0; i < N; i++) sArr[i] = Integer.parseInt(sLine[i]);
        String[] dLine = scanner.nextLine().split("\\s+");
        for(int i = 0; i < N; i++) dArr[i] = Integer.parseInt(dLine[i]);

        for(int k = 0; k < K; k++) {
            for(int i = 0; i < N; i++) {
                pArr[dArr[i]-1] = sArr[i];
            }
            // sArr = pArr; 틀린 코드 : 얕은 복사
            for(int p = 0; p < N; p++) sArr[p] = pArr[p];
        }

        printArr(pArr);
    }

    public static void printArr(int[] arr) {
        String arrStr = "";
        for(int i : arr) arrStr += (i + " ");
        System.out.println(arrStr);
    }
}
