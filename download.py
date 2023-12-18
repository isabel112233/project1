import requests
import csv
import sqlite3
import os
import pandas as pd
import glob

#===============讀取API之參數代號====================

'''
    地區別代碼【KLC: 基隆市, TPE: 臺北市, NTP: 新北市, TYC: 桃園市, HCC: 新竹市, HCH: 新竹縣, MLH: 苗栗縣, TCC: 臺中市, CHH: 彰化縣, NTH: 南投縣, YUH: 雲林縣, CYC: 嘉義市, CYH: 嘉義縣, TNC: 臺南市, KHC: 高雄市, PTH: 屏東縣, TTH: 臺東縣, HLH: 花蓮縣, YIH: 宜蘭縣, PHH: 澎湖縣, KMH: 金門縣, LCH: 連江縣, TWN: 臺灣, X1: 無縣市, LCSUM: 六都十六縣, MCT: 六都, LOC: 十六縣】

    Available values : KLC, TPE, NTP, TYC, HCC, HCH, MLH, TCC, CHH, NTH, YUH, CYC, CYH, TNC, KHC, PTH, TTH, HLH, YIH, PHH, KMH, LCH, TWN, X1, LCSUM, MCT, LOC

    產業類別代碼【FD: 食品餐飲類, CT: 服飾類, LG: 住宿類, TR: 交通類, EE: 文教康樂類, DP: 百貨類, X2: 無產業, OT: 其他類, ALL: 全部產業, IDSUM: 各產業類】
    Available values : FD, CT, LG, TR, EE, DP, X2, OT, ALL, IDSUM

    1:男性 2:女性
    63000000: 臺北市 64000000: 高雄市 65000000: 新北市 66000000: 臺中市 67000000: 臺南市 68000000: 桃園市
    10002000: 宜蘭縣 10004000: 新竹縣 10005000: 苗栗縣 10007000: 彰化縣 10008000: 南投縣 10009000: 雲林縣
    10010000: 嘉義縣 10020000: 嘉義市 10013000: 屏東縣 10014000: 臺東縣 10015000: 花蓮縣 10016000: 澎湖縣
    10017000: 基隆市 10018000: 新竹市 09020000: 金門縣 09007000: 連江縣
'''
 #---------------------------------------------   

#====================共同參數設定=================
new_area={'63000000': '臺北市' ,'64000000':'高雄市', '65000000': '新北市', '66000000': '臺中市' ,'67000000': '臺南市', '68000000': '桃園市','10002000': '宜蘭縣', '10004000': '新竹縣', '10005000': '苗栗縣','10007000': '彰化縣' ,'10008000': '南投縣', '10009000': '雲林縣','10010000': '嘉義縣','10020000': '嘉義市', '10013000': '屏東縣' ,'10014000': '臺東縣', '10015000': '花蓮縣' ,'10016000': '澎湖縣','10017000': '基隆市', '10018000': '新竹市' ,'9020000': '金門縣', '9007000': '連江縣'}  
df_new_area = pd.DataFrame.from_dict(new_area, orient='index', columns=['地區'])   

area = ['KLC', 'TPE', 'NTP', 'TYC', 'HCC', 'HCH', 'MLH', 'TCC', 'CHH', 'NTH', 'YUH', 'CYC', 'CYH', 'TNC', 'KHC','PTH', 'TTH', 'HLH', 'YIH', 'PHH', 'KMH', 'LCH', 'X1','LCSUM', 'MCT', 'LOC']

industry = ['FD', 'CT', 'LG', 'TR', 'EE', 'DP', 'X2', 'OT', 'IDSUM']
gender = {'M':'0','F':'1'}
DataType = {'age':'年齡層', 'income':'年收入', 'job':'職業類別', 'education':'教育程度類別'}
#-------------------------------------------------

#==============下載資料=======================
def __download_data() -> csv: 
    print('開始下載資料')
    # 各年齡層消費樣態資料
    for A in area:
        for B in industry:
            for C in gender:
                age_url = f"https://bas.nccc.com.tw/nccc-nop/OpenAPI/C11/GenderAgeGroup/{A}/{B}/{C}"
                response_age = requests.request("GET", age_url)
                if len(response_age.text) == 0:
                    continue
                with open(f'./rawdata/age/age{A}{B}{C}.csv', 'wb') as file:
                    file.write(response_age.content)
                file.close()
    print('年齡層消費資料讀取成功')

    #兩性x各年收入族群消費樣態資料

    for A in area:
        for B in industry:
            for C in gender:
                income_url = f"https://bas.nccc.com.tw/nccc-nop/OpenAPI/C12/GenderAnnualIncome/{A}/{B}/{C}"
                response_income = requests.request("GET", income_url)
                if len(response_income.text) == 0:
                    continue
                with open(f'./rawdata/income/income{A}{B}{C}.csv', 'wb') as file:
                    file.write(response_income.content)
                file.close()
    print('年收入消費資料讀取成功')

    #職業類別消費樣態資料
    for A in area:
        for B in industry:
            for C in gender:
                job_url = f"https://bas.nccc.com.tw/nccc-nop/OpenAPI/C13/GenderClassifiedEmployment/{A}/{B}/{C}"
                response_job = requests.request("GET", job_url)
                if len(response_job.text) == 0:
                    continue
                with open(f'./rawdata/job/job{A}{B}{C}.csv', 'wb') as file:
                    file.write(response_job.content)
                file.close()
    print('職業類別消費資料讀取成功')

    #教育程度類別消費樣態資料
    for A in area:
        for B in industry:
            for C in gender:
                education_url = f"https://bas.nccc.com.tw/nccc-nop/OpenAPI/C14/GenderEducationLevel/{A}/{B}/{C}"
                response_education = requests.request("GET", education_url)
                if len(response_education.text) == 0:
                    continue
                with open(f'./rawdata/education/education{A}{B}{C}.csv', 'wb') as file:
                    file.write(response_education.content)
                file.close()
    print('教育程度類別消費資料讀取成功')
   

    #===============合併csv檔案==================

    print('開始合併csv檔')
    # 指定CSV檔案所在的資料夾路徑
    for datatype in DataType:        
        folder_path = f'./rawdata/{datatype}/'
        # 使用glob模組取得資料夾中所有的CSV檔案路徑
        files = glob.glob(folder_path + '*.csv')
        result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)    
        result.to_csv(f'./datasource/{datatype}.csv', index=False)

        print("檔案合併成功")

#---------------------------------------------------


#===============建立資料庫欄位==================
def __create_table(conn:sqlite3.Connection):       
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS age(
            "id"	INTEGER,
            "年月"	TEXT NOT NULL,
            "地區"	TEXT NOT NULL,
            "產業別"	TEXT NOT NULL,
            "性別"	TEXT NOT NULL,
            "年齡層"	TEXT NOT NULL,            
            "交易筆數"	IINTEGER,
            "交易金額"	INTEGER,            
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(年月,地區,產業別,性別,年齡層) ON CONFLICT REPLACE
        );
        '''
    )
    conn.commit()
    
    print("年齡層table建立成功")

    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS income(
            "id"	INTEGER,
            "年月"	TEXT NOT NULL,
            "地區"	TEXT NOT NULL,
            "產業別"	TEXT NOT NULL,
            "性別"	TEXT NOT NULL,
            "年收入"	TEXT NOT NULL,
            "交易筆數"	INTEGER,
            "交易金額"	INTEGER,            
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(年月,地區,產業別,性別,年收入) ON CONFLICT REPLACE
        );
        '''
    )
    conn.commit()
    
    print("年收入table建立成功")
        
    
    cursor = conn.cursor()
    cursor.execute(
            '''
            CREATE TABLE  IF NOT EXISTS job(
                "id"	INTEGER,
                "年月"	TEXT NOT NULL,
                "地區"	TEXT NOT NULL,
                "產業別"	TEXT NOT NULL,
                "性別"	TEXT NOT NULL,
                "職業類別"	TEXT NOT NULL,
                "交易筆數"	INTEGER,
                "交易金額"	INTEGER,            
                PRIMARY KEY("id" AUTOINCREMENT),
                UNIQUE(年月,地區,產業別,性別,職業類別) ON CONFLICT REPLACE
            );
            '''
        )
    conn.commit()
    
    print("職業類別table建立成功")

    cursor = conn.cursor()
    cursor.execute(
            '''
            CREATE TABLE  IF NOT EXISTS education(
                "id"	INTEGER,
                "年月"	TEXT NOT NULL,
                "地區"	TEXT NOT NULL,
                "產業別"	TEXT NOT NULL,
                "性別"	TEXT NOT NULL,
                "教育程度類別"	TEXT NOT NULL,
                "交易筆數"	INTEGER,
                "交易金額"	INTEGER,            
                PRIMARY KEY("id" AUTOINCREMENT),
                UNIQUE(年月,地區,產業別,性別,教育程度類別) ON CONFLICT REPLACE
            );
            '''
        )
    conn.commit()
    
    print("教育程度類別table建立成功")
#--------------------------------------------------



#===============下載並更新資料==================

def updata_sqlite_data()->None:
    
    '''
    下載,並更新資料庫
    '''
    #__download_data()
    conn = sqlite3.connect('proj1_creditcard.db')  #連線資料庫
    cursor = conn.cursor()  
    __create_table(conn) 
    for datatype in DataType:        
        df = pd.read_csv(f'./datasource/{datatype}.csv') 
        df.rename(columns={'信用卡交易筆數':'交易筆數','信用卡交易金額[新台幣]':'交易金額'},inplace=True)   
        df['地區'] = df['地區'].astype(str)
    # 替換 '地區' 列的值
        df['地區'] = df['地區'].replace(df_new_area['地區'])
        

        conn = sqlite3.connect('proj1_creditcard.db')  #連線資料庫
        cursor = conn.cursor()
        sql=   f'''
        INSERT INTO {datatype}(年月,地區,產業別,性別,{DataType[datatype]},交易筆數,交易金額)VALUES(?,?,?,?,?,?,?)        ''' 
        
        values = tuple(df.iloc[0])
        cursor.execute(sql,values)  #連線資料表
        conn.commit()
        df.to_sql(datatype, conn, if_exists='append', index=False) 


#=================讀取資料庫資料================

def lastest_datetime_data()->list[tuple]:
    conn = sqlite3.connect("proj1_creditcard.db")
    cursor = conn.cursor()
    sql = '''
        SELECT 年月,地區,產業別,性別,年齡層,交易筆數,交易金額
        FROM age
        '''
    cursor.execute(sql)
    rows= cursor.fetchall()
    cursor.close()
    return rows

#===============搜尋資料庫中資料==================

def search_data(start,end,datatype:str)->list[tuple]:
    column_names(creditTreeView, 4, DataType[datatype])
    conn = sqlite3.connect("proj1_creditcard.db")
    cursor = conn.cursor()
    sql = f'''
        SELECT 年月,地區,產業別,性別,{DataType[datatype]},交易筆數,交易金額
        from {datatype}
        WHERE 年月 between {start} and {end}
        '''
    
    cursor.execute(sql)
    rows= cursor.fetchall()
    cursor.close()
    conn.close
    return rows
           
                      
    


    
    