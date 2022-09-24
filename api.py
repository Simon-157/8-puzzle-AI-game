from EightPuzzle import EightPuzzleProb
from dfs import dfs


def gameStart():
    print("Welcome to the 8-puzzle game\n" + "-" * 50 + "\n")

    start_state = input("Enter the initial state :")
    goal_state = input("Enter the initial state : ")
    start = [int(i) for i in start_state.split()]
    goal = [int(i) for i in goal_state.split()]

    if check_if_solvable(start):

        myProb = EightPuzzleProb(start, goal)
        # myProb.print_prob()
        print()
        # Calling the dfs function and printing the solution.
        solution = dfs(myProb)
        print("DFS returned",solution)
    print()
    print("sorry game state given is not solvable with this easy level method")