# -*- coding: utf-8 -*-
import random
import math
import numpy as np
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """ An agent that learns to drive in the Smartcab world.
    This is the object you will be modifying. """

    def __init__(self, env, learning=False, epsilon=1.0, alpha=0.5, gamma=0.0):
        super(LearningAgent, self).__init__(env)     # Set the agent in the evironment
        self.planner = RoutePlanner(self.env, self)  # Create a route planner
        self.valid_actions = self.env.valid_actions  # The set of valid actions

        # Set parameters of the learning agent
        self.learning = learning # Whether the agent is expected to learn
        self.Q = dict()          # Create a Q-table which will be a dictionary of tuples
        self.epsilon = epsilon   # Random exploration factor
        self.alpha = alpha       # Learning factor

        # -----------
        # TO DO
        # -----------
        # Set any additional class parameters as needed
        self.gamma = gamma      # discount factor
        self.train_cnt = 0      # training count


    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
        'testing' is set to True if testing trials are being used
        once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)

        # -----------
        # TO DO
        # -----------
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0

        # -----------
        # Implement a Q-Learning Driving Agent
        # -----------
        # In addition, use the following decay function for  ϵϵ :
        #
        #  ϵt+1=ϵt−0.05,for trial number t
        #
        #  If you have difficulty getting your implementation to work, try
        #  setting the 'verbose' flag to True to help debug. Flags that have
        #  been set here should be returned to their default setting when
        #  debugging. It is important that you understand what each flag does
        #  and how it affects the simulation!
        #

        if testing == True:
           self.epsilon = 0
           self.alpha = 0
        else:
            if self.learning and self.train_cnt is not 0:
                # -----------
                # Implement a Q-Learning Driving Agent
                # -----------
                # Note: default Q learning epsilon function
                #  self.epsilon -= 0.05

                # Note: epsilon function variation
                self.epsilon = self.alpha * math.pow( self.alpha, self.train_cnt/5.0 )

                # Note: Another epsilon function
                # self.epsilon = 1/(self.train_cnt)**2
                # self.epsilon = math.e**(-self.alpha*self.train_cnt)
                # self.epsilon = math.cos(self.alpha * self.train_cnt)

        self.train_cnt += 1.0
        return None

    def build_state(self):
        """ The build_state function is called when the agent requests data from the
        environment. The next waypoint, the intersection inputs, and the deadline
        are all features available to the agent. """

        # Collect data about the environment
        waypoint = self.planner.next_waypoint() # The next waypoint
        inputs = self.env.sense(self)           # Visual input - intersection light and traffic
        deadline = self.env.get_deadline(self)  # Remaining deadline

        # -----------
        # TO DO   #
        # -----------
        # Set 'state' as a tuple of relevant data for the agent
        state = {
            "waypoint": waypoint,
            "light": inputs["light"],
            "oncoming": inputs["oncoming"],
            "left": inputs["left"],
        }

        return state


    def get_maxQ_value(self, state):
        """ The get_max_Q function is called when the agent is asked to find the
        maximum Q-value of all actions based on the 'state' the smartcab is in. """

        # -----------
        # TO DO
        # -----------
        # Calculate the maximum Q-value of all actions for a given state

        maxQ = None
        for action in self.valid_actions:
            Qvalue_cursor = self.Q_value_for(state, action)
            if  maxQ is None or Qvalue_cursor > maxQ:
                maxQ = Qvalue_cursor

        return maxQ

    def get_maxQ_action(self, state):
        """Using the status value received from the parameter, the ACTION with
        the highest Q value in the current state is obtained."""

        maxQaction = None
        maxQvalue = None
        for action in self.valid_actions:
            Qvalue_cursor = self.Q_value_for(state, action)
            if maxQvalue is None or Qvalue_cursor > maxQvalue:
                maxQvalue = Qvalue_cursor
                maxQaction = action
        return maxQaction


    def createQ(self, state):
        """ The createQ function is called when a state is generated by the agent. """

        # -----------
        # TO DO
        # -----------
        # When learning, check if the 'state' is not in the Q-table
        # If it is not, create a new dictionary for that state
        #   Then, for each action available, set the initial Q-value to 0.0

        key = self.Q_key_for(state)
        if not self.Q.has_key(key):
            for action in self.valid_actions:
                self.Q[key] = dict()
                self.Q[key][action] = 0.0

        return

    def Q_value_for(self, state, action):
        key = self.Q_key_for(state)
        if self.Q.has_key(key):
            if self.Q[key].has_key(action):
                return self.Q[key][action]
        return 0.0

    def Q_key_for(self, state):
        return "waypoint:{}|light:{}|oncoming:{}|left:{}".format(state["waypoint"], state["light"], state["oncoming"], state["left"])


    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
        which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = None

        # -----------
        # TO DO
        # -----------
        # When not learning, choose a random action
        # When learning, choose a random action with 'epsilon' probability
        #   Otherwise, choose an action with the highest Q-value for the current state
        action = random.choice(self.valid_actions)

        if self.learning:
            # choose the best action according to Q-function
            maxQ_action = self.get_maxQ_action(state)

            # # choose intended action with probaility epsilon
            # probs = np.array([self.epsilon]+[(1.0-self.epsilon) / len(self.valid_actions)]*len(self.valid_actions))
            # probs /= probs.sum()                        # to nomalize probabilities
            # random_action = np.random.choice([self.next_waypoint]+self.valid_actions, 1, replace=False, p = probs )[0]

            # In the selection of ACTION, ignore the WAYPOINT and select the complete random action.
            # choose intended action with probaility epsilon
            random_action = np.random.choice(self.valid_actions, 1)[0]

            # choose the best antion or intended action with probability epsilon
            # if training will be done and testing is about to begin, epsilon
            # will be 0.0 then we always choose the best action

            print "probability epsilon : {}".format(self.epsilon)
            action = np.random.choice([random_action, maxQ_action], 1, replace=False, p = [self.epsilon, 1.0-self.epsilon] )[0]
        return action


    def learn(self, state, action, reward):
        """ The learn function is called after the agent completes an action and
        receives an award. This function does not consider future rewards
        when conducting learning. """

        # -----------
        # TO DO
        # -----------
        # When learning, implement the value iteration update rule
        #   Use only the learning rate 'alpha' (do not use the discount factor 'gamma')
        if self.learning:
            cur_value = self.Q_value_for(state, action)
            new_state = self.build_state()

            # The reason for exclusion of future rewards will be discussed in
            # the last rubric (Q9) : 
            # learned_value = reward +  (self.gamma * self.get_maxQ_value(new_state))

            # Since our example does not consider future REWARDs, the value of
            # self.gamma is set to an initial value of 0.0.
            # Note: self.gamma = 0.0
            learned_value = reward +  self.gamma * self.get_maxQ_value(new_state)
            new_value = cur_value + (self.alpha * (learned_value - cur_value))

            key = self.Q_key_for(state)
            self.Q[key][action] = new_value
        return


    def update(self):
        """ The update function is called when a time step is completed in the
        environment for a given trial. This function will build the agent
        state, choose an action, receive a reward, and learn if enabled. """

        state = self.build_state()          # Get current state
        self.createQ(state)                 # Create 'state' in Q-table
        action = self.choose_action(state)  # Choose an action
        reward = self.env.act(self, action) # Receive a reward
        self.learn(state, action, reward)   # Q-learn

        return


def run():
    """ Driving function for running the simulation.
    Press ESC to close the simulation, or [SPACE] to pause the simulation. """

    # ------------------
    # Create the environment
    # Flags:
    #   verbose     - set to True to display additional output from the simulation
    #   num_dummies - discrete number of dummy agents in the environment, default is 100
    #   grid_size   - discrete number of intersections (columns, rows), default is (8, 6)
    env = Environment(verbose=False)

    # ------------------
    # Create the driving agent
    # Flags:
    #   learning   - set to True to force the driving agent to use Q-learning
    #    * epsilon - continuous value for the exploration factor, default is 1
    #    * alpha   - continuous value for the learning rate, default is 0.5
    agent = env.create_agent(LearningAgent, learning=True, epsilon=1.0, alpha=0.8, gamma=0.0 )

    # ------------------
    # Follow the driving agent
    # Flags:
    #   enforce_deadline - set to True to enforce a deadline metric
    env.set_primary_agent(agent, enforce_deadline=True)

    # ------------------
    # Create the simulation
    # Flags:
    #   update_delay - continuous time (in seconds) between actions, default is 2.0 seconds
    #   display      - set to False to disable the GUI if PyGame is enabled
    #   log_metrics  - set to True to log trial and simulation results to /logs
    #   optimized    - set to True to change the default log file name

    # Simulation variables are initialized for real-time learning agent construction.
    #  sim = Simulator(env, display=True, update_delay=0.1, log_metrics=True)
    sim = Simulator(env, display=False, update_delay=0.00005, log_metrics=True, optimized=True, discounted=False)

    # ------------------
    # Run the simulator
    # Flags:
    #   tolerance  - epsilon tolerance before beginning testing, default is 0.05
    #   n_test     - discrete number of testing trials to perform, default is 0
    sim.run(n_test=10, tolerance=0.00000000000001)


if __name__ == '__main__':
    run()
