import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import download

class Window(tk.Tk):                     
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #===========更新資料庫資料================#
        try:
            download.updata_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()
        #------------------------------------------       

    
        #===============主執行程式=================
def main():  
    #print("3",end=" ")  
    def update_data(w:Window)->None:                             
        download.updata_sqlite_data()   
        
    root = Window()                             
    root.title('信用卡消費資料')
    root.geometry('600x300')
    root.resizable(width=False,height=False)
    update_data(root)                           #執行程序1-主執行程式
    root.mainloop()

if __name__ == '__main__':
    main()