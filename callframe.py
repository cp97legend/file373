from frame1 import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, Qt
from reuse_middelpage import Ui_Dialog


class PageTotal(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #  消除主窗口边框，为了自定义标题栏,但是无法通过边缘放大缩小窗口，也无法拖动窗口
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        # 消除主窗口边框，可以通过边缘放大缩小窗口，但是无法拖动窗口
        self.setupUi(self)
        self.midpage = middle_page()
        self.test_btn.clicked.connect(self.middle_show)
        self.test_btn.setStyleSheet("border:none;")  # 消除按钮边框
        self.initSize(0.9)  # 根据桌面初始化窗口大小，系数0.9
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setMenuBar()

#  由于无边框导致窗口无法移动，所以定义鼠标关联窗口移动行为
    def mousePressEvent(self, QMouseEvent):  # 鼠标按下操作
        if QMouseEvent.button() == Qt.Qt.LeftButton:
            self.flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))  # 设置光标为手型

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标移动操作
        if Qt.Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标释放操作
        self.flag = False
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))  # 设置光标为箭头

    def mouseDoubleClickEvent(self, QMouseEvent):  # 鼠标双击操作
        if self.isMaximized():  # 如果已经全屏，则恢复到正常大小
            self.showNormal()
        else:  # 否则全屏显示
            self.showMaximized()


    def initSize(self, rate):  # 根据屏幕初始化窗口大小
        desktop = QtWidgets.QApplication.desktop()
        self.screenWidth = desktop.width() * rate
        self.screenHeight = desktop.height() * rate
        self.resize(self.screenWidth, self.screenHeight)

    def middle_show(self):  # 定义中间窗口显示的函数
        self.jump_layout.addWidget(self.midpage)
        self.midpage.show()


class middle_page(Ui_Dialog, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    show1 = PageTotal()
    # 设置qss样式，将按钮边框消除，后面可以把qss样式单独写成一个文件
    qssStyle = '''
    QToolButton[objectName = "reboot_btn"] {border:none}
    QToolButton[objectName = "start_btn"] {border:none}
    QToolButton[objectName = "redo_btn"] {border:none}
    QToolButton[objectName = "undo_btn"] {border:none}
    QToolButton[objectName = "forward_btn"] {border:none}
    QToolButton[objectName = "backward_btn"] {border:none}
    QToolButton[objectName = "saveas_btn"] {border:none}
    QToolButton[objectName = "save_btn"] {border:none}
    QToolButton[objectName = "delete_btn"] {border:none}
    '''
    show1.setStyleSheet(qssStyle)  # 设置主窗口的样式为上面定义的qss样式
    show1.show()
    sys.exit(app.exec_())