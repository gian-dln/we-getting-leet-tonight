import java.util.*;

public class lab8part2 {
    
    /**
     * Main lab8part2 method - replace this with your actual problem logic
     * 
     */
    
	public int countReachable(LinkedList<Integer>[] acyclicGraph, Integer[] broken){
		boolean[] visited = new boolean[acyclicGraph.length];
		Stack<Integer> stack = new Stack<Integer>();
		int count = 0;
		for (int i=0; i<broken.length; i++) {
			visited[broken[i]] = true;
		}

		for (int i=0; i<acyclicGraph.length; i++) {
			if (visited[i] != true) {
				visited[i] = false;
			}
		}


		stack.push(0);

		while (!stack.isEmpty()) {
			int current = stack.pop();
			if (!visited[current]) {
				visited[current] = true;
				count++;
			}

			if (acyclicGraph[current] == null) {
				continue;
			}
			
			for (Integer neighbour: acyclicGraph[current]) {
				if (!visited[neighbour]) {
					stack.push(neighbour);
				}
			}


		}



		return count;
	}

	public static void main(String[] args){
		//This is just an example skeleton you can use to quickly test
		//your code, but it does not affect the tests, it is only for you and you
		// can ignore it or modify the example input to test your code.
		LinkedList<Integer>[] exampleGraph = new LinkedList[5];
		exampleGraph[0] = new LinkedList<Integer>(Arrays.asList(1, 2, 3));
		exampleGraph[3] = new LinkedList<Integer>(Arrays.asList(4));

		lab8part2 solution = new lab8part2();

		int result = solution.countReachable(exampleGraph, new Integer[]{2, 4});

		System.out.println(result);
	}
}