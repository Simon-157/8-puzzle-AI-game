import tkinter as tk
from tkinter.messagebox import showinfo 
import tkinter.ttk as ttk
import time
from solvable import check_if_solvable
from dfs import dfs
from EightPuzzle import *

solution =[]
num=[]
#clear button
def clearButton():
	for i in range(3):
		for j in range(3):
			listBt[i][j]['text']=''
			# listBt[i][j]['image']=''
			listBt[i][j]['state']='normal'
		

def createTable(num):
	for i in range(3):
		for j in range(3):
			listBt[i][j]["text"]=num[i*3+j]
			if(listBt[i][j]["text"]==0):
				listBt[i][j]['bg']='yellow'
			# else:
			# 	listBt[i][j]["text"]=''


#show solution in lbOutput, bottom of the form
def setLabel():
	solutionString = 'Solution: \n'
	global solution
	for i in range(len(solution)):
		solutionString=solutionString+ solution[i] +' --> '
		if(i%7==6):
			solutionString=solutionString+'\n'
	solutionString = solutionString +'Win!!!'
	lbOutput['text']=solutionString
	lbPath['text']='Path cost: ' + str(len(solution))


#swap blank button with neighbour button 
def swapButton(btn, btAny):
    temp = btn['text']
    btn['text']=btAny['text']
    btn['state'] = 'normal'
    btAny['text']=temp
    btn['bg'] = 'green'

	# bt0['image'] = btAny['image']
	# btAny['text']=''
	# btAny['image']= ''
    btAny['state']='disabled'

#move follow the solution
def move():

	indx = 0
	indy=0
	step=''
	global solution
	if(solution!= []):
		step=solution.pop(0)
		if(solution!= []):
			lbNextstep['text']=solution[0]
	for i in range(3):
		for j in range(3):
			if(listBt[i][j]["text"]==0):
				indx=i
				indy=j
				break
	if(step=='L'):
		swapButton(listBt[indx][indy], listBt[indx][indy-1])
	if(step=='R'):
		swapButton(listBt[indx][indy], listBt[indx][indy+1])
	if(step=='U'):
		swapButton(listBt[indx][indy], listBt[indx-1][indy])
	if(step=='D'):
		swapButton(listBt[indx][indy], listBt[indx+1][indy])
		

#find solution from num input
def findSolution(num):
    global solution
    if check_if_solvable(num) == True:
        myProb = EightPuzzleProb(num,[1,2,3,4,5,6,7,8,0])
        solution = dfs(myProb)
        print(solution[1])
        # solution =  dfs(tuple(num))
        lbNextstep['text']=solution[0]
        setLabel()
    else:
        showinfo("Unsolvable", "Given configuration is not solvable")
        

    
#click to use textbox value to find solution
def ClickOK():
    clearButton()
    if(len(str(entryInput.get())))==9 and str(entryInput.get())[0]!='0':
        num=[int(x) for x in str(entryInput.get())]
        createTable(num)
        # if check_if_solvable(num):
        findSolution(num)
    else:
        showinfo("Invalid Entry", "Please check the length of the entry")

#random number and find solu
	
def AutoRun():
	ClickOK()
	for i in range(len(solution)):
		move()
		time.sleep(0.25)
		root.update()

def start_gui():
    global root,lbOutput, lbPath, lbNextstep, entryInput, bt0, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, listBt
    root = tk.Tk()

    #add widget
    canvas = tk.Canvas(root, height=560, width=630)
    canvas.pack()


    frame = tk.Frame(root, bg='yellow')
    frame.place(relwidth=0.8, relheight=0.9)

    soluFrame = tk.Frame(root,bg='red')
    soluFrame.place(relwidth=0.8, relheight=0.1, relx=0, rely=0.9)

    rightFrame = tk.Frame(root, bg='#58636E')
    rightFrame.place(relwidth=0.2, relheight=1, relx=0.8, rely=0)


    Ilabel = tk.Label(rightFrame, text="Initial Config")
    Ilabel.place(relx=0.1, rely=0.05, relwidth=0.8, height=30)
    entryInput = tk.Entry(rightFrame)
    entryInput.place(relx=0.1, rely=0.1, relwidth=0.8, height=30)

    btOK =tk.Button(rightFrame, text='OK', command=ClickOK)
    btOK.place(relx=0.1, rely=0.2)

    lbNextstep = tk.Label(rightFrame,  bg='#58636E')
    lbNextstep.place(relx=0.1, rely=0.3)

    btNextstep = tk.Button(rightFrame, text='Hint', command=move)
    btNextstep.place(relx=0.1, rely=0.35)


    lbTime2 = tk.Label(rightFrame, text='Time: ', bg ='#58636E' )
    lbTime2.place(relx = 0.1, rely = 0.57)

    lbTime = tk.Label(rightFrame,  bg='#58636E')
    lbTime.place(relx=0.1, rely=0.6)

    lbPath=tk.Label(rightFrame,  bg='#58636E')
    lbPath.place(relx=0.1, rely=0.65)

    lbOutput = tk.Label(soluFrame)
    lbOutput.place(relwidth=1, relheight=1, relx=0, rely=0)


    btAutoRun = tk.Button(rightFrame, text='Auto', command = AutoRun)
    btAutoRun.place(relx = 0.1, rely=0.42)

    btnRest = tk.Button(rightFrame, text='Reset Board', command = clearButton)
    btnRest.place(relx = 0.1, rely=0.62)

    photo =[]

    #cteate button
    bt0 = tk.Button(frame)
    bt0.place(relx=0, rely=0, relwidth=1/3, relheight=1/3)
    bt1 = tk.Button(frame)
    bt1.place(relx=1/3, rely=0, relwidth=1/3, relheight=1/3)
    bt2 = tk.Button(frame)
    bt2.place(relx=2/3, rely=0, relwidth=1/3, relheight=1/3)
    bt3 = tk.Button(frame)
    bt3.place(relx=0, rely=1/3, relwidth=1/3, relheight=1/3)
    bt4 = tk.Button(frame)
    bt4.place(relx=1/3, rely=1/3, relwidth=1/3, relheight=1/3)
    bt5 = tk.Button(frame)
    bt5.place(relx=2/3, rely=1/3, relwidth=1/3, relheight=1/3)
    bt6 = tk.Button(frame)
    bt6.place(relx=0, rely=2/3, relwidth=1/3, relheight=1/3)
    bt7 = tk.Button(frame)
    bt7.place(relx=1/3, rely=2/3, relwidth=1/3, relheight=1/3)
    bt8 = tk.Button(frame)
    bt8.place(relx=2/3, rely=2/3, relwidth=1/3, relheight=1/3)

    listBt =[[bt0, bt1, bt2],
            [bt3, bt4, bt5],
            [bt6, bt7, bt8]]
    root.mainloop()

if __name__ == "__main__":
    start_gui()