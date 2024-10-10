from tkinter import*
import math
def click(value):
    ex=entryField.get()
    answer=''#remove error if the user clicks undifined button
    #memory = StringVar()
    #memory.set('')
    memory=entryMemory.get()
    try:
      if value=='C':
          ex=ex[0:len(ex)-1]
        #slicing a string
          entryField.delete(0,END)
          entryField.insert(0,ex)
          return
      elif value=='CE':
          entryField.delete(0,END)
      elif value=='√':
          answer=math.sqrt(eval(ex))#if value string becomes float, if value float becomes string
      elif value=='π':
          answer=math.pi
      elif value=='cos':
          answer=math.cos(math.radians(eval(ex)))
      elif value=='tan':
          answer=math.tan(math.radians(eval(ex)))
      elif value=='sin':
          answer=math.sin(math.radians(eval(ex)))
      elif value=='cosh':
          answer=math.cosh(eval(ex))
      elif value=='tanh':
          answer=math.tanh(eval(ex))
      elif value=='sinh':
          answer=math.sinh(eval(ex))
      elif value=='3√x':
          answer=eval(ex)**(1/3)#power 1 by 3
      elif value=='x^y':
          entryField.insert(END,'**')
          return
      elif value=='x^3':
          answer=eval(ex)**3
      elif value=='x^2':
          answer=eval(ex)**2
      elif value=='Ln':
          answer=math.log2(eval(ex))
      elif value=='Deg':
          answer=math.degrees(eval(ex))
      elif value=='Rad':
          answer=math.radians(eval(ex))
      elif value=='n!':
          answer=math.factorial(ex)
      elif value=='/':
          entryField.insert(END,"/")
          return
      elif value=='=':
          answer=eval(ex)
      elif value =='\xb1':
          answer=-(eval(ex))
      elif value=='log':
          answer=math.log(eval(ex))
      elif value=='Exp':
          answer=math.exp(eval(ex))
      elif value=='Mod':
          entryField.insert(END,"%")
          return
      elif value == 'Int':
          answer = int(eval(ex))
      elif value == '1/x':
          answer = 1 / eval(ex)
      elif value == 'MC':
          #memory.set(eval('0'))
          entryMemory.delete(0, END)
      elif value == 'MR':
          #answer = memory
          #entryField.insert(0,answer)
          memory_value = entryMemory.get().split(';')[-1]  # get the last value before ';' from memory
          answer = float(memory_value) if memory_value else 0  # convert to float if non-empty, otherwise set to 0
          entryField.delete(0, END)
          entryField.insert(0, answer)
      elif value == 'MS':
          #memory.set(eval(ex))==eval(answer)
          if memory=='':
              memory=eval(ex)
          #entryMemory.insert(END,';'+str(memory))
              entryMemory.insert(END,eval(ex))
          else:
              memory = eval(ex)
              entryMemory.insert(END, ';' + str(memory))
      elif value == 'M+':
          if ';' in memory:
              values = memory.split(';')
              last_value = values[-1]
              if last_value.isdigit():
                  answer = eval(last_value + value + ex)
                  entryMemory.delete(0, END)
                  entryMemory.insert(END, ';'.join(values[:-1]) + ';' + str(answer))
              else:
                  try:
                      starting_value = int(values[-2])
                  except ValueError:
                      return
                  answer = eval(str(starting_value) + value + ex)
                  entryMemory.delete(0, END)
                  entryMemory.insert(END, ';'.join(values[:-2]) + ';' + str(answer))
          else:
              entryMemory.insert(END, ';' + str(eval(entryMemory.get() + '+' + ex)))
          answer = 0
      elif value == 'M-':
          if ';' in memory:
              values = memory.split(';')
              last_value = values[-1]
              if last_value.isdigit():
                  answer = eval(last_value + value + ex)
                  entryMemory.delete(0, END)
                  entryMemory.insert(END, ';'.join(values[:-1]) + ';' + str(answer))
              else:
                  try:
                      starting_value = int(values[-2])
                  except ValueError:
                      return
                  answer = eval(str(starting_value) + value + ex)
                  entryMemory.delete(0, END)
                  entryMemory.insert(END, ';'.join(values[:-2]) + ';' + str(answer))
          else:
              entryMemory.insert(END, ';' + str(eval(entryMemory.get() + '-' + ex)))
          answer = 0
      elif value == '10^x':
          entryField.insert(END,10)
          entryField.insert(END,'**')
          answer = 10**eval(ex)
          return
      elif value == 'Inv':
          answer = 1/eval(ex)
      elif value =='y√x' :
          #window.Label="√"
          entryField.insert(END,"√")
          answer=math.pow( eval(ex),1/ eval(ex))
          return
      elif value=='%':
          try:
              answer = float(eval(entryField.get())) / 100
              entryField.delete(0, END)
              entryField.insert(0, str(answer))
          except ValueError:
              entry.delete(0, END)
              entry.insert(0, "Error")
      elif value==';':
         entryMemory.insert(END,';')
      else:
          entryField.insert(END,value)#for inserting the numbers
          return
      entryField.delete(0,END)
      entryField.insert(0,answer)
    except (SyntaxError,ZeroDivisionError):
        entryField.delete(0, END)
        entryField.insert(0, "Error")
        pass
window=Tk()
window.title("Scientific calculator Ivayla Markova")
window.config(bg='#A9CCE3')
window.geometry("680x486+100+100")

entryField=Entry(window,font=('Consolas',20),bg="#F5F5F5",justify=RIGHT,
                 fg="black",bd=3, relief=RAISED,width=43)
entryField.grid(row=0,column=0,columnspan=10)
#entryField.insert(0,int(0))
entryMemory=Entry(window,font=('Consolas',15),bg="#F5F5F5",justify=RIGHT,
                 fg="black",bd=3, relief=RAISED,width=30)
entryMemory.grid(row=1,column=0,columnspan=10)
#entryMemory.insert(0,int(0))
button_text_list=['Deg','Rad',';','','', 'MC','MR','MS','M+','M-','','Inv','Ln','','',
                  '','CE',
                  'C','\xb1','√','Int',
                  'sinh','sin','x^2','n!','7','8',
                  '9','/','%','','cosh','cos','x^y','y√x','4','5','6',
                  '*','1/x','π','tanh','tan','x^3','3√x','1','2','3','-','','Exp','Mod','log','10^x',
                  '0','.','+','=']
rowvalue=2
columnvalue=0
for i in button_text_list:
    button=Button(window,width=5,height=1,bd=1,relief=RAISED,text=i,bg="#F5F5F5",
                  fg="black",font=('Consolas',15),command=lambda button=i:click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>9:
        rowvalue+=1
        columnvalue=0
window.mainloop()#endless loop
