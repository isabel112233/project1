from tkinter import ttk
import tkinter as tk
from tkinter.simpledialog import Dialog
import download

class creditTreeView(ttk.Treeview):    
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.parent = parent
        
        #------設定欄位名稱---------------        

        industry_values = ['食','衣','住','行','百貨','文教康樂','其他']
        area_values = ['台北市','新北市','桃園市','台中市','台南市','高雄市','其他']
        column_names = ['年','月','地區','產業別','年齡層','交易筆數','交易金額']
        
        

        style = ttk.Style()
        style.configure('TCombobox', font=('Arial', 22, 'bold'))
        style.configure('TLabel',font=('Arial', 14, 'bold'))

        title_label = ttk.Label(root,text="信用卡消費樣態",
                                font=('Arial',20,'bold')).grid(column=0, row=0,columnspan=15,sticky=tk.W+tk.E+tk.N)
        year_label = ttk.Label(root,text="年度:",width=5,
                            style='TLabel').grid(column=0, row=1,padx=5,pady=12)
        year_combobox = ttk.Combobox(root,width=10,                             
                                    values=[i for i in range(2014,2024)],
                                    style='TCombobox').grid(column=1, row=1,pady=12)
        month_label = ttk.Label(root,text="月份:",width=5,
                                style='TLabel').grid(column=2, row=1,pady=10,padx=8)
        month_combobox = ttk.Combobox(root,width=10,                             
                                    values=[i for i in range(1,13)],
                                    style='TCombobox').grid(column=3, row=1,pady=12)
        industry_label = ttk.Label(root,text="產業別:",width=7,
                                style='TLabel').grid(column=4, row=1,pady=10,padx=8)
        industry_combobox = ttk.Combobox(root,width=10,
                                        style='TCombobox', 
                                        values=industry_values).grid(column=5, row=1,pady=12,ipadx=3)
        area_label = ttk.Label(root,text="地區:",width=5,
                            style='TLabel').grid(column=6, row=1,pady=12,padx=8)
        area_combobox = ttk.Combobox(root,width=10,
                                    style='TCombobox',
                                    values=area_values).grid(column=7, row=1,pady=12,)

        

        root = tk.Tk                            
        root.title('信用卡消費資料')
        root.geometry('600x300')
        root.resizable(width=False,height=False)
        root.mainloop()
if __name__ == '__main__':
    creditTreeView()