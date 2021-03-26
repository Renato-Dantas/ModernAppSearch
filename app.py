#pyuic5 modern.ui -o modern.py
from sys import argv
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QTableWidgetItem, QMessageBox
from PyQt5 import QtGui
from modern import Ui_MainWindow
from sqlStructure import sqliteFunctions


class main(QMainWindow, Ui_MainWindow, sqliteFunctions):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        super()
        self.sql = sqliteFunctions()

    # Buttons!
        self.btSign.clicked.connect(self.start)
        self.btSave.clicked.connect(self.saveInfo)
        self.btStartSearch.clicked.connect(self.showTable)

    # RadioButton!
        self.rbArea.clicked.connect(self.areaSearch)
        self.rbName.clicked.connect(self.nameSearch)

    # ComboBox Insert Area
        areaList = self.sql.readTxt()
        for area in areaList:
            self.cbInputArea.addItem(area)

    # ComboBox Functions!
    def areaSearch(self):
        self.cbSearch.clear()
        areaList = self.sql.readTxt()
        for area in areaList:
            self.cbSearch.addItem(area)
            
    def nameSearch(self):
        self.cbSearch.clear()
        nameList = self.sql.searchListNames()
        for name in nameList:
            self.cbSearch.addItem(str(name[0]))
        
    # Button Functions!
    def start(self):
        user = self.inputUser.text()
        password = self.inputPassword.text()
        self.lbName.setText(f'Welcome {user}!')
        self.resetWindow()

    def saveInfo(self):
        cod = self.inputCod.text()
        name = self.inputName.text()
        area = self.cbInputArea.currentText()
        city = self.inputCity.text()
        email = self.inputEmail.text()
        phone1 = self.inputPhone1.text()
        phone2 = self.inputPhone2.text()
        link = self.inputLink.text()

        if cod == '' or name == '' or area == '' or city == '' or email == '' or phone1 == '':
            self.popup('Please insert all required data')
        else:        
            info = [cod, name, area, city, email, phone1, phone2, link]
        try:
            self.sql.startDb()
            self.sql.insertValues(info)
            self.popup('Information saved on the database')
        except:
            self.popup('You trying put a duplicated information. Please Try Again!')
        finally:
            self.sql.closeConnection()

    def searchInfo(self):
        try:
            if self.rbArea.isChecked() == True:
                area = self.cbSearch.currentText()

                if area == 'All Information':
                    data = self.sql.selectAllData()
                else:
                    data = self.sql.searchSqlArea(area)

            elif self.rbName.isChecked() == True:
                name = self.cbSearch.currentText()
                data = self.sql.searchSqlName(name)
            return data

        except UnboundLocalError:
            self.popup('Please select the form and the area or name to search!')
        

    def showTable(self):
        try:
            data = self.searchInfo()
            information = []
            for info in data:
                info = list(info)
                information.append(info)
            
            row = 0
            index = 0
            self.tableWidget.setRowCount(len(information))
            for info in information:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(information[index][0]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(information[index][1]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(information[index][2]))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(information[index][3]))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(information[index][4]))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(information[index][5]))
                self.tableWidget.setItem(row, 6, QTableWidgetItem(information[index][6]))
                self.tableWidget.setItem(row, 7, QTableWidgetItem(information[index][7]))
                row +=1
                index +=1

            if self.rbName.isChecked() == True:
                self.getValues()
                self.btSave.setEnabled(False)
                self.btUpdate.setEnabled(True)
                self.btUpdate.clicked.connect(self.updateValues)
            else:
                self.btUpdate.setEnabled(False)
                self.btSave.setEnabled(True)
            
        except TypeError:
            try:
                pass
            except IndexError:
                pass
        
    def getValues(self):
        if self.rbName.isChecked() == True:
                name = self.cbSearch.currentText()
                data = self.sql.searchSqlName(name)
                data = list(data[0])

                self.inputCod.setText(data[0])
                self.inputName.setText(data[1])
                self.cbInputArea.setCurrentText(data[2])
                self.inputCity.setText(data[3])
                self.inputEmail.setText(data[4])
                self.inputPhone1.setText(data[5])
                self.inputPhone2.setText(data[6])
                self.inputLink.setText(data[7])
        
        else:
                self.inputCod.setText('')
                self.inputName.setText('')
                self.cbInputArea.setCurrentText('')
                self.inputCity.setText('')
                self.inputEmail.setText('')
                self.inputPhone1.setText('')
                self.inputPhone2.setText('')
                self.inputLink.setText('')

    def updateValues(self):
        actual_name = self.cbSearch.currentText()
        cod = self.inputCod.text()
        name = self.inputName.text()
        area = self.cbInputArea.currentText()
        city = self.inputCity.text()
        email = self.inputEmail.text()
        phone1 = self.inputPhone1.text()
        phone2 = self.inputPhone2.text()
        link = self.inputLink.text()

        if cod == '' or name == '' or area == '' or city == '' or email == '' or phone1 == '':
            self.popup('Please insert all required data')
        else:        
            info = [cod, name, area, city, email, phone1, phone2, link, actual_name]
        try:
            self.sql.startDb()
            self.sql.updateData(info)
            self.popup('Information saved on the database')
            self.resetWindow()
        finally:
            self.sql.closeConnection()

    def resetWindow(self):
        pass
        # self.rbArea.setChecked
        # self.rbArea.checkStateSet()

    def popup(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(texto)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

if __name__ == '__main__':
    qt = QApplication(argv)
    screen = main()
    screen.show()
    qt.exec_()