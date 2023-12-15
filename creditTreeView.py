from tkinter import ttk
import tkinter as tk
from tkinter.simpledialog import Dialog
import download
import pandas as pd

class creditTreeView(ttk.Treeview):    
    def __init__(self,**kwargs):
        #super().__init__(parent,**kwargs)
        #self.parent = parent

        root = tk.Tk()
        root.title('信用卡消費資料')
        #root.geometry('600x300')
        #root.resizable(width=False,height=False)

        topframe = tk.Frame(root)
        topframe.pack()

        #------設定欄位名稱---------------        

        industry_values = ['食','衣','住','行','百貨','文教康樂','其他']
        area_values = ['台北市','新北市','桃園市','台中市','台南市','高雄市','其他']
        column_names = ['年月','地區','產業別','性別','年齡層','交易筆數','交易金額']
        
        #建立style

        style = ttk.Style()
        style.configure('TCombobox', font=('Arial', 22, 'bold'))
        style.configure('TLabel',font=('Arial', 14, 'bold'))

        #建立查詢欄位

        self.titleLabel = ttk.Label(topframe,text="信用卡消費樣態",
                                font=('Arial',20,'bold')).grid(column=0, row=0,columnspan=12)
        self.yearLabel = ttk.Label(topframe,text="年度:",width=5,
                            style='TLabel').grid(column=0, row=1,padx=5,pady=12)
        self.yearCombobox = ttk.Combobox(topframe,width=10,
                                    values=[i for i in range(2014,2024)],
                                    style='TCombobox').grid(column=1, row=1,pady=12)
        self.monthLabel = ttk.Label(topframe,text="月份:",width=5,
                                style='TLabel').grid(column=2, row=1,pady=10,padx=8)
        self.monthCombobox = ttk.Combobox(topframe,width=10,                             
                                    values=[i for i in range(1,13)]
                                    ).grid(column=3, row=1,pady=12)
        self.industryLabel = ttk.Label(topframe,text="產業別:",width=7,
                                style='TLabel').grid(column=4, row=1,pady=10,padx=8)
        self.industryCombobox = ttk.Combobox(topframe,width=10,
                                        style='TCombobox', 
                                        values=industry_values).grid(column=5, row=1,pady=12,ipadx=3)
        self.areaLabel = ttk.Label(topframe,text="地區:",width=5,
                            style='TLabel').grid(column=6, row=1,pady=12,padx=8)
        self.areaCombobox = ttk.Combobox(topframe,width=10,
                                    style='TCombobox',
                                    values=area_values).grid(column=7, row=1,pady=12,)
        self.selectBtn = ttk.Button(topframe,text="查詢",width=8
                            ).grid(column=8, row=1,pady=12,padx=8)
        

        ###取得查詢值
        def option_selected(event):
            year = self.yearCombobox.get()
            month = self.monthCombobox.get() 
            
            
            combo.bind("<<ComboboxSelected>>", option_selected)

        textframe = tk.Frame(root)


        #設定treeview的欄位名稱及寬度
        self.treeview = ttk.Treeview(textframe, columns=column_names, height=5)
        self.treeview.pack(fill='both', expand=1)
        self.treeview.column("#0", width=2)
        self.treeview.column("年月", width=5)
        self.treeview.column("地區", width=10)
        self.treeview.column("產業別", width=10)
        self.treeview.column("性別", width=5)
        self.treeview.column("年齡層", width=15)
        self.treeview.column("交易筆數", width=25)
        self.treeview.column("交易金額", width=35)

        self.treeview.heading("#0", text="序號")
        self.treeview.heading("年月", text="年月")
        self.treeview.heading("地區", text="地區")
        self.treeview.heading("產業別", text="產業別")
        self.treeview.heading("性別", text="性別")
        self.treeview.heading("年齡層", text="年齡層")
        self.treeview.heading("交易筆數", text="交易筆數")
        self.treeview.heading("交易金額", text="交易筆金額")


        #設定捲軸
        

        self.treeview.pack(side='left')
        vsb = ttk.Scrollbar(textframe,orient="vertical",command=self.treeview.yview)
        vsb.pack(side='left',fill='y')        
        self.treeview.configure(yscrollcommand=vsb.set)        
        textframe.pack(pady=(0,30),padx=20)  



def update_data(w:root)->None:                             
        download.updata_sqlite_data()   
        #===========更新TreeView資料                  
        select_data = download.select_data()
        root.mainloop()


if __name__ == '__main__':
    update_data()
    