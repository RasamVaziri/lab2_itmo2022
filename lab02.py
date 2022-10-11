import csv

def DownloadsCount():
  with open('books-en.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    Downcounter = 0
    for row in csv_reader:
        if row["Downloads"].isnumeric():
            booksDownloads = row["Downloads"]
            if int(booksDownloads) >10:
                Downcounter +=1
    print(f'Количество книг, скачанных более 10 раз, составляет: {Downcounter} books.')
    x = int(input("Enter percentage you want to show: "))
    digits = [int(n) for n in str(x)]
    rows = max(digits)
    bar_graph = []
    for row in range(rows, 0, -1):
        bar_graph.append(['x' if digit >= row else ' ' for digit in digits])
    for row in bar_graph:
        print('    '.join(row))
    print('--' * (2 * len(digits) + 3))
    for i in range(10, 31, 10):
        print(i, end="   ")


def draw_y_equals_x_div_3():
    for x in range(4, 0, -1):
        t = x * 3
        y = t / 3
        temp = int(y) * " " + (x - 1) * " "
        print(x.__str__() + temp + "*")

    for i in range(0, 13, 3):
        print(i, end=" ")



def Flag():
    RED = '\u001b[41m'
    WHITE = '\u001b[47m'
    BLUE = '\u001b[44m'
    END = '\u001b[0m'
    for i in range(0, 7):
        if i <= 1:
            print(f'{RED}{" " * 28}{END}')
        elif i == 2:
            print(f'{RED}{" " * 12}{WHITE}{" " * 4}{RED}{" " * 12}{END}')
        elif i == 3:
            print(f'{RED}{" " * 8}{WHITE}{" " * 12}{RED}{" " * 8}{END}')
        elif i == 4:
            print(f'{RED}{" " * 12}{WHITE}{" " * 4}{RED}{" " * 12}{END}')
        else:
            print(f'{RED}{" " * 28}{END}')



def Circle():
    diameter = 7
    radius = diameter / 2 - .5
    r = (radius + .25) ** 2 + 1
    r_min = (radius - 1) ** 2 + 1  # <-------- here
    result = ''
    Black = '\u001b[40m'
    for i in range(diameter):
        y = (i - radius) ** 2
        for j in range(diameter):
            x = (j - radius) ** 2
            if r_min <= x + y <= r:  # <----- here
                result = result + '*  '
            else:
                result = result + '   '
        for j in range(diameter):
            x = (j - radius) ** 2
            if r_min <= x + y <= r:  # <----- here
                result = result + '*  '
            else:
                result = result + '   '
        result = result + '\n'
    print(f'{Black}{result}')


DownloadsCount()
print("\n--------------------------------------------------------------- ")
draw_y_equals_x_div_3()
print("\n--------------------------------------------------------------- ")
Flag()
print("\n--------------------------------------------------------------- ")
Circle()
print("\n--------------------------------------------------------------- ")





