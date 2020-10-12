import pydealer

from player import Player, Dealer

# Create dealer and player class
dealer = Dealer()
player = Player()

# Create and shuffle deck of shoe size 1
deck = pydealer.Deck()
deck.shuffle()

def deal_cards(dealer, player):
	dealer.hand = deck.deal(2)
	player.hand = deck.deal(2)

def check_natural(dealer, player):
	# Return a list of players with natural 21
	naturals = []

	# Check if dealer has natural 21
	if dealer.has_natural():
		naturals.append(dealer)
	
	# Check if player has natural 21
	if player.has_natural():
		naturals.append(player)

	return naturals

def hit(player):
	player.hand += deck.deal(1)

