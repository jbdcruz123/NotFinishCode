

#RSM 6/26/2022
#dont use pack() or grid() when using place

import tkinter
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
def fPrcd():
      inp_str = txt_1.get("1.0", "end")      
      inp_str = inp_str.strip()    
      if inp_str == "tama ba":
            showinfo(title="message", message= "tama sagot mo...")
      else:
            showinfo(title="message", message= "mali sagot mo...")
def fCncl():
      showinfo(title="message", message= "nag cancel ka, i blank ko ung textbox")
      txt_1.delete("1.0", "end")
      txt_1.insert("1.0", "")

def fClose():
      rtrn_str = askyesno(title="message", message= "gusto mo bang i exit....")
      if rtrn_str == True:      
            mstr.destroy()
      
mstr=tkinter.Tk()
mstr.title("RSM for testing")
mstr.resizable(False, False)
mstr.geometry("400x300")

lbl_1 = tkinter.Label(mstr, text = "input: tama ba")
lbl_1.place(x=90, y=50)
txt_1 = tkinter.Text(mstr, width=26, height=1, font = ("Arial", 11, "bold") )
txt_1.place(x=90, y =70)
btn_1=tkinter.Button(mstr, text="proceed", width=10, height=1, font = ("Arial", 11, "bold"), command = fPrcd )
btn_1.place(x=90, y=100)

btn_2=tkinter.Button(mstr, text="cancel", width=10, height=1, font = ("Arial", 11, "bold"), command = fCncl )
btn_2.place(x=200, y=100)

btn_3=tkinter.Button(mstr, text="close", width=10, height=1, font = ("Arial", 11, "bold"), command = fClose )
btn_3.place(x=150, y=150)


#button1.pack() #cannot be use chose only on pack(), place(), grid()
mstr.mainloop()
