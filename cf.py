import random

def CoinFlip():
    coin = ['Orzeł', 'Reszka']
    coinFlip = random.choice(coin)

    print(coinFlip)

def restart():
    while True:
        CoinFlip()
        answer = input("Czy chcesz kontynuowac [T/N] ")
        if(answer.upper() != 'T'):
            break



restart()