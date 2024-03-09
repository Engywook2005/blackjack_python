import numpy as np

from .playing_card import Card

class Deck:
    def __init__(self):
        self.cards = np.array([])

        denoms = list(range(2,11))
        faces_and_aces = ['j', 'q', 'k', 'a']
        suits = ['clubs', 'spades', 'diamonds', 'hearts']

        for f in faces_and_aces:
            denoms.append(f)

        for denom in denoms:
            for suit in suits:
                next_card = Card(suit, denom)
                self.cards = np.append(self.cards, [next_card])
        
    def shuffle_cards(self, reshuffle = False):
        if(not reshuffle) or (len(self.shuffle_cards) < 1):
            self.shuffled_cards = np.copy(self.cards)
        np.random.shuffle(self.shuffled_cards)
        return self.shuffled_cards
    
    def draw_card(self):
        dealed_card = self.shuffled_cards[0]
        self.shuffled_cards = np.delete(self.shuffled_cards, 0)
        return dealed_card
    
    def burn_card(self, card):
        np.append(self.shuffled_cards, [card])
    
