import sys
import random
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QColor


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        
                                            
        self.loadTable()                                                # 테이블 생성과 글꼴, 배경색 등 정의
        self.ui.add_button.clicked.connect(self.data_save)              # 추가 버튼을 누르면 data_save 함수가 실행되도록 연결하는 것
        self.ui.delete_button.clicked.connect(self.data_delete)          # 삭제 버튼을 누르면 data_delete 함수가 실행되도록 연결하는 것
        self.ui.AllDelete_button.clicked.connect(self.data_alldelete)   # 모두 삭제 버튼을 누르면 data_alldelete 함수가 실행되도록 연결하는 것
        self.ui.random_button.clicked.connect(self.data_random)         # 무작위 버튼을 누르면 data_random 함수가 실행되도록 연결하는 것
        
        self.ui.add_button_2.clicked.connect(self.core_save)
        self.ui.delete_button_2.clicked.connect(self.core_delete)
        self.ui.AllDelete_button_2.clicked.connect(self.core_alldelete)
        self.ui.random_button_2.clicked.connect(self.core_random)
        
        self.ui.run_button.clicked.connect(self.Run)
       
    '''
       self.ui.totalconsumption.setText('24W') # 전체 소비전력 출력 
       
    '''
            
        
        
    
    def data_random(self):                                          # 무작위 버튼을 누르면 실행되는 함수
        if self.ui.tableWidget.rowCount() <= 0:
            
            processNum = random.randrange(1,16)
            for i in range(0,processNum):
                ID = i
                AT = str(random.randrange(1,11))
                BT = str(random.randrange(1,11))
                rowCount = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowCount)
                self.ui.resultTable.insertRow(rowCount)
                self.ui.resultTable.setVerticalHeaderLabels([''] * self.ui.tableWidget.rowCount())
                self.ui.tableWidget.setVerticalHeaderLabels([''] * self.ui.tableWidget.rowCount())
                self.ui.tableWidget.setItem(rowCount,0,QTableWidgetItem(str(ID)))
                self.ui.tableWidget.setItem(rowCount,1,QTableWidgetItem(AT))
                self.ui.tableWidget.setItem(rowCount,2,QTableWidgetItem(BT))
                for i in range(0,3):
                        self.ui.tableWidget.item(rowCount,i).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
    def data_delete(self):                                       # 삭제 버튼을 누르면 실행되는 함수
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.removeRow(rowCount-1)
        self.ui.resultTable.removeRow(rowCount-1)    
    
    def data_alldelete(self):                                    # 모두 삭제 버튼을 누르면 실행되는 함수
        self.ui.tableWidget.setRowCount(0)
        self.ui.resultTable.setRowCount(0)
    
    def data_save(self):                                         # 추가 버튼을 누르면 실행되는 함수
        ID = self.ui.Process_ID.text()
        AT = self.ui.Process_AT.text()
        BT = self.ui.Process_BT.text()
        
        if (ID and AT and BT is not None) and (BT != "0"):                        # ID 혹은 AT 나 BT가 입력되지 않으면 실행되지 않음 and BT가 0이면 add 불가능
            rowCount = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowCount)
            self.ui.resultTable.insertRow(rowCount)
            self.ui.resultTable.setVerticalHeaderLabels([''] * self.ui.tableWidget.rowCount())
            self.ui.tableWidget.setVerticalHeaderLabels([''] * self.ui.tableWidget.rowCount())
            self.ui.tableWidget.setItem(rowCount,0,QTableWidgetItem(ID))
            self.ui.tableWidget.setItem(rowCount,1,QTableWidgetItem(AT))
            self.ui.tableWidget.setItem(rowCount,2,QTableWidgetItem(BT))
            for i in range(0,3):
                self.ui.tableWidget.item(rowCount,i).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
      
            
    def core_save(self):
        Type = self.ui.coreType.currentText()
        
        rowCount = self.ui.coreTable.rowCount()
        if rowCount<=3:
            self.ui.coreTable.insertRow(rowCount)
            self.ui.coreTable.setItem(rowCount,0,QTableWidgetItem(Type))
            self.ui.coreTable.item(rowCount,0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
           
    def core_delete(self):
        rowCount = self.ui.coreTable.rowCount()
        self.ui.coreTable.removeRow(rowCount-1)
        
    
    def core_alldelete(self):
        self.ui.coreTable.setRowCount(0)

    
    def core_random(self):
        processNum = random.randrange(1,5)
        
        for i in range(0,processNum):
            typelist = ["P-Core","E-Core"]
            Type = typelist[random.randrange(0,2)]
            rowCount = self.ui.coreTable.rowCount()
            if rowCount <=3:
                self.ui.coreTable.insertRow(rowCount)
                self.ui.coreTable.setItem(rowCount,0,QTableWidgetItem(Type))
                self.ui.coreTable.item(rowCount,0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            else:
                break
     
    def loadTable(self):
        font = QFont('Bahnschrift SemiBold', 10)                  
        font.setBold(True)                                       #  제목 글꼴 두껍게 
        font.setPointSize(10)           
        
        color = QColor(71, 144, 209)
        self.ui.coreTable.horizontalHeader().setStyleSheet('QHeaderView::section { background-color: %s }' % color.name())  # 제목 배경 색 지정 
        self.ui.coreTable.horizontalHeader().setFont(font)
        self.ui.coreTable.setRowCount(0)
        self.ui.coreTable.setColumnCount(2)
        self.ui.coreTable.setHorizontalHeaderLabels(('Type','Power Consumption'))  # 테이블 제목 지정
        self.ui.coreTable.setColumnWidth(0,195)    # col 길이 조정
        self.ui.coreTable.setColumnWidth(1,196)
        self.ui.coreTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch) # 열 길이 자동 맞추기
        
        self.ui.tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section { background-color: %s }' % color.name())  # 제목 배경 색 지정 
        self.ui.tableWidget.horizontalHeader().setFont(font)
        self.ui.tableWidget.setRowCount(0)                      # 테이블 위젯 Row 설정
        self.ui.tableWidget.setColumnCount(3)                   # 테이블 위젯 Col 설정
        self.ui.tableWidget.setVerticalHeaderLabels([''] * self.ui.tableWidget.rowCount())
        self.ui.tableWidget.setHorizontalHeaderLabels(('ID','ArrivalTime','BurstTime'))  # 테이블 제목 지정
        self.ui.tableWidget.setColumnWidth(0,51)    # col 길이 조정
        self.ui.tableWidget.setColumnWidth(1,170)
        self.ui.tableWidget.setColumnWidth(2,170)
        
        self.ui.resultTable.horizontalHeader().setStyleSheet('QHeaderView::section { background-color: %s }' % color.name())  # 제목 배경 색 지정 
        self.ui.resultTable.horizontalHeader().setFont(font)
        self.ui.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 행 길이 자동 맞추기
        
    def resultTable_input(self,list):
        
        for i in range(0, len(list)):
                self.ui.resultTable.insertRow(i)
                self.ui.resultTable.setItem(i,0,QTableWidgetItem(list[i]['ProcessID']))
                self.ui.resultTable.setItem(i,1,QTableWidgetItem(list[i]['AT']))
                self.ui.resultTable.setItem(i,2,QTableWidgetItem(list[i]['BT']))
                self.ui.resultTable.setItem(i,3,QTableWidgetItem(list[i]['WT']))
                self.ui.resultTable.setItem(i,4,QTableWidgetItem(list[i]['TT']))
                self.ui.resultTable.setItem(i,5,QTableWidgetItem(list[i]['NTT']))
                for j in range(0,6):
                    self.ui.resultTable.item(i,j).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    
    def PowerConsumption(self,list):
        for i in range(0,len(list)):
            self.ui.coreTable.setItem(i,1),QTableWidgetItem(list[i]['PowerConsumption']) 
            self.ui.coreTable.item(i,1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
    def Run(self):
        self
  
def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())
    
create_app()