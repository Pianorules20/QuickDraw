import random
import math
print("")
print("'WELCOME TO QUICKDRAW'")
print("")
Hand = []
DiscardPile = []
CardsDeck = [
  "Ace of Spades",
  "Ace of Hearts",
  "Ace of Clubs",
  "Ace of Diamonds",
  "Deuce of Spades",
  "Deuce of Hearts",
  "Deuce of Clubs",
  "Deuce of Diamonds",
  "Three of Spades",
  "Three of Hearts",
  "Three of Clubs",
  "Three of Diamonds",
  "Four of Spades",
  "Four of Hearts",
  "Four of Clubs",
  "Four of Diamonds",
  "Five of Spades",
  "Five of Hearts",
  "Five of Clubs",
  "Five of Diamonds",
  "Six of Spades",
  "Six of Hearts",
  "Six of Clubs",
  "Six of Diamonds",
  "Seven of Spades",
  "Seven of Hearts",
  "Seven of Clubs",
  "Seven of Diamonds",
  "Eight of Spades",
  "Eight of Hearts",
  "Eight of Clubs",
  "Eight of Diamonds",
  "Nine of Spades",
  "Nine of Hearts",
  "Nine of Clubs",
  "Nine of Diamonds",
  "Ten of Spades",
  "Ten of Hearts",
  "Ten of Clubs",
  "Ten of Diamonds",
  "Jack of Spades",
  "Jack of Hearts",
  "Jack of Clubs",
  "Jack of Diamonds",
  "Queen of Spades",
  "Queen of Hearts",
  "Queen of Clubs",
  "Queen of Diamonds",
  "King of Spades",
  "King of Hearts",
  "King of Clubs",
  "King of Diamond",
  ]
print("Cards and Their Points")
print("")
print("Ace = 1 Point.   Deuce = 2 Points.   Numbered Cards = Points By Number.   Jack  = 11 Points.   Queen = 12 Points.   King = 13 Points.")
print("")
print("How to Win:")
print("")
print("Two Ways To Win!! 1st Winner is Declared by Traditional Poker Rules.  2nd Winner is Declared by Most Points Held. Winners split the earnings.")
print("")
print("How to Play:")
print("")
print("Begin with 5 Cards.  You may pay a chip for a new deal, twice.   You may pay a chip  for up to 6 New Cards, drawn one at a time, taking turns.  Each turn you may pay any number of chips for an equal number of cards from which you choose only one.  The last round is the 'Draw' round.  Bet chips to make your opponent fold.  Fold to protect yourself from losing chips. ")
print("")
Shuffled = CardsDeck
print("Please shuffle the deck...")
#user input
#insert delay
print("")
print("'Thank you!'")
#print("'Referee Check!'") # for testing
#Referee = print(Shuffled) # for testing
print("")
print("Let's Deal, Shall We?")
#user input
#insert delay
print("")
TriesLeft = 3
def Deal():
  random.shuffle(Shuffled)
  NewList = Shuffled
  global TriesLeft
  TriesLeft = TriesLeft
  global Hand
  Hand = Hand
  global DiscardPile
  DiscardPile= DiscardPile
  Hand.append(NewList[0])
  Hand.append(NewList[1])
  Hand.append(NewList[2])
  Hand.append(NewList[3])
  Hand.append(NewList[4])
  NewList.pop(0)
  NewList.pop(0)
  NewList.pop(0)
  NewList.pop(0)
  NewList.pop(0)
  #print(len(Hand))
  print("")
  print(Hand)
  global Like
  Like = False
  print(f"Tries Left = {TriesLeft -1}")
  TriesLeft -=1
  print("Do You Like This Hand?")
  #user input
print("Look at your Hand")
Deal()
print("")
if TriesLeft >= 0:
  Deal()
  Like = True
  print("")
  DiscardPile.append(Hand[0:5])
  Hand.pop(0)
  Hand.pop(0)
  Hand.pop(0)
  Hand.pop(0)
  Hand.pop(0)
  #print(len(Hand))
  print("Deal Again")
  Deal()
elif TriesLeft < 0:
   print("")
   DiscardPile.append(Hand[0:5])
   Hand.pop(0)
   Hand.pop(0)
   Hand.pop(0)
   Hand.pop(0)
   Hand.pop(0)
   print("Deal Again")
   print(Hand)
else:
  print("This is Your Hand")
print("")
print("Choose your way to win.  Points or Poker.")
print("")
print("Draw!!!")
print("")
Thumb = Hand[0]
Pointer  = Hand[1]
Middle = Hand[2]
Ring = Hand[3]
Pinky = Hand[4]
YourFive = [Thumb, Pointer, Middle, Ring, Pinky]
DuplicateCheck = set(YourFive)
print("Testing Card Positions")
print(YourFive)
print("")
print("Reference: Script Line 118")
print("")
#insert user input ThumbDiscard
DiscardThumb =  Hand.pop(0)
if DiscardThumb:
   Shuffled.pop(0), Hand.insert(0, Shuffled[0])
print("'Testing Thumb Discard'")  
print(Hand)
print("")
#insert user input PointerDiscard
DiscardPointer = Hand.pop(1)
if DiscardPointer:
     Shuffled.pop(0), Hand.insert(1, Shuffled[0])
print("'Testing for Duplicates in Pointer'")
print(Hand)
#insert user input MiddleDiscard
DiscardMiddle = Hand.pop(2)
if DiscardMiddle:
     Shuffled.pop(0), Hand.insert(2, Shuffled[0])
#insert user input RingDiscard
DiscardRing = Hand.pop(3)
if DiscardRing:
     Shuffled.pop(0), Hand.insert(3, Shuffled[0])
#insert user input PinkyDiscard
DiscardPinky = Hand.pop(4)
if DiscardPinky:
     Shuffled.pop(0), Hand.insert(4, Shuffled[0])
     print("")
print("Testing The Rest")
print(Hand)
print("")
print("Testing Remaining Deck")
print(Shuffled)
print("")
print("Testing Discard Pile")
print(DiscardPile)
