# Blackjack

The goal of this project is to build a working text based Blackjack game, using the standard rules as [described on the Bicycle website](https://bicyclecards.com/how-to-play/blackjack/). Then, I will use this game to determine the optimal play for a given situation by using a Monte Carlo simulation. 

- [Blackjack](#blackjack)
	- [Basic Rules](#basic-rules)
		- [The Shoe](#the-shoe)
		- [Payouts](#payouts)
		- [Dealer's Play](#dealers-play)
		- [Optional Rules](#optional-rules)
	- [Dependencies](#dependencies)
	- [How to Play](#how-to-play)
	- [Questions I Want To Answer](#questions-i-want-to-answer)

## Basic Rules
While most Blackjack rules are standard, some rules may vary. Here is a brief description of the rules that might be specific to this version. 

### The Shoe
Multiple decks may be shuffled together to form the "shoe". The size of the shoe can be defined. A large shoe is used to mitigate card counting. 

### Payouts
A player win against the dealer pays out equal to the original bet. For example, if the player bet $100, and wins against the dealer, the player earns $100. 

If the player gets a natural 21 and the dealer does not, the dealer pays out 1.5 times the original bet. For example, if the player bet $100, and gets a natural 21, the player earns $150. 

If the player loses against the dealer, the player loses their original bet. 

### Dealer's Play
The dealer is dealt one card face up, and one card face down. If the dealer is dealt a natural 21, then the round ends. Any player with a natural 21 will tie, all other players lose. 

The dealer will continue to take cards until their total is greater than or equal to 17. 

### Optional Rules
Splitting pairs is always allowed. 

Enabling Insurance is optional.

Enabling Settlement is optional. 

## Dependencies
Blackjack uses [pydealer](https://github.com/Trebek/pydealer) to handle card and deck classes. 

## How to Play
The main game is located in `play.py`. 

```python3 play.py```

## Questions I Want To Answer

- What is the probability of getting dealt a natural 21?
- If you hit with a hand value of x, what is the probability of busting? 
- If you stand with a hand value of x, what is the probability of winning?
- If you have a pair of x, should you split?
- What is the ideal move in each hand value situation?
- Does a change in shoe size change these probabilities?
- How do I format the data to answer all of these questions?