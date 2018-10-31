from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
author = 'Lunzheng Li'

doc = """
This the stage 2 + survey for the salience paper.
"""


class Constants(BaseConstants):
    name_in_url = 'stage2'
    players_per_group = None
    num_rounds = 3

    # let make up some questions, just to test the app
    # all_list = [[(14, 0.1),(4, 0.9),(0, 0),(5,1),(0,0),(0,0)], [(14, 0.1),(4, 0.9),(0, 0),(5,1),(0,0),(0,0)], [(14, 0.1),(4, 0.9),(0, 0),(5,1),(0,0),(0,0)]]
    all_list = [[14, 4, 0, 0.1, 0.9, 0, 5, 0, 0, 1, 0, 0], [19, 9, 0, 0.1, 0.9, 0, 10, 0, 0, 1, 0, 0], [21, 13, 0, 0.25, 0.75, 0, 15, 0, 0, 1, 0, 0]]
class Subsession(BaseSubsession):
    def creating_session(self):
        # group or player, I need to figure this out
        for p in self.get_players():
            p.xa1 = Constants.all_list[self.round_number - 1][0]
            p.xa2 = Constants.all_list[self.round_number - 1][1]
            p.xa3 = Constants.all_list[self.round_number - 1][2]
            p.pa1 = Constants.all_list[self.round_number - 1][3]
            p.pa2 = Constants.all_list[self.round_number - 1][4]
            p.pa3 = Constants.all_list[self.round_number - 1][5]
            p.xb1 = Constants.all_list[self.round_number - 1][6]
            p.xb2 = Constants.all_list[self.round_number - 1][7]
            p.xb3 = Constants.all_list[self.round_number - 1][8]
            p.pb1 = Constants.all_list[self.round_number - 1][9]
            p.pb2 = Constants.all_list[self.round_number - 1][10]
            p.pb3 = Constants.all_list[self.round_number - 1][11]

        # the idea is that  at the begining of the experiment we pick the random question for player, and
        # show it at the end of the experiment

        if self.round_number == Constants.num_rounds: # if we set round_number = 1, result page will give us None. Since the result
            for p in self.get_players():             # caculate at the last round, we should set round_number to Constants.num_rounds
                p.paying_question = random.randint(1, Constants.num_rounds)
                p.paying_xa1 = Constants.all_list[p.paying_question - 1][0]
                p.paying_xa2 = Constants.all_list[p.paying_question - 1][1]
                p.paying_xa3 = Constants.all_list[p.paying_question - 1][2]
                p.paying_pa1 = Constants.all_list[p.paying_question - 1][3]
                p.paying_pa2 = Constants.all_list[p.paying_question - 1][4]
                p.paying_pa3 = Constants.all_list[p.paying_question - 1][5]
                p.paying_xb1 = Constants.all_list[p.paying_question - 1][6]
                p.paying_xb2 = Constants.all_list[p.paying_question - 1][7]
                p.paying_xb3 = Constants.all_list[p.paying_question - 1][8]
                p.paying_pb1 = Constants.all_list[p.paying_question - 1][9]
                p.paying_pb2 = Constants.all_list[p.paying_question - 1][10]
                p.paying_pb3 = Constants.all_list[p.paying_question - 1][11]
    pass



class Group(BaseGroup):


    pass


class Player(BasePlayer):

    # the payment in stage 2
    payment_s2 = models.FloatField()
    # the total payment
    total_payment = models.FloatField()

    choice = models.StringField(
        choices=['A', 'B',],
        widget=widgets.RadioSelectHorizontal,
    )
    # stage2
    xa1 = models.FloatField()
    xa2 = models.FloatField()
    xa3 = models.FloatField()
    pa1 = models.FloatField()
    pa2 = models.FloatField()
    pa3 = models.FloatField()

    xb1 = models.FloatField()
    xb2 = models.FloatField()
    xb3 = models.FloatField()
    pb1 = models.FloatField()
    pb2 = models.FloatField()
    pb3 = models.FloatField()

    # survey
    gender = models.StringField(blank=True,
                                choices=['M', 'F', 'Other', 'Prefer not to answer'],
                                widget=widgets.RadioSelectHorizontal,
                                )
    nationality = models.StringField(blank=True)
    major = models.StringField(blank=True)
    year_of_study = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)

    # randompick
    paying_question = models.IntegerField()

    paying_xa1 = models.FloatField()
    paying_xa2 = models.FloatField()
    paying_xa3 = models.FloatField()
    paying_pa1 = models.FloatField()
    paying_pa2 = models.FloatField()
    paying_pa3 = models.FloatField()

    paying_xb1 = models.FloatField()
    paying_xb2 = models.FloatField()
    paying_xb3 = models.FloatField()
    paying_pb1 = models.FloatField()
    paying_pb2 = models.FloatField()
    paying_pb3 = models.FloatField()

    paying_choice = models.StringField() # this is the player's choice for the paying round

    dice1 = models.StringField()
    dice2 = models.StringField()
    dice3 = models.StringField()

    # def find_decision(self):# not sure how it works, if I put it in the random pick page, it give us
    #                         # '<' not supported between instances of 'NoneType' and 'int', I guess it because we haven't get all the decisions
    #     self.paying_choice = self.in_round(self.paying_question).choice
    def find_decision(self):
        list10 = [i for i in range(1, 10)]
        list10.append(0)
        list100 = [i for i in range(1,100)]
        list100.append(0)
        if self.round_number == Constants.num_rounds:
            self.paying_choice = self.in_round(self.paying_question).choice
            # let's work oon the dice statement, how dice number related to payment
            # it seems that we can define the dice number under this function
            # if self.paying_choice == 'A':
            #     if self.paying_pa1 in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            #         if self.paying_pa1 + self.paying_pa2 == 1:
            #             dice1_lst = list10[0:10*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list10[10*self.paying_pa1::]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #         elif self.paying_pa1 + self.paying_pa2 + self.paying_pa3== 1:
            #             dice1_lst = list10[0:10*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list10[10*self.paying_pa1:10*(self.paying_pa1+self.paying_pa2)]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #             dice3_lst = list10[10*(self.paying_pa1+self.paying_pa2)::]
            #             self.dice3 = ''.join(str(e) for e in dice3_lst)
            #     else:
            #         if self.paying_pa1 + self.paying_pa2 == 1:
            #             dice1_lst = list100[0:100*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list100[100*self.paying_pa1::]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #         elif self.paying_pa1 + self.paying_pa2 + self.paying_pa3== 1:
            #             dice1_lst = list100[0:100*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list100[100*self.paying_pa1:100*(self.paying_pa1+self.paying_pa2)]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #             dice3_lst = list100[100*(self.paying_pa1+self.paying_pa2)::]
            #             self.dice3 = ''.join(str(e) for e in dice3_lst)
            # else:
            #     if self.paying_pa1 in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            #         if self.paying_pa1 + self.paying_pa2 == 1:
            #             dice1_lst = list10[0:10*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list10[10*self.paying_pa1::]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #         elif self.paying_pa1 + self.paying_pa2 + self.paying_pa3== 1:
            #             dice1_lst = list10[0:10*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list10[10*self.paying_pa1:10*(self.paying_pa1+self.paying_pa2)]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #             dice3_lst = list10[10*(self.paying_pa1+self.paying_pa2)::]
            #             self.dice3 = ''.join(str(e) for e in dice3_lst)
            #     else:
            #         if self.paying_pa1 + self.paying_pa2 == 1:
            #             dice1_lst = list100[0:100*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list100[100*self.paying_pa1::]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #         elif self.paying_pa1 + self.paying_pa2 + self.paying_pa3== 1:
            #             dice1_lst = list100[0:100*self.paying_pa1]
            #             self.dice1 = ''.join(str(e) for e in dice1_lst)
            #             dice2_lst = list100[100*self.paying_pa1:100*(self.paying_pa1+self.paying_pa2)]
            #             self.dice2 = ''.join(str(e) for e in dice2_lst)
            #             dice3_lst = list100[100*(self.paying_pa1+self.paying_pa2)::]
            #             self.dice3 = ''.join(str(e) for e in dice3_lst)
            #         else:
            #             self.dice1 = 1

 # retrieve the xs in the chosen option
# the above block aabout the dice statement is super complicated and something might be worng
#  let's figure out everything using a raw python file. We bulid a function which input
#  a list of numbers like in Constants list, and output a dice statement
#  let make every other thing work, tackle this problem in the end.





    pass

