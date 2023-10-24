import random
def roll():
    dice = random.randint(1, 6)
    print(f'Вы бросили кубик и выпало: {dice}')

    if dice in (5, 6):
        print('Вы победили!')
    elif dice in (3, 4):
        print('Вы бросаете кубик ещё раз.')
        roll()
    else:
        print('Вы проиграли.')

if __name__ == '__main__':
    roll()
