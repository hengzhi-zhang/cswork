################################
# Hand Class:
################################

# This class will be useful as it can serve as a data structure to group
# each of a players cards together into one hand object. Think about the
# instance variables you will need to implement this class. For example,
# it would make sense to treat a hand as a list of Card objects. We also
# might need to know the size of the hand. Do we need an instance variable
# for this or would that be redundant information? Why or why not? Also,
# make sure to consider writing methods for the various actions that it may
# make sense to do with a hand.
from PIL import ImageTk, Image
from Card import Card
import Game
OFFSET = 75
CARD_HEIGHT = 96
CARD_STACK_NUMBER = 25
COMPUTER_TEXT_ROW = 150
PLAYER_TEXT_ROW = 325 

def setCardFront(card):
    card_file = 'cards/' + card['text'] + '.gif'
    image = ImageTk.PhotoImage(Image.open(card_file))
    card.config(image = image)
    card.image = image

class Hand(object):
    def __init__(self, hand):
        self.cards = hand

    def takeCard(self, card, opponent_hand):
        for o_card in opponent_hand.cards[::-1]:
            if str(card[1:]) == str(o_card['text'][1:]):
                opponent_hand.cards.remove(o_card)
                setCardFront(o_card)
                self.cards.append(o_card)

    def drawCard(self, deck, player_name):
        if deckHasCards(deck):
            card = deck.pop(0)
            self.cards.append(card)
            if player_name == 'Player':
                card_image = ImageTk.PhotoImage(Image.open('cards/'+card['text'] + '.gif'))
                card.config(image=card_image)
                card.image = card_image

    def checkForCard(self, card_info):
        player_card = card_info[1:]
        for card in self.cards:
            opponent_card = card['text'][1:]
            if player_card == opponent_card:
                return True
        return False

    def printHand(self, canvas, name, row, points, back_card=''):
        column = 0
        for card in self.cards:
            if back_card != '':
                card.config(image=back_card)
                card.image = back_card

            card.place(x=OFFSET + column * CARD_STACK_NUMBER, y = row*CARD_HEIGHT)
            card.lift()
            column = column + 1
            print(card['text'])
        print()
        canvas.create_text(250 + column * 25, row * 96  + 50, font='Times 20',
            text = name + 'Score: ' + str(points))

    def printDeck(canvas, deck, back_card):
        column = 0
        for card in deck:
            card.config(image=back_card)
            card.image = back_card
            card.place(x=75 + column*10, y=192)
            card.lower()
            column = column + 1

    def emptyHand(self):
        return len(self.cards) <= 0

    def draw7Cards(self, deck, name):
        for i in range(7):
            if deckHasCards(deck):
                card = deck.pop(0)  
                if name == 'Player':
                    setCardFront(card)
                self.cards.append(card)

    def checkPlayerHands(deck, player, computer):
        p_hand = player.hand
        c_hand = computer.hand
        if p_hand.emptyHand():
            p_hand.draw7Cards(deck, player.name)
        if c_hand.emptyHand():
            c_hand.draw7Cards(deck, computer.name)




    def checkForPairs(self, player, canvas):
        has_pairs = False
        hand = self.cards
        hand_length = len(hand)
        cards_to_remove = []
        indexes_to_remove = []

        for i in range(hand_length - 1):
            card1 = hand[i]['text']
            card1_num = card1[1:]
            for j in range(i+1, hand_length):
                card2 = hand[j]['text']
                card2_num = card2[1:]
                if card1_num == card2_num and card1 not in cards_to_remove and card2 not in cards_to_remove:
                    cards_to_remove.append(card1)
                    cards_to_remove.append(card2)
                    indexes_to_remove.append(i)
                    indexes_to_remove.append(j)
                    # prints out the card info
                    card1_info = Card.getCardNum(card1[1:]) + ' of ' + Card.getCardSuit(card1[1])
                    card2_info = Card.getCardNum(card2[1:]) + ' of ' + Card.getCardSuit(card2[:1])

                    row = PLAYER_TEXT_ROW if player.name == 'Player' else COMPUTER_TEXT_ROW
                    # print("POPPED CARD: " + card1)
                    the_pair = canvas.create_text(300, row, font='Times 20', text=player.name + ' has matched two ' + Card.getCardNum(card1[1:]) + 's')
                    Game.waitAndDeleteMessage(canvas, the_pair)
                    '''
                    message = player.name + ' has matched ' + card1_info + ' and ' + card2_info
                    box.insert(END, message)
                    '''
        # removes pairs from hand
        print('cards_to_remove: ' + str(cards_to_remove))
        indexes_to_remove.sort()

        for i in range(len(indexes_to_remove)-1, -1, -1):
            popped_card = hand.pop(indexes_to_remove[i])
            popped_card.destroy() # removes the card from the screen 

            if i % 2 == 0: # increment once for 2 cards
                player.increaseScore()
                has_pairs = True

        return has_pairs

def deckHasCards(deck):
    return len(deck) > 0