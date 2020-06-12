# Written By Matthew Bodenstein
# DD/MM/YYYY
# 12/06/2020
# This is a basic calculator
from tkinter import *


class Calculator:

    def __init__(self):
        self.main = Tk()
        self.main.resizable(0, 0)
        self.main.title("CALCULATOR")

        self.width = 7  # button width
        self.height = 3  # button height

        ######### FRAMES ########
        self.fifthbottomframe = Frame(self.main)
        self.fifthbottomframe.pack(side=BOTTOM)

        self.fourthbottomframe = Frame(self.fifthbottomframe)
        self.fourthbottomframe.pack(side=BOTTOM)

        self.thirdbottomframe = Frame(self.fourthbottomframe)
        self.thirdbottomframe.pack(side=BOTTOM)

        self.secondbottomframe = Frame(self.thirdbottomframe)
        self.secondbottomframe.pack(side=BOTTOM)

        self.bottomframe = Frame(self.secondbottomframe)
        self.bottomframe.pack(side=BOTTOM)

        ######### Bottom Row #########

        self.dotButton = Button(self.bottomframe, text=".", command=lambda: self.changeText('.'), width=self.width,height=self.height, bg = '#666666')
        self.dotButton.pack(side=LEFT)

        self._0Button = Button(self.bottomframe, text="0", command=lambda: self.changeText(0), width=self.width , height=self.height,bg = '#888888')
        self._0Button.pack(side = LEFT)

        self.piButton = Button(self.bottomframe, text="DEL", command=lambda: self.changeText('DEL'), width=self.width, height=self.height,bg = '#666666')
        self.piButton.pack(side= LEFT )

        self.eqlButton = Button(self.bottomframe, text="=", command=lambda: self.changeText('='), width=self.width, height=self.height,bg = '#FA6E00')
        self.eqlButton.pack(side=LEFT)
        #############################################

        self._1Button = Button(self.secondbottomframe, text="1", command=lambda: self.changeText(1), width=self.width, height=self.height,bg = '#888888')
        self._1Button.pack(side = LEFT)

        self._2Button = Button(self.secondbottomframe, text="2", command=lambda: self.changeText(2), width=self.width, height=self.height,bg = '#888888')
        self._2Button.pack(side=LEFT)

        self._3Button = Button(self.secondbottomframe, text="3", command=lambda: self.changeText(3), width=self.width, height=self.height,bg = '#888888')
        self._3Button.pack(side=LEFT)

        self.plusButton = Button(self.secondbottomframe, text="+", command=lambda: self.changeText('+'), width=self.width, height=self.height,bg = '#666666')
        self.plusButton.pack(side=LEFT)
        ############################################

        self._4Button = Button(self.thirdbottomframe, text="4", command=lambda: self.changeText(4), width=self.width, height=self.height,bg = '#888888')
        self._4Button.pack(side=LEFT)

        self._5Button = Button(self.thirdbottomframe, text="5", command=lambda: self.changeText(5), width=self.width, height=self.height,bg = '#888888')
        self._5Button.pack(side=LEFT)

        self._6Button = Button(self.thirdbottomframe, text="6", command=lambda: self.changeText(6), width=self.width, height=self.height,bg = '#888888')
        self._6Button.pack(side=LEFT)

        self.minusButton = Button(self.thirdbottomframe, text="-", command=lambda: self.changeText('-'), width=self.width, height=self.height,bg = '#666666')
        self.minusButton.pack(side=LEFT)
        ###########################################

        self._7Button = Button(self.fourthbottomframe, text="7", command=lambda: self.changeText(7), width=self.width, height=self.height,bg = '#888888')
        self._7Button.pack(side=LEFT)

        self._8Button = Button(self.fourthbottomframe, text="8", command=lambda: self.changeText(8), width=self.width, height=self.height,bg = '#888888')
        self._8Button.pack(side=LEFT)

        self._9Button = Button(self.fourthbottomframe, text="9", command=lambda: self.changeText(9), width=self.width, height=self.height,bg = '#888888')
        self._9Button.pack(side=LEFT)

        self.timesButton = Button(self.fourthbottomframe, text="*", command=lambda: self.changeText('*'), width=self.width, height=self.height,bg = '#666666')
        self.timesButton.pack(side=LEFT)

        ###########################################
        self.ceButton = Button(self.fifthbottomframe, text="CE", command=lambda: self.changeText('CE'), width=self.width, height=self.height,bg = '#FA6E00')
        self.ceButton.pack(side=LEFT)

        self.lbButton = Button(self.fifthbottomframe, text="(", command=lambda: self.changeText('('), width=self.width, height=self.height,bg = '#666666')
        self.lbButton.pack(side=LEFT)

        self.rbButton = Button(self.fifthbottomframe, text=")", command=lambda: self.changeText(')'), width=self.width, height=self.height,bg = '#666666')
        self.rbButton.pack(side=LEFT)

        self.divButton = Button(self.fifthbottomframe, text="/", command=lambda: self.changeText('/'), width=self.width, height=self.height,bg = '#666666')
        self.divButton.pack(side=LEFT)
        ##########################################

        self.label = Label(self.main, text='', height = 3)
        self.label.config(font=("Courier", 14))
        self.label.pack()

        self.main.mainloop()
        ##########################################

    def changeText(self, num):
        if str(num) == "CE":
            self.label['text'] = ''
        elif str(num)=="=":
            equation = self.label['text']
            equation = eval(equation)
            self.label['text'] = str(equation)
        elif str(num) == 'DEL':
            self.label['text'] = self.label['text'][:len(self.label['text'])-1]
        else:
            self.label['text'] += str(num)
        print(self.label['text'])

##### MAIN CODE #####
running = Calculator()