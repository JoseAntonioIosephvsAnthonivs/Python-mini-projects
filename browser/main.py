from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
	
	def go_home(self):
		self.browser.setUrl(QUrl('https://duckduckgo.com/'))
	
	def go_url(self):
		url = self.url_bar.text()
		self.browser.setUrl(QUrl(url))
		
	def update_url(self, url):
		self.url_bar.setText(url.toString())
		
	def __init__(self):
		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('https://duckduckgo.com/'))
		self.setCentralWidget(self.browser)
		self.showMaximized()
		
		# navbar
		navbar = QToolBar()
		self.addToolBar(navbar) 
		
		#Buttons
		
		# arrow back
		btn_arrow_back = QAction('<-', self)
		btn_arrow_back.triggered.connect(self.browser.back)
		navbar.addAction(btn_arrow_back)
		
		# arrow forward
		btn_arrow_forward = QAction('->', self)
		btn_arrow_forward.triggered.connect(self.browser.forward)
		navbar.addAction(btn_arrow_forward)
				

		
		#refresh 
		btn_refresh = QAction('Refresh', self)
		btn_refresh.triggered.connect(self.browser.reload)
		navbar.addAction(btn_refresh)
		
		#home
		btn_home = QAction('Home', self)
		btn_home.triggered.connect(self.go_home)
		navbar.addAction(btn_home)
		
		# addres bar
		self.url_bar = QLineEdit()
		self.url_bar.returnPressed.connect(self.go_url)
		navbar.addWidget(self.url_bar)
		self.browser.urlChanged.connect(self.update_url)

app = QApplication(sys.argv)
QApplication.setApplicationName('pybrowser')
windows = MainWindow()
app.exec()













