from tkinter import ttk
import tkinter as tk
from tkinter.simpledialog import Dialog
import download
import pandas as pd

class CreditTreeView(ttk.Treeview):    
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.parent = parent

       
        #------設定欄位名稱---------------        

        industry_values = ['食','衣','住','行','百貨','文教康樂','其他']
        area_values = ['台北市','新北市','桃園市','台中市','台南市','高雄市','其他']
    

        #設定treeview的寬度
        print('建立treeview欄位寬度')
        self.column("#0", width=20)
        self.column("年月", width=80)
        self.column("地區", width=80)
        self.column("產業別", width=80)
        self.column("性別", width=50)
        self.column("年齡層", width=100)
        self.column("交易筆數", width=100)
        self.column("交易金額", width=150)

        print('建立treeview欄位')

        ##self.heading("#0", text="序號")
        #self.heading("年月", text="年月")
        #self.heading("地區", text="地區")
        #self.heading("產業別", text="產業別")
        #self.heading("性別", text="性別")
        #self.heading("年齡層", text="年齡層")
        #self.heading("交易筆數", text="交易筆數")
        #self.heading("交易金額", text="交易筆金額")


       

    def update_content(self,year_datas):
        
        
        '''
        更新內容
        '''
        print('資料寫入資料庫')
        #清除所有內容
        for i in self.get_children():
            self.delete(i) 
       
        for index,年月 in enumerate(year_datas):
            
            self.insert('','end',text=f"abc{index}",values=年月)   
        
    


    
       
