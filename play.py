import pydealer

deck = pydealer.Deck()
deck.shuffle()
hand = deck.deal(7)
hand.sort()
print(hand)