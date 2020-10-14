import pydealer

from player import Player, Dealer

class Blackjack:
	def __init__(self, players = [], shoe_size = 1):
		self.dealer = Dealer("Dealer")
		self.shoe_size = shoe_size
		self.deck = self.new_deck()
		self.players = players

	def shuffle_deck_in_place(self):
		self.deck.shuffle()

	def new_deck(self):
		shoe = pydealer.Stack()

		for i in range(self.shoe_size):
			shoe.add(pydealer.Deck())
		
		shoe.shuffle()

		return shoe

	def add_player(self, player):
		# Expect player to be class Player
		self.players.append(player)
	
	def remove_player(self, player):
		# Expect player to be class Player
		# Remove player from blackjack table
		self.players.remove(player)
	
	def empty_hand(self, player):
		# Removes all cards from the players hand.
		player.hand.empty()
	
	def deal_card(self, player):
		# Deal one card from the top of self.deck to the player. Remove the card from deck. 
		player.hand.add(self.deck.deal(1))

	def deal_random_card(self, player):
		# Deal a random card from self.deck to the player. Remove the card from deck.
		player.hand.add(self.deck.random_card(remove=True))

	def set_cards(self, player, cards):
		# Set the hand to be cards. All other cards in hand are removed.
		player.set_cards(cards)

	# def check_natural(self, player):
	# 	# Return a list of players with natural 21
	# 	naturals = []

	# 	# Check if dealer has natural 21
	# 	if self.dealer.has_natural():
	# 		naturals.append(self.dealer)
		
	# 	# Check if player has natural 21
	# 	if player.has_natural():
	# 		naturals.append(player)

	# 	return naturals

	def hit(self, player):
		player.hand += self.deck.deal(1)

	def new_round(self, dealer, players):
		# Expect players to be a list of class Player

		# Create results list. Results will have the same number of elements as players, and each result matches a player. 
		results = [1 for player in players]
		# After the round has ended, return results. The value inside results is the payout to the player. 
		# 0 indicates that the player lost, and is paid nothing. 
		# 1 is a placeholder, and no scenario should return a 1. A 1 will return the players original bet. 
		# 2 indicates that a player beat the dealer, and the player is paid out equal to their original bet.
		# 2.5 indicates that the player beat the dealer and got a natural 21. 

		# Empty the hands of the dealer and players
		self.empty_hand(dealer)
		for player in players:
			self.empty_hand(player)

		# Deal new cards to dealer and players. 
		# Start with players, then dealer. Deal cards one at a time. 
		for i in range(2):
			for player in players:
				self.deal_card(player)
			self.deal_card(dealer)

		# Immediately after cards are dealt, check if anyone has a natural 21. 



# class Round():
# 	def __init__(self, dealer, players):
# 		# expect dealer to be class Dealer
# 		# expect players to be a list of class Player
		