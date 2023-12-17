import tkinter as tk
from tkinter import ttk
from creditTreeView import CreditTreeView
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

        #=================建立介面-==============
        style = ttk.Style()
        style.configure('TCombobox', font=('Arial', 22, 'bold'))
        style.configure('TLabel',font=('Arial', 12, 'bold'))
        DataType = {'age':'年齡層', 'income':'年收入', 'job':'職業類別', 'education':'教育程度類別'}



    
        

        topframe = tk.Frame()
        topframe.pack()

        self.startyearVar = tk.StringVar()
        self.startmonthVar = tk.StringVar()
        self.endyearVar = tk.StringVar()
        self.endmonthVar = tk.StringVar()
        datatypeVar = tk.StringVar()


        self.titleLabel = ttk.Label(topframe,text="信用卡消費樣態",
                                        font=('Arial',20,'bold'))
        self.titleLabel.grid(column=0, row=0,columnspan=12)
        self.datatypeLabel = ttk.Label(topframe,text="資料類別:",width=8,
                    style='TLabel')
        self.datatypeLabel.grid(column=0, row=1,padx=5,pady=12)

        self.datatypeCombobox = ttk.Combobox(topframe,width=6,
                                        textvariable=datatypeVar,
                                        values=[i for i in DataType],
                                        style='TCombobox')
        self.datatypeCombobox.grid(column=1, row=1,pady=12)

        self.yearLabel = ttk.Label(topframe,text="年月:",width=6,
                            style='TLabel')
        self.yearLabel.grid(column=2, row=1,padx=5,pady=12)
        self.startyearCombobox = ttk.Combobox(topframe,width=6,
                                        textvariable=self.startyearVar,
                                        values=[i for i in range(2014,2024)],
                                        style='TCombobox')
        self.startyearCombobox.grid(column=3, row=1,pady=12)
        self.startmonthCombobox = ttk.Combobox(topframe,width=3,
                                        textvariable=self.startmonthVar,
                                        values=[str(i).zfill(2) for i in range(1,13)],
                                        style='TCombobox')
        self.startmonthCombobox.grid(column=4, row=1,pady=12)
        yearLabel = ttk.Label(topframe,text="~",width=1,
                            style='TLabel').grid(column=5, row=1,padx=5,pady=12)
        self.endyearCombobox = ttk.Combobox(topframe,width=6,
                                    textvariable=self.endyearVar,
                                        values=[i for i in range(2014,2024)],
                                        style='TCombobox', state='readonly')
        self.endyearCombobox.grid(column=6, row=1,pady=12)
        self.endmonthCombobox = ttk.Combobox(topframe,width=3,
                                        textvariable=self.endmonthVar,
                                        values=[str(i).zfill(2) for i in range(1,13)],
                                        style='TCombobox')
        self.endmonthCombobox.grid(column=7, row=1,pady=12)

        self.selectBtn = ttk.Button(topframe,text="查詢",width=6,)
                            
        self.selectBtn.grid(column=8, row=1,pady=12,padx=8)

        self.selectBtn.bind()

        column_names = ['年月','地區','產業別','性別','年齡層','交易筆數','交易金額']

        textFrame = tk.Frame(self)

        self.creditTreeView = CreditTreeView(textFrame,show="headings",
                        columns=column_names,height=20)   #height 設定為20行

        #設定捲軸
        

        self.creditTreeView.pack(side='left')
        vsb = ttk.Scrollbar(textFrame,orient="vertical",command=self.credittreeview.yview)
        vsb.pack(side='left',fill='y')        
        self.creditTreeView.configure(yscrollcommand=vsb.set)        
        textFrame.pack(fill='both',expand=1)  

     ###取得查詢值

    def button_event(start,end,datatype,**kwargs)->(tuple):
        datatype = self.datatypeCombobox.get()
        start = self.startyearCombobox.get() + self.startmonthCombobox.get()
        end = self.endyearCombobox.get() + self.endmonthCombobox.get()
        month = (int(end[:4])-int(start[:4])) * 12 +(int(end[4:6])-int(start[4:6])) + 1
        
        if month >12  or month < 1 :
            if month >12 :
                print (f'請選擇一年內資料:{month}')
            else :
                print (f'=迄年度輸入錯誤:{month}')
        return (start,end,datatype)







#===============主執行程式=================

def main():  
      
    def update_data(w:Window)->None:                             
        download.updata_sqlite_data() 
        
        #===========更新TreeView資料                  
        lastest_data = download.lastest_datetime_data()
        w.creditTreeView.update_content(lastest_data)
        
    window = Window()                             
    window.title('信用卡消費資料')
    window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)                           #執行程序1-主執行程式
    window.mainloop()

if __name__ == '__main__':
    main()