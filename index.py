from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel ,QFrame ,QRadioButton,  QLineEdit, QPushButton,QMessageBox,QButtonGroup
import sys

class fenêtre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,700,900)
        self.setFixedSize(700,950)
        self.setStyleSheet("background-color:#4F46E5;")
        
                
        self.title=QLabel("Weight Conversion \n         Calculator",self)
        self.title.setGeometry(100,-80,500,350)
        self.title.setStyleSheet(" color:#FFFFFF;font-size:50px;font-weight:900;font-family:Arial;")
        
        #frame 1:
        self.frame1=QFrame(self)
        self.frame1.setGeometry(60, 180, 560, 800)
        self.rb1 = QRadioButton("Kilograms to Pounds", self.frame1)
        self.rb1.setGeometry(80, 70, 400, 60)
        self.rb1.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.rb2 = QRadioButton("Pounds to Kilograms", self.frame1)
        self.rb2.setGeometry(80, 150, 400, 60)
        self.rb2.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;color:#7C2D12;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500; ")
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.rb1)
        self.button_group.addButton(self.rb2)
        
        self.entry_label=QLabel("Enter the weight:",self.frame1)
        self.entry_label.setGeometry(80,250,400,70)
        self.entry_label.setStyleSheet("color:#FFFFFF;padding:10px ; border-radius:30px;font-family:Arial;font-size:20px;font-weight:500;")
        self.entry_input=QLineEdit(self.frame1)
        self.entry_input.setGeometry(80,340,400,70)
        self.entry_input.setStyleSheet("background:rgba(255, 248, 240, 0.9); border:2px solid #CA8A04;border-radius:20px; ")
        self.entry_input.setPlaceholderText("0.00")
        
        self.calculate=QPushButton("Calculate",self.frame1)
        self.calculate.setGeometry(80,460,100,50)
        self.calculate.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#F97316;")
        self.calculate.clicked.connect(self.calculate_function)
        self.exit=QPushButton("Exit",self.frame1)
        self.exit.setGeometry(365,460,100,50)
        self.exit.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#7C3AED;")
        self.exit.clicked.connect(self.close)
        #self.frame1.hide()
        
        
        
        # frame2 result
        self.frame2=QFrame(self)
        self.frame2.setGeometry(60, 180, 560, 700)
        self.entry_label=QLabel("Result:",self.frame2)
        self.entry_label.setGeometry(80,50,400,100)
        self.entry_label.setStyleSheet("color:#10B981;font-weight:900;font-size:40px;font-family:Arial;")
        self.result_label=QLabel("",self.frame2)
        self.result_label.setGeometry(95,140,400,80)
        self.result_label.setStyleSheet("color:black;font-weight:700;font-size:25px;font-family:Arial;border:2px solid violet;")

        
        self.home_btn=QPushButton("Home", self.frame2)
        self.home_btn.setGeometry(80,230,80,50)
        self.home_btn.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#F97316;")
        self.home_btn.clicked.connect(self.home)
        self.exit_btn=QPushButton("Exit", self.frame2)
        self.exit_btn.setGeometry(330,230,80,50)
        self.exit_btn.setStyleSheet("color:black;font-weight:700;font-size:15px;border-radius:20px;background-color:#F59E0B;")
        self.exit_btn.clicked.connect(self.close)

        self.frame2.hide()
        
    def calculate_function(self):
        try:  
            if self.entry_input.text()=="":
                QMessageBox.warning(self,"Error","Please enter a weight")
                return          
            input=float(self.entry_input.text())
            if  input < 0 or input==0:
                QMessageBox.warning(self,"Error" , "Weight can't be Negative. Enter a Positive Number")
                return
            if not self.button_group.checkedButton():
                QMessageBox.warning(self,"Error","Please select a conversion type")
                self.entry_input.clear()
                return
            
            

            if self.rb1.isChecked():
                result_1=input*2.20462
                self.result_label.setText(f"{input}Kg = {result_1:.2f}Ib")
            elif self.rb2.isChecked():
                result_2=input/2.20462
                self.result_label.setText(f"{input}Ib = {result_2:.2f}Kg")
            self.frame1.hide()
            self.frame2.show()
        except ValueError:
            QMessageBox.warning(self,"Error","Enter valid number")
            self.home()
            
            
    def home(self):

        self.entry_input.clear()
        self.button_group.setExclusive(False)
        for rb in [self.rb1,self.rb2]:
            rb.setChecked(False)
        self.button_group.setExclusive(True)
        self.frame1.show()
        self.frame2.hide()
        
def main():
    app=QApplication(sys.argv)
    window=fenêtre()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()