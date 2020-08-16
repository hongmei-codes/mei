import arith


def mei():
    '''
    Basic command line interphase.
    '''

    text = ''

    while True:   
        text = input('🌈 mei > ')
        if text == 'q':
            print('Existed 🌈 mei')
            break
        else:
            print(arith.calc(text))


if __name__ == '__main__':
    mei()