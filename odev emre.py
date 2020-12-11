from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mysql.connector
class stokTedarik(QDialog):
    def __init__(self,parent=None):
        super(stokTedarik,self).__init__(parent)
        grid=QGridLayout()

        
        grid.addWidget(QLabel("Çikolata"),0,0)
        grid.addWidget(QLabel("Peynir"),1,0)
        grid.addWidget(QLabel("Tavuk"),2,0)
        grid.addWidget(QLabel("Ekmek"),3,0)
        grid.addWidget(QLabel("Süt"),4,0)

        self.gofretSat=QLineEdit()
        self.peynirSat=QLineEdit()
        self.tavukSat=QLineEdit()
        self.ekmekSat=QLineEdit()
        self.sutSat=QLineEdit()

        self.gofretSip=QLineEdit()
        self.peynirSip=QLineEdit()
        self.tavukSip=QLineEdit()
        self.ekmekSip=QLineEdit()
        self.sutSip=QLineEdit()

        self.gofretAdet=QLabel()
        self.peynirAdet=QLabel()
        self.tavukAdet=QLabel()
        self.ekmekAdet=QLabel()
        self.sutAdet=QLabel()
        
        self.satisButon=QPushButton("SAT")       
        self.siparisButon=QPushButton("SİPARİŞ")
        
        
      #ekrana ekleme
        
        grid.addWidget(self.gofretSat,0,1)
        grid.addWidget(self.peynirSat,1,1)
        grid.addWidget(self.tavukSat,2,1)
        grid.addWidget(self.ekmekSat,3,1)
        grid.addWidget(self.sutSat,4,1)
        
        grid.addWidget(self.gofretSip,0,2)
        grid.addWidget(self.peynirSip,1,2)
        grid.addWidget(self.tavukSip,2,2)
        grid.addWidget(self.ekmekSip,3,2)
        grid.addWidget(self.sutSip,4,2)

        grid.addWidget(self.gofretAdet,0,3)
        grid.addWidget(self.peynirAdet,1,3)
        grid.addWidget(self.tavukAdet,2,3)
        grid.addWidget(self.ekmekAdet,3,3)
        grid.addWidget(self.sutAdet,4,3)

        grid.addWidget(self.satisButon,5,1)           
        grid.addWidget(self.siparisButon,5,2)     

        self.setLayout(grid)

        def sat(self):
            gofret=self.gofretAdet.text()
            baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="bimbucasube")
            isaretci=baglanti.cursor()
            isaretci.execute('''SELECT * FROM stokyonetimi '''%stok_miktar)
            row=isaretci.fetchall()#[[25]]
            for r in row:#[25]
                res=int(''.join(map(str,r)))#25
                res=res-1#24
                isaretci.execute('''SELECT * FROM stokyonetimi ''')
                gelenler=isaretci.fetchall()#[[can,111,515,515]]
                for row in gelenler:#[can,111,515,515]
                    self.gofretAdet.setText(row[1])#can
                    self.peynirAdet.setText(row[2])
                    self.tavukAdet.setText(row[3])
                    self.ekmekAdet.setText(row[4])
                    self.sutAdet.setText(row[5])
                 
            baglanti.close()
            
            

        













uyg=QApplication([])
pencere=stokTedarik()
pencere.show()
uyg.exec_()
