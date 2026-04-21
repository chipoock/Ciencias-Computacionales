while True:
    numL = ['0', '1', '2', '3','4', '5', 
            '6', '7','8', '9', 'A', 'B',
            'C', 'D', 'E', 'F']

    def conBase( num, base):
        x = num
        if x >= base:
            x = num // base
            conBase(x, base)
            print(numL[num % base], end='')
        else:
            print(numL[x], end='')

    if __name__ == '__main__':
        numero = int(input('Dame numero: '))
        base =   int(input('Base.......: '))
        conBase(numero, base)