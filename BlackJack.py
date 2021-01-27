import random


def new_coloda():
    size = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit = ['♥', '♦', '♣', '♠']
    for x in suit:
        for y in size:
            cards.append(x + y)
    random.shuffle(cards)

def count_cards(arr):
    r = 0
    for x in arr: #♥10
        if x[1:].isnumeric():
            r += int(x[1:])
        else:
            if x[1:] == 'A':
                if r > 10:
                    r+=1
                else:
                    r+=11
            else:
                r+=10
    return r


while True:
    s = input('Еще игра? y/n ')
    if s != 'y':
        break
    print('New game')
    cards = []
    new_coloda()
    your_hand = []
    dealer = []
    game_over = False
    while count_cards(your_hand) < 21:
        e = input('Карту? y/n ')
        if e == 'y':
            your_hand.append(cards.pop())
            c = count_cards(your_hand)
            print(your_hand,f'Your score {c}')
            if c == 21:
                print('You win!!!')
                game_over = True
            elif c > 21:
                print('You lose!!!')
                game_over = True
        else:
            break

    while count_cards(dealer) < 18 and game_over == False:
        dealer.append(cards.pop())

    d = count_cards(dealer)
    print(dealer, f'dealer score {d}')
    print('ffff{}'.format('a'))
    if d > 21:
        print('You win!!!')
    else:
        if 21-c < 21-d:
            print('You win!!!')
        else:
            print('You lose!!!')
