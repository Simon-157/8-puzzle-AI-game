from copy import deepcopy
from Problem import Problem

class EightPuzzleProb(Problem):


    def __init__(self, init_state, goal_state) -> None:
        super().__init__(init_state, goal_state)
    
    def __str__(self) -> str:
        return ""


    def goal_test(self, state):
        return self.goal_state == state

    
    def actions(self, state):
        state = deepcopy(state)
        index_blank = state.index(0)
        actions = []
        succ_states = []

        if index_blank==0:
            # state = deepcopy(state)
            actions=["R", "D"]
            succ_states.append(self.result_state(state, 'R'))
            succ_states.append(self.result_state(state, 'D'))
  
        if index_blank == 1 :
            # state = deepcopy(state)
            actions=["R", "L","D"]
            succ_states.append(self.result_state(state, 'R'))
            succ_states.append(self.result_state(state, 'L'))
            succ_states.append(self.result_state(state, 'D'))

        
        if index_blank == 2 :
            # state = deepcopy(state)
            actions=["L","D"]
            succ_states.append(self.result_state(state, 'L'))
            succ_states.append(self.result_state(state, 'D'))

        

        if index_blank == 3 :
            # state = deepcopy(state)
            actions=["R", "U","D"]
            succ_states.append(self.result_state(state, 'R'))
            succ_states.append(self.result_state(state, 'U'))
            succ_states.append(self.result_state(state, 'D'))

        if index_blank == 4 :
            # state = deepcopy(state)
            actions=["R", "L","D", "U"]
            succ_states.append(self.result_state(state, 'R'))
            succ_states.append(self.result_state(state, 'L'))
            succ_states.append(self.result_state(state, 'D'))
            succ_states.append(self.result_state(state, 'U'))

        if index_blank == 5 :
            # state = deepcopy(state)
            actions=["U", "L","D"]
            succ_states.append(self.result_state(state, 'U'))
            succ_states.append(self.result_state(state, 'L'))
            succ_states.append(self.result_state(state, 'D'))
      

        if index_blank == 6 :
            # state = deepcopy(state)
            actions=["U", "R"]
            succ_states.append(self.result_state(state, 'U'))
            succ_states.append(self.result_state(state, 'R'))

        if index_blank == 7 :
            # state = deepcopy(state)
            actions=["R", "L","U"]
            succ_states.append(self.result_state(state, 'R'))
            succ_states.append(self.result_state(state, 'L'))
            succ_states.append(self.result_state(state, 'U'))
                
          

        if index_blank == 8 :
            # state = deepcopy(state)
            actions=["L","U"]
            succ_states.append(self.result_state(state, 'L'))
            succ_states.append(self.result_state(state, 'U'))
       
        return actions, succ_states

            

    def result_state(self, state, action):
        blank_loc=state.index(0)
        if action=="U": 
            newstate=deepcopy(state)
            new_blank_loc=blank_loc-3
            newstate[new_blank_loc],newstate[blank_loc]=newstate[blank_loc],newstate[new_blank_loc]
        if action=="D": 
            newstate=deepcopy(state)
            new_blank_loc=blank_loc+3
            newstate[new_blank_loc],newstate[blank_loc]=newstate[blank_loc],newstate[new_blank_loc]

        if action=="L": 
            newstate=deepcopy(state)
            new_blank_loc=blank_loc-1
            newstate[new_blank_loc],newstate[blank_loc]=newstate[blank_loc],newstate[new_blank_loc]

        if action=="R": 
            newstate=deepcopy(state)
            new_blank_loc=blank_loc+1
            newstate[new_blank_loc],newstate[blank_loc]=newstate[blank_loc],newstate[new_blank_loc]
        return newstate



    # def actions(self, state):
    #     blank_loc = state.index(0)
    #     actions=[]
    #     succ_states = []
        
    #     if(blank_loc>2): 
    #         actions.append("U")
            
    #     if(blank_loc<6): 
    #         actions.append("D")
            
    #     if(blank_loc%3!=0): 
    #         actions.append("L")
            
    #     if blank_loc%3!=2: 
    #         actions.append("R")

    #     for action in actions:

    #         stae = self.result_state(state, action)      
    #         succ_states.append(stae)     
    #     return actions, succ_states
