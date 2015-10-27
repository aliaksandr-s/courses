# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        hnd = ""
        for card in range(len(self.cards)):
            hnd += self.cards[card].suit + self.cards[card].rank + " "
        return hnd

    def add_card(self, card):
        if (card.suit in SUITS) and (card.rank in RANKS):
            self.cards.append(card)
            
    
    def busted(self):
        if self.get_value() > 21:
            return True
        else:
            return False

    def get_value(self):
        value = 0
        ace = False
        for card in range (0, len(self.cards)):
            value += VALUES[self.cards[card].rank]
            if self.cards[card].rank == 'A':
                ace = True
        if ace and value + 10 <= 21:
            value += 10
        return value
    
    def draw(self, canvas, p):
        for count in range (1, len(self.cards)):
            self.cards[count].draw(canvas, [p[0] + CARD_CENTER[0] + count * (35 + CARD_SIZE[0]), p[1] + CARD_CENTER[1]])
       
    
# define deck class 
class Deck:
    def __init__(self):
        self.cards = [Card(SUITS[i], RANKS[j]) for i in range (0, len(SUITS)) for j in range (0, len(RANKS))]

    def shuffle(self):
        self.__init__()
        random.shuffle(self.cards)

    def deal_card(self):
        
        card_dealt = self.cards.pop(0)
        return card_dealt
    
    def __str__(self):
        result = ""
        for count in range (0, len(self.cards)):
            result += self.cards[count].suit + self.cards[count].rank + "\n"
        return result



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, new_deck, dealer_hand, score

    new_deck = Deck()
    new_deck.shuffle()
    outcome = ""
    
    player_hand = Hand()
    player_hand.add_card(new_deck.deal_card())
    player_hand.add_card(new_deck.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal_card())
    dealer_hand.add_card(new_deck.deal_card())
    
    if in_play:        
        outcome = "You lose."
        score -= 1
    
    in_play = True
#    print dealer_hand,  player_hand, "dealer hand:", dealer_hand.get_value(), "player hand:", player_hand.get_value()
    
def hit():
    global in_play, player_hand, new_deck, score, outcome
    
    if in_play:
        player_hand.add_card(new_deck.deal_card())
        
    if player_hand.busted():
        outcome = "You went bust and lose." 
        score -= 1
        in_play = False
        
#    print dealer_hand,  player_hand, "dealer hand:", dealer_hand.get_value(), "player hand:", player_hand.get_value(), outcome

    
def stand():
    global dealer_hand, player_hand, new_deck, in_play, score, outcome
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(new_deck.deal_card())

    # assign a message to outcome, update in_play and score
        if player_hand.busted():
            outcome = "You have busted."
        else:
            if dealer_hand.busted():
                outcome = "Dealer went busted and you win."
                score += 1
            elif dealer_hand.get_value() < player_hand.get_value():
                outcome = "You win."
                score += 1
            else:
                outcome = "You lose."
                score -= 1
        in_play = False
        
#    print dealer_hand,  player_hand, "dealer hand:", dealer_hand.get_value(), "player hand:", player_hand.get_value(), outcome

    

# draw handler    
def draw(canvas):
    global in_play, dealer_hand, player_hand
    
    canvas.draw_text("Blackjack", [100, 100], 35, "Black")
    canvas.draw_text("Score " + str(score), [450, 100], 25, "Black")
    canvas.draw_text("Dealer", [80, 170], 25, "Black")
    canvas.draw_text(outcome, [200, 170], 25, "Black")
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [60 + CARD_BACK_SIZE[0], 170 + CARD_BACK_SIZE[1]], CARD_SIZE)
    else:
        dealer_hand.cards[0].draw(canvas, [60 + CARD_CENTER[0], 170 + CARD_CENTER[1]])
    dealer_hand.draw(canvas, [60, 170])
    
    canvas.draw_text("Player", [80, 370], 25, "Black")
    
    if in_play:
        canvas.draw_text("Hit or stand?", [200, 370], 25, "Black")
    else:
        canvas.draw_text("New deal?", [200, 370], 25, "Black")
    
    player_hand.cards[0].draw(canvas, [60 + CARD_CENTER[0], 370 + CARD_CENTER[1]])
    player_hand.draw(canvas, [60, 370])


# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()

# get things rolling
frame.start()


# remember to review the gradic rubric
