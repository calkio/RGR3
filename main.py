import sys  # sys нужен для передачи argv в QApplication
import design_window
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design_window.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  
    main()  



def get_avg(mylist):  # Считает среднее значения mylist
    return sum(mylist) / len(mylist)

def get_dispersia(mylist):  # Считает дисперсию mylist
    avg = get_avg(mylist)
    cko = [(item - avg)**2 for item in mylist]
    return sum(cko) / len(cko)

def func_G(x):  # Возвращяет функию g(x): x^2
    return x**2

def proizvodnai_funcG(x):  # Возвращяет производную функии g(x): 2 * x
    return 2 * x