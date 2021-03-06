#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working definition of individual class for ABM
 of environmental migration

@author: kelseabest
"""

#import packages
from matplotlib.colors import LinearSegmentedColormap
import random
import math
import numpy as np
import matplotlib.pyplot as plt

class Individual :
    next_uid = 1

    def __init__(self, ag_factor): #initialize
        self.unique_id = Individual.next_uid
        Individual.next_uid += 1
        self.age = random.randrange(1, 80, 1)
        gend_arr = ['M', 'F']
        self.gender = np.random.choice(gend_arr, 1)
        self.hh = None
        self.employment = None
        self.salary = 0
        self.employer = None
        self.can_migrate  = False
        self.head = False
        self.migrated = False
        self.ag_factor = ag_factor


    def age_up(self):
        self.age = self.age + 1

    def check_eligibility(self):
        #is the agent eligible to migrate?
        if self.age >= 14 and self.gender == 'M' and self.migrated == False:
            self.can_migrate = True

        #individuals look for work within community
    def find_work(self, hh_set, mig_util): #how will this connect to community later?
        #look for ag in own land first
        util_migrate = mig_util #global var
        poss_employers = []
        my_hh = hh_set[hh_set['hh_id'] == self.hh]
        if self.hh == None:
            return
        else:
            my_house = my_hh.loc[0,'household']

        if self.migrated == True:
            self.salary = util_migrate
            return
        else:
            pass
        #too young to work?
        if self.age < 14 and self.gender != 'M':
            self.employment = 'None'
            self.salary = 0
        #work in ag on own land
        elif my_house.land_impacted == False:
            self.employment = "SelfAg"
            self.salary = my_house.land_owned * self.ag_factor #random productivity value here
        else: #otherwise look for ag employment in community
            for a in hh_set['household']:
                if a.wtp >= my_house.wta and a.land_impacted == False:
                    poss_employers.append(a)
                if len(poss_employers) != 0:
                    employer = random.choice(poss_employers)
                    self.employer = employer
                    self.salary = (my_house.wta + employer.wtp)/2
                    self.employment = "OtherAg"
                    pay = self.salary
                    employer.employees.append(self)
                    employer.payments.append(pay)
                    hh_set.loc[(hh_set['household'] == employer), 'household'] = employer
