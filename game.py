import pydealer
from time import sleep

from player import Player, Dealer

suits_char = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}
values_char = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10", "Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"}

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
		player.hand.set_cards(cards)

	def check_natural(self, dealer, players):
		# Return a list of players with natural 21
		naturals = []

		# Check if dealer has natural 21
		if dealer.has_natural():
			naturals.append(dealer)
		
		# Check if player has natural 21
		for player in players:
			if player.has_natural():
				naturals.append(player)

		return naturals

	def print_hand_dealer(self):
		# Print dealers hand, hiding second card.
		print(f"Dealer's Hand: {values_char[self.dealer.hand.cards[0].value]}{suits_char[self.dealer.hand.cards[0].suit]}, ??")

	def print_hand(self, player):
		# Prints the players current hand. 

		# Make a list of all the players cards
		hand_text = []
		for card in player.hand.cards:
			hand_text.append(f"{values_char[card.value]}{suits_char[card.suit]}")
		hand_text_str = ", ".join(hand_text)
		# Print players hand
		print(f"{player.name}'s Hand: {hand_text_str}")

		# Print players hand_value
		print(f"{player.name}'s Hand Value: {player.hand_value()}")

	def new_round(self):
		dealer = self.dealer
		players = self.players
		# Expect players to be a list of class Player

		# Create results list. Results will have the same number of elements as players, and each result matches a player. 
		results = []
		# After the round has ended, return results. The value inside results is the payout to the player. 
		# 0 indicates that the player lost, and is paid nothing. 
		# 1 indicates a tie. A 1 will return the players original bet. 
		# 2 indicates that a player beat the dealer, and the player is paid out equal to their original bet.
		# 2.5 indicates that the player beat the dealer and got a natural 21. 

		# Empty the hands of the dealer and players
		self.empty_hand(dealer)
		for player in players:
			self.empty_hand(player)

		# Deal new cards to dealer and players. 
		print("Dealing cards...")
		# Start with players, then dealer. Deal cards one at a time. 
		for i in range(2):
			for player in players:
				self.deal_card(player)
			self.deal_card(dealer)

		# Immediately after cards are dealt, check if anyone has a natural 21. 
		naturals = self.check_natural(dealer, players)
		if naturals:
			# Someone has a natural 21
			if isinstance(naturals[0], Dealer):
				# Dealer has a natural 21
				print("Dealer has a natural 21. The round is over.")
				# The round is over. 
				# If any player also has a natural, they will tie. All other players lose. 
				results = [1 if player in naturals else 0 for player in players]
				return results
			# else:
			# 	# Only players have a natural 21
			# 	# The round does not end. 
			# 	results = [2.5 if player in naturals else 0 for player in players]
		
		# It is now the players turn. 
		# Go one player at a time. 
		for player in players:
			if player.has_pair():
				# Give player the option to split
				pass

			self.print_hand_dealer()
			self.print_hand(player)
			
			player_turn = not player.has_natural()
			# player_turn is False if he player has a natural 21. 
			while player.hand_value() < 21 and player_turn:
				get_player_input = True
				# Ask whether to hit or stand as long as get_player_input is true. 
				while get_player_input:
					player_input = input("Hit or Stand?: ")
					if player_input in ["h", "H", "hit", "Hit", "HIT"]:
						self.deal_card(player)
						get_player_input = False
					elif player_input in ["s", "S", "stand", "Stand", "STAND"]:
						get_player_input = False
						# Players Turn is over
						player_turn = False

				self.print_hand_dealer()
				self.print_hand(player)
			
			# If player.hand_value() > 21, they bust.
			if player.hand_value() > 21:
				print("Player Busts!")
		
		# All players have finished their turn. 
		# Dealers turn now. 
		print("All players have finished their turn.")
		print("Dealer's turn...")
		while dealer.hit():
			self.deal_card(dealer)
		self.print_hand(dealer)

		print("Determining winners...")
		for player in players:
			if player.has_natural():
				# Player got natural 21, set result = 2.5
				results.append(2.5)
			elif player.hand_value() > 21:
				# Player busts, set result = 0
				results.append(0)
			elif dealer.hand_value() > 21:
				# Dealer busts, set result = 2
				results.append(2)
			elif player.hand_value() > dealer.hand_value():
				# Player beat dealer, set result = 2
				results.append(2)
			elif player.hand_value() < dealer.hand_value():
				# Player loses to dealer, set result = 0
				results.append(0)
			elif player.hand_value() == dealer.hand_value():
				# player ties dealer, set result = 1
				results.append(1)
		
		return results
