import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                            QPushButton, QLabel, QLineEdit, QTabWidget, QTabBar,
                             QStackedLayout, QToolBar, QAction, QMainWindow, QDesktopWidget, QFrame, QGraphicsDropShadowEffect, QShortcut,
                             QKeySequenceEdit, QSplitter, QSplitterHandle)
from PyQt5.QtGui import QIcon, QColor, QKeySequence, QWindow, QPainter, QPixmap, QImage, QImageReader
from PyQt5.QtCore import *
from PyQt5.QtNetwork import QNetworkProxyFactory, QNetworkRequest
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()



class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.CreateApp()
        self.setBaseSize(1366, 786)

    def CreateApp(self):

        #Keep track of tabs
        self.tabCount = 0
        self.tabs = []

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        #Creating tabs
        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.CloseTab)
        self.tabbar.tabBarClicked.connect(self.SwitchTab)

        self.tabbar.setCurrentIndex(0)

        #create addressbar
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = AddressBar()
        #new tab button
        self.AddTabButton = QPushButton("+")
        #connect address bar and button signals
        self.AddTabButton.clicked.connect(self.AddTab)
        self.addressbar.returnPressed.connect(self.BrowseTo)
        #set toolbar buttons
        self.BackButton = QPushButton("<")
        self.ForwardButton = QPushButton(">")
        self.RelaodButton = QPushButton("R")
        #connect toolbar buttons
        self.BackButton.clicked.connect(self.GoBack)
        self.ForwardButton.clicked.connect(self.GoForward)
        self.RelaodButton.clicked.connect(self.Reload)
        #build toolbar
        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.BackButton)
        self.ToolbarLayout.addWidget(self.ForwardButton)
        self.ToolbarLayout.addWidget(self.RelaodButton)
        self.ToolbarLayout.addWidget(self.addressbar)
        self.ToolbarLayout.addWidget(self.AddTabButton)
        #set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.layout.addWidget(self.container)
        self.setLayout(self.layout)

        self.AddTab()
        self.show()

    def CloseTab(self, i):
        self.tabbar.removeTab(i)

    def AddTab(self):
        i = self.tabCount

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        #giving id to tabs
        self.tabs[i].setObjectName("tab"+str(i))

        #create and open web view
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("http://google.com"))

        self.tabs[i].content.titleChanged.connect(lambda: self.SetTabContent(i, "title"))
        self.tabs[i].content.iconChanged.connect(lambda: self.SetTabContent(i, "icon"))
        self.tabs[i].content.urlChanged.connect(lambda: self.SetTabContent(i, "url"))
        #add web view to tabs layout
        self.tabs[i].layout.addWidget(self.tabs[i].content)
        #set top level tab from list to layout
        self.tabs[i].setLayout(self.tabs[i].layout)
        #add tab to top level stacked widget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])
        #set tab at the top of the screen
        self.tabbar.addTab("New Tab")
        self.tabbar.setTabData(i, {"object" : "tab{}".format(i), "initial":i})
        self.tabbar.setCurrentIndex(i)

        self.tabCount +=1

    def SwitchTab(self,i):
        if self.tabbar.tabData(i):
            td = self.tabbar.tabData(i)['object']
            tabContent = self.findChild(QWidget, td)
            self.container.layout.setCurrentWidget(tabContent)
            new_url = tabContent.url().toString()
            self.addressbar.setText(new_url)

    def BrowseTo(self):
        text = self.addressbar.text()
        i = self.tabbar.currentIndex()
        td = self.tabbar.tabData(i)['object']
        wv = self.findChild(QWidget, td).content

        if 'http' not in text:
            if "." not in text:
                url = "https://www.google.ca/#q={}".format(text)
            else:
                url = "http://{}".format(text)
        else:
            url = text

        wv.load(QUrl.fromUserInput(url))


    def SetTabContent(self, i, type):
        tab_name = self.tabs[i].objectName()
        count = 0
        running = True
        curr_tab = self.tabbar.tabData(self.tabbar.currentIndex())['object']

        if curr_tab == tab_name and type == 'url':
            new_url = self.findChild(QWidget, tab_name).content.url().toString()
            self.addressbar.setText(new_url)
            return False

        while running:
            tab_data_name = self.tabbar.tabData(count)

            if count >= 99:
                running = False
            if tab_name == tab_data_name['object']:
                if type == 'title':
                    newTitle = self.findChild(QWidget, tab_name).content.title()
                    self.tabbar.setTabText(count, newTitle)
                elif type == 'icon':
                    newIcon = self.findChild(QWidget, tab_name).content.icon()
                    self.tabbar.setTabIcon(count, newIcon)
                running = False
            else:
                count +=1

    def GoForward(self):
        activeIndex = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(activeIndex)['object']
        tab_content = self.findChild(QWidget, tab_name).content
        tab_content.forward()

    def GoBack(self):
        activeIndex = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(activeIndex)['object']
        tab_content = self.findChild(QWidget, tab_name).content
        tab_content.back()

    def Reload(self):
        activeIndex = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(activeIndex)['object']
        tab_content = self.findChild(QWidget, tab_name).content
        tab_content.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    with open("style.css","r") as style:
        app.setStyleSheet(style.read())
    sys.exit(app.exec_())
