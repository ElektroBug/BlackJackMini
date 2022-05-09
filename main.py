koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)

print('Lets play BlackJack')
count = 0

while True:
    choice = input('Do you need a cart? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('You got a card of value %d' %current)
        count += current
        if count > 21:
            print('Sorry but you lost!')
            break
        elif count == 21:
            print('Congratulations, you scored 21 and won!')
            break
        else:
            print('You have %d points.' %count)
    elif choice == 'n':
        print('You have %d points and you finished game.' %count)
        break
    print('See you soon!')

