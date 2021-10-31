#Two Winners in QuickDraw: Points Accumulation by card value with faces being (11, 12, 13), aces being 1; and by traditional poker rules.
import random
import math
print("")
print("'WELCOME TO QUICKDRAW'")
print("")
CardsDeck = {
  "Ace of Spades": 1, 
  "Deuce of Spades": 2, 
  "Three of Spades": 3, 
  "Four of Spades": 4,
  "Five of Spades": 5,
  "Six of Spades": 6,
  "Seven of Spades": 7,
  "Eight of Spades": 8,
  "Nine of Spades": 9, 
  "Ten of Spades": 10, 
  "Jack of Spades": 11,
  "Queen of Spades": 12, 
  "King of Spades": 13, 
  "Ace of Hearts": 1,
  "Deuce of Hearts": 2, 
  "Three of Hearts": 3,
  "Four of Hearts": 4,
  "Five of Hearts": 5,
  "Six of Hearts": 6,
  "Seven of Hearts": 7,
  "Eight of Hearts": 8,
  "Nine of Hearts": 9,
  "Ten of Hearts": 10,
  "Jack of Hearts": 11,
  "Queen of Hearts": 12,
  "King of Hearts": 13,
  "Ace of Clubs": 1,
  "Deuce of Clubs": 2,
  "Three of Clubs": 3,
  "Four of Clubs": 4,
  "Five of Clubs": 5,
  "Six of Clubs": 6, 
  "Seven of Clubs": 7,
  "Eight of Clubs": 8,
  "Nine of Clubs": 9, 
  "Ten of Clubs": 10,
  "Jack of Clubs": 11,
  "Queen of Clubs": 12,
  "King of Clubs": 13,
  "Ace of Diamonds": 1,
  "Deuce of Diamonds": 2,
  "Three of Diamonds": 3,
  "Four of Diamonds": 4,
  "Five of Diamonds": 5,
  "Six of Diamonds": 6,
  "Seven of Diamonds": 7,
  "Eight of Diamonds": 8,
  "Nine of Diamonds": 9,
  "Ten of Diamonds":10,
  "Jack of Diamonds": 11,
  "Queen of Diamonds": 12,
  "King of Diamonds": 13
  }
print("Cards and Their Points")
ShowDeck = print(CardsDeck)
ShowDeck
print("")
Shuffled = list(CardsDeck)
print("Please shuffle the deck...")
print("")
print("'Thank you!'")
print("")
random.shuffle(Shuffled)
print("'Referee Check!'")
Referee = print(Shuffled)
print("")
def Draw():
   print("'Take Your Hand'")
   print(random.sample(Shuffled, 5))
Draw()
print("")
print("Do you Like this Hand?")
like = True
if not like:
    Draw()
    like = True
print("")
def DrawAgain():
  like = False
DrawAgain()
print("")