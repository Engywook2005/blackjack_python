from app import Deck

deck = Deck()

deck.shuffle_cards()

new_card = deck.draw_card()

print(new_card)