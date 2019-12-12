from frame1 import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, Qt, QtGui
from PyQt5.QtCore import QPropertyAnimation  # 导入动画模块
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
        #  为最大化和恢复按钮加入不同的图标
        icon_fullscreen = QtGui.QIcon()
        icon_exitfullscreen = QtGui.QIcon()
        icon_fullscreen.addPixmap(QtGui.QPixmap("rsc/fullscreen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_exitfullscreen.addPixmap(QtGui.QPixmap("rsc/exitfullscreen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_or_min_btn.setIcon(icon_fullscreen)  # 设置最大化&恢复按钮的初始图标
        self.max_or_min_btn.setIconSize(QtCore.QSize(20, 20))
        self.max_or_min_btn.clicked.connect(self.max_or_min)  # 最大化, 恢复按钮
        self.max_or_min_btn.clicked.connect(lambda: self.iconchange(icon_exitfullscreen, icon_fullscreen))
        # 该按钮触发的同时改变自身图标
        self.min_btn.clicked.connect(self.showMinimized)  # 最小化按钮
        self.close_btn.clicked.connect(self.close)  # 关闭按钮
        self.test_btn.clicked.connect(self.middle_show)
        self.test_btn.setStyleSheet("border:none;")  # 消除按钮边框
        self.initSize(0.9)  # 根据桌面初始化窗口大小，系数0.9
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # 自定义菜单栏，删除原有菜单栏
        self.menu_file = QtWidgets.QAction(Qt.QIcon(""), '文件', self)
        self.menu_show = QtWidgets.QAction(Qt.QIcon(""), '显示', self)
        self.menu_window = QtWidgets.QAction(Qt.QIcon(""), '窗口', self)
        self.menu_set = QtWidgets.QAction(Qt.QIcon(""), '设置', self)
        self.menu_account = QtWidgets.QAction(Qt.QIcon(""), '账户', self)
        self.menu_help = QtWidgets.QAction(Qt.QIcon(""), '帮助', self)
        menu1 = QtWidgets.QMenu(self)
        menu2 = QtWidgets.QMenu(self)
        menu3 = QtWidgets.QMenu(self)
        menu4 = QtWidgets.QMenu(self)
        menu5 = QtWidgets.QMenu(self)
        menu6 = QtWidgets.QMenu(self)
        menu1.addAction(self.menu_file)
        menu2.addAction(self.menu_show)
        menu3.addAction(self.menu_window)
        menu4.addAction(self.menu_set)
        menu5.addAction(self.menu_account)
        menu6.addAction(self.menu_help)




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

    def max_or_min(self):
        if self.isMaximized():  # 如果已经全屏，则恢复到正常大小
            self.showNormal()
        else:  # 否则全屏显示
            self.showMaximized()

    def middle_show(self):  # 定义中间窗口显示的函数
        self.jump_layout.addWidget(self.midpage)
        self.midpage.show()

    def iconchange(self, icon_exitfullscreen, icon_fullscreen):
        if self.isMaximized():  # 如果已经全屏
            self.max_or_min_btn.setIcon(icon_exitfullscreen)
            self.max_or_min_btn.setIconSize(QtCore.QSize(20, 20))
        else:  # 否则
            self.max_or_min_btn.setIcon(icon_fullscreen)
            self.max_or_min_btn.setIconSize(QtCore.QSize(20, 20))


class middle_page(Ui_Dialog, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    show1 = PageTotal()
    # 设置qss样式，将按钮边框消除，后面可以把qss样式单独写成一个文件,或者直接把所有QToolButton设置成无边框
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