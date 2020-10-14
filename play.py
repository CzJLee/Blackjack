from game import Blackjack
from player import Player, Dealer
import pydealer

bj = Blackjack()
player = Player("Christian", 1000)
bj.add_player(player)

while True:
	print(bj.new_round())
	print("GAME OVER")
	print("")