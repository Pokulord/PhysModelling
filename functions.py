import matplotlib.pyplot as plt
import numpy as np

def parameters():
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title
    plt.grid()
# Для работы с дробными числами

def frange(x1, x2, jump):
    while x1 < x2:
        yield x1
        x1 += jump

def draw_function1(sn = 8):
    global x_listf1, y1, ax_2
    figure = plt.figure()
    x_listf1 = [elem for elem in range(-50,50,1)]

    # print(x_listf1)
    y1 = [(2*x**2+6*x + sn) for x in x_listf1]
    ax1 = figure.add_subplot(221)
    ax1.plot(x_listf1,y1)
    ax1.title.set_text('График 1')
    ax_2 = figure.add_subplot(222)
    ax_2.title.set_text('График 2')
    parameters()
    drawfunction2()
    plt.show()

def drawfunction2():
    x_listf2 = [x for x in frange(-1.0, 1.001, 0.01)]
    print(x_listf2)
    y2 = [((1 - x ** 2) ** 0.5 + (abs(x)) ** 0.5) for x in x_listf2]
    print(y2)
    ax_2.plot(x_listf2, y2, color = 'red')
    drawfunc3(x_listf2,y2)

def drawfunc3(lf3,yf3):
    figure , axis = plt.subplots()
    axis1 = axis.twinx()
    axis.plot(lf3,yf3, color = 'red')
    axis1.plot(x_listf1,y1, color = 'blue')
    axis.set_ylabel('Первый график')
    axis1.set_ylabel('Второй график')
    axis.legend(['2'])
    axis1.legend(['1'])
    axis1.grid()
if __name__ == '__main__':
    # stud_number = int(input("Введите номер вашего студенческого : "))
    draw_function1()

