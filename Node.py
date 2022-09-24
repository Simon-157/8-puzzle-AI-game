import numpy as np

class Node:
    """ This class represents a node in the search tree"""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __hash__(self):
        return self.state.__hash__()

    def __str__(self):
        mystr = "Node with state=" + str(self.state);
        if (self.parent != None):
            mystr += (", parent=" + str(self.parent.state) +
                    ", action=" + str(self.action) +
                    ", path_cost=" + str(self.path_cost))
        return mystr


    def __eq__(self, other):
        return (isinstance(other,Node) and 
                self.state == other.state)
    
    
    def solution_path(self):

        seq_actions = []
        seq_states = []
        
        curr_node = Node(self.state, self.parent, self.action)
        while(curr_node.parent != None):
            seq_actions.insert(0, curr_node.action)
            seq_states.insert(0, curr_node.state)
            curr_node = curr_node.parent
            # print("move ---------------- ",curr_node.action)
            # print(np.array(curr_node.state).reshape(3,3))
        return seq_states, seq_actions


    def display_path(self, solution):
        states_at_action, actions_to_goal = solution[0], solution[1]

        for i in range(len(actions_to_goal)):
            print("action: ", actions_to_goal[i], " move ")
            print(np.array(states_at_action[i]).reshape(3,3))

        return None
