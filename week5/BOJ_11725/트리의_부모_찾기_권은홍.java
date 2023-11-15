import java.util.LinkedList;
import java.util.HashMap;
import java.util.Queue;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 트리의_부모_찾기_11725_실버2 {
    static class Graph {
        HashMap<Integer, LinkedList<Integer>> adjListMap;
        int V;
        Integer[] parents; // 부모가 누군지 기록하는 배열

        public Graph(int v) {
            adjListMap = new HashMap<>();
            V = v;
            parents = new Integer[v];

            for(int i = 0; i < v; i++) {
                adjListMap.put(i, new LinkedList<>());
            }
        }

        public void addEdge(int vertex1, int vertex2) {
            adjListMap.get(vertex1).add(vertex2);
            adjListMap.get(vertex2).add(vertex1);
        }

        public void bfs(int start) {
            boolean[] visited = new boolean[V];
            Queue que = new LinkedList<Integer>();
            que.add(start);
            visited[start] = true;
            while(!que.isEmpty()) {
                int curr = (int) que.poll();
                for(int adj : adjListMap.get(curr)) {
                    if(!visited[adj]) {
                        visited[adj] = true;
                        que.add(adj);
                        parents[adj] = curr;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine());
        Graph graph = new Graph(N+1);

        for(int i = 0; i < N-1; i++) {
            String[] edge = reader.readLine().split(" ");
            int ver1 = Integer.parseInt(edge[0]);
            int ver2 = Integer.parseInt(edge[1]);
            graph.addEdge(ver1, ver2);
        }

        graph.bfs(1);
        for(int p = 2; p < N+1; p++) {
            System.out.println(graph.parents[p]);
        }
    }
}
