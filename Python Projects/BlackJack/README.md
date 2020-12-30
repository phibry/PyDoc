# BlackJack

This is a terminal game

## Functionality

Computer Dealer
Human Player

Start with a nomal deck of cards,
a represenation of a deck will be created with python
with OOP


Computer Dealer -> Bank Role
Human Player -> places a bet
Deck with 52 Cards

PC start with 1 card face up and 1 card face down
P start with 2 cards face up

P goes first:
P Goal: Get close to a total value of 21 than the dealer does
    1. Hit(Receive another card)
    2. Stay(Stop Receiving Cards)
    We'll ignore actions like 'Insurande', 'Split', 'Double', 'Down'
    Maybe include later

Hit -> new card -> 3 cards -> sum
Stay -> 2 cards -> sum

After P turn:
If P under 21, PC hits until they either beat the P or the PC busts.

Game End: Player Busts
If P keeps hitting and goes over 21, they bust and lost the bet.
The game is then over and dealer collects the money

Game End: PC beats Player
After P-Turn: If P is under 21. Dealer then hits until they either beat the player or the PC busts.
PC sum higher than player sum and still under 21.

Game End: Player Wins

Special Rules:
    Face Cards (Jack, Queen, King) count as value of 10
    Aces can count as either 1 or 11, whichever value is preferable to the player
