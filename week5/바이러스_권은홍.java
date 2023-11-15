import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Queue;
import java.util.LinkedList;

public class 바이러스_2026_실버3 {
    static class Graph
    {
        HashMap<Integer, ArrayList<Integer>> adjacMap;
        int n = 0; // 노드개수

        public Graph(int n)
        {
            this.adjacMap = new HashMap<>();
            this.n = n;
            for(int i = 0; i < (n+1); i++)
            {
                adjacMap.put(i, new ArrayList<>()); // 컴퓨터 개수만큼 인접리스트를 만든다.
            }
        }

        public void addEdge(int vertex1, int vertex2)
        {
            adjacMap.get(vertex1).add(vertex2);
            adjacMap.get(vertex2).add(vertex1);
        }

        public int bfs(int start)
        {
            boolean[] visited = new boolean[n+1];
            int infected = 0; // 감염된 컴퓨터 수 (연결된 노드 수)
            Queue<Integer> que = new LinkedList<Integer>();
            que.add(start);
            visited[start] = true;
            while(!que.isEmpty())
            {
                int current = que.poll();
                for(int adj : adjacMap.get(current))
                {
                    if(!visited[adj])
                    {
                        visited[adj] = true;
                        infected++;
                        que.add(adj);
                    }
                }
            }
            return infected;
        }
    }


    public static void main(String[] args) throws Exception
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int computerNum = Integer.parseInt(reader.readLine());
        int edgeNum = Integer.parseInt(reader.readLine());
        Graph graph = new Graph(computerNum);

        for(int e = 0; e < edgeNum; e++)
        {
            String[] pair = reader.readLine().split(" ");
            int vertex1 = Integer.parseInt(pair[0]);
            int vertex2 = Integer.parseInt(pair[1]);
            graph.addEdge(vertex1, vertex2);
        }

        System.out.println(graph.bfs(1));
    }
}
