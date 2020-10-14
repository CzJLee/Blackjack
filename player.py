import pydealer

card_values = {
			"2": 2,
			"3": 3,
			"4": 4,
			"5": 5,
			"6": 6,
			"7": 7,
			"8": 8,
			"9": 9,
			"10": 10,
			"Jack": 10,
			"Queen": 10,
			"King": 10,
			"Ace": 11
			}

class Player:
	def __init__(self, player_name, wallet):
		self.hand = pydealer.Stack()
		self.name = player_name
		self.wallet = wallet

	def hand_value(self):
		# Take in a pydealer.Stack, and return the Blackjack value of the hand. 
		total = 0

		# Iterate over the cards in the hand and add the value to the total. 
		for card in self.hand.cards:
			total += card_values[card.value]

		if total <= 21:
			return total
		else:
			# If the total is over 21, check if there is an ace in the hand that can be reduced. 

			# Find the index of the Aces in the hand, if any, and count the number of elements in the list.
			# This is the number of Aces in the hand. 
			num_aces = len(self.hand.find("Ace"))
			
			# If the player has an ace in the hand, treat it as a 1. (Effectively reduces the total by 10.)
			while num_aces > 0 and total > 21:
				total -= 10
				num_aces -= 1
			
			# Return the total value. If there are not any Aces to reduce the value, then total will be greater than 21. 
			return total

	def has_natural(self):
		if self.hand.size == 2 and self.hand_value() == 21:
			return True
		else:
			return False

	def has_pair(self):
		if self.hand.size == 2 and card_values[self.hand.cards[0].value] == card_values[self.hand.cards[1].value]:
			return True
		else: 
			return False

# Make dealer class a subclass of Player class
class Dealer(Player):
	def __init__(self, player_name):
		super().__init__(player_name, 0)

	def hit(self):
		if self.hand_value() < 17:
			return True
		else:
			return False