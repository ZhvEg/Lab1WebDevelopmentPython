from math import sin

def getInput():
    while type:
        x = input("Введите значение х: ")
        try:
            getTempNumber = int(x)
        except ValueError:
            print(f'{x} не является целым числом')
        else:
            break
    return int(x)

def productOfSeries(data):
    return sin(data)

def printComposition(data):
    print(f'Решение данного выражения с данным {x} = {data}')


if __name__ == '__main__':
    x = getInput()
    POS = productOfSeries(x)
    printComposition(POS)
