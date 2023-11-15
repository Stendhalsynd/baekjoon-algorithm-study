import java.util.HashMap;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;

public class DFS와_BFS_1260_실버2 {
    static class Graph {
        HashMap<Integer, ArrayList<Integer>> adjListMap;
        int V; // 정점 개수
        String printStr = "";

        public Graph(int v) {
            adjListMap = new HashMap<>();
            V = v;
            for(int i = 0; i < v; i++) adjListMap.put(i, new ArrayList<Integer>());
        }

        public void addEdge(int vertex1, int vertex2) {
            for(int adj : adjListMap.get(vertex1)) {
                if(adj == vertex2) {
                    return; // 두 정점을 잇는 간선이 여러 개가 들어올 수 있는데 다 추가할 필요는 없으므로
                }
            }
            adjListMap.get(vertex1).add(vertex2);
            adjListMap.get(vertex2).add(vertex1);
        }

        public void dfs(int start) { // dfs 시작
            printStr = "";
            boolean[] visited = new boolean[V];
            visited[start] = true;
            dfsUtil(start, visited);
        }

        public void dfsUtil(int current, boolean[] visited) { // dfs 재귀함수
            printStr += current + " ";
            for(int adj : adjListMap.get(current)) {
                if (!visited[adj]) {
                    visited[adj] = true;
                    dfsUtil(adj, visited);
                }
            }
        }

        public void bfs(int start) {
            printStr = "";
            boolean[] visited = new boolean[V];
            Queue que = new LinkedList<Integer>();
            que.add(start);
            visited[start] = true;
            while(!que.isEmpty()) {
                int curr = (int) que.poll();
                printStr += curr + " ";
                for(int adj : adjListMap.get(curr)) {
                    if(!visited[adj]) {
                        visited[adj] = true;
                        que.add(adj);
                    }
                }
            }
        }

        public void printSearch() {
            System.out.println(printStr.substring(0, printStr.length()-1)); // 마지막 " " 떼기
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] info = reader.readLine().split(" ");
        int N = Integer.parseInt(info[0]);
        int M = Integer.parseInt(info[1]);
        int V = Integer.parseInt(info[2]);

        Graph graph = new Graph(N+1);
        for(int i = 0; i < M; i++) {
            String[] edge = reader.readLine().split(" ");
            int vertex1 = Integer.parseInt(edge[0]);
            int vertex2 = Integer.parseInt(edge[1]);
            graph.addEdge(vertex1, vertex2);
        }
        for(int j = 0; j < N+1; j++) {
            Collections.sort(graph.adjListMap.get(j));
        }

        graph.dfs(V);
        graph.printSearch();
        graph.bfs(V);
        graph.printSearch();
    }
}
