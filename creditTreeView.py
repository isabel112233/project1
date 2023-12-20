from tkinter import ttk
import tkinter as tk
from tkinter.simpledialog import Dialog
import download
import pandas as pd

class CreditTreeView(ttk.Treeview):    
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.parent = parent

       

        ###取得查詢值

        #def button_event(start,end,datatype,**kwargs)->(tuple):
        #    DataType = {'age':'年齡層', 'income':'年收入', 'job':'職業類別', 'education':'教育程度類別'}
        #    new_colnames = ['年月','地區','產業別','性別',DataType[datatype],'交易筆數','交易金額']
        #    datatype = self.datatypeCombobox.get()
        #    start = self.startyearCombobox.get() + self.startmonthCombobox.get()
        #    end = self.endyearCombobox.get() + self.endmonthCombobox.get()
        #    month = (int(end[:4])-int(start[:4])) * 12 +(int(end[4:6])-int(start[4:6])) + 1
            
        #    if month >12  or month < 1 :
        #        if month >12 :
        #            print (f'請選擇一年內資料:{month}')
        #        else :
         #           print (f'=迄年度輸入錯誤:{month}')
            
        #    for i in new_colnames :
        #        self.heading("#0", text="序號")
        #        self.heading(i,text = i)
        #    return (start,end,datatype)

        
        #------設定欄位名稱---------------        

        industry_values = ['食','衣','住','行','百貨','文教康樂','其他']
        area_values = ['台北市','新北市','桃園市','台中市','台南市','高雄市','其他']
    

        #設定treeview的欄位名稱及寬度
        
        self.column("#0", width=20)
        self.column("年月", width=80)
        self.column("地區", width=80)
        self.column("產業別", width=80)
        self.column("性別", width=50)
        self.column("年齡層", width=100)
        self.column("交易筆數", width=100)
        self.column("交易金額", width=150)

        self.heading("#0", text="序號")
        self.heading("年月", text="年月")
        self.heading("地區", text="地區")
        self.heading("產業別", text="產業別")
        self.heading("性別", text="性別")
        self.heading("年齡層", text="年齡層")
        self.heading("交易筆數", text="交易筆數")
        self.heading("交易金額", text="交易筆金額")


       

    def update_content(self,year_datas):
        
        
        '''
        更新內容
        '''
        #清除所有內容
        for i in self.get_children():
            self.delete(i) 
       
        for index,年月 in enumerate(year_datas):
            
            self.insert('','end',text=f"abc{index}",values=年月)   
        
    


    
       
