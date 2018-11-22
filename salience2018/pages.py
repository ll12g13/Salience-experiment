from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
    def is_displayed(self):
        return self.player.round_number == 1
    pass


class Stage1Start(Page):
    def is_displayed(self):
        return self.player.round_number == 1
    pass


class Stage1(Page):
    form_model = 'player'
    form_fields = ['choice1','choice2','choice3','choice4','choice5','choice6','choice7','choice8',]
    pass


page_sequence = [
    # WelcomePage,
    # Stage1Start,
    Stage1,
]
