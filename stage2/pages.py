from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Stage2Start(Page):
    def is_displayed(self):
        return self.player.round_number == 1
    pass


class Stage2(Page):
    form_model = 'player'
    form_fields = ['choice']
    pass

# class RandomPickWait(Page): # according to the documetation, "Wait pages are necessary
#                             # when one player needs to wait for others to take some action before they can proceed. "
#                             # in this case, I dont think we need a waitpage
#     def is_displayed(self):
#         self.player.find_decision()
#         return self.player.round_number == Constants.num_rounds
#     pass

# anyway I think we should put a wait page here, for two reasons
#     1. to pick a random questions
#     2. also, I think we need everyone at the end of stage2 , and start random pick together

class RandomPickWait(WaitPage):
    title_text = "Please wait"
    body_text = "The computer will randomly select a question, and your will be paid according to your decision of this question."
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def after_all_players_arrive(self):
        for player in self.group.get_players():
                player.find_decision()

class RandomPick(Page):
    form_model = 'player'
    form_fields = ['payment_s2', 'total_payment']
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds
    pass


class Results(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds
    pass


class Survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'nationality', 'major', 'age']

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds
    pass


page_sequence = [
    Stage2Start,
    Stage2,
    RandomPickWait,
    RandomPick,
    Survey,
]
