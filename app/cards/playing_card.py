class Card:
    def __init__(self, suit, denom):
        numbers = list(range(2, 11))
        numbers_as_string = map(str, numbers)
        face_cards = ['j', 'q', 'k']
        ace_cards = ['a']
        black_suits = ['clubs', 'spades']
        red_suits = ['diamonds', 'hearts']

        self.suit = suit
        self.designation = str(denom)
        if self.designation in numbers_as_string:
            self.card_type = 'num'
        elif self.designation in face_cards:
            self.card_type = 'face'
        elif self.designation in ace_cards:
            self.card_type = 'ace'
        else:
            self.card_type = 'joker'

        if suit in black_suits: 
            self.color = 'black'
        elif suit in red_suits:  
            self.color = 'red'
        else: 
            self.color = 'joker'

        return self
    
    def get_type(self):
        return self.card_type

    def get_designation(self):
        return self.designation

    def get_suit(self):
        return self.suit

    def get_color(self):
        return self.color 