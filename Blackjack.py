import random

#CREATE THE VALUES FOR CARDS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

#CREATE A CARD CLASS
class Card():
    
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return(f"{self.rank} of {self.suit}")

#CREATE A DECK CLASS
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(rank,suit))
    
    def __str__(self):
        list_of_cards = " "
        for card in self.deck:
            list_of_cards += "\n"+card.__str__()
        return(list_of_cards)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return(single_card)

#CREATE A HAND CLASS
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#CREATE A CHIPS CLASS
class Chips:
    
    def __init__(self,total=100):
        self.total = total # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#WRITE A FUNCTION FOR CREATING BETS
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips would you like to bet? "))
        except:
            print("Please enter a value.")
        else:
            if chips.bet > chips.total:
                print("You do not have enough chips. Please rebet.")
            else:
                print("Your bet has been accepted.")
                break

#FUNCTION FOR TAKING HITS
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#FUNCTION FOR HIT OR STAY
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        action = input("Press 1 to Hit or 2 to Stay: ")
        if action=="1":
            hit(deck,hand)
            
        elif action=="2":
            print("Stay. Dealer's turn.")
            playing = False
        else:
            print("Please enter 1 or 2.")
            continue
        break

#FUNCTION TO DISPLAY CARDS
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

#END GAME SCENARIOS
def player_busts(player,dealer,chips):
    print("You busted.")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("You win!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins.")
    chips.lose_bet()
    
def push(player,dealer):
    print("You pushed.")

#GAMEPLAY!
while True:
    # Print an opening statement
    print("Welcome to Blackjack!")
    
    # Create & shuffle the deck, deal two cards to each player
    game_deck = Deck()
    game_deck.shuffle()
    
    game_player_hand = Hand()
    game_dealer_hand = Hand()
    
    game_player_hand.add_card(game_deck.deal())
    game_dealer_hand.add_card(game_deck.deal())
    game_player_hand.add_card(game_deck.deal())
    game_dealer_hand.add_card(game_deck.deal())
    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(game_player_hand,game_dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(game_deck,game_player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(game_player_hand,game_dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if game_player_hand.value > 21:
            player_busts(game_player_hand,game_dealer_hand,player_chips)
            break

            
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if game_player_hand.value <= 21:
        
        while game_dealer_hand.value < 17:
                hit(game_deck,game_dealer_hand)
                
        # Show all cards
        show_all(game_player_hand,game_dealer_hand)
                       
        # Run different winning scenarios
        if game_dealer_hand.value > 21:
            dealer_busts(game_player_hand,game_dealer_hand,player_chips)

        elif game_player_hand.value > game_dealer_hand.value:
            player_wins(game_player_hand,game_dealer_hand,player_chips)

        elif game_player_hand.value < game_dealer_hand.value:
             dealer_wins(game_player_hand,game_dealer_hand,player_chips)

        else:
            push(game_player_hand,game_dealer_hand)
    
    # Inform Player of their chips total 
    print(f"Your current chip count is at: {player_chips.total}")
                       
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break