"""
Quick Explanation of code:
The following is a program that works as a casino with two games, BlackJack and Roulette.

For Roulette, you choose a number between 1–36, and keep spinning until you hit the number.
Once you hit, you get a return of 35X the bet amount. But every spin costs you, and if you 
run out of money you must leave.

BlackJack has more rules:
You are dealt two cards, and the dealer also gets two (one hidden). You choose to either 
'hit' (draw another card) or 'stand' (end your turn). If your total exceeds 21, you bust 
and lose. The dealer then reveals their second card and must keep hitting until they reach 
at least 17. If the dealer busts, you win. If not, whoever has the higher total wins. A draw 
returns your bet. You can't bet more than your balance, and winnings are added accordingly.


For both games, your winnins/losses and remaining balance are tracked. You can leave with profit, or leave when you're broke.
"""




import random
import sys
#BEGINNING OF RUN
print("Welcome to the Casino!")
nBalance = int(input("How much did you come to the table with? USD: ")) #user chooses their cash balance in the beginning
nProfit = 0
nTempProfit = 0
#roulette function, where it spins until you hit your chosen number
def play_roulette():
    global nBalance, nProfit
    if nBalance <= 0:
        print("You're broke, can't play.")
        return

    intBetAmount = int(input("How much would you like to bet per spin (PS: spins continue until you hit or go broke): "))
    if intBetAmount > nBalance:
        print("You can't bet more than your balance.")
        return

    intPlayerNumber = int(input("What number would you like to bet on (0-36): "))
    if intPlayerNumber < 0 or intPlayerNumber > 36:
        print("Invalid number.")
        return

    intRouletteNum = ""
    i = 0
    intPlayerTotalBet = 0

    while True: 
        if nBalance < intBetAmount: #If you run out of money before the number hits:
            print("You ran out of money before hitting your number!")
            break

        nBalance -= intBetAmount
        intPlayerTotalBet += intBetAmount
        intRouletteNum = random.randrange(0, 37) #Roulette wheel lands on a random number
        i += 1

        if intPlayerNumber == intRouletteNum: #if your number equals the number it lands on, you make 35x the bet amount
            intWinning = intBetAmount * 35
            nBalance += intWinning
            intRoundProfit = intWinning - intPlayerTotalBet
            nProfit += intRoundProfit

            print("You finally hit", intPlayerNumber, "after", i, "tries")
            print("You won: $", intWinning)
            print("Your total bet was", intBetAmount, "*", i, "= $", intPlayerTotalBet)
            print("Profit made:", intRoundProfit, "USD")
            print("Your new profit is: $", nProfit)
            print("Your new balance is: $", nBalance)
            break
def play_blackjack(): #BlackJack function
    global nBalance, nProfit
    nTempProfit = 0
    nBet = int(input("How much would you like to bet? "))
    if nBet > nBalance:
        print("You can't bet more than your balance.")
        return
    #The dealer gets his two cards, but only one will be revealed initally
    print("The game starts")
    intDealerCard1 = random.randrange(1,11)
    intDealerCard2 = random.randrange(1,11)
    intDealerIni = intDealerCard1 + intDealerCard2
    print("The dealer has a", intDealerCard1)
    #The player gets his two cards, both are revealed
    intPlayerCard1 = random.randrange(1,11)
    intPlayerCard2 = random.randrange(1,11)
    intPlayerTotal = intPlayerCard1 + intPlayerCard2
    print("You pulled a", intPlayerCard1, "and a", intPlayerCard2)
    print("Your total is", intPlayerTotal)

    nBust = False
    nDealBust = False
    nDealIniActive = False
    #As long as player total is not greater than 21, the player can choose to hit or stand
    while intPlayerTotal <= 21:
        strHitOrStand = input("Would you like to hit or stand? Type 'hit' or 'stand': ")
        if strHitOrStand == "hit":
            intPlayerTotal += random.randrange(1,11)
            if intPlayerTotal > 21:
                print("BUST!")
                nBust = True
                break
            else:
                print("Your new total is", intPlayerTotal)
        elif strHitOrStand == "stand":
            break
    #if player busts, that's a loss
    if nBust:
        print("You lose")
        nProfit -= nBet
        print("-$", nBet)
        nBalance -= nBet
        print("Your new profit is: $", nProfit)
        print("Your new balance is: $", nBalance)
        return
    #If the player doesn't bust, it continues here where the dealer's second card is revealed
    print("The dealer reveals a", intDealerCard2, "total of:", intDealerIni)
    if intDealerIni > 16:
        nDealIniActive = True #This boolean exists to check if the dealer's inital two already equal 17 or above, because the dealer must stop pulling new cards at 17
        if intDealerIni > intPlayerTotal: #If dealer's total is more than yours at the end, you lose
            print("You lose")
            nProfit -= nBet
            nBalance -= nBet
            print("- $", nBet)
        elif intDealerIni < intPlayerTotal: #You win if your total is greater
            print("You win")
            nProfit += nBet
            nBalance += nBet
            print("+ $", nBet * 2)
        else:
            print("You drew")
            print("+ $0")
    else:
        intDealerTotal = intDealerIni
        while intDealerTotal < 17: #As long as dealer total is less than 17, he keeps pulling new cards
            intDealerHit = random.randrange(1,11)
            intDealerTotal += intDealerHit
            print("The dealer pulled a", intDealerHit)
            if intDealerTotal > 21: #if dealer total exceeds 21 he busts and you win
                print("Dealer busts")
                print("You win!")
                nProfit += nBet
                nBalance += nBet
                print("+ $", nBet * 2)
                break
            elif intDealerTotal < 17:
                continue
            else: #if dealer total at this point is between 21 and 17, he stops pulling and reveals
                print("The dealer's total is", intDealerTotal)
                break

        if intPlayerTotal > intDealerTotal and intDealerTotal <= 21:
            print("You win!")
            nProfit += nBet
            nBalance += nBet
            print("+ $", nBet * 2)
        elif intPlayerTotal < intDealerTotal and intDealerTotal <= 21:
            print("You lose!")
            nProfit -= nBet
            nBalance -= nBet
            print("- $", nBet)
        elif intPlayerTotal == intDealerTotal:
            print("You drew")
            print("+ $0")

    print("Your new profit is: $", nProfit)
    print("Your new balance is: $", nBalance)

# Game menu
while nBalance > 0:
    print("\n--- Game Menu ---")
    print("1: Play Blackjack")
    print("2: Play Roulette")
    print("3: Leave Casino")
    choice = input("Choose a game (1/2) or 3 to exit: ")
    if choice == "1":
        play_blackjack()
    elif choice == "2":
        play_roulette()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")

if nBalance == 0:
    print("You're broke.")

print("You left the casino with $", nBalance)
print("Total profit/loss: $", nProfit)
#END
