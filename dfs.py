from solvable import check_if_solvable
from EightPuzzle import EightPuzzleProb
from Node import Node

def dfs(problem):
   
    print("Starting DFS on ", problem)
    node = Node(problem.init_state)

    if not check_if_solvable(problem.init_state):
        print("Sorry this choose of game board is not solvable")
        return 

    if problem.goal_test(node.state):
        return node.solution_path()

    frontier= [node]
    explored = set()
    num_processed_nodes = 0                 # counter keeping track of the number of nodes processed
    max_len_frontier = 1                    # counter keeping track of the maximum length of frontier through the search
    while (len(frontier) > 0):
        node = frontier.pop()
        print("Popped ", node)
        
        explored.add(tuple(node.state))
        num_processed_nodes +=1             #incrementing the number of nodes processed
        actions, successors = problem.actions(node.state)
        
        print("actions =", actions, "successors= ", successors)
        for i in range(len(actions)):
            child_node = Node(successors[i], node, actions[i], node.path_cost + 1)
            if (tuple(child_node.state) not in explored )and (child_node not in frontier):
                if problem.goal_test(child_node.state):
                    print("Found solution! ",child_node)
                    print("--------------------------------")
                    path = child_node.solution_path()
                    child_node.display_path(path)
                    return path[1]
                frontier.append(child_node)
                max_len_frontier = max(max_len_frontier, len(frontier))
            

    return None

def bfs(problem):
    """
    > We start with a node that represents the initial state of the problem. If the initial state is a
    goal state, we return the solution path. Otherwise, we add the node to the frontier and start
    exploring. We explore by popping a node from the frontier, adding it to the explored set, generating
    its successor states, and adding them to the frontier if they are not already in the frontier or the
    explored set. If any of the successor states is a goal state, we return the solution path. If we run
    out of nodes in the frontier, we return None.
    
    :param problem: the problem to be solved
    :return: The solution path is being returned.
    """

    print("About to do BFS on problem: ", problem)
    node = Node(problem.init_state)
    
    if problem.goal_test(node.state):
        return node.solution_path()
    
    frontier = [node]
    explored = set()
    num_processed_nodes = 0         # counter keeping track of the number of nodes processed
    max_len_frontier = 1            # counter keeping track of the maximum length of frontier through the search


    while(len(frontier) > 0):
        node = frontier.pop(0)
        explored.add(tuple(node.state))
        num_processed_nodes +=1     #incrementing the number of nodes processed
        print("Popped: ",node)

        actions, successors = problem.actions(node.state)
        print("Generated successor states: ",successors)
        for i in range(len(actions)):
            child = Node(successors[i], node, actions[i],
                         node.path_cost+1)
            if (tuple(child.state) not in explored and
                child not in frontier):
                if (problem.goal_test(child.state)):
                    print("Found a solution! ", child)
                    path = child.solution_path()
                    child.display_path()
                    return path[0], path[1], child.path_cost, num_processed_nodes, max_len_frontier
                frontier.append(child)
        max_len_frontier = max(max_len_frontier, len(frontier))
        
                
    return None # failure




if __name__ == '__main__':
    print("Instantiating a 8-puzzle")
    grid = [[1,2,3],[7,4,0], [6,5,8]]

    myProb = EightPuzzleProb([1,2,0,4,5,3,7,8,6],[1,2,3,4,5,6,7,8,0])
    # myProb.print_prob()
    print() 

    # run breadth-first search on the instantiated problem
    solution = dfs(myProb)
    print("DFS returned",solution)