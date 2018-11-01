from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import numpy as np
import itertools
import random

author = 'Lunzheng Li'

doc = """
An empirical test on salience theory
It basicly all kinds of binary choice qustions displays in random order for each subjects
- find out in my old Ztree study, the order is random and same for all or is random for each(differently)
- also, I should  go with the old notation in Ztree because of the analysis codes
"""


class Constants(BaseConstants):
    name_in_url = 'salience2018'
    players_per_group = None
    num_rounds = 3

    # outcomes = [[50, 0], [20, 0], [15, 5], [20, 10]]
    # probabilities = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
    #
    # optionBs = []
    # for i in range(4):
    #     optionB = np.linspace(outcomes[i][0] - 0.5, outcomes[i][1] + 0.5, 8).tolist()
    #     optionB = [round(num * 2) / 2 for num in optionB]
    #     optionBs.append(optionB)
    #
    # ou_and_op = [outcomes[i] + optionBs[i] for i in range(4)]
    #
    # all_list = []
    # for i in itertools.product(ou_and_op, probabilities):
    #     all_list.append(i)
    #
    # # alllist is a list of tuples, two elements in one tuple ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.01)
    # # a list of payoffs and a prob
    # random.shuffle(all_list)

    all_list = [([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.9), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.05), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.9), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.99), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.1), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.75), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.01), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.05), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.1), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.5), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.1), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.75), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.95), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.05), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.95), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.01), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.99), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.75), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.5), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.01), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.9), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.05), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.75), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.01), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.9), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.99), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.95), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.5), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.5), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.95), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.25), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.1), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.99)]
class Subsession(BaseSubsession):
    def creating_session(self):
        # group or player, I need to figure this out
        for p in self.get_players():
            p.x1 = Constants.all_list[self.round_number - 1][0][0]
            p.x2 = Constants.all_list[self.round_number - 1][0][1]
            p.p1 = Constants.all_list[self.round_number - 1][1]
            p.p2 = round(1 - Constants.all_list[self.round_number - 1][1], 2)# check if every decimal works, make sure the numbers are right.
            p.s1 = Constants.all_list[self.round_number - 1][0][2]
            p.s2 = Constants.all_list[self.round_number - 1][0][3]
            p.s3 = Constants.all_list[self.round_number - 1][0][4]
            p.s4 = Constants.all_list[self.round_number - 1][0][5]
            p.s5 = Constants.all_list[self.round_number - 1][0][6]
            p.s6 = Constants.all_list[self.round_number - 1][0][7]
            p.s7 = Constants.all_list[self.round_number - 1][0][8]
            p.s8 = Constants.all_list[self.round_number - 1][0][9]

    pass


class Group(BaseGroup):

    pass


class Player(BasePlayer):
    choice1 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)
    choice2 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)
    choice3 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)
    choice4 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)
    choice5 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)
    choice6 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)
    choice7 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)
    choice8 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal,)

    x1 = models.FloatField()
    x2 = models.FloatField()
    p1 = models.FloatField()
    p2 = models.FloatField()
    s1 = models.FloatField()
    s2 = models.FloatField()
    s3 = models.FloatField()
    s4 = models.FloatField()
    s5 = models.FloatField()
    s6 = models.FloatField()
    s7 = models.FloatField()
    s8 = models.FloatField()
    pass
