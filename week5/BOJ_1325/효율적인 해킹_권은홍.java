import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static class Graph {
        HashMap<Integer, ArrayList<Integer>> adjListMap;
        int V;

        public Graph(int v) {
            V = v;
            adjListMap = new HashMap<>();

            for(int i = 0; i < v; i++) {
                adjListMap.put(i, new ArrayList<Integer>());
            }
        }

        public void addEdge(int ver1, int ver2) { // 방향 그래프 ver2 -> ver1
            adjListMap.get(ver2).add(ver1);
        }

        public int bfs(int start) {
            Queue que = new LinkedList<Integer>();
            boolean[] visited = new boolean[V];
            int hackCnt = 0; // 해킹한 컴퓨터 수
            que.add(start);
            visited[start] = true;
            while(!que.isEmpty()) {
                int curr = (int) que.poll();
                for(int adj : adjListMap.get(curr)) {
                    if(!visited[adj]) {
                        visited[adj] = true;
                        hackCnt++;
                        que.add(adj);
                    }
                }
            }
            return hackCnt;
        }
    }

    public static void main(String[] args) throws Exception {
        ArrayList<Integer> result = new ArrayList<>();
        int maxCnt = 0; // 현재 해킹가능 최대 컴 개수

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] info = reader.readLine().split(" ");
        int N = Integer.parseInt(info[0]);
        int M = Integer.parseInt(info[1]);
        Graph graph = new Graph(N+1);

        for(int i = 0; i < M; i++) {
            String[] edge = reader.readLine().split(" ");
            int v1 = Integer.parseInt(edge[0]);
            int v2 = Integer.parseInt(edge[1]);
            graph.addEdge(v1, v2);
        }

        for(int j = 1; j < N+1; j++) {
            int curCnt = graph.bfs(j);
            if (curCnt > maxCnt) {
                maxCnt = curCnt;
                result.clear();
                result.add(j);
            }
            else if (curCnt == maxCnt) {
                result.add(j);
            }
        }

        Collections.sort(result);
        String resultStr = "";
        for(int k : result) {
            resultStr += k + " ";
        }
        System.out.println(resultStr.substring(0, resultStr.length()-1));
    }
}
