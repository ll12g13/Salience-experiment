from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

# import numpy as np
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
    num_rounds = 36
    
    
    # # # I tried to create the questions in otree. However, diffcult to get it work 
    # outcomes = [[50, 0], [20, 0], [15, 5], [20, 10]]
    # probabilities = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
    
    # optionBs = []
    # for i in range(4):
        # optionB = np.linspace(outcomes[i][0] - 0.5, outcomes[i][1] + 0.5, 8).tolist()
        # optionB = [round(num * 2) / 2 for num in optionB]
        # optionBs.append(optionB)
    
    # ou_and_op = [outcomes[i] + optionBs[i] for i in range(4)]
    
    # all_list = []
    # for i in itertools.product(ou_and_op, probabilities):
        # all_list.append(i)
    
    # # alllist is a list of tuples, two elements in one tuple ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.01)
    # # a list of payoffs and a prob
    # random.shuffle(all_list   
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    all_list = [([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.9), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.05), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.9), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.99), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.1), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.75), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.01), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.05), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.1), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.5), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.1), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.75), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.95), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.05), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.95), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.01), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.99), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.75), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.5), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.01), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.9), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.05), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.75), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.01), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.9), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.99), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.95), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.5), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.5), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.95), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.25), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.1), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.99)]
    # random.shuffle(all_list) # different session different order

    [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12, list13, list14, list15, list16,]  = 16 * [None,]
    lists = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12, list13, list14, list15, list16,]
    for i in range(1, 17):
        random.shuffle(all_list)
        lists[i-1] = all_list.copy()



class Subsession(BaseSubsession):
    def creating_session(self):
        # for i in range(1, 17):
        #     p = self.get_player_by_id(i) # it won't work, Since failed to create session: "'Subsession' object has no attribute 'get_player_by_id'"
        i = 0
        for p in self.get_players():
            p.x1 = Constants.lists[i][self.round_number - 1][0][0]
            p.x2 = Constants.lists[i][self.round_number - 1][0][1]
            p.p1 = Constants.lists[i][self.round_number - 1][1]
            p.p2 = round(1 - Constants.lists[i][self.round_number - 1][1], 2)# check if every decimal works, make sure the numbers are right.
            p.s1 = Constants.lists[i][self.round_number - 1][0][2]
            p.s2 = Constants.lists[i][self.round_number - 1][0][3]
            p.s3 = Constants.lists[i][self.round_number - 1][0][4]
            p.s4 = Constants.lists[i][self.round_number - 1][0][5]
            p.s5 = Constants.lists[i][self.round_number - 1][0][6]
            p.s6 = Constants.lists[i][self.round_number - 1][0][7]
            p.s7 = Constants.lists[i][self.round_number - 1][0][8]
            p.s8 = Constants.lists[i][self.round_number - 1][0][9]
            i += 1
        # it seems that for now, I get it right. We can understand the creating_sessions function in this way:
        #     in round one, it starts with i = 0, then loop from p1 to p16, and i becomes 15
        #     in round two, it starts with i = 0 again....

        #
        # # # group or player, I need to figure this out
        # for p in self.get_players():
        #     p.x1 = Constants.all_list[self.round_number - 1][0][0]
        #     p.x2 = Constants.all_list[self.round_number - 1][0][1]
        #     p.p1 = Constants.all_list[self.round_number - 1][1]
        #     p.p2 = round(1 - Constants.all_list[self.round_number - 1][1], 2)# check if every decimal works, make sure the numbers are right.
        #     p.s1 = Constants.all_list[self.round_number - 1][0][2]
        #     p.s2 = Constants.all_list[self.round_number - 1][0][3]
        #     p.s3 = Constants.all_list[self.round_number - 1][0][4]
        #     p.s4 = Constants.all_list[self.round_number - 1][0][5]
        #     p.s5 = Constants.all_list[self.round_number - 1][0][6]
        #     p.s6 = Constants.all_list[self.round_number - 1][0][7]
        #     p.s7 = Constants.all_list[self.round_number - 1][0][8]
        #     p.s8 = Constants.all_list[self.round_number - 1][0][9]

        # # # let's shuffle the questions
        # # # I tried several ways, however, cannot get it done

        # question_id = list(range(5)) # it seems that if we do not put this thing in under an if statement, it will only run once, make sure about this !!!
                                    # it's not working!!! same question keep coming out.
        # we need to figure out how to pass var between rounds,
        
        # # # # the following block of codes are written in the office , let try it at home
        # # # # the idea is to create a shuffled list in round 1 and pass it to the following rounds
        
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        # for p in self.get_players():
        
            # # if self.round_number == 1:
            # #     question_id = list(range(5))  # figure out where to put it.
            # #     random.shuffle(question_id)# put the shuffle code here is not gonna work
            # #                             # since: If your app has multiple rounds, creating_session gets run multiple times consecutively:
            # #                              # OK, now we only let the code run once when round_number == 1
            # # elif self.round_number > 1:
        
            # p.x1 = Constants.all_list[question_id[self.round_number - 1]][0][0]
            # p.x2 = Constants.all_list[question_id[self.round_number - 1]][0][1]
            # p.p1 = Constants.all_list[question_id[self.round_number - 1]][1]
            # p.p2 = round(1 - Constants.all_list[question_id[self.round_number - 1]][1], 2)  # check if every decimal works, make sure the numbers are right.
            # p.s1 = Constants.all_list[question_id[self.round_number - 1]][0][2]
            # p.s2 = Constants.all_list[question_id[self.round_number - 1]][0][3]
            # p.s3 = Constants.all_list[question_id[self.round_number - 1]][0][4]
            # p.s4 = Constants.all_list[question_id[self.round_number - 1]][0][5]
            # p.s5 = Constants.all_list[question_id[self.round_number - 1]][0][6]
            # p.s6 = Constants.all_list[question_id[self.round_number - 1]][0][7]
            # p.s7 = Constants.all_list[question_id[self.round_number - 1]][0][8]
            # p.s8 = Constants.all_list[question_id[self.round_number - 1]][0][9]

        
        # for p in self.get_players():
            # p.x1 = p.shuffled_all_list[self.round_number - 1][0][0]
            # p.x2 = p.shuffled_all_list[self.round_number - 1][0][1]
            # p.p1 = p.shuffled_all_list[self.round_number - 1][1]
            # p.p2 = round(1 - p.shuffled_all_list[self.round_number - 1][1], 2)# check if every decimal works, make sure the numbers are right.
            # p.s1 = p.shuffled_all_list[self.round_number - 1][0][2]
            # p.s2 = p.shuffled_all_list[self.round_number - 1][0][3]
            # p.s3 = p.shuffled_all_list[self.round_number - 1][0][4]
            # p.s4 = p.shuffled_all_list[self.round_number - 1][0][5]
            # p.s5 = p.shuffled_all_list[self.round_number - 1][0][6]
            # p.s6 = p.shuffled_all_list[self.round_number - 1][0][7]
            # p.s7 = p.shuffled_all_list[self.round_number - 1][0][8]
            # p.s8 = p.shuffled_all_list[self.round_number - 1][0][9]
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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


    # # # I made following fields just for testing purpose, remember to get it back before the real sessions
    # choice1 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)
    # choice2 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)
    # choice3 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)
    # choice4 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)
    # choice5 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)
    # choice6 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)
    # choice7 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)
    # choice8 = models.StringField(choices=['A', 'B',], widget=widgets.RadioSelectHorizontal, blank=True)

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
    
    
    # # # I tried to shuffle the lst in the player class, however, seems not work
    # shuffled_all_list = [([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.9), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.05), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.9), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.99), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.1), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.75), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.01), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.05), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.1), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.5), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.1), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.75), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.95), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.05), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.95), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.01), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.99), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.75), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.5), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.01), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.9), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.05), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.75), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.01), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.9), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.25), ([15, 5, 14.5, 13.0, 12.0, 10.5, 9.5, 8.0, 7.0, 5.5], 0.99), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.95), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.5), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.5), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.95), ([20, 0, 19.5, 17.0, 14.0, 11.5, 8.5, 6.0, 3.0, 0.5], 0.25), ([20, 10, 19.5, 18.0, 17.0, 15.5, 14.5, 13.0, 12.0, 10.5], 0.1), ([50, 0, 49.5, 42.5, 35.5, 28.5, 21.5, 14.5, 7.5, 0.5], 0.99)]
    #
    # random.shuffle(shuffled_all_list)

    # question_id = models.StringField() # set a field here, i think this should be the solution, since different player have different questhin order
                                         # another stupid way is to create 16 different list.
                                         # this seems very complicated, I need to get a long string and transfer it back to lst, and shuffle
    pass
