
class Problem:
    """ This class represents a generic Problem to be solved by search."""

    def __init__(self, init_state, goal_state):
        self.init_state = init_state
        self.goal_state = goal_state

    def __str__(self):
        return (type(self).__name__ + ": Init state=" + str(self.init_state) +
                ", goal state=" + str(self.goal_state))
    
    def goal_test(self, state):
        return False

    def actions(self, state):
        return None, None
