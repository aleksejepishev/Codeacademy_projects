import random

money = 100

#Write your game of chance functions here

def flipping_coin(bet, side):
  flip=int(random.randint(1,2))
  if side is "Heads" and flip==1:
    return "Win! "+ str("+"+str(bet))
  elif side is "Heads" and flip==2:
    return "Lose! "+ str("-"+str(bet))
  elif side is "Tails" and flip==1:
    return "Lose! "+ str("-"+str(bet))
  elif side is "Tails" and flip==2:
    return "Win! " + str("+"+str(bet))




def cho_han(both, bet):
  dice1=int(random.randint(1,6))
  dice2=int(random.randint(1,6))
  a=(dice1+dice2)%2
  if both is "Even" and a==0:
    return "Even!" + str("You win +"+str(bet))
  elif both is "Even" and a!=0:
    return "Odd!" + str("You lose -"+str(bet))
  elif both is "Odd" and a!=0:
    return "Odd!" + str("You win +"+str(bet))
  elif both is "Odd" and a==0:
    return "Even!" + str("You lose -"+str(bet))



def picking_card(card, bet):
  card1=int(random.randint(1,10))
  card2=int(random.randint(1,10))
  if card is "Higher" and card1>card2:
    return "Your number is higher! You win +" + str(bet)
  elif card is "Higher" and card1<card2:
    return "Your number is lower! You lose -" + str(bet)
  else:
    return "It`s a tie! You win 0"
  



def roulette(number, bet):
  num=int(random.randint(1,35))
  a=num%2==0
  b=num%2!=0
  if number is "Even" and a is True :
    return "Even! You win +"+str(bet)
  elif number is "Even" and a is False:
    return "Odd! You lose -"+str(bet)
  elif number is "Odd" and b is True:
    return "Odd! You win +"+ str(bet)
  elif number is "Odd" and b is False:
    return "Even! You lose -"+str(bet)
 
  if number==num:
    return "You got it! You win +"+str(bet*35)
  else:
    return "Lose! You lose -"+str(bet)


 
#Call your game of chance functions here

print(flipping_coin(60, "Heads"))
print(cho_han("Even", 40))
print(picking_card("Higher", 50))
print(roulette(5, 30))


print(flipping_coin(60, "Heads"))
print(cho_han("Even", 40))
print(picking_card("Higher", 50))
print(roulette(5, 30))



