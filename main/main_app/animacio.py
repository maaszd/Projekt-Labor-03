import os
from PySide6.QtCore import Qt, QPoint, Property, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve
from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect
from PySide6.QtGui import QPixmap, QPainter


class SebzesAnimacio:
    def __init__(self, ui):
        self.ui = ui

        self.ui.sebzes_lbl.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.ui.sebzes_lbl.raise_()

        self.opacity = QGraphicsOpacityEffect(self.ui.sebzes_lbl)
        self.opacity.setOpacity(0.0)
        self.ui.sebzes_lbl.setGraphicsEffect(self.opacity)

        self.pos_anim = QPropertyAnimation(self.ui.sebzes_lbl, b"pos", ui.page4_harc)
        self.pos_anim.setDuration(650)
        self.pos_anim.setEasingCurve(QEasingCurve.OutCubic)

        self.fade_anim = QPropertyAnimation(self.opacity, b"opacity", ui.page4_harc)
        self.fade_anim.setDuration(650)
        self.fade_anim.setStartValue(1.0)
        self.fade_anim.setEndValue(0.0)

        self.anim = QParallelAnimationGroup(ui.page4_harc)
        self.anim.addAnimation(self.pos_anim)
        self.anim.addAnimation(self.fade_anim)

    def start(self, cel_widget, sebzes_ertek):
        lbl = self.ui.sebzes_lbl
        self.anim.stop()

        lbl.setText(f"-{sebzes_ertek}")
        lbl.adjustSize()
        lbl.resize(lbl.width() + 20, lbl.height() + 10)

        kozpont = cel_widget.mapTo(self.ui.page4_harc, cel_widget.rect().center())
        start_pos = QPoint(kozpont.x() - lbl.width() // 2, kozpont.y() - 30)

        self.pos_anim.setStartValue(start_pos)
        self.pos_anim.setEndValue(QPoint(start_pos.x(), start_pos.y() - 60))
        self.opacity.setOpacity(1.0)

        lbl.move(start_pos)
        self.anim.start()


class KardAnimacio(QWidget):
    def __init__(self, ui):
        super().__init__(ui.page4_harc)
        self.ui = ui
        self.projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        self.felszerelt_kard_kep = None

        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setFixedSize(144, 144)
        self.hide()

        self._pixmap = QPixmap()
        self._szog = 0.0
        self._irany = 1
        self._callback = None

        self.pos_anim = QPropertyAnimation(self, b"pos", self)
        self.pos_anim.setDuration(500)

        self.szog_anim = QPropertyAnimation(self, b"szog", self)
        self.szog_anim.setDuration(500)
        self.szog_anim.setEasingCurve(QEasingCurve.InCubic)

        self.anim = QParallelAnimationGroup(self)
        self.anim.addAnimation(self.pos_anim)
        self.anim.addAnimation(self.szog_anim)
        self.anim.finished.connect(self._end)

    @Property(float)
    def szog(self):
        return self._szog

    @szog.setter
    def szog(self, ertek):
        self._szog = ertek
        self.update()

    def start(self, jobbra=True, becsapodas_callback=None):
        self.anim.stop()
        forras, cel = (self.ui.lbl_hos_img, self.ui.lbl_szorn_img) if jobbra else (self.ui.lbl_szorn_img, self.ui.lbl_hos_img)

        kep_utvonal = os.path.join(self.projekt_mappa, "assets", "sword.png")
        if jobbra and self.felszerelt_kard_kep:
            kep_utvonal = os.path.join(self.projekt_mappa, self.felszerelt_kard_kep)

        pixmap = QPixmap(kep_utvonal)
        pixmap = pixmap.scaled(96, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._pixmap = pixmap

        self._irany = 1 if jobbra else -1
        start = forras.mapTo(self.ui.page4_harc, forras.rect().center()) - self.rect().center()
        cel_pos = cel.mapTo(self.ui.page4_harc, cel.rect().center()) - self.rect().center()
        lendites = cel_pos + QPoint(-30 * self._irany, -35)
        end = cel_pos + QPoint(25 * self._irany, 25)

        self.pos_anim.setStartValue(start)
        self.pos_anim.setKeyValueAt(0.55, lendites)
        self.pos_anim.setEndValue(end)

        self.szog_anim.setStartValue(0.0)
        self.szog_anim.setKeyValueAt(0.55, -60.0 * self._irany)
        self.szog_anim.setEndValue(80.0 * self._irany)

        self._szog = 0.0
        self._callback = becsapodas_callback

        self.move(start)
        self.show()
        self.raise_()
        self.ui.sebzes_lbl.raise_()
        self.update()
        self.anim.start()

    def paintEvent(self, event):
        if self._pixmap.isNull():
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.translate(self.rect().center())
        painter.rotate(self._szog)
        painter.scale(self._irany, 1)
        painter.drawPixmap(-self._pixmap.rect().center(), self._pixmap)
        painter.end()

    def _end(self):
        self.hide()
        if self._callback:
            cb = self._callback
            self._callback = None
            cb()
