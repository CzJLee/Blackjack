import pydealer

from game import Blackjack
from player import Player, Dealer
from time import sleep

natural_hand = pydealer.Stack()
natural_hand.add(pydealer.Card("Ace", "Spades"))
natural_hand.add(pydealer.Card("Jack", "Diamonds"))

bj = Blackjack()
player = Player("Player Name", 1000)

print("\n"*10)
print(f"Welcome {player.name} to Crazy Casino Blackjack!")

print(f"You have ${player.wallet}.")

# bet = int(input("Place your bets: "))
bet = 10
player.wallet -= bet

print(f"{player.name} bet ${bet}.")
print()

print("Dealing cards...")
sleep(0.5)

bj.deal_cards(player)

print(f"Dealer's Hand: {bj.dealer.hand.cards[0].value}, ?")
print(f"Player's Hand: {player.hand.cards[0].value}, {player.hand.cards[1].value}")
print(f"Player's Hand Total Value: {player.hand_value()}")
print()

naturals = bj.check_natural(player)
if naturals:
	# Someone has a natural 21
	if isinstance(naturals[0], Dealer):
		# Dealer has a natural 21
		# Check if there are players who also have natural 21
		if len(naturals) > 1:
			# Dealer and Player have a natural 21
			print("Dealer and Player both have a natural 21. You tie.")
			player.wallet += bet
		else:
			# Only dealer has a natural 21
			print("Dealer has a natural 21. Sorry, you lose this round.")
	
	else:
		# Only player has a natural 21
		print(f"Player has a natural 21! You win ${int(bet * 1.5)}.")
		player.wallet += bet * 2.5

player_turn = True
while player.hand_value() < 21 and player_turn:
	get_player_input = True
	while get_player_input:
		player_input = input("Hit or Stand?: ")
		if player_input in ["h", "H", "hit", "Hit", "HIT"]:
			bj.hit(player)
			print(f"Dealer's Hand: {bj.dealer.hand.cards[0].value}, ?")
			player_cards = []
			for i in range(player.hand.size):
				player_cards.append(player.hand.cards[i].value)
			print(f"Player's Hand: {player_cards}")
			print(f"Player's Hand Total Value: {player.hand_value()}")
			print()
			get_player_input = False
		elif player_input in ["s", "S", "stand", "Stand", "STAND"]:
			get_player_input = False
			player_turn = False
	
if player.hand_value() > 21:
	print("PLAYER BUSTS!")
	print("Sorry, you lose")
else:
	print("Player Stands.")
	player_cards = []
	for i in range(player.hand.size):
		player_cards.append(player.hand.cards[i].value)
	print(f"Player's Hand: {player_cards}")
	print(f"Player's Hand Total Value: {player.hand_value()}")
	print()

print("Dealer's Turn.")

dealer_cards = []
for i in range(bj.dealer.hand.size):
	dealer_cards.append(bj.dealer.hand.cards[i].value)
print(f"Dealer's Hand: {dealer_cards}")
print(f"Dealer's Hand Total Value: {bj.dealer.hand_value()}")
print()
while bj.dealer.hit():
	bj.hit(bj.dealer)
	dealer_cards = []
	for i in range(bj.dealer.hand.size):
		dealer_cards.append(bj.dealer.hand.cards[i].value)
	print(f"Dealer's Hand: {dealer_cards}")
	print(f"Dealer's Hand Total Value: {bj.dealer.hand_value()}")
	print()