import sys  # sys нужен для передачи argv в QApplication
import design_window
from PyQt5 import QtWidgets
import os

class ExampleApp(QtWidgets.QMainWindow, design_window.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.decide.clicked.connect(self.click_button)



    def click_button(self):  # Нажатие на копку "Решить"
        text = self.input_value.toPlainText().split(' ')  # Забрали текст из texBox и рапарсили по пробелам

        values = [float(value) for value in text]  # Поместили все числа в массив values в числовом виде
        avg = self.get_avg(values)  
        dispersia = self.get_dispersia(values)  

        myavg_Y = self.func_G(avg)
        mydispersia_Y = self.proizvodnai_funcG(avg)**2 * dispersia

        self.avg_Y.setPlainText(str(myavg_Y))  # Присвоение значений в textBox
        self.cko_Y.setPlainText(str(mydispersia_Y))




    def get_avg(self, mylist):  # Считает среднее значения mylist
        return sum(mylist) / len(mylist)

    def get_dispersia(self, mylist):  # Считает дисперсию mylist
        avg = self.get_avg(mylist)
        cko = [(item - avg)**2 for item in mylist]
        return sum(cko) / len(cko)

    def func_G(self, x):  # Возвращяет функию g(x): x^2
        return x**2

    def proizvodnai_funcG(self, x):  # Возвращяет производную функии g(x): 2 * x
        return 2 * x


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # Запуск приложения

if __name__ == '__main__':  
    main()



