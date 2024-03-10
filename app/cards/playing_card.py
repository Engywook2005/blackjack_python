class Card:
    def __init__(self, suit, denom):
        numbers = list(range(2, 11))
        numbers_as_string = map(str, numbers)
        face_cards = ['j', 'q', 'k']
        ace_cards = ['a']
        black_suits = ['clubs', 'spades']
        red_suits = ['diamonds', 'hearts']

        self.suit = suit
        self.denom = str(denom)
        self.face_up = False
        if self.denom in numbers_as_string:
            self.card_type = 'num'
        elif self.denom in face_cards:
            self.card_type = 'face'
        elif self.denom in ace_cards:
            self.card_type = 'ace'
        else:
            self.card_type = 'joker'

        if suit in black_suits: 
            self.color = 'black'
        elif suit in red_suits:  
            self.color = 'red'
        else: 
            self.color = 'joker'
    
    def get_type(self):
        return self.card_type

    def get_denom(self):
        return self.denom

    def get_suit(self):
        return self.suit

    def get_color(self):
        return self.color 
    
    def get_face_up(self):
        return self.face_up 
    
    # The only setting that can be updated after card is created
    # If reshuffling will need to make sure car is facedown
    def set_face_up(self, reveal = None):
        if reveal == None:
            self.face_up = not self.face_up

