import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class PencereOne(QWidget):
    def __init__(self):
        super().__init__()
    def pencereGenel(self,Form):
        self.pencereler = []
        self.Form = Form
        self.yazi = QLabel("Lütfen notepad ismini giriniz: ")
        self.enter = QPushButton("Ok")
        self.notepadName = QLineEdit()

        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.ArrowCursor))

        horizLay = QHBoxLayout()
        vL = QVBoxLayout()

        horizLay.addStretch()
        horizLay.addWidget(self.yazi)
        horizLay.addStretch()
        horizLay.addWidget(self.notepadName)
        horizLay.addStretch()
        horizLay.addWidget(self.enter)

        vL.addLayout(horizLay)
        Form.setLayout(vL)

        self.enter.clicked.connect(self.click)

    def click(self):
        pencere2 = PencereTwo()
        pencere2.setWindowTitle(self.notepadName.text())
        self.pencereler.append(pencere2)
        Form.close()

class PencereTwo(QWidget):
    def __init__(self):
        super().__init__()
        self.gorsel()

    def gorsel(self):
        horizLay = QHBoxLayout()
        vL = QVBoxLayout()

        vL.addWidget(Pencere2Menu())

        self.setLayout(vL)
        self.setGeometry(500, 500, 600, 600)
        self.show()
class Pencere2Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencereMenusu()
    def pencereMenusu(self):

        self.yazi2 = QPlainTextEdit()
        self.setCentralWidget(self.yazi2)

        font= QFontDatabase.systemFont(QFontDatabase.FixedFont)
        font.setPointSize(13)
        font.setFamily("Comic Sans MS")
        font.setItalic(True)
        self.yazi2.setFont(font)

        self.path = None

        status= QStatusBar()
        self.setStatusBar(status)

        toolbar=QToolBar()
        toolbar.setIconSize(QSize(14,14))
        self.addToolBar(toolbar)

        menuOlustur=QMenuBar()
        menuOlustur=self.menuBar()

        dosyaM=menuOlustur.addMenu("Dosya")
        duzenMen=menuOlustur.addMenu("Düzen")

        dYeni=QAction("Yeni",self)
        dosyaM.addAction(dYeni)

        dYeniPencere=QAction("Yeni pencere",self)
        dosyaM.addAction(dYeniPencere)

        dAc=QAction(QIcon(os.path.join("dosya_ac.png")),"Aç..",self)
        dAc.setStatusTip("istediğiniz dosyayı açmanızı sağlar..")
        dAc.setShortcut("Ctrl+O")
        toolbar.addAction(dAc)
        dosyaM.addAction(dAc)


        dKaydet=QAction(QIcon(os.path.join("kaydet.png")),"Kaydet",self)
        dKaydet.setStatusTip("dosyanızı kaydedin")
        dKaydet.setShortcut("Ctrl+S")
        toolbar.addAction(dKaydet)
        dosyaM.addAction(dKaydet)

        dFarkliKaydet=QAction(QIcon(os.path.join("farkli_kaydet.png")),"Farklı Kaydet",self)
        dKaydet.setStatusTip("dosyanızı bilgisayarınızda farklı kaydedin")
        toolbar.addAction(dFarkliKaydet)
        dosyaM.addAction(dFarkliKaydet)

        dYazdir=QAction(QIcon(os.path.join("yazdir.png")),"yazdır",self)
        dYazdir.setStatusTip("dosyanızı yazdırmanızı sağlar")
        dYazdir.setShortcut("Ctrl+W")
        toolbar.addAction(dYazdir)
        dosyaM.addAction(dYazdir)

        dCikis=QAction("Çıkış",self)
        dCikis.setShortcut("Esc")
        dosyaM.addAction(dCikis)

        gAl=QAction(QIcon(os.path.join("geri_al.png")),"Geri Al",self)
        gAl.setStatusTip("yapılan işlemi geri alır.")
        gAl.setShortcut("Ctrl+Z")
        toolbar.addAction(gAl)
        duzenMen.addAction(gAl)

        ilerAl = QAction(QIcon(os.path.join("ileri_al.png")), "İleri Al", self)
        ilerAl.setStatusTip("yapılan işlemi ileri alır.")
        ilerAl.setShortcut("Ctrl+Y")
        toolbar.addAction(ilerAl)
        duzenMen.addAction(ilerAl)

        kes = QAction(QIcon(os.path.join("kes.png")), "Kes", self)
        kes.setStatusTip("seçili kısmı kesmenizi sağlar.")
        kes.setShortcut("Ctrl+X")
        toolbar.addAction(kes)
        duzenMen.addAction(kes)

        kop = QAction(QIcon(os.path.join("kopyala.png")), "Kopyala", self)
        kop.setStatusTip("seçili kısmı kopyalamanızı sağlar.")
        kop.setShortcut("Ctrl+C")
        toolbar.addAction(kop)
        duzenMen.addAction(kop)

        yap = QAction(QIcon(os.path.join("yapistir.png")), "Yapıştır", self)
        yap.setStatusTip("Seçtiğiniz kısmı yapıştırmanızı sağlar.")
        yap.setShortcut("Ctrl+V")
        toolbar.addAction(yap)
        duzenMen.addAction(yap)

        hepSec = QAction(QIcon(os.path.join("hepsini_sec.png")), "Hepsini Seç", self)
        hepSec.setStatusTip("sayfanın tümünü seçer.")
        hepSec.setShortcut("Ctrl+A")
        toolbar.addAction(hepSec)
        duzenMen.addAction(hepSec)

        dAc.triggered.connect(self.DosyaAc)
        dKaydet.triggered.connect(self.DosyaKaydet)
        dFarkliKaydet.triggered.connect(self.DosyaFarkliKaydet)
        dYazdir.triggered.connect(self.DosyaYazdir)

        gAl.triggered.connect(self.yazi2.undo)
        ilerAl.triggered.connect(self.yazi2.redo)
        kes.triggered.connect(self.yazi2.cut)
        kop.triggered.connect(self.yazi2.copy)
        yap.triggered.connect(self.yazi2.paste)
        hepSec.triggered.connect(self.yazi2.selectAll)

        dCikis.triggered.connect(self.CikisYapma)

        self.normalGeometry()
        self.show()

    def basligi_guncelle(self):
        self.setWindowTitle("{} - NotePad".format(os.path.basename(self.path) if self.path else "Untitled"))

    def hataMesaji(self,mesaj):
        hata=QMessageBox()
        hata.setText(mesaj)
        hata.setIcon(QMessageBox.Critical)
        hata.show()
    def DosyaAc(self):
        path,_ = QFileDialog.getOpenFileName(self,"Dosya aç","","Text Dosyaları(*.txt)")
        if path:
            try:
                with open(path,"r") as file:
                    text=file.read()
            except Exception as e:
                self.hataMesaji(e)
            else:
                self.yazi2.setPlainText(text)
                self.path=path
                self.basligi_guncelle()

    def DosyaKaydet(self):
        if (self.path==None):
            return self.DosyaFarkliKaydet()
        text = self.yazi2.toPlainText()
        try:
            with open(self.path,"w") as file:
                file.write(text)
        except Exception as e:
            self.hataMesaji(e)

    def DosyaFarkliKaydet(self):
        path, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", "", "Text Dosyaları (*.txt)")
        if not path:
            return
        text= self.yazi2.toPlainText()
        try:
            with open(path,"w") as file:
                file.write(text)
        except Exception as e:
            self.hataMesaji(e)
        else:
            self.path=path
            self.basligi_guncelle()
    def DosyaYazdir(self):
        mesaj=QPrintDialog()
        if mesaj.exec_():
            self.yazi2.print_(mesaj.printer())

    def CikisYapma(self):
        qApp.exit()


app = QApplication(sys.argv)
Form = QWidget()
Po = PencereOne()
Po.pencereGenel(Form)
Form.show()
sys.exit(app.exec_())