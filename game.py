from app import Deck

deck = Deck()

deck.shuffle_cards()

new_card = deck.draw_card()

print({
    'color': new_card.get_color(),
    'suit': new_card.get_suit(),
    'denom': new_card.get_designation(),
    'card_type': new_card.get_type(),
    'face_up': new_card.get_face_up()
})