# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1524, 746)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setBaseSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 1511, 691))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_expedicio = QPushButton(self.frame_3)
        self.btn_expedicio.setObjectName(u"btn_expedicio")

        self.verticalLayout.addWidget(self.btn_expedicio)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.btn_karakter = QPushButton(self.frame_3)
        self.btn_karakter.setObjectName(u"btn_karakter")

        self.verticalLayout.addWidget(self.btn_karakter)

        self.btn_kilepes_2 = QPushButton(self.frame_3)
        self.btn_kilepes_2.setObjectName(u"btn_kilepes_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_kilepes_2.sizePolicy().hasHeightForWidth())
        self.btn_kilepes_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.btn_kilepes_2.setFont(font)
        self.btn_kilepes_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.verticalLayout.addWidget(self.btn_kilepes_2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.stackedWidget = QStackedWidget(self.layoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page0_fomenu = QWidget()
        self.page0_fomenu.setObjectName(u"page0_fomenu")
        self.horizontalLayout_2 = QHBoxLayout(self.page0_fomenu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(238, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_folytatas = QPushButton(self.page0_fomenu)
        self.btn_folytatas.setObjectName(u"btn_folytatas")

        self.verticalLayout_2.addWidget(self.btn_folytatas)

        self.btn_ujjatek = QPushButton(self.page0_fomenu)
        self.btn_ujjatek.setObjectName(u"btn_ujjatek")

        self.verticalLayout_2.addWidget(self.btn_ujjatek)

        self.btn_betoltes = QPushButton(self.page0_fomenu)
        self.btn_betoltes.setObjectName(u"btn_betoltes")

        self.verticalLayout_2.addWidget(self.btn_betoltes)

        self.btn_beallitasok = QPushButton(self.page0_fomenu)
        self.btn_beallitasok.setObjectName(u"btn_beallitasok")

        self.verticalLayout_2.addWidget(self.btn_beallitasok)

        self.btn_kilepes = QPushButton(self.page0_fomenu)
        self.btn_kilepes.setObjectName(u"btn_kilepes")

        self.verticalLayout_2.addWidget(self.btn_kilepes)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.page0_fomenu)
        self.page1_terkep = QWidget()
        self.page1_terkep.setObjectName(u"page1_terkep")
        self.btn_dungeon_soteterdo = QPushButton(self.page1_terkep)
        self.btn_dungeon_soteterdo.setObjectName(u"btn_dungeon_soteterdo")
        self.btn_dungeon_soteterdo.setGeometry(QRect(250, 210, 80, 24))
        self.btn_dungeon_kripta = QPushButton(self.page1_terkep)
        self.btn_dungeon_kripta.setObjectName(u"btn_dungeon_kripta")
        self.btn_dungeon_kripta.setGeometry(QRect(1130, 220, 80, 24))
        self.stackedWidget.addWidget(self.page1_terkep)
        self.page2_soteterdo = QWidget()
        self.page2_soteterdo.setObjectName(u"page2_soteterdo")
        self.verticalLayout_4 = QVBoxLayout(self.page2_soteterdo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.graphicsView = QGraphicsView(self.page2_soteterdo)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.graphicsView)

        self.verticalSpacer_3 = QSpacerItem(20, 245, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.page2_soteterdo)
        self.page3_karakter = QWidget()
        self.page3_karakter.setObjectName(u"page3_karakter")
        self.gridLayoutWidget_2 = QWidget(self.page3_karakter)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(470, 420, 241, 271))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.gridLayoutWidget_2)
        self.label_91.setObjectName(u"label_91")
        font1 = QFont()
        font1.setBold(True)
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_91, 8, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_83 = QLabel(self.gridLayoutWidget_2)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_83, 3, 1, 1, 1)

        self.label_86 = QLabel(self.gridLayoutWidget_2)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_86, 5, 0, 1, 1)

        self.label_87 = QLabel(self.gridLayoutWidget_2)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_87, 5, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_90 = QLabel(self.gridLayoutWidget_2)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font1)
        self.label_90.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_90, 7, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_16, 1, 1, 1, 1)

        self.label_85 = QLabel(self.gridLayoutWidget_2)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_85, 4, 1, 1, 1)

        self.label_88 = QLabel(self.gridLayoutWidget_2)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font1)
        self.label_88.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_88, 6, 0, 1, 1)

        self.label_84 = QLabel(self.gridLayoutWidget_2)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_84, 4, 0, 1, 1)

        self.label_93 = QLabel(self.gridLayoutWidget_2)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font1)
        self.label_93.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_93, 8, 1, 1, 1)

        self.label_92 = QLabel(self.gridLayoutWidget_2)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font1)
        self.label_92.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_92, 7, 1, 1, 1)

        self.label_82 = QLabel(self.gridLayoutWidget_2)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_82, 2, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_89 = QLabel(self.gridLayoutWidget_2)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font1)
        self.label_89.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_89, 6, 1, 1, 1)

        self.label_94 = QLabel(self.gridLayoutWidget_2)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_94, 0, 0, 1, 1)

        self.layoutWidget1 = QWidget(self.page3_karakter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 1391, 421))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_cipo = QPushButton(self.layoutWidget1)
        self.btn_cipo.setObjectName(u"btn_cipo")
        self.btn_cipo.setMinimumSize(QSize(64, 64))
        self.btn_cipo.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_cipo, 3, 1, 1, 1)

        self.btn_pajzs = QPushButton(self.layoutWidget1)
        self.btn_pajzs.setObjectName(u"btn_pajzs")
        self.btn_pajzs.setMinimumSize(QSize(64, 64))
        self.btn_pajzs.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_pajzs, 4, 2, 1, 1)

        self.btn_kesztyu = QPushButton(self.layoutWidget1)
        self.btn_kesztyu.setObjectName(u"btn_kesztyu")
        self.btn_kesztyu.setMinimumSize(QSize(64, 64))
        self.btn_kesztyu.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_kesztyu, 1, 0, 1, 1)

        self.btn_nadrag = QPushButton(self.layoutWidget1)
        self.btn_nadrag.setObjectName(u"btn_nadrag")
        self.btn_nadrag.setMinimumSize(QSize(64, 64))
        self.btn_nadrag.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_nadrag, 2, 1, 1, 1)

        self.btn_sisak = QPushButton(self.layoutWidget1)
        self.btn_sisak.setObjectName(u"btn_sisak")
        self.btn_sisak.setMinimumSize(QSize(64, 64))
        self.btn_sisak.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_sisak, 0, 1, 1, 1)

        self.btn_gyuru = QPushButton(self.layoutWidget1)
        self.btn_gyuru.setObjectName(u"btn_gyuru")
        self.btn_gyuru.setMinimumSize(QSize(64, 64))
        self.btn_gyuru.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_gyuru, 1, 2, 1, 1)

        self.btn_mellvert = QPushButton(self.layoutWidget1)
        self.btn_mellvert.setObjectName(u"btn_mellvert")
        self.btn_mellvert.setMinimumSize(QSize(64, 64))
        self.btn_mellvert.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_mellvert, 1, 1, 1, 1)

        self.btn_kard = QPushButton(self.layoutWidget1)
        self.btn_kard.setObjectName(u"btn_kard")
        self.btn_kard.setMinimumSize(QSize(64, 64))
        self.btn_kard.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b2b2b;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 1px solid #5fb35f;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_kard, 4, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalSpacer = QSpacerItem(250, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.listWidget = QListWidget(self.layoutWidget1)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_7.addWidget(self.listWidget, 0, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_7)

        self.stackedWidget.addWidget(self.page3_karakter)
        self.page4_harc = QWidget()
        self.page4_harc.setObjectName(u"page4_harc")
        self.layoutWidget2 = QWidget(self.page4_harc)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(1, 2, 1401, 411))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_harcinditas = QPushButton(self.layoutWidget2)
        self.btn_harcinditas.setObjectName(u"btn_harcinditas")

        self.gridLayout_4.addWidget(self.btn_harcinditas, 1, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_203 = QLabel(self.layoutWidget2)
        self.label_203.setObjectName(u"label_203")

        self.gridLayout_8.addWidget(self.label_203, 0, 3, 1, 1)

        self.lbl_hos_vedekezes_ertek = QLabel(self.layoutWidget2)
        self.lbl_hos_vedekezes_ertek.setObjectName(u"lbl_hos_vedekezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_hos_vedekezes_ertek, 1, 2, 1, 1)

        self.label_98 = QLabel(self.layoutWidget2)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_8.addWidget(self.label_98, 2, 1, 1, 1)

        self.label_96 = QLabel(self.layoutWidget2)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_8.addWidget(self.label_96, 1, 1, 1, 1)

        self.label_205 = QLabel(self.layoutWidget2)
        self.label_205.setObjectName(u"label_205")

        self.gridLayout_8.addWidget(self.label_205, 1, 3, 1, 1)

        self.label_95 = QLabel(self.layoutWidget2)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_8.addWidget(self.label_95, 0, 1, 1, 1)

        self.lbl_szorny_kezdemenyezes_ertek = QLabel(self.layoutWidget2)
        self.lbl_szorny_kezdemenyezes_ertek.setObjectName(u"lbl_szorny_kezdemenyezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_szorny_kezdemenyezes_ertek, 2, 4, 1, 1)

        self.lbl_hos_kezdemenyezes_ertek = QLabel(self.layoutWidget2)
        self.lbl_hos_kezdemenyezes_ertek.setObjectName(u"lbl_hos_kezdemenyezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_hos_kezdemenyezes_ertek, 2, 2, 1, 1)

        self.lbl_hos_ero_ertek = QLabel(self.layoutWidget2)
        self.lbl_hos_ero_ertek.setObjectName(u"lbl_hos_ero_ertek")

        self.gridLayout_8.addWidget(self.lbl_hos_ero_ertek, 0, 2, 1, 1)

        self.label_207 = QLabel(self.layoutWidget2)
        self.label_207.setObjectName(u"label_207")

        self.gridLayout_8.addWidget(self.label_207, 2, 3, 1, 1)

        self.lbl_szorny_ero_ertek = QLabel(self.layoutWidget2)
        self.lbl_szorny_ero_ertek.setObjectName(u"lbl_szorny_ero_ertek")

        self.gridLayout_8.addWidget(self.lbl_szorny_ero_ertek, 0, 4, 1, 1)

        self.frame = QFrame(self.layoutWidget2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lbl_hos_img = QLabel(self.frame)
        self.lbl_hos_img.setObjectName(u"lbl_hos_img")
        self.lbl_hos_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.lbl_hos_img, 0, 0, 1, 1)

        self.lbl_hos_nev = QLabel(self.frame)
        self.lbl_hos_nev.setObjectName(u"lbl_hos_nev")
        self.lbl_hos_nev.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.lbl_hos_nev, 2, 0, 1, 1)

        self.pb_hos_hp = QProgressBar(self.frame)
        self.pb_hos_hp.setObjectName(u"pb_hos_hp")
        self.pb_hos_hp.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    background-color: #222;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #d32f2f; \n"
"    border-radius: 3px;\n"
"}")
        self.pb_hos_hp.setValue(100)

        self.gridLayout_9.addWidget(self.pb_hos_hp, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 0, 3, 1)

        self.lbl_szorn_vedekezes_ertek = QLabel(self.layoutWidget2)
        self.lbl_szorn_vedekezes_ertek.setObjectName(u"lbl_szorn_vedekezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_szorn_vedekezes_ertek, 1, 4, 1, 1)

        self.frame_2 = QFrame(self.layoutWidget2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_szorn_img = QLabel(self.frame_2)
        self.lbl_szorn_img.setObjectName(u"lbl_szorn_img")
        self.lbl_szorn_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_szorn_img)

        self.pb_szorny_hp = QProgressBar(self.frame_2)
        self.pb_szorny_hp.setObjectName(u"pb_szorny_hp")
        self.pb_szorny_hp.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    background-color: #222;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #d32f2f;\n"
"    border-radius: 3px;\n"
"}")
        self.pb_szorny_hp.setValue(100)

        self.verticalLayout_3.addWidget(self.pb_szorny_hp)

        self.lbl_szorny_nev = QLabel(self.frame_2)
        self.lbl_szorny_nev.setObjectName(u"lbl_szorny_nev")
        self.lbl_szorny_nev.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_szorny_nev)


        self.gridLayout_8.addWidget(self.frame_2, 0, 5, 3, 1)


        self.gridLayout_4.addLayout(self.gridLayout_8, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page4_harc)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(835, 441, 671, 251))
        self.textBrowser.setMinimumSize(QSize(0, 10))
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1524, 21))
        self.menuPROJEKT_LABOR_RPG_J_T_K = QMenu(self.menubar)
        self.menuPROJEKT_LABOR_RPG_J_T_K.setObjectName(u"menuPROJEKT_LABOR_RPG_J_T_K")
        self.menu03 = QMenu(self.menubar)
        self.menu03.setObjectName(u"menu03")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPROJEKT_LABOR_RPG_J_T_K.menuAction())
        self.menubar.addAction(self.menu03.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_expedicio.setText(QCoreApplication.translate("MainWindow", u"T\u00e9rk\u00e9p", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Kov\u00e1cs", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"T\u00e1borhely", None))
        self.btn_karakter.setText(QCoreApplication.translate("MainWindow", u"Karakter", None))
        self.btn_kilepes_2.setText(QCoreApplication.translate("MainWindow", u"Kil\u00e9p\u00e9s", None))
        self.btn_folytatas.setText(QCoreApplication.translate("MainWindow", u"Folytat\u00e1s", None))
        self.btn_ujjatek.setText(QCoreApplication.translate("MainWindow", u"\u00daj J\u00e1t\u00e9k(Coming Soon!)", None))
        self.btn_betoltes.setText(QCoreApplication.translate("MainWindow", u"Bet\u00f6lt\u00e9s(Coming Soon!)", None))
        self.btn_beallitasok.setText(QCoreApplication.translate("MainWindow", u"Be\u00e1ll\u00edt\u00e1sok(Coming Soon!)", None))
        self.btn_kilepes.setText(QCoreApplication.translate("MainWindow", u"Kil\u00e9p\u00e9s", None))
        self.btn_dungeon_soteterdo.setText(QCoreApplication.translate("MainWindow", u"S\u00f6t\u00e9t erd\u0151", None))
        self.btn_dungeon_kripta.setText(QCoreApplication.translate("MainWindow", u"Kripta", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"\u00d6sszes Kezdem\u00e9nyez\u00e9s:", None))
        self.label_12.setText("")
        self.label_83.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Potion(Kezdem\u00e9nyez\u00e9s):", None))
        self.label_87.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"V\u00e9dekez\u00e9s:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Fegyver(Er\u0151):", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u00d6sszes V\u00e9dekez\u00e9s:", None))
        self.label_16.setText("")
        self.label_85.setText("")
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u00d6sszes Er\u0151:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Felszerel\u00e9s(V\u00e9dekez\u00e9s):", None))
        self.label_93.setText("")
        self.label_92.setText("")
        self.label_82.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Kezdem\u00e9nyez\u00e9s:", None))
        self.label_89.setText("")
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Er\u0151:", None))
        self.btn_cipo.setText(QCoreApplication.translate("MainWindow", u"Cip\u0151", None))
        self.btn_pajzs.setText(QCoreApplication.translate("MainWindow", u"Pajzs", None))
        self.btn_kesztyu.setText(QCoreApplication.translate("MainWindow", u"Keszt\u0171", None))
        self.btn_nadrag.setText(QCoreApplication.translate("MainWindow", u"Nadr\u00e1g", None))
        self.btn_sisak.setText(QCoreApplication.translate("MainWindow", u"Sisak", None))
        self.btn_gyuru.setText(QCoreApplication.translate("MainWindow", u"Gy\u0171r\u0171", None))
        self.btn_mellvert.setText(QCoreApplication.translate("MainWindow", u"Mellv\u00e9rt", None))
        self.btn_kard.setText(QCoreApplication.translate("MainWindow", u"Kard", None))
        self.btn_harcinditas.setText(QCoreApplication.translate("MainWindow", u"Harc ind\u00edt\u00e1sa", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Er\u0151:", None))
        self.lbl_hos_vedekezes_ertek.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Kezdem\u00e9nyez\u00e9s:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"V\u00e9dekez\u00e9s:", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"V\u00e9dekez\u00e9s:", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Er\u0151:", None))
        self.lbl_szorny_kezdemenyezes_ertek.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lbl_hos_kezdemenyezes_ertek.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lbl_hos_ero_ertek.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"Kezdem\u00e9nyez\u00e9s:", None))
        self.lbl_szorny_ero_ertek.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lbl_hos_img.setText(QCoreApplication.translate("MainWindow", u"H\u0151sImg", None))
        self.lbl_hos_nev.setText(QCoreApplication.translate("MainWindow", u"H\u0151s - Level 1", None))
        self.pb_hos_hp.setFormat(QCoreApplication.translate("MainWindow", u"%v / %m", None))
        self.lbl_szorn_vedekezes_ertek.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lbl_szorn_img.setText(QCoreApplication.translate("MainWindow", u"Sz\u00f6rnyImg", None))
        self.pb_szorny_hp.setFormat(QCoreApplication.translate("MainWindow", u"%v / %m", None))
        self.lbl_szorny_nev.setText(QCoreApplication.translate("MainWindow", u"Sz\u00f6rny - Level 1", None))
        self.menuPROJEKT_LABOR_RPG_J_T_K.setTitle(QCoreApplication.translate("MainWindow", u"PROJEKT LABOR - RPG J\u00c1T\u00c9K", None))
        self.menu03.setTitle(QCoreApplication.translate("MainWindow", u"03", None))
    # retranslateUi

