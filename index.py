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
        label_font =  ('Arial', 14, 'bold') 
        combobox_font= ('Arial', 12, 'bold') 

        DataType = {'age':'年齡層', 'income':'年收入', 'job':'職業類別', 'education':'教育程度類別'}
        

        topframe = tk.Frame()
        topframe.pack()

        self.startyearVar = tk.StringVar()
        self.startmonthVar = tk.StringVar()
        self.endyearVar = tk.StringVar()
        self.endmonthVar = tk.StringVar()
        self.datatypeVar = tk.StringVar()


        titleLabel = ttk.Label(topframe,text="信用卡消費樣態",
                                        font=('Arial',20,'bold'),foreground='gray')
        titleLabel.grid(column=0, row=0,columnspan=12)
        self.datatypeLabel = ttk.Label(topframe,text="資料類別:",width=8,
                    font=label_font ,foreground='gray')
        self.datatypeLabel.grid(column=0, row=1,padx=5,pady=12)

        self.datatypeCombobox = ttk.Combobox(topframe,width=6,
                                        textvariable=self.datatypeVar,
                                        values=[i for i in DataType],
                                        font=combobox_font)
        self.datatypeCombobox.grid(column=1, row=1,pady=12)

        yearLabel = ttk.Label(topframe,text="年月:",width=6,
                            font=label_font ,foreground='gray')
        yearLabel.grid(column=2, row=1,padx=5,pady=12)
        self.startyearCombobox = ttk.Combobox(topframe,width=6,
                                        textvariable=self.startyearVar,
                                        values=[i for i in range(2014,2024)],
                                        font=combobox_font)
        self.startyearCombobox.grid(column=3, row=1,pady=12)
        self.startmonthCombobox = ttk.Combobox(topframe,width=3,
                                        textvariable=self.startmonthVar,
                                        values=[str(i).zfill(2) for i in range(1,13)],
                                        font=combobox_font)
        self.startmonthCombobox.grid(column=4, row=1,pady=12)
        yearLabel = ttk.Label(topframe,text="~",width=1,
                            font=label_font ).grid(column=5, row=1,padx=5,pady=12)
        self.endyearCombobox = ttk.Combobox(topframe,width=6,
                                    textvariable=self.endyearVar,
                                        values=[i for i in range(2014,2024)],
                                        font=combobox_font, state='readonly')
        self.endyearCombobox.grid(column=6, row=1,pady=12)
        self.endmonthCombobox = ttk.Combobox(topframe,width=3,
                                        textvariable=self.endmonthVar,
                                        values=[str(i).zfill(2) for i in range(1,13)],
                                        font=combobox_font)
        self.endmonthCombobox.grid(column=7, row=1,pady=12)

        selectBtn = ttk.Button(topframe, text="查詢", width=8, command=lambda: self.OnbuttonClick())
        selectBtn.grid(column=8, row=1, pady=12, padx=8)

        column_names = ['年月','地區','產業別','性別','年齡層','交易筆數','交易金額']

        textFrame = tk.Frame(self)

        self.creditTreeView = CreditTreeView(textFrame, show="headings", columns=column_names, height=20)
        self.creditTreeView.pack(side='left', fill='both', expand=True)  # 修改这一行，添加 fill 和 expand 参数

        vsb = ttk.Scrollbar(textFrame, orient="vertical", command=self.creditTreeView.yview)
        vsb.pack(side='left', fill='y')
        self.creditTreeView.configure(yscrollcommand=vsb.set)

        textFrame.pack(pady=(0, 20), padx=10)
     ###取得查詢值

    def OnbuttonClick(self):   
           
        datatype = self.datatypeCombobox.get()
        start = self.startyearCombobox.get() + self.startmonthCombobox.get()
        end = self.endyearCombobox.get() + self.endmonthCombobox.get()
        month = (int(end[:4]) - int(start[:4])) * 12 + (int(end[4:6]) - int(start[4:6])) + 1
        print(start, end, datatype)
        DataType = {'age':'年齡層', 'income':'年收入', 'job':'職業類別', 'education':'教育程度類別'}
        new_colnames = ['年月','地區','產業別','性別',DataType[datatype],'交易筆數','交易金額']  
        for i, colname in enumerate(new_colnames):
            if i == 0:                
                CreditTreeView.heading("#0", text="序號")
            else:
                column_id = "#" + str(i)
                CreditTreeView.heading(column_id, text=colname)
                        

        if datatype == "" and start == "" and end == "":
            lastest_data = download.lastest_datetime_data()
            self.creditTreeView.update_content(lastest_data)
        else:
            if month > 12:
                print(f'請選擇一年內資料:{month}')
            if month < 0:
                print(f'迄年度輸入錯誤:{month}')
            else:
                search_data = download.search_data(start, end, datatype)
                print("取得資料")
                self.creditTreeView.update_content(search_data) 
                DataType = {'age':'年齡層', 'income':'年收入', 'job':'職業類別', 'education':'教育程度類別'}
                new_colnames = ['年月','地區','產業別','性別',{DataType[datatype]},'交易筆數','交易金額'] 
                
                
#===============主執行程式=================

def main():  
      
    def update_data(w:Window)->None:                             
        
        #===========更新TreeView資料                  
        lastest_data = download.lastest_datetime_data()
        w.creditTreeView.update_content(lastest_data)
        
    window = Window()                             
    window.title('信用卡消費樣態')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)                           #執行程序1-主執行程式
    window.mainloop()

if __name__ == '__main__':
    main()