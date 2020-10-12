import pydealer

from player import Player, Dealer

class Blackjack:
	def __init__(self, shoe_size = 1):
		self.dealer = Dealer("Dealer")
		self.shoe_size = shoe_size
		self.deck = self.new_deck()

	def shuffle_deck_in_place(self):
		self.deck.shuffle()

	def new_deck(self):
		shoe = pydealer.Stack()

		for i in range(self.shoe_size):
			shoe.add(pydealer.Deck())
		
		shoe.shuffle()

		return shoe

	def deal_cards(self, player):
		self.dealer.hand = self.deck.deal(2)
		player.hand = self.deck.deal(2)

	def check_natural(self, player):
		# Return a list of players with natural 21
		naturals = []

		# Check if dealer has natural 21
		if self.dealer.has_natural():
			naturals.append(self.dealer)
		
		# Check if player has natural 21
		if player.has_natural():
			naturals.append(player)

		return naturals

	def hit(self, player):
		player.hand += self.deck.deal(1)