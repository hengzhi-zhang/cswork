################################
# Game:
################################

# This is where your game logic will reside. A game will have several instance 
# variables such as 2+ players, a deck of cards(possible modeled as a list 
# of Card objects), a status such as GAME_OVER or IN_PROGRESS (perhaps we 
# can model these as class variables and treat them like constants). It also 
# may be helpful to include some methods in this class to deal with animation
# so that it is easier to implement your game from within the SkeletonGraphics 
# framework
from Player import Player
from Card import Card
from Hand import Hand
from random import *
COMPUTER_ROW = 0
PLAYER_ROW = 4
ONE_SECOND = 1000
COMPUTER_TEXT_ROW = 150
PLAYER_TEXT_ROW = 325 

class Game(object):

    def createPlayersAndHands(self, deck):
        p_hand = []
        c_hand = [] 

        for i in range(10):
            card = deck.pop(0)
            if i % 2 == 0:
                p_hand.append(card)
            else:
                c_hand.append(card)
        self.player = Player('Player', p_hand)
        self.computer = Player('Computer', c_hand)

    def printCardsToCanvas(self, canvas):
        c_points = self.computer.score
        p_points = self.player.score
        self.computer.hand.printHand(canvas, self.computer.name, COMPUTER_ROW, c_points, self.back_card)
        Hand.printDeck(canvas, self.deck, self.back_card)
        self.player.hand.printHand(canvas, self.player.name, PLAYER_ROW, p_points)

    def playerTurn(self, canvas, model, card_info):
        c_hand = self.computer.hand
        p_hand = self.player.hand
        deck = self.deck
        p_name = self.player.name
        player = self.player

        askForCard(canvas, card_info, PLAYER_TEXT_ROW)
        canvas.after(ONE_SECOND)
        opponent_has_card = c_hand.checkForCard(card_info)

        self.opponentResponse(canvas, p_name, opponent_has_card, card_info)
        has_pairs = p_hand.checkForPairs(player, canvas)

        Hand.checkPlayerHands(deck, self.player, self.computer)
        self.checkWinner(canvas)

        return has_pairs    

    def computerTurn(self, canvas, model):
        c_hand = self.computer.hand
        p_hand = self.player.hand
        deck = self.deck
        c_name = self.computer.name
        computer = self.computer

        random_num = randint(0, len(c_hand.cards)-1)
        card = c_hand.cards[random_num]
        card_info = card['text']

        askForCard(canvas, card_info, COMPUTER_TEXT_ROW)
        canvas.after(ONE_SECOND)
        opponent_has_card = p_hand.checkForCard(card_info)

        self.opponentResponse(canvas, c_name, opponent_has_card, card_info)
        has_pairs = c_hand.checkForPairs(computer, canvas)

        Hand.checkPlayerHands(deck, self.player, self.computer)
        self.checkWinner(canvas)

        return has_pairs


    def opponentResponse(self, canvas, name, has_card, card_info):
        response = None
        opponent = 'Computer'
        opponent_hand = self.computer.hand
        p_hand = self.player.hand
        opponent_row = COMPUTER_TEXT_ROW

        if name == 'Computer':
            opponent = 'Player'
            opponent_hand = self.player.hand
            p_hand = self.computer.hand
            opponent_row = PLAYER_TEXT_ROW

        card_num = Card.getCardNum(card_info[1:])
        if has_card:
            response = canvas.create_text(300, opponent_row, font='Times 20', 
                text='Yes, I have a ' + card_num + ', here you go')
        else:
            response = canvas.create_text(300, opponent_row, font='Times 20', 
                text='No, I don\'t have a ' + card_num + ', go fish')
        waitAndDeleteMessage(canvas, response)

        if has_card:
            p_hand.takeCard(card_info, opponent_hand)
        else:
            p_hand.drawCard(self.deck, name)

    def checkWinner(self, canvas):
        p_hand = self.player.hand.cards
        p_name = self.player.name
        p_score = self.player.score

        c_hand = self.computer.hand.cards
        c_name = self.computer.name
        c_score = self.computer.score 

        deck = self.deck
        print("checking")

        if len(p_hand) + len(c_hand) + len(deck) == 0:
            print("winner")
            winner_text = 'It\'s a tie, there is no winner'
            if p_score > c_score:
                winner_text = 'The winner is ' + p_name
            elif c_score > p_score:
                winner_text = 'The winner is ' + c_name
            canvas.create_text(300, 200, font='Times 30', 
                text=winner_text)
            canvas.update()
            canvas.after(10000)


    def __init__(self):
        self.player = None
        self.computer = None
        self.deck = []
        self.back_card = None

def askForCard(canvas, card_info, row):
    card_num = card_info[1:]
    card_name = Card.getCardNum(card_num)

    question = canvas.create_text(300, row, font='Times 20',
        text='Do you have a ' + card_name + '?')
    waitAndDeleteMessage(canvas, question)
    
def waitAndDeleteMessage(canvas, text):
    canvas.update()
    canvas.after(1500)
    canvas.delete(text)
    canvas.update()

        
        
