# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pygame
import threading, _thread
#from mutagen.mp3 import MP3
#import stackprinter
from VishFileDialog import VishApp
import os



timeSeekerSliderValue = 0
globalComponentTimeSeeker = None
globalSoundLength = -1
globalCurrentSongFilePathURL = "D:\\bumbro.mp3"


class Ui_MainWindow(object):

    isMusicPlaying = "False"

    def getTimeSeekerComponent(self):
        return self.timeSeekHorizontalSlider



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(20, 10, 93, 28))
        self.playButton.setObjectName("playButton")
        self.playButton.clicked.connect(self.playButton_onClicked)


        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(20, 60, 93, 28))
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.clicked.connect(self.pauseButton_onClicked)


        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(20, 110, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.stopButton_onClicked)

        self.nextTrackButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextTrackButton.setGeometry(QtCore.QRect(20, 160, 93, 28))
        self.nextTrackButton.setObjectName("nextTrackButton")

        self.prevTrackButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevTrackButton.setGeometry(QtCore.QRect(20, 210, 93, 28))
        self.prevTrackButton.setObjectName("prevTrackButton")

        #please note  the listwidget was initially named playlistListView and later 
        #the listview was changed to listWidget, but the name wasnt changed. so the 
        #named object playlistListView is not a QListView but a QListWidget
        self.playlistListView = QtWidgets.QListWidget(self.centralwidget)
        self.playlistListView.setGeometry(QtCore.QRect(20, 340, 256, 261))
        self.playlistListView.setObjectName("playlistListView")
        self.playlistListView.clicked.connect(self.playlist_onClicked)
        self.playlistListView.itemDoubleClicked.connect(self.playlist_onDoubleClicked)
        global globalCurrentSongFilePathURL
        globalCurrentSongFilePathURL = "D:\\bumbro.mp3"


        self.addMP3ToPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.addMP3ToPlaylistButton.setGeometry(QtCore.QRect(30, 620, 93, 28))
        self.addMP3ToPlaylistButton.setObjectName("addMP3ToPlaylistButton")
        self.addMP3ToPlaylistButton.clicked.connect(self.addMP3Button_onClicked)


        self.removeMP3FromPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeMP3FromPlaylistButton.setGeometry(QtCore.QRect(160, 620, 93, 28))
        self.removeMP3FromPlaylistButton.setObjectName("removeMP3FromPlaylistButton")

        self.timeSeekHorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSeekHorizontalSlider.setGeometry(QtCore.QRect(30, 290, 231, 22))
        self.timeSeekHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSeekHorizontalSlider.setObjectName("timeSeekHorizontalSlider")
        self.timeSeekHorizontalSlider.valueChanged.connect(self.timeSeekHorizontalSlider_onValueChanged)
        global globalComponentTimeSeeker
        globalComponentTimeSeeker = self.timeSeekHorizontalSlider

        self.volumeVerticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeVerticalSlider.setGeometry(QtCore.QRect(250, 20, 22, 91))
        self.volumeVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeVerticalSlider.setObjectName("volumeVerticalSlider")
        #self.volumeVerticalSlider.setValue(0.55)
        self.volumeVerticalSlider.valueChanged.connect(self.volumeVerticalSlider_onValueChanged)
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VishMP3 Player"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.nextTrackButton.setText(_translate("MainWindow", "Next Track"))
        self.prevTrackButton.setText(_translate("MainWindow", "Prev Track"))
        self.addMP3ToPlaylistButton.setText(_translate("MainWindow", "Add Mp3"))
        self.removeMP3FromPlaylistButton.setText(_translate("MainWindow", "Remove Mp3"))



    def addMP3Button_onClicked(self):
        print("add mp3 button clicked")
        #fname = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "MP3 files (*.mp3)")
        self.openFileNameDialog()


    def openFileNameDialog(self):
        print("inside App:openFileNameDialog() method")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        dialog = QtWidgets.QFileDialog()
        fileName, _ = QFileDialog.getOpenFileName(dialog, "Add Mp3 to playlist", "", "All Files(*);; MP3 Files (*.mp3)", options=options)

        if fileName:
            print("file selected:"+fileName)
            #as of now, the path of the song is being added, because we need to access the mp3 path when QListWidget is clicked
            #songName = os.path.basename(fileName)   #later we can change the reqd variable from fileName to songName
            #self.playlistListView.addItem(songName)            
            self.playlistListView.addItem(fileName)            
                

    def volumeVerticalSlider_onValueChanged(self):
        offsetValue = self.volumeVerticalSlider.value()
        print("volume offset value:"+str(offsetValue))
        changeCurrentVolumeToValue(offsetValue)


    def timeSeekHorizontalSlider_onValueChanged(self):
        offsetValue = self.timeSeekHorizontalSlider.value()
        print("timeSeeker moved:"+str(offsetValue))
        pygame.mixer.music.rewind


        
    def updateTimeSeekHorizontalSliderAutomatically():
            print("updating TimeSeekHorizontalSlider automatically")

    def playlist_onClicked(self):
        print("playlist clicked")
        print("selected item:"+str(self.playlistListView.currentItem().text()))
        global globalCurrentSongFilePathURL
        globalCurrentSongFilePathURL = self.playlistListView.currentItem().text()
        print("inside method playlist_onClicked: value of globalCurrentSongFilePathURL: "+globalCurrentSongFilePathURL)

    def playlist_onDoubleClicked(self):
        print("inside method playlist_onDoubleClicked: ")
        global globalCurrentSongFilePathURL
        globalCurrentSongFilePathURL = self.playlistListView.currentItem().text()
        print("inside method playlist_onDoubleClicked: value of globalCurrentSongFilePathURL: "+globalCurrentSongFilePathURL)
        playmusic(globalCurrentSongFilePathURL)
        self.isMusicPlaying = "True"


    def playButton_onClicked(self):
            print("play button clicked")
            
            try:
                initMixer()
                filename = 'D:\\bumbro.mp3'
                
                #playmusic(filename)
                global globalCurrentSongFilePathURL
                playmusic(globalCurrentSongFilePathURL)
                print("inside method playButton_onClicked: value of globalCurrentSongFilePathURL:"+globalCurrentSongFilePathURL)
                self.isMusicPlaying = "True"
            except KeyboardInterrupt:   # to stop playing, press "ctrl-c"
                print("\nPlay Stopped by user")
            except Exception:
                print("unknown error")

    def pauseButton_onClicked(self):
        print("pause button clicked")
        try:
            if(self.isMusicPlaying is None):
                return

            if(self.isMusicPlaying == "True"):
                print("Value of isMusicPlaying:"+self.isMusicPlaying)
                pauseMusic()
                self.isMusicPlaying = "False"

            elif(self.isMusicPlaying == "False"):
                print("Value of isMusicPlaying:"+self.isMusicPlaying)
                unPauseMusic()
                self.isMusicPlaying = "True"


                
        except KeyboardInterrupt:   # to stop playing, press "ctrl-c"
            #pauseMusic()
            print("\nException:keyboard interrupt")
        except Exception as e:
            #print("Exception:"+e.message())
            print("Exception occured:"+e)


    def stopButton_onClicked(self):
        print("stop button clicked")
        try:
            stopmusic()
        except Exception as e:
            print("Exception occured while trying to invoke stopmusic() function")



def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
       This will load the whole sound into memory before playback
    """    
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        print("Playing...")
        clock.tick(1000)

def pauseMusic():
    pygame.mixer.music.pause()
    print("pygame pauseMusic function invoked")
#    currentTime = pygame.mixer.music.get_pos()
 #   print("current time of song:"+str(currentTime))


def unPauseMusic():
    pygame.mixer.music.unpause()
    print("pygame unPauseMusic function invoked")

def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
       This will stream the sound from disk while playing.
    """

    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    isMusicPlaying = "True" 
    print("soundfile:"+ soundfile)

    try:
        from mutagen.mp3 import MP3
        audio = MP3(soundfile)
        global globalSoundLength
        globalSoundLength = audio.info.length
        print("sound length:"+str(globalSoundLength))
        

    except Exception as e:
        print("Encountered Exception: Unable to start thread")
        print("Exception message:"+e.message())
        print("Exception arguments:"+ e.args())


def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()

def changeCurrentVolumeToValue(reqdVolumeValue):
    volumeValue = reqdVolumeValue/100.0
    print("volume value changed to :"+str(volumeValue))
    pygame.mixer.music.set_volume(volumeValue)

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()

    return freq, size, chan


def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)




##############################################################


def autoUpdateMethod(threadName, delay):
    print("inside autoupdate method")
    count = 0
    print("globalComponentTimeSeeker:"+str(globalComponentTimeSeeker.value()) )
    if globalComponentTimeSeeker == None:
        print("time seeker is none,exiting from method")
        

    if(pygame.mixer.get_init()==None):
        print("pygame's mixer is not initialized, exiting from method")
        

    while True:
        try:    
            offsetValue = globalComponentTimeSeeker.value()
            songDuration = pygame.mixer.music.get_pos()
            timeSeekerOffsetValue = 100.0/globalSoundLength
            reqdTimeSeekerValue = timeSeekerOffsetValue * songDuration
            reqdTimeSeekerValue = reqdTimeSeekerValue/1000.0 # converting milliseconds to seconds
            globalComponentTimeSeeker.setValue(reqdTimeSeekerValue)

        except Exception as exc:
            # strValue = sys.exc_info[0]
            # print("value of strValue:"+strValue)

            # if(sys.exc_info[0]=='pygame.error'):
            #     print("its a pygame error")

            errorList = sys.exc_info()
            errorString = "mixer not initialized"
            if(errorList[1] == errorString): # basically stopping the exception from raising when the pygame mixer module has not been initialized
                print("Exception raised when trying to access timeSeeker object")
                print("Exception :"+ format(exc))
                print("Exception reason, sys.exc_info[0]:"+ str(errorList[0]))
                print("Exception reason, sys.exc_info[1]:"+ str(errorList[1]))
                print("Exception reason, sys.exc_info[2]:"+ str(errorList[2]))            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)


    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    obj = ui.getTimeSeekerComponent()
    offsetValue = obj.value()
    #global timeSeekerSliderValue

    #timeSeekerSliderValue = offsetValue

    _thread.start_new_thread(autoUpdateMethod, ("AutoThread1", 1,))


    sys.exit(app.exec_())

