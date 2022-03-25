"""Blackjack game using OOP concepts as taught by Jose Portilla in the Udemy course, 2022 Complete Python Bootcamp: From Zero to Hero in Python. Also utilizing methods 
    and concepts as taught by the tutorial in the the Python documentation at Python.org"""
    
    
"""1.) Need to create a simple text-based Blackjack game.
   2.) The game needs to have one player versus an automated dealer.
   3.) The player can stand or hit.
   4.) The player must be able to pick their betting amount.
   5.) Need to keep track of the player's total money.
   6.) Need to alert the player of wins, losses, or busts, etc."""

    
import random

"""lists and dict for building card and deck objects"""
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 
         'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
          'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

  
class Card:
    # creating card objects
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit 


class Deck:
    # take in the Card class and the building blocks for each card and generate a deck object
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # requires Card class to be defined
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        """shuffle deck"""
        random.shuffle(self.all_cards)
        
    def deal_card(self):
        """deal a card from the deck"""
        return self.all_cards.pop(0)


class Player:
    
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        
    def __str__(self):
        return f'Player: {self.name}. \nTotal Cash: ${self.cash}.'
        
    def place_bet(self):
        while True:
            elected_bet = int(input('Please enter a bet: '))
            if elected_bet > self.cash:
                print('You do not have enough cash to place that bet.')
                print('Your current balance is ', self.cash)
                pass
            else:
                self.cash -= elected_bet
                return elected_bet
            
    def show_hand(self, cards):
        """method to show player and dealers hands, taking list input"""
        print("{}'s hand: ".format(self.name))
        for card in cards:
            print('{} '.format(card))
        print('\n')
                    
    def won_hand(self, bet):
        """method to add cash to winner's account"""
        bet *= 2
        self.cash += bet
        
    def lost_hand(self, bet):
        self.cash -= bet
        
    def double_down(self, card_one, card_two):
        """method checking down for double down condition and asking player
            to double down or not. Returns 'y' affirming"""
        if ((card_one.value + card_two.value == 9) or
            (card_one.value + card_two.value == 10) or
            (card_one.value + card_two.value == 11)):
            will_double = input("Would you like to double down? (y) or (no): ")
            return will_double.lower() == 'y'
    
    def soft_hand(self, card_one, card_two):
        """method checking if player would like to change value of ace
            depending upon soft condition"""
        if ((card_one.rank == 'Ace' and card_two.value != 10) or
        (card_one.value != 10 and card_two.rank == 'Ace')):
            change_value = input('Would you like to play the Ace with a value of 1? (y) or (n): ')
            change_value.lower()
            if change_value != 'y':
                card_one.value = 11
                return card_one.value
            else:
                card_one.value = 1
                return card_one.value
    
    def hit(self):
        """method for checking if player would like to hit"""
        hit = input("Would you like to hit? (y) or (n): ")
        if hit == 'y':
            return True
        else:
            return False


def natural(card_one, card_two):
    """Global function to check if inital cards dealt were a combination of an Ace and a card valued at 10."""    
    return  (card_one.rank == 'Ace' and card_two.value == 10) or (card_one.value == 10 and card_two.rank == 'Ace')


def is_splittable(card_one, card_two):  
    """Global function to check if dealt cards are splittable."""
    return(card_one.rank == card_two.rank)


def sum_cards(cards):
    """Global function to sum hand totals"""
    sum_of = 0
    for card in cards:
        sum_of += card.value
    return sum_of


def keep_playing():
    """Global function to ask if player would like to keep playing"""
    to_play = input("Would you like to play another hand? (y) or (no): ")
    if to_play.lower() == 'y':
        pass
    else:
        return False


print("Welcome to Blackjack!")
print("The object of the game is to either achieve a total of 21 or have a total card value higher than the dealer AND less than 21.")
print("Non-face cards will have a value equivalent to their digit.")
print("Face cards will all have values equivalent to 10, except for Aces that can equal 1 or 11 at your discretion.")
print("Before each hand, you will be asked to place a wager.")
print("Make your wager and the dealer will match, then proceed to deal cards.")
print("The dealer will deal a total of two cards to the each of you.")
print("Your two cards will be played face up. The dealer's card will be placed face down.")
print("You may elect to 'double down' (d) and double your initial bet once the cards have been dealt.")  
print("You will then to elect to 'hit' (y) or 'stay' (n)")
print("Special conditions:")
print("If your first two cards are an Ace AND either a 10 or face card, you atuomatically win 1.5 times your bet amount. If the dealer holds a natural, automatic loss.")
print("If your first two cards are the same denomination, you may elect to 'split' in which you one card will be turned into a second hand you must match your original bet.")
print('\n')

player_name = input("Please enter your name: ")
player_cash = int(input("What is your cash amount: "))
player = Player(player_name, player_cash)
dealer = Player('House', 10000000)
print('\n')


at_table = True
playing = True

while at_table:

    while playing:
        
        # Lists to hold player and dealer cards.
        player_hand = []
        dealer_hand = []
        
        # Variable assignment for player bet.
        bet_placed = player.place_bet()     
        print('\n')
        
        # Create and shuffle deck.
        deck = Deck()
        deck.shuffle()
        
        # Dealing cards
        player_hand.append(deck.deal_card())
        dealer_hand.append(deck.deal_card())
        player_hand.append(deck.deal_card())
        dealer_hand.append(deck.deal_card())
        
        # Show player and dealer cards
        print("Dealer's cards:")
        print(dealer_hand[0])
        print('\n') 
        player.show_hand(player_hand)
        print('\n')
        
        # Check if player hand is soft, and ask if they'd like to alter the value of an Ace
        player.soft_hand(player_hand[0], player_hand[1])
        print('\n')
        
        # Calculate hand totals
        player_sum = sum_cards(player_hand)
        dealer_sum = sum_cards(dealer_hand)
        
        # Check for automatic win condition
        if natural(player_hand[0], player_hand[1]):
            bet_placed *= 1.5
            player.won_hand(bet_placed)
            dealer.show_hand(dealer_hand)
            player.show_hand(player_hand)
            print("Player wins.")
            print(player)
            print('\n')
            continue
        elif natural(dealer_hand[0], dealer_hand[1]):
            dealer.won_hand(bet_placed)
            dealer.show_hand(dealer_hand)
            player.show_hand(player_hand)
            print("House wins.")
            print(player)
            print('\n')
            continue
        else:
            pass
        
        # Give player option to double down.
        double_it = player.double_down(player_hand[0], player_hand[1])
        if double_it:
            print("Doubled Down")    
            bet_placed *= 2
        else:
            pass
        
        # Loop to allow player to repeatedly hit, unless they opt otherwise. Then Break out of loop.
        while player_sum < 21:
            if player.hit():
                print("Player hits.")
                player_hand.append(deck.deal_card())
                player_sum = sum_cards(player_hand)
                player.show_hand(player_hand)
                player_sum = sum_cards(player_hand)
                if player_sum == 21:
                    break
                elif player_sum >= 17 and player_sum < 21:
                    continue
                elif player_sum < 17:
                    continue
                else:
                    break
            else:
                dealer.show_hand(dealer_hand)
                player.show_hand(player_hand)
                print("Player stands.")
                print('\n')
                break
        
        if player_sum > 21:
            dealer.won_hand(bet_placed)
            dealer.show_hand(dealer_hand)
            player.show_hand(player_hand)
            print("House wins.")
            print('\n')
            print(player)
            break
        else:
            pass

        # Loop for dealer play
        dealer.show_hand(dealer_hand)
        
        while dealer_sum < 21:        
            if dealer_sum == 21:
                break
            elif dealer_sum > 17 and dealer_sum < 21:
                print("Dealer stands")
                print('\n')
                break
            elif dealer_sum < 17:
                dealer_hand.append(deck.deal_card())
                dealer_sum = sum_cards(dealer_hand)
                dealer.show_hand(dealer_hand)
                player.show_hand(player_hand)
                print('\n')
                continue
            else:
                break
        
        # Dealer bust if greater than 21
        if dealer_sum > 21:
            dealer.won_hand
            dealer.show_hand(dealer_hand)
            player.show_hand(player_hand)
            print("Player wins.")
            print(player)
            print('\n')
            break
        else:
            pass
        
        # Check whether player or dealer won
        if ((player_sum < 21 and player_sum > dealer_sum) or
            (player_sum == 21)):
            player.won_hand(bet_placed)
            dealer.show_hand(dealer_hand)
            player.show_hand(player_hand)
            print("Player wins.")
            print(player)
            print('\n')
            break
        else:
            dealer.won_hand(bet_placed)
            dealer.show_hand(dealer_hand)
            player.show_hand(player_hand)
            print("House wins")
            print(player)
            print('\n')
            break
        
        
        

    # Check if player still has cash and still want's to play        
    if player.cash < 0 or player.cash == 0:
        print('\n')
        print(player)
        print("You are out of money.")
        play_more = input("Would you like to play more? (y) or (n): ")
        if play_more == 'y':
            player_sum = int(input("How much would you like to add to your cash?: "))
        else:
            break
        