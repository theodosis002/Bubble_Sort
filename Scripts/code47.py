'''
Γούβης Γεώργιος (up 1079261) - Κωνσταντής Αθανάσιος (up1084033) - Κρατημένος Χρήστος (up10898982)
Μαρίνης Επαμεινώνδας (up1073584)- Μητσόπουλος Αργύριος (up1083893) - Μπουρτσουκλής Θεοδόσιος (up1083891)
'''

'''
Αυτή τη εργασία χορηγείται με άδεια Creative Commons Αναφορά Δημιουργού - Παρόμοια Διανομή 4.0 Διεθνές .

You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material
for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.
'''
import tkinter as tk
from turtle import *
from PIL import Image, ImageTk
import os
import tkinter.ttk as ttk
import pygame
import cv2
import numpy as np
import random
from moviepy.editor import VideoFileClip
from tkinter import filedialog
import time
import sys
from winsound import Beep



filepath = os.path.dirname(os.path.realpath(__file__))
mainpath = filepath.replace("\Scripts", "")
mainpath2=filepath+'\\Data2\\'
os.chdir(mainpath)
flag=0
flag2=0

class Intro(): #Creates Intro

    def __init__(self):
        self.fl=0
        self.canvas1()
        if self.fl==1: 
            self.canvas2()


    def canvas1(self): #Starting menu, Function author: up1083891
            self.root=tk.Tk()
            w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            self.root.geometry("%dx%d+0+0" % (w, h))
            self.canvas=tk.Canvas(self.root,height=h,width=w,bg='black')
            self.canvas.pack(fill='both',expand=True)
            self.img = self.canvas.create_image(w/2,h/2,image='')
            self.root.attributes('-fullscreen', True)
            self.root.bind("<Escape>",
                            lambda event: self.root.attributes("-fullscreen",
                                        False))
            self.root.bind("<F11>",
                            lambda event: self.root.attributes("-fullscreen",
                                        True))
            filename=mainpath+'\\Images\\intro.png'
            img=cv2.imread(filename)
            height, width, channels = img.shape
            if w!=width or h!=height:#Μετατρέπει το μέγεθος της αρχικής εικόνας στις διαστάσεις του παραθύρου και αντικαθιστά το αρχικό αρχείο
                imgs = cv2.resize(img, (w, h))
                os.chdir(mainpath+'\\Images')
                cv2.imwrite('intro.png', imgs)
            image = Image.open(filename)
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.itemconfig(self.img,image=self.photo)
            image1=mainpath+'\\Images\\buttons.png'
            img=cv2.imread(image1)
            height, width, channels = img.shape
            imgs = cv2.resize(img, (int(w/4.860759493670886), int(h/5.76)))#Μετατρέπει το μέγεθος του κουμπιού ανάλογα με τις διατάσεις του παραθύρου
            os.chdir(mainpath+'\\Images')
            cv2.imwrite('buttons.png', imgs)
            image1=Image.open(mainpath+"\\Images\\buttons.png")
            photo1=ImageTk.PhotoImage(image1)
            tk.Button(self.canvas,highlightthickness=0,borderwidth=0,image=photo1,command=self.flg).place(x=w/2.430379746835443,y=h/1.5737704918032787)
            #Τοποθετεί το κουμπί σε σημείο το οποίο έχει ως μεταβλητή τις διαστάσεις του παραθύρου
            self.root.mainloop()


    def canvas2(self): #Selection menu
        self.root=tk.Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.canvas=tk.Canvas(self.root,height=h,width=w,bg='black')
        self.canvas.pack(fill='both',expand=True)
        self.img = self.canvas.create_image(w/2,h/2,image='')
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>",
                         lambda event: self.root.attributes("-fullscreen",
                                    False))
        self.root.bind("<F11>",
                         lambda event: self.root.attributes("-fullscreen",
                                    True))
        filename=mainpath+'\\Images\\intro.jpg'
        img=cv2.imread(filename)
        height, width, channels = img.shape
        if w!=width or h!=height:#Μετατρέπει το μέγεθος της αρχικής εικόνας στις διαστάσεις του παραθύρου και αντικαθιστά το αρχικό αρχείο
            imgs = cv2.resize(img, (w, h))
            os.chdir(mainpath+'\\Images')
            cv2.imwrite('intro.jpg', imgs)
        image = Image.open(filename)
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.itemconfig(self.img,image=self.photo)
        image1=mainpath+'\\Images\\button.png'
        img=cv2.imread(image1)
        height, width, channels = img.shape
        imgs = cv2.resize(img, (int(w/15.058823529411764), int(h/8.150943396226415)))#Μετατρέπει το μέγεθος του κουμπιού ανάλογα με τις διατάσεις του παραθύρου
        os.chdir(mainpath+'\\Images')
        cv2.imwrite('button.png', imgs)
        image1=Image.open(mainpath+"\\Images\\button.png")
        photo1=ImageTk.PhotoImage(image1)
        tk.Button(self.canvas,highlightthickness=0,borderwidth=0,image=photo1,command=self.nontas_argiris).place(x=w/4.938906752411576,y=h/1.8741865509761388)
        #Τοποθετεί το κουμπί σε σημείο το οποίο έχει ως μεταβλητή τις διαστάσεις του παραθύρου
        image2=mainpath+'\\Images\\button2.png'
        img=cv2.imread(image2)
        height, width, channels = img.shape
        imgs = cv2.resize(img, (int(w/14.76923076923077), int(h/8.307692307692308)))#Μετατρέπει το μέγεθος του κουμπιού ανάλογα με τις διατάσεις του παραθύρου
        os.chdir(mainpath+'\\Images')
        cv2.imwrite('button2.png', imgs)
        image2=Image.open(mainpath+"\\Images\\button2.png")
        photo2=ImageTk.PhotoImage(image2)
        #Τοποθετεί το κουμπί σε σημείο το οποίο έχει ως μεταβλητή τις διαστάσεις του παραθύρου
        tk.Button(self.canvas,highlightthickness=0,borderwidth=0,image=photo2,command=self.giorgos_xristos).place(x=w/2.1880341880341883,y=h/1.6210131332082551)
        image3=mainpath+'\\Images\\button3.png'
        img=cv2.imread(image3)
        height, width, channels = img.shape
        imgs = cv2.resize(img, (int(w/15.058823529411764), int(h/8.307692307692308)))#Μετατρέπει το μέγεθος του κουμπιού ανάλογα με τις διατάσεις του παραθύρου
        os.chdir(mainpath+'\\Images')
        cv2.imwrite('button3.png', imgs)
        image3=Image.open(mainpath+"\\Images\\button3.png")
        photo3=ImageTk.PhotoImage(image3)
        tk.Button(self.canvas,highlightthickness=0,borderwidth=0,image=photo3,command=self.thanasis_theodosis).place(x=w/1.247766043866775,y=h/1.9547511312217194)
        #Τοποθετεί το κουμπί σε σημείο το οποίο έχει ως μεταβλητή τις διαστάσεις του παραθύρου
        self.root.mainloop()
    
    def thanasis_theodosis(self): #Starts Theodosis-Thanasis
        self.root.destroy()
        Theodosis_Thanasis()
        self.canvas2()
    
    def nontas_argiris(self): #Starts Nontas-Argiris
        self.root.destroy()
        GUI()
        self.canvas2()


    def giorgos_xristos(self): #Starts Giorgos-Xristos
        self.root.destroy()
        Giorgos_Xristos(20,100,400)
        self.canvas2()

    

    def flg(self): #Sound, Παίζει το αρχείο ήχου Spaceship_Pass_By.mp3 όταν πατηθεί το αρχικό κουμπί
        self.fl=1
        pygame.mixer.init()
        pygame.mixer.music.load(mainpath+'\\Sounds\\Spaceship_Pass_By.mp3')
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.9)
        pygame.mixer.music.play(loops=0)
        self.root.after(1000,self.root.destroy)



class GUI():               ###authors:Argiris(up1083893),Nodas(up1073584)

    def __init__(self):                 ###δημιουργία παραθύρου και καμβά
        TurtleScreen._RUNNING=True
        if(not os.path.isdir(mainpath2) or len(os.listdir(mainpath2)) == 0):
            os.makedirs(mainpath2)
            self.create_sqr()
            Frame_Rename()
        os.chdir(mainpath2)
        self.turtleList = []                ###Δημιουργία κενής λίστας για της χελώνες 
        self.ImageList = os.listdir(mainpath2)
        self.screen = Screen()
        self.screen.screensize()
        self.screen.setup(width=1.0, height=1.0, startx=None, starty=None)
        self.screen.bgcolor("cyan")
        self.canvas = self.screen.getcanvas()
        self.root = self.canvas.winfo_toplevel()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>",              
                        lambda event: self.root.attributes("-fullscreen",
                                    False))         ###με το πατήμα του 'esc' σμίκρυνση οθόνης
        self.root.bind("<F11>",
                        lambda event: self.root.attributes("-fullscreen",
                                    True))         ###με το πατήμα του 'F11' μεγέθυνση οθόνης  
        self.destroy_button()                       ###κλήση των συναρτήσεων των δύο κουμπιών
        self.restart_button()
        self.restart_button["state"] = "disabled"     ###γίνεται disabled το κουμπί μέχρι το τέλος του υποπρογράμματος
        self.turtles2() 
        self.position(w,h) 
        self.bubblesort()
        mainloop()

    def destroy_button(self):             ###δημιουργία του κουμπιού 'EXIT'
        self.exit_button = tk.Button(self.canvas.master ,bg = "red" ,text="EXIT",font = "Arial 30",command = self.destroy_button2 ,state = "disabled")
        self.exit_button.pack(fill= 'both' ,side='right') 
        
    
    def destroy_button2(self):           ###με το πάτημα του κουμπιού καταστρέφεται το υποπρόγραμμα
        self.screen._destroy()
        

    def restart_button(self):             ###δημιουργία του κουμπιού 'RESTART'
        self.restart_button = tk.Button(self.canvas.master,bg="orange", text="RESTART",font = "Arial 30",command = self.restart_button2 )
        self.restart_button.pack(fill= 'both' ,side = 'left')
        
    def restart_button2(self):            ###η συνάρτηση που εκτελείται με το πάτημα του 'RESTART' κουμπιού 
        clearscreen()
        self.exit_button.destroy()
        self.restart_button.destroy()
        GUI()
    



    def create_sqr(self):                     ###συνάρτηση για την δημιουργία των τετραγώνων
        os.chdir(mainpath2)
        for i in range(30):
            img = np.zeros((150, 150, 3), dtype="uint8")
            img[:] = (10,225,80)
            font2=cv2.FONT_HERSHEY_PLAIN
            e = random.randint(10,99)
            cv2.putText((img),"{}".format(e), (25, 100), font2, (5), (0,0,0), 5, cv2.LINE_AA)
            cv2.rectangle(img,(0,0),(150,150),(100,100,100),3)
            cv2.imwrite(str(e)+'.png', img)


    def turtles2(self):                     ###συνάρτηση για την δημιουργία χελώνων που λαμβάνουν την μορφή τετραγώνων που προκείπτουν από την create_sqr
        self.ImageList = random.sample(self.ImageList,6)
        for i in range(len(self.ImageList)):
                self.turtleList.append(Turtle())
                self.turtleList[i].speed(0)
                self.screen.addshape(self.ImageList[i])
                self.turtleList[i].shape(self.ImageList[i])
                self.turtleList[i].penup()
                self.turtleList[i].speed(3)

    def position(self,w,h):                 ###συνάρτηση που καθορίζει τις αρχικές θέσεις (συντεταγμένες) κάθε χελώνας 
        g = int(w/7)
        x = g-w/2
        for i in range (len(self.ImageList)):
            self.turtleList[i].goto(x,0)
            x+=g
            self.turtleList[i].speed(1)

    def bubblesort(self):                   ###συνάρτηση που ταξινομεί τα τετράγωνα σε αύξουσα σειρά σύμφωνα με τον αλγόριθμο bubble Sort
        for j in range(len(self.turtleList)):

            for i in range(len(self.turtleList)-1):

                if self.ImageList[i] > self.ImageList[i+1]:
                    p = self.turtleList[i].pos()
                    r = self.turtleList[i+1].pos()
                    self.turtleList[i].goto(r)
                    self.turtleList[i+1].goto(p)
                    self.turtleList[i],self.turtleList[i+1]=self.turtleList[i+1],self.turtleList[i]
                    self.ImageList[i],self.ImageList[i+1]=self.ImageList[i+1],self.ImageList[i]
        self.exit_button["state"] = "normal"
        self.restart_button["state"] = "normal"

class Frame_Rename():                 ###authors:Argiris(up1083893),Nodas(up1073584)

        def __init__(self):             ###Δημιουργεί μια λίστα που αποτελείται από τα ονόματα των εικόνων που περιέχονται στο φάκελο.
            self.ImageList = os.listdir(mainpath2)
            self.correctedImageList = self.strip()
            self.rename()
        
        def strip(self):                ###Δημιουργεί μια κενή λίστα στην οποία προστίθεται μια εικόνα την φορά από την λίστα ‘Imagelist’ δίχως να έχει πλέον τον τύπο ‘.png’
            correctedImageList = []
            for i in self.ImageList:
                i = i.split('.')
                i.remove('png')
                correctedImageList.append(i)
            return correctedImageList
        
        def rename(self):               ###Αλλάζει το τύπο του αρχείου απο “.png” σε “.gif”
            for i in self.correctedImageList:
                i[0] +='.gif'
            c=0
            os.chdir(mainpath2)
            for i in os.listdir(os.getcwd()):
                os.rename(i,self.correctedImageList[c][0])
                c+=1
            os.chdir(mainpath2)


class Theodosis_Thanasis():

    class VideoRec():

        def __init__(self):   #Function authors: up1084033, up1083891
            self.root1=tk.Tk()
            self.root1.wm_attributes("-topmost", 1)
            self.root1.title('Video selection')
            ttk.Label(self.root1,text='Select a mp4 file',font='Consolas 20').pack()
            ttk.Button(self.root1, text='Open file',width=50, command=self.callback).pack(fill='x')
            ttk.Button(self.root1,text='Exit',width=50,command=self.exit1).pack(fill='x')
            w, h = self.root1.winfo_screenwidth(), self.root1.winfo_screenheight()
            self.root1.geometry('300x100+%d+%d'%(w/2-150,h/2-50))
            self.root1.resizable(width=False, height=False)
            self.root1.mainloop()
            


        def callback(self):
            name= filedialog.askopenfilename()#Ζητά από τον χρήστη ένα mp4 αρχείο
            while name[-4:]!='.mp4':#Ελέγχει την εγγυρότητα του τύπου του
                if name=='':break
                tk.messagebox.showinfo('Error',"Only mp4 files are acceptable!")#Μήνυμα λάθους προς τον χρήστη
                name= filedialog.askopenfilename()
                
            else:
                self.root1.destroy()
                global y
                video = VideoFileClip(name)
                y=float((video.duration*30))#Βρίσκει την διάρκεια του βίντεο και έπειτα τον αριθμό των frames για 30 fps video.
                self.progressbar(name)


        def progressbar(self,name):
            self.root2=tk.Tk()
            self.root2.wm_attributes("-topmost", 1)
            w, h = self.root2.winfo_screenwidth(), self.root2.winfo_screenheight()
            self.name=name
            self.root2.title('Frame creation')
            self.root2.geometry('300x100+%d+%d'%(w/2-150,h/2-50))
            self.root2.resizable(width=False, height=False)
            tk.messagebox.showinfo('Info',"While frames are beeing created don't use your computer!")#Μήνυμα προς τον χρήστη
            self.prog=ttk.Progressbar(self.root2,orient=tk.HORIZONTAL,length=200)
            self.prog.pack(pady=10)
            self.star_cr=ttk.Button(self.root2,text='Click to create frames',width=50,command=self.start).pack()
            self.exit_pr=ttk.Button(self.root2,text='Exit',width=50,command=self.exit).pack()
            self.root2.mainloop()
        

        def start(self):
            os.chdir(mainpath)
            self.root2.title('Creating...')
            self.cap = cv2.VideoCapture(self.name)
            try:
                if not os.path.exists('Data'):
                    os.makedirs('Data')
                    os.chdir(mainpath)
            except OSError:
                print ('Error: Creating directory of data')
            self.convert_To_Frames_And_Save()
            
        def convert_To_Frames_And_Save(self):    #Δημιουργεί τα frames
            os.chdir(mainpath)
            global flag
            flag=1
            currentFrame = 0
            while(True):
                try:
                    self.prog['value']=int((1-(y-currentFrame)/y)*100)
                    self.root2.update_idletasks() #Ενημερώνει το progressbar για την πρόοδο

                    
                    if int(len(str(y)))>=int(len(str(currentFrame))):
                        x=(int(len(str(y)))-int(len(str(currentFrame))))*'0'
                        ret, frame = self.cap.read()
                        name = './Data/' +str(x)+ str(currentFrame) + '.png'
                        cv2.imwrite(name, frame)
                        currentFrame += 1
                   


                except:
                    self.root2.destroy()
                    break
            
            self.cap.release()
            cv2.destroyAllWindows()

        def exit(self):
            global flag2
            flag2=1
            self.root2.destroy()   

        def exit1(self):
            global flag2
            flag2=1
            self.root1.destroy()



        


    class Initiate_Task3_UI():          #Initiate the task by Theodosis-Thanasis(up1084033 , up1083891)

        
        def __init__(self,amount):
            self.amount=amount
            self.root3=tk.Tk()
            self.root3.bind("<Escape>",
                         lambda event: self.root3.attributes("-fullscreen",
                                    False))
            w, h = self.root3.winfo_screenwidth(), self.root3.winfo_screenheight()
            self.root3.geometry("%dx%d+0+0" % (w, h))
            self.root3.attributes('-fullscreen', True)
            self.canvas = tk.Canvas(self.root3,height=h,width=w,bg='black')
            self.root3.title('Video')
            self.canvas.pack(fill='both',expand=True)
            self.img = self.canvas.create_image(w/2,h/2,image='')
            self.i=0
            self.change_photo()
            self.root3.mainloop()
            
        def change_photo(self):# Εναλλάσει τις εικόνες στον καμβά, Function author: up1083891
        
            path = mainpath + '\\Data'
            if self.i<len(self.amount)-1:
                filename = path+'\\'+ self.amount[self.i]
                image = Image.open(filename)
                self.photo = ImageTk.PhotoImage(image)
                self.canvas.itemconfig(self.img, image=self.photo)
                self.i+=1
                self.root3.after(2,self.change_photo)
                



    class GUI():

        def __init__(self):
            self.fl3=0
            self.shuffled=[]
            self.hsort=[]
            self.fsort=[]
            self.exframes()

        def exframes(self):#Δημιουργεί παράθυρο tkinter με ενα κουμπι και ενα Label
                self.root4=tk.Tk()
                self.root4.wm_attributes("-topmost", 1)
                self.root4.title('Video')
                w, h = self.root4.winfo_screenwidth(), self.root4.winfo_screenheight()
                self.root4.geometry('350x100+%d+%d'%(w/2-175,h/2-50))
                self.root4.resizable(width=False, height=False)
                if flag==0:message='Frames already created'#Αλλαγή μηνύματος Label ανάλογα με το αν τα frames εχουν ήδη δημιουργηθεί
                    
                else:message='Frames created'
                    
                ttk.Label(self.root4,text=message,font='Consolas 20').pack()
                ttk.Button(self.root4,text='Shuffle frames',width=50,command=self.shuffle).pack()
                self.root4.mainloop()

        def shuffle(self):#Ανακατέβει τα ονόματα των frames στην λίστα και καλεί την bubblesort
            path = mainpath + '\\Data'
            self.amount = os.listdir(path)
            random.shuffle(self.amount)
            self.root4.destroy()
            self.bubbleSort()
            
        def bubbleSort(self):  #Ανακατατάσει την λίστα δημιουργώντας αλλες 3 σε δίαφορες χρονικές στιγμές της διαδικασίας
            n = len(self.amount)
            arr=self.amount
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if arr[j] > arr[j+1] :
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                if int(i)==0:
                    self.shuffled=arr[:]
                if int(i) ==int(n/2):
                    self.hsort=arr[:]
                if int(i) == int(n-2):
                    self.fsort=arr[:]
                
            self.control()

        def control(self): #Δημιουργεί παράθυρο το οποίο δίνει στον χρήστη να επιλέξει ποιό βίντεο θέλει να παίξει
            self.root5=tk.Tk()
            self.root5.wm_attributes("-topmost", 1)
            self.root5.title('Bubblesort')
            w, h = self.root5.winfo_screenwidth(), self.root5.winfo_screenheight()
            self.root5.geometry('350x140+%d+%d'%(w/2-175,h/2-70))
            self.root5.resizable(width=False, height=False)
            if self.fl3==0:
                tk.messagebox.showinfo('Info','When video is playing: \nPress Left Click and then Escape to exit fullscreen.')#Οδηγίες προς τον χρήστη
            ttk.Label(self.root5,text='Frames shuffled',font='Consolas 20').pack()
            ttk.Button(self.root5,text='Play shuffled frames',command=lambda: self.play(2)).pack(fill='x')
            ttk.Button(self.root5,text='Play half sorted frames',command=lambda: self.play(0)).pack(fill='x')
            ttk.Button(self.root5,text='Play fully sorted frames',command=lambda: self.play(1)).pack(fill='x')
            ttk.Button(self.root5,text='Exit',command=lambda: self.root5.destroy() ).pack(fill='x')
            self.root5.mainloop()
            
        def play(self,fl): #Ανάλογα με τη τιμή του fl δίνει στην Initiate_Task3_UI την αντιστοιχη λίστα
            self.root5.destroy()
            self.fl=fl
            if fl==0:
                Theodosis_Thanasis.Initiate_Task3_UI(self.hsort)
            if fl==1:
                Theodosis_Thanasis.Initiate_Task3_UI(self.fsort)
            if fl==2:
                Theodosis_Thanasis.Initiate_Task3_UI(self.shuffled)
            self.fl3=1
            self.control()

        
    #function author: up1084033,up1083891
    
    def __init__(self): #Init function of Project_47 class
        
        while(not os.path.isdir(mainpath + "\\Data") or len(os.listdir(mainpath + "\\Data")) == 0):#Ελέγχει την ύπαρξη του φακέλου Data και καλει την κλάση VideoRec
            self.rec = self.VideoRec()  #Record the video - Turn it into frames
            if flag2==1:
                break
                
        if(os.path.isdir(mainpath + "\\Data")==True and len(os.listdir(mainpath + "\\Data"))!= 0):#Ελέγχει την ύπαρξη του φακέλου Data και καλει την κλάση VideoRec
            self.GUI()     

class Giorgos_Xristos():


    def __init__(self ,numlines,minH,maxH):
        TurtleScreen._RUNNING=True
        self.numlines=numlines
        self.maxH=maxH
        self.minH=minH
        self.main(numlines, minH, maxH)


#Το βασικό πρόγραμμα
    def main(self,numlines,minH,maxH):
        lines = [random.randint(minH, maxH) for iteration in range(numlines)]
        a=lines[:]
        n=0
        self.start(lines, numlines, maxH)
        count=0
        freq = 1000
        dur = 5
        for k in range(len(lines)-1):

            for i in range(len(lines) - k -1):

                if lines[i] > lines[i + 1]:

                    count += 1
                    try:
                        Beep(freq + count * 5, dur)
                    except ValueError:
                        n = +1
                        Beep(freq + (count - n) * 10, dur)
                    self.switch(maxH, lines, i, i + 1)
                    time.sleep(0.2)

        self.last_sound()
        self.highlight(maxH, lines, 0)
        self.highlight(maxH, lines, int(numlines)-1)
        self.count_1(count, maxH, lines )
        self.new_nums(a,maxH)
        time.sleep(4)
        self.restart_button["state"] = "normal"
        self.exit_button["state"] = "normal"
        mainloop()


#Φορτώνει στο πρόγρμμα τα χρώματα
    def load_colors(self):
        
        color_list = []
        with open(mainpath+'\\light_colors.txt', 'r', encoding='utf-8') as f:
            while True:
                line =f.readline().strip("\n")
                color_list.append(line)
                if not line:
                    break
        color_list=color_list[:-1]
        return color_list


#Το πρόγραμμα σχεδιάζει το περιβάλλον
    def start(self,lines,numlines,maxH):
        self.screen = Screen()
        self.screen.screensize()
        self.screen.setup(width=1.0, height=1.0, startx=None, starty=None)
        self.canvas = self.screen.getcanvas()
        self.root = self.canvas.winfo_toplevel()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>",lambda event: self.root.attributes("fullscreen",False))
        self.root.bind("<F11>",lambda event: self.root.attributes("-fullscreen",True))
        self.screen.bgcolor(0.1,0.1,0.1)
        self.destroy()
        self.restart()
        self.restart_button["state"] = "disabled"
        self.exit_button["state"] = "disabled"
        self.root.bind("<Escape>",
                         lambda event: self.root.attributes("-fullscreen",
                                    False))
        self.root.bind("<F11>",
                         lambda event: self.root.attributes("-fullscreen",
                                    True))

        ht()
        speed(100)
        width(8)
        pu()
        setpos(-numlines-100,-maxH / 2-100)
        seth(90)
        delay(3)
        pencolor("white")


    # Το πρόγραμμα σχεδιάζει τις γραμμές
        for line in lines:
            pd()
            fd(line)
            pu()
            bk(line)
            seth(0)
            fd(10)
            seth(90)
        self.old_nums(lines,maxH)


#Οι κινήσεις της turtle για σωστό σχεδιασμό
    def move(self,maxH,lines,p):
        x0 =-len(lines) -100
        y0 = -maxH / 2 -100
        pu()
        seth(0)
        setpos(x0,y0)
        fd (p * 10 )
        seth(90)
        pd()
        bgcolor(0.1,0.1,0.1)


#Αλλαγή του χρώματος μιας γραμμής p1 σε ένα τυχαίο χρώμα
#και του ύψους μιας γραμμής p1 σύμφωνα με το ύψος μιας άλλης γραμμής p2
    def turtle_replace_line(self,lines,p1,p2):
        pencolor(0.1,0.1,0.1)
        fd(lines[p1])
        bk(lines[p1])
        pencolor(self.load_colors()[random.randint(0,len(self.load_colors())-1)])
        fd(lines[p2])


#Οι κινήσεις για την αλλαγή
    def switch(self,maxH,lines,p1,p2):
        self.move(maxH,lines,p1)
        self.turtle_replace_line(lines,p1,p2)
        self.move (maxH,lines,p2)
        self.turtle_replace_line(lines,p2,p1)
        lines[p1],lines[p2]=lines[p2],lines[p1]


#Χρωματίζει κόκκινη μια συγκεκρμένη γραμμή
    def highlight(self,maxH,line,p):
        self.move(maxH,line,p)
        pencolor("red")
        forward(line[p])


#Βρίσκει τον συνολικό αριθμό των εναλλαγών γραμμών που έγιναν και τον παρουσιάζει
    def count_1(self,count,maxH,lines):
        pu()
        setpos(len(lines)/2-230,maxH-130)
        fillcolor('beige')
        begin_fill()
        width(0)
        for i in range(2):
            forward(100)
            rt(90)
            fd(500)
            rt(90)
        end_fill()

        pencolor("beige")
        STRING = "The number of switches was: \n  {}".format(count)
        FONT_SIZE = 20
        DELTA_SIZE = 1
        FONT = ("Ariel", FONT_SIZE, "normal")
        OUTLINE_FONT = ("Ariel", FONT_SIZE + 2 * DELTA_SIZE, "bold")
        screen = Screen()
        X, Y = -len(lines)/2-200, maxH-100
        goto(X, Y)
        for letter in STRING:
            color('grey')
            oldx = xcor()
            write(letter, move=True, align="left", font=OUTLINE_FONT)
            newx = xcor()
            color("black")
            setposition(oldx + (newx - oldx) // 2, Y + DELTA_SIZE)
            write(letter, align="center", font=FONT)
            setposition(newx, Y)


#Παρουσιάζει τους αριθμούς με οργάνωση
    def new_nums(self,lines,maxH):
        pu()
        setpos(len(lines)/2+300,maxH-750)
        pencolor("beige")
        s=""
        for o in sorted(lines):
            s = s +"\n" + str(o)
        s="The {} numbers ordered:".format(len(lines))+s
        pd()
        fillcolor("blue")
        write(s, font=["Courier", 16, "normal","underline"])


# Παρουσιάζει τους αριθμούς δίχως οργάνωση
    def old_nums(self,lines,maxH):
        pu()
        setpos(len(lines)/2-550,maxH-750)
        pencolor("beige")
        s=""
        for o in lines:
            s = s +"\n" + str(o)
        s="The {} numbers unordered:".format(len(lines))+s
        pd()
        fillcolor("blue")
        write(s, font=("Courier", 16, "normal"))


#Παίζει εναν ήχο μολις το πρόγραμμα τελειώνει
    def last_sound(self):
        file =mainpath + '\\Sounds\\' 'Victory_sound_effect.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()

    def destroy(self):
        self.exit_button = tk.Button(self.canvas.master, bg="blue", text="EXIT", font="Arial 30",
                                     command=self.screen._destroy)
        self.exit_button.pack(fill='both', side='right')


    def restart(self):
        self.restart_button = tk.Button(self.canvas.master, bg="yellow", text="RESTART", font="Arial 30",
                                        command=self.restart_command)
        self.restart_button.pack(fill='both', side='left')


    def restart_command(self):
        clearscreen()
        self.exit_button.pack_forget()
        self.restart_button.pack_forget()
        Giorgos_Xristos(self.numlines,self.minH,self.maxH)



Intro()
