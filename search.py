# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
   
def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    visited = []
    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    
    while not queue.isEmpty():
        current, path = queue.pop()
        if current in visited:
            continue
        visited.append(current)
        if problem.isGoalState(current):
            return path
        for nearby in problem.getSuccessors(current):
            queue.push((nearby[0], path + [nearby[1]]))

    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startNode=problem.getStartState()
    if problem.isGoalState(startNode):
        return []
    checkedNodes=[]
    priority_queue=util.PriorityQueue()
    priority_queue.push((startNode,[],0),0)
    while not priority_queue.isEmpty():
        node_tmp,act_history,cost_tmp=priority_queue.pop()
        if node_tmp not in checkedNodes:
            checkedNodes.append(node_tmp)
            if problem.isGoalState(node_tmp):
                return act_history
            for node_future,act_future,cost_future in problem.getSuccessors(node_tmp):
                act_next=act_history+[act_future]
                priority=cost_tmp+cost_future
                priority_queue.push((node_future,act_next,priority),priority)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    "*** YOUR CODE HERE ***"
    visited = []
    startNode = problem.getStartState()
    priority_queue = util.PriorityQueue()
    priority_queue.push((startNode, [], 0), 0)
    while not priority_queue.isEmpty():
        node, act_history, cost = priority_queue.pop()
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return act_history
            for neighbor, act_future, cost_future in problem.getSuccessors(node):
                act_next = act_history + [act_future]
                cost_next = cost + cost_future
                priority = cost_next + heuristic(neighbor, problem)
                priority_queue.push((neighbor, act_next, cost_next), priority)
                
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
