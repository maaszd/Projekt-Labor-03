# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

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
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_73 = QLabel(self.page2_soteterdo)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setScaledContents(True)

        self.gridLayout.addWidget(self.label_73, 5, 2, 1, 1)

        self.label_60 = QLabel(self.page2_soteterdo)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setScaledContents(True)

        self.gridLayout.addWidget(self.label_60, 5, 8, 1, 1)

        self.label_80 = QLabel(self.page2_soteterdo)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setScaledContents(True)

        self.gridLayout.addWidget(self.label_80, 8, 2, 1, 1)

        self.label5 = QLabel(self.page2_soteterdo)
        self.label5.setObjectName(u"label5")
        self.label5.setScaledContents(True)

        self.gridLayout.addWidget(self.label5, 2, 6, 1, 1)

        self.label_59 = QLabel(self.page2_soteterdo)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setScaledContents(True)

        self.gridLayout.addWidget(self.label_59, 7, 7, 1, 1)

        self.label_81 = QLabel(self.page2_soteterdo)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setScaledContents(True)

        self.gridLayout.addWidget(self.label_81, 8, 0, 1, 1)

        self.label_40 = QLabel(self.page2_soteterdo)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setScaledContents(True)

        self.gridLayout.addWidget(self.label_40, 6, 8, 1, 1)

        self.label_75 = QLabel(self.page2_soteterdo)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setScaledContents(True)

        self.gridLayout.addWidget(self.label_75, 8, 7, 1, 1)

        self.label_61 = QLabel(self.page2_soteterdo)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setScaledContents(True)

        self.gridLayout.addWidget(self.label_61, 8, 1, 1, 1)

        self.label_48 = QLabel(self.page2_soteterdo)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setScaledContents(True)

        self.gridLayout.addWidget(self.label_48, 3, 8, 1, 1)

        self.label_3 = QLabel(self.page2_soteterdo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)

        self.label4 = QLabel(self.page2_soteterdo)
        self.label4.setObjectName(u"label4")
        self.label4.setScaledContents(True)

        self.gridLayout.addWidget(self.label4, 2, 2, 1, 1)

        self.label_17 = QLabel(self.page2_soteterdo)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setScaledContents(True)

        self.gridLayout.addWidget(self.label_17, 1, 6, 1, 1)

        self.label_55 = QLabel(self.page2_soteterdo)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setScaledContents(True)

        self.gridLayout.addWidget(self.label_55, 7, 5, 1, 1)

        self.label_43 = QLabel(self.page2_soteterdo)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setScaledContents(True)

        self.gridLayout.addWidget(self.label_43, 4, 6, 1, 1)

        self.label_28 = QLabel(self.page2_soteterdo)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setScaledContents(True)

        self.gridLayout.addWidget(self.label_28, 7, 1, 1, 1)

        self.label_31 = QLabel(self.page2_soteterdo)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setScaledContents(True)

        self.gridLayout.addWidget(self.label_31, 4, 1, 1, 1)

        self.label_30 = QLabel(self.page2_soteterdo)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setScaledContents(True)

        self.gridLayout.addWidget(self.label_30, 3, 1, 1, 1)

        self.label_33 = QLabel(self.page2_soteterdo)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setScaledContents(True)

        self.gridLayout.addWidget(self.label_33, 3, 2, 1, 1)

        self.label_65 = QLabel(self.page2_soteterdo)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setScaledContents(True)

        self.gridLayout.addWidget(self.label_65, 6, 0, 1, 1)

        self.label_32 = QLabel(self.page2_soteterdo)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setScaledContents(True)

        self.gridLayout.addWidget(self.label_32, 5, 1, 1, 1)

        self.label_64 = QLabel(self.page2_soteterdo)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setScaledContents(True)

        self.gridLayout.addWidget(self.label_64, 5, 0, 1, 1)

        self.label_57 = QLabel(self.page2_soteterdo)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setScaledContents(True)

        self.gridLayout.addWidget(self.label_57, 6, 6, 1, 1)

        self.label_67 = QLabel(self.page2_soteterdo)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setScaledContents(True)

        self.gridLayout.addWidget(self.label_67, 6, 2, 1, 1)

        self.label_50 = QLabel(self.page2_soteterdo)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setScaledContents(True)

        self.gridLayout.addWidget(self.label_50, 3, 6, 1, 1)

        self.label_27 = QLabel(self.page2_soteterdo)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setScaledContents(True)

        self.gridLayout.addWidget(self.label_27, 9, 5, 1, 1)

        self.label_49 = QLabel(self.page2_soteterdo)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setScaledContents(True)

        self.gridLayout.addWidget(self.label_49, 3, 7, 1, 1)

        self.label_44 = QLabel(self.page2_soteterdo)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setScaledContents(True)

        self.gridLayout.addWidget(self.label_44, 4, 5, 1, 1)

        self.label_72 = QLabel(self.page2_soteterdo)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setScaledContents(True)

        self.gridLayout.addWidget(self.label_72, 5, 3, 1, 1)

        self.label_45 = QLabel(self.page2_soteterdo)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setScaledContents(True)

        self.gridLayout.addWidget(self.label_45, 4, 4, 1, 1)

        self.label_77 = QLabel(self.page2_soteterdo)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setScaledContents(True)

        self.gridLayout.addWidget(self.label_77, 8, 5, 1, 1)

        self.label_19 = QLabel(self.page2_soteterdo)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setScaledContents(True)

        self.gridLayout.addWidget(self.label_19, 1, 5, 1, 1)

        self.label_53 = QLabel(self.page2_soteterdo)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setScaledContents(True)

        self.gridLayout.addWidget(self.label_53, 5, 5, 1, 1)

        self.label_70 = QLabel(self.page2_soteterdo)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setScaledContents(True)

        self.gridLayout.addWidget(self.label_70, 6, 3, 1, 1)

        self.label_76 = QLabel(self.page2_soteterdo)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setScaledContents(True)

        self.gridLayout.addWidget(self.label_76, 8, 6, 1, 1)

        self.label_35 = QLabel(self.page2_soteterdo)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setScaledContents(True)

        self.gridLayout.addWidget(self.label_35, 3, 5, 1, 1)

        self.label_10 = QLabel(self.page2_soteterdo)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setScaledContents(True)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_22 = QLabel(self.page2_soteterdo)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setScaledContents(True)

        self.gridLayout.addWidget(self.label_22, 2, 3, 1, 1)

        self.label_20 = QLabel(self.page2_soteterdo)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setScaledContents(True)

        self.gridLayout.addWidget(self.label_20, 1, 4, 1, 1)

        self.label7_10 = QLabel(self.page2_soteterdo)
        self.label7_10.setObjectName(u"label7_10")
        self.label7_10.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_10, 0, 1, 1, 1)

        self.label_41 = QLabel(self.page2_soteterdo)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setScaledContents(True)

        self.gridLayout.addWidget(self.label_41, 5, 7, 1, 1)

        self.label_63 = QLabel(self.page2_soteterdo)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setScaledContents(True)

        self.gridLayout.addWidget(self.label_63, 4, 0, 1, 1)

        self.label_79 = QLabel(self.page2_soteterdo)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setScaledContents(True)

        self.gridLayout.addWidget(self.label_79, 8, 3, 1, 1)

        self.label_78 = QLabel(self.page2_soteterdo)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setScaledContents(True)

        self.gridLayout.addWidget(self.label_78, 8, 4, 1, 1)

        self.label_29 = QLabel(self.page2_soteterdo)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setScaledContents(True)

        self.gridLayout.addWidget(self.label_29, 6, 1, 1, 1)

        self.label7_14 = QLabel(self.page2_soteterdo)
        self.label7_14.setObjectName(u"label7_14")
        self.label7_14.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_14, 0, 7, 1, 1)

        self.label_37 = QLabel(self.page2_soteterdo)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setScaledContents(True)

        self.gridLayout.addWidget(self.label_37, 4, 7, 1, 1)

        self.label_42 = QLabel(self.page2_soteterdo)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setScaledContents(True)

        self.gridLayout.addWidget(self.label_42, 4, 8, 1, 1)

        self.label7_15 = QLabel(self.page2_soteterdo)
        self.label7_15.setObjectName(u"label7_15")
        self.label7_15.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_15, 0, 6, 1, 1)

        self.label_24 = QLabel(self.page2_soteterdo)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setScaledContents(True)

        self.gridLayout.addWidget(self.label_24, 2, 5, 1, 1)

        self.label_58 = QLabel(self.page2_soteterdo)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setScaledContents(True)

        self.gridLayout.addWidget(self.label_58, 7, 6, 1, 1)

        self.label_34 = QLabel(self.page2_soteterdo)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setScaledContents(True)

        self.gridLayout.addWidget(self.label_34, 3, 3, 1, 1)

        self.label_39 = QLabel(self.page2_soteterdo)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setScaledContents(True)

        self.gridLayout.addWidget(self.label_39, 6, 7, 1, 1)

        self.label_54 = QLabel(self.page2_soteterdo)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setScaledContents(True)

        self.gridLayout.addWidget(self.label_54, 6, 5, 1, 1)

        self.label8 = QLabel(self.page2_soteterdo)
        self.label8.setObjectName(u"label8")
        self.label8.setScaledContents(True)

        self.gridLayout.addWidget(self.label8, 1, 2, 1, 1)

        self.label_8 = QLabel(self.page2_soteterdo)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setScaledContents(True)

        self.gridLayout.addWidget(self.label_8, 9, 6, 1, 1)

        self.label7_12 = QLabel(self.page2_soteterdo)
        self.label7_12.setObjectName(u"label7_12")
        self.label7_12.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_12, 0, 3, 1, 1)

        self.label_6 = QLabel(self.page2_soteterdo)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setScaledContents(True)

        self.gridLayout.addWidget(self.label_6, 2, 8, 1, 1)

        self.label = QLabel(self.page2_soteterdo)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_56 = QLabel(self.page2_soteterdo)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setScaledContents(True)

        self.gridLayout.addWidget(self.label_56, 5, 6, 1, 1)

        self.label2 = QLabel(self.page2_soteterdo)
        self.label2.setObjectName(u"label2")
        self.label2.setScaledContents(True)

        self.gridLayout.addWidget(self.label2, 2, 1, 1, 1)

        self.label_23 = QLabel(self.page2_soteterdo)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setScaledContents(True)

        self.gridLayout.addWidget(self.label_23, 2, 4, 1, 1)

        self.label_74 = QLabel(self.page2_soteterdo)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setScaledContents(True)

        self.gridLayout.addWidget(self.label_74, 8, 8, 1, 1)

        self.label_71 = QLabel(self.page2_soteterdo)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setScaledContents(True)

        self.gridLayout.addWidget(self.label_71, 5, 4, 1, 1)

        self.label7_17 = QLabel(self.page2_soteterdo)
        self.label7_17.setObjectName(u"label7_17")
        self.label7_17.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_17, 0, 4, 1, 1)

        self.label_5 = QLabel(self.page2_soteterdo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setScaledContents(True)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label7_16 = QLabel(self.page2_soteterdo)
        self.label7_16.setObjectName(u"label7_16")
        self.label7_16.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_16, 0, 5, 1, 1)

        self.label7_13 = QLabel(self.page2_soteterdo)
        self.label7_13.setObjectName(u"label7_13")
        self.label7_13.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_13, 0, 8, 1, 1)

        self.label6 = QLabel(self.page2_soteterdo)
        self.label6.setObjectName(u"label6")
        self.label6.setScaledContents(True)

        self.gridLayout.addWidget(self.label6, 2, 7, 1, 1)

        self.label_21 = QLabel(self.page2_soteterdo)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setScaledContents(True)

        self.gridLayout.addWidget(self.label_21, 1, 3, 1, 1)

        self.label_25 = QLabel(self.page2_soteterdo)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setScaledContents(True)

        self.gridLayout.addWidget(self.label_25, 9, 3, 1, 1)

        self.label_66 = QLabel(self.page2_soteterdo)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setScaledContents(True)

        self.gridLayout.addWidget(self.label_66, 7, 0, 1, 1)

        self.label_4 = QLabel(self.page2_soteterdo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(True)

        self.gridLayout.addWidget(self.label_4, 9, 8, 1, 1)

        self.label_26 = QLabel(self.page2_soteterdo)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setScaledContents(True)

        self.gridLayout.addWidget(self.label_26, 9, 4, 1, 1)

        self.label_69 = QLabel(self.page2_soteterdo)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setScaledContents(True)

        self.gridLayout.addWidget(self.label_69, 7, 3, 1, 1)

        self.label_47 = QLabel(self.page2_soteterdo)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setScaledContents(True)

        self.gridLayout.addWidget(self.label_47, 4, 2, 1, 1)

        self.label3 = QLabel(self.page2_soteterdo)
        self.label3.setObjectName(u"label3")
        self.label3.setScaledContents(True)

        self.gridLayout.addWidget(self.label3, 9, 1, 1, 1)

        self.label_52 = QLabel(self.page2_soteterdo)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setScaledContents(True)

        self.gridLayout.addWidget(self.label_52, 7, 4, 1, 1)

        self.label_2 = QLabel(self.page2_soteterdo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 1, 8, 1, 1)

        self.label_38 = QLabel(self.page2_soteterdo)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setScaledContents(True)

        self.gridLayout.addWidget(self.label_38, 7, 8, 1, 1)

        self.label_68 = QLabel(self.page2_soteterdo)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setScaledContents(True)

        self.gridLayout.addWidget(self.label_68, 7, 2, 1, 1)

        self.label7_11 = QLabel(self.page2_soteterdo)
        self.label7_11.setObjectName(u"label7_11")
        self.label7_11.setScaledContents(True)

        self.gridLayout.addWidget(self.label7_11, 0, 2, 1, 1)

        self.label_51 = QLabel(self.page2_soteterdo)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setScaledContents(True)

        self.gridLayout.addWidget(self.label_51, 6, 4, 1, 1)

        self.label7 = QLabel(self.page2_soteterdo)
        self.label7.setObjectName(u"label7")
        self.label7.setScaledContents(True)

        self.gridLayout.addWidget(self.label7, 1, 1, 1, 1)

        self.label_18 = QLabel(self.page2_soteterdo)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setScaledContents(True)

        self.gridLayout.addWidget(self.label_18, 1, 7, 1, 1)

        self.label_46 = QLabel(self.page2_soteterdo)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setScaledContents(True)

        self.gridLayout.addWidget(self.label_46, 4, 3, 1, 1)

        self.label_9 = QLabel(self.page2_soteterdo)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setScaledContents(True)

        self.gridLayout.addWidget(self.label_9, 9, 2, 1, 1)

        self.label_62 = QLabel(self.page2_soteterdo)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setScaledContents(True)

        self.gridLayout.addWidget(self.label_62, 3, 0, 1, 1)

        self.label_7 = QLabel(self.page2_soteterdo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setScaledContents(True)

        self.gridLayout.addWidget(self.label_7, 9, 7, 1, 1)

        self.label_36 = QLabel(self.page2_soteterdo)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setScaledContents(True)

        self.gridLayout.addWidget(self.label_36, 3, 4, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

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

        self.widget = QWidget(self.page3_karakter)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1391, 421))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_cipo = QPushButton(self.widget)
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

        self.btn_pajzs = QPushButton(self.widget)
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

        self.btn_kesztyu = QPushButton(self.widget)
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

        self.btn_nadrag = QPushButton(self.widget)
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

        self.btn_sisak = QPushButton(self.widget)
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

        self.btn_gyuru = QPushButton(self.widget)
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

        self.btn_mellvert = QPushButton(self.widget)
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

        self.btn_kard = QPushButton(self.widget)
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
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_7.addWidget(self.listWidget, 0, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_7)

        self.stackedWidget.addWidget(self.page3_karakter)
        self.page4_harc = QWidget()
        self.page4_harc.setObjectName(u"page4_harc")
        self.widget1 = QWidget(self.page4_harc)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(1, 2, 1401, 411))
        self.gridLayout_4 = QGridLayout(self.widget1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_harcinditas = QPushButton(self.widget1)
        self.btn_harcinditas.setObjectName(u"btn_harcinditas")

        self.gridLayout_4.addWidget(self.btn_harcinditas, 1, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_203 = QLabel(self.widget1)
        self.label_203.setObjectName(u"label_203")

        self.gridLayout_8.addWidget(self.label_203, 0, 3, 1, 1)

        self.lbl_hos_vedekezes_ertek = QLabel(self.widget1)
        self.lbl_hos_vedekezes_ertek.setObjectName(u"lbl_hos_vedekezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_hos_vedekezes_ertek, 1, 2, 1, 1)

        self.label_98 = QLabel(self.widget1)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_8.addWidget(self.label_98, 2, 1, 1, 1)

        self.label_96 = QLabel(self.widget1)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_8.addWidget(self.label_96, 1, 1, 1, 1)

        self.label_205 = QLabel(self.widget1)
        self.label_205.setObjectName(u"label_205")

        self.gridLayout_8.addWidget(self.label_205, 1, 3, 1, 1)

        self.label_95 = QLabel(self.widget1)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_8.addWidget(self.label_95, 0, 1, 1, 1)

        self.lbl_szorny_kezdemenyezes_ertek = QLabel(self.widget1)
        self.lbl_szorny_kezdemenyezes_ertek.setObjectName(u"lbl_szorny_kezdemenyezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_szorny_kezdemenyezes_ertek, 2, 4, 1, 1)

        self.lbl_hos_kezdemenyezes_ertek = QLabel(self.widget1)
        self.lbl_hos_kezdemenyezes_ertek.setObjectName(u"lbl_hos_kezdemenyezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_hos_kezdemenyezes_ertek, 2, 2, 1, 1)

        self.lbl_hos_ero_ertek = QLabel(self.widget1)
        self.lbl_hos_ero_ertek.setObjectName(u"lbl_hos_ero_ertek")

        self.gridLayout_8.addWidget(self.lbl_hos_ero_ertek, 0, 2, 1, 1)

        self.label_207 = QLabel(self.widget1)
        self.label_207.setObjectName(u"label_207")

        self.gridLayout_8.addWidget(self.label_207, 2, 3, 1, 1)

        self.lbl_szorny_ero_ertek = QLabel(self.widget1)
        self.lbl_szorny_ero_ertek.setObjectName(u"lbl_szorny_ero_ertek")

        self.gridLayout_8.addWidget(self.lbl_szorny_ero_ertek, 0, 4, 1, 1)

        self.frame = QFrame(self.widget1)
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

        self.lbl_szorn_vedekezes_ertek = QLabel(self.widget1)
        self.lbl_szorn_vedekezes_ertek.setObjectName(u"lbl_szorn_vedekezes_ertek")

        self.gridLayout_8.addWidget(self.lbl_szorn_vedekezes_ertek, 1, 4, 1, 1)

        self.frame_2 = QFrame(self.widget1)
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

        self.stackedWidget.setCurrentIndex(4)


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
        self.label_73.setText("")
        self.label_60.setText("")
        self.label_80.setText("")
        self.label5.setText("")
        self.label_59.setText("")
        self.label_81.setText("")
        self.label_40.setText("")
        self.label_75.setText("")
        self.label_61.setText("")
        self.label_48.setText("")
        self.label_3.setText("")
        self.label4.setText("")
        self.label_17.setText("")
        self.label_55.setText("")
        self.label_43.setText("")
        self.label_28.setText("")
        self.label_31.setText("")
        self.label_30.setText("")
        self.label_33.setText("")
        self.label_65.setText("")
        self.label_32.setText("")
        self.label_64.setText("")
        self.label_57.setText("")
        self.label_67.setText("")
        self.label_50.setText("")
        self.label_27.setText("")
        self.label_49.setText("")
        self.label_44.setText("")
        self.label_72.setText("")
        self.label_45.setText("")
        self.label_77.setText("")
        self.label_19.setText("")
        self.label_53.setText("")
        self.label_70.setText("")
        self.label_76.setText("")
        self.label_35.setText("")
        self.label_10.setText("")
        self.label_22.setText("")
        self.label_20.setText("")
        self.label7_10.setText("")
        self.label_41.setText("")
        self.label_63.setText("")
        self.label_79.setText("")
        self.label_78.setText("")
        self.label_29.setText("")
        self.label7_14.setText("")
        self.label_37.setText("")
        self.label_42.setText("")
        self.label7_15.setText("")
        self.label_24.setText("")
        self.label_58.setText("")
        self.label_34.setText("")
        self.label_39.setText("")
        self.label_54.setText("")
        self.label8.setText("")
        self.label_8.setText("")
        self.label7_12.setText("")
        self.label_6.setText("")
        self.label.setText("")
        self.label_56.setText("")
        self.label2.setText("")
        self.label_23.setText("")
        self.label_74.setText("")
        self.label_71.setText("")
        self.label7_17.setText("")
        self.label_5.setText("")
        self.label7_16.setText("")
        self.label7_13.setText("")
        self.label6.setText("")
        self.label_21.setText("")
        self.label_25.setText("")
        self.label_66.setText("")
        self.label_4.setText("")
        self.label_26.setText("")
        self.label_69.setText("")
        self.label_47.setText("")
        self.label3.setText("")
        self.label_52.setText("")
        self.label_2.setText("")
        self.label_38.setText("")
        self.label_68.setText("")
        self.label7_11.setText("")
        self.label_51.setText("")
        self.label7.setText("")
        self.label_18.setText("")
        self.label_46.setText("")
        self.label_9.setText("")
        self.label_62.setText("")
        self.label_7.setText("")
        self.label_36.setText("")
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

