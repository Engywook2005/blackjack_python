import numpy as np
import re

class BlackJackPlayer:

    # Should be able to pass game to this as well so we can keep raising the bet if we need to
    def __init__(self, game, initial_bank): 
        self.game = game
        self.initial_bank = initial_bank
        self.start_hand(self)
        self.stood = False
        self.bust = False

    def start_hand(self):    
        self.cards = np.array([])
        self.score = 0

    def initial_bet(self, initial_pot):
        self.game.pence_to_pot = initial_pot    

    def bet(self):
        pence_to_pot = self.game.pence_to_pot
        if pence_to_pot <= self.bank:
            self.game.add_to_pot(pence_to_pot)
            self.bank -= pence_to_pot
        else:
            # Need to throw some error here
            print('shite, we are broke bothers')
        
    
    def pass_turn(self):
        self.game.pass_turn()

    def stand(self): 
        self.bet()
        self.pass_turn()

    # Will need a double down here...
        
    def eval_card(self, card):
        pattern = r"^\d+(?:\.\d+)?$"
        is_number = re.match(pattern, card.denom) is not None
        aces = np.array(list([]))

        if(is_number):
            self.score += int(card.denom)
        elif(card.denom == 'face'):
            self.score += 10
        else: np.append(aces, [card])

        while len(self.aces) > 1:
            np.delete(self.aces, 0)
            if self.score < 11:
                self.score += 1
            else: 
                self.score += 11
                            
    def receive_card(self, card):
        np.append(self.cards, [card])
        self.eval_card(self, card) # Actually do this when all cards have been delivered by dealer
        # display or not display depending on whether this card is face-up or face-down

    def hit(self): 
        self.game.receive_card()
        # No additional bet here?
        self.game.pass_turn()




