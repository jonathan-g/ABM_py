#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the actual model with scheduling and steps for
 ABM of environmental migration

@author: kelseabest
"""

#import packages
from matplotlib.colors import LinearSegmentedColormap
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#initialize model
class ABM_Model:
    def __init__(self, N_hh, N, decision, mig_threshold):
        self.decision = decision #set decision type
        self.mig_threshold = mig_threshold #wealth threshold to migrate
        #self.network_structure = network_structure
        self.num_hh = N_hh #households
        self.num_individuals = N
        init_time = 0
        self.tick = init_time
        self.migrations = 0 #Initialize number of overall migrations

        #create individuals
        self.individual_set = pd.DataFrame()
        for i in range(self.num_individuals):
            ind = Individual()
            row = pd.DataFrame({'ind': [ind], 'id': [ind.unique_id],
                                'age': [ind.age],
                               'gender': [ind.gender]})
            self.individual_set = pd.concat([self.individual_set, row])

        # Create households
        self.household = pd.DataFrame() #empty list to store agents created
        for i in range(self.num_hh):
            a = Household()
            a.individuals = a.gather_members(self.individual_set)
            a.land_owned = a.assign_land(self.patch_list) #assign land ownership
            row = pd.DataFrame({'agent': [a], 'id': [a.unique_id], 'wtp': [a.wtp],
                               'wta': [a.wta], 'employer': [a.employer]})
            self.household = pd.concat([self.household, row])

        #for a in self.household['agent']:
            #a.set_network()


    def model_step(self): #model step does each
        random_sched = np.random.permutation(self.num_hh)
        #random schedule each time

        env.Shock()

        for i in random_sched: #these are the steps for each agent to go through
            #add seed
            agent_var = self.household[self.household.id == i].agent
            agent_var.check_network()
            agent_var.check_land()
            agent_var.look_for_work()
            agent_var.migrate()
            agent_var.update_wealth()

        self.tick += 1


    def data_collect: #use this eventually to collect model level data
        pass
