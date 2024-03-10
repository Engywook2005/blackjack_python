from app import Deck

# Will really just keep track of:
# What is in pot
# What phase it is (dealing, hit/stand, etc)
# Whose turn it is

deck = Deck()

deck.shuffle_cards()

new_card = deck.draw_card()

print({
    'color': new_card.get_color(),
    'suit': new_card.get_suit(),
    'denom': new_card.get_denom(),
    'card_type': new_card.get_type(),
    'face_up': new_card.get_face_up()
})