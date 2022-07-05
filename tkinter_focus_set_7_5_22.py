
import tkinter as tk

def f_btn_1_clck():#1
      entry_1.focus_set()      
#1

def f_btn_2_clck(p):#1a
      #hanggang dalawa lang ba ung pang extend ng global, hindi kasi madetect
      #ng interpreter ung pang 3rd ung entry_1_chld
      global chld; entry_1 
      global entry_1_chld       

      def f_fcs_mn_chld():#2
            mn.focus_set()
            entry_1.focus_set()
      #2

      chld = tk.Toplevel(p)
      chld.title("child")
      chld.geometry("400x300")
      chld.resizable(False, False)

      entry_1_chld = tk.Entry(chld, bg= "blue", fg = "yellow")
      entry_1_chld.grid(row =0, column =1)      
      btn_1_chld = tk.Button(chld, text ="focus main", command = f_fcs_mn_chld)
      btn_1_chld.grid(row =1, column =1)

          
#1a

def f_btn_3_clck():#1b
      global entry_1_chld     
      print(f"L50 type(chld) {type(chld)}")
      chld.focus_set()
      entry_1_chld.focus_set() 
     
#1b

chld= None
entry_1_chld  =None
mn = tk.Tk()

mn.title("set_focus")
mn.geometry("400x300")
mn.resizable(False, False)

frme = tk.Frame(mn, bg= "white")

entry_1 = tk.Entry(frme, bg = "cyan", fg = "red")
entry_1.grid(row = 0, column =1)

tk.Entry(frme, bg = "red", fg = "cyan").grid(row = 0, column =2, padx = 5)

#cant control the the size of Entry box it shows 3 column then i use
#3 column the get centered
btn_1 = tk.Button(frme, text = "Btn_1 focus entry", bg = "yellow", fg="blue", command = f_btn_1_clck)
btn_1.grid(row = 1, column =1, pady = 10)

btn_2 = tk.Button(frme, text = "Btn_2 child", bg = "yellow", fg="blue", command = lambda: f_btn_2_clck(mn))
btn_2.grid(row = 1, column = 2)

btn_3 = tk.Button(frme, text = "Btn_3 focus_set_chld", bg = "yellow", fg="blue", command = f_btn_3_clck)
btn_3.grid(row = 2, column =0, pady = 10, columnspan = 3, sticky = tk.N)


frme.place( anchor = tk.CENTER, relx = .5, rely = .5)
mn.mainloop()

