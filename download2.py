import requests
import csv
import sqlite3
import os
import pandas as pd
from glob import glob


def __download_credit_data() -> csv:

    '''地區別代碼【KLC: 基隆市, TPE: 臺北市, NTP: 新北市, TYC: 桃園市, HCC: 新竹市, HCH: 新竹縣, MLH: 苗栗縣, TCC: 臺中市, CHH: 彰化縣, NTH: 南投縣, YUH: 雲林縣, CYC: 嘉義市, CYH: 嘉義縣, TNC: 臺南市, KHC: 高雄市, PTH: 屏東縣, TTH: 臺東縣, HLH: 花蓮縣, YIH: 宜蘭縣, PHH: 澎湖縣, KMH: 金門縣, LCH: 連江縣, TWN: 臺灣, X1: 無縣市, LCSUM: 六都十六縣, MCT: 六都, LOC: 十六縣】

    Available values : KLC, TPE, NTP, TYC, HCC, HCH, MLH, TCC, CHH, NTH, YUH, CYC, CYH, TNC, KHC, PTH, TTH, HLH, YIH, PHH, KMH, LCH, TWN, X1, LCSUM, MCT, LOC

    產業類別代碼【FD: 食品餐飲類, CT: 服飾類, LG: 住宿類, TR: 交通類, EE: 文教康樂類, DP: 百貨類, X2: 無產業, OT: 其他類, ALL: 全部產業, IDSUM: 各產業類】
    Available values : FD, CT, LG, TR, EE, DP, X2, OT, ALL, IDSUM

    1:男性 2:女性
    63000000: 臺北市 64000000: 高雄市 65000000: 新北市 66000000: 臺中市 67000000: 臺南市 68000000: 桃園市
    10002000: 宜蘭縣 10004000: 新竹縣 10005000: 苗栗縣 10007000: 彰化縣 10008000: 南投縣 10009000: 雲林縣
    10010000: 嘉義縣 10020000: 嘉義市 10013000: 屏東縣 10014000: 臺東縣 10015000: 花蓮縣 10016000: 澎湖縣
    10017000: 基隆市 10018000: 新竹市 09020000: 金門縣 09007000: 連江縣

    '''
    

new_area={'63000000': '臺北市' ,'64000000':' 高雄市', '65000000': '新北市', '66000000': '臺中市' ,'67000000': '臺南市', '68000000': '桃園市','10002000': '宜蘭縣', '10004000': '新竹縣', '10005000': '苗栗縣',' 10007000': '彰化縣' ,'10008000': '南投縣', '10009000': '雲林縣','10010000': '嘉義縣','10020000': '嘉義市', '10013000': '屏東縣' ,'10014000': '臺東縣', '10015000': '花蓮縣' ,'10016000': '澎湖縣','10017000': '基隆市', '10018000': '新竹市' ,'09020000': '金門縣', '09007000': '連江縣'}    

area = ['KLC', 'TPE', 'NTP', 'TYC', 'HCC', 'HCH', 'MLH', 'TCC', 'CHH', 'NTH', 'YUH', 'CYC', 'CYH', 'TNC', 'KHC',' PTH', 'TTH', 'HLH', 'YIH', 'PHH', 'KMH', 'LCH', 'X1',' LCSUM', 'MCT', 'LOC']

industry = ['FD', 'CT', 'LG', 'TR', 'EE', 'DP', 'X2', 'OT', ' IDSUM']
gender : ['M','F']
DataType = ['age', 'income', 'job', 'education']


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
print('職業類別消費資料讀取成功')
#---------------------------------------------------

#===============合併csv檔案==================
# 指定CSV檔案所在的資料夾路徑
for item in DataType:
    folder_path = './rwasata/'    
    
# 使用glob模組取得資料夾中所有的CSV檔案路徑
    files = glob.glob(folder_path + '*.csv')

# 創建一個空的DataFrame
    combined_data = pd.DataFrame()
# 迴圈讀取每個CSV檔案，並合併到combined_data中
for file in files:
    df = pd.read_csv(file)    
    combined_data = combined_data.append(df, ignore_index=True)
# 將合併後的資料寫入新的CSV檔案
combined_data.to_csv(f'./{item}.csv', index=False)

#---------------------------------------------------


#===============建立資料庫欄位==================
def __create_table(conn:sqlite3.Connection('proj1_creditcard.db')):       
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS age(
            "id"	INTEGER,
            "年月"	TEXT NOT NULL,
            "地區"	TEXT NOT NULL,
            "產業別"	TEXT NOT NULL,
            "性別"	INTEGER NOT NULL,
            "年齡層"	INTEGER NOT NULL,            
            "交易筆數"	INTEGER,
            "交易金額"	INTEGER,            
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(年月,年齡層) ON CONFLICT REPLACE
        );
        '''
    )
    conn.commit()
    cursor.close
    print("年齡層資料庫建立成功")

    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS income(
            "id"	INTEGER,
            "年月"	TEXT NOT NULL,
            "地區"	TEXT NOT NULL,
            "產業別"	TEXT NOT NULL,
            "性別"	INTEGER NOT NULL,
            "年收入"	INTEGER NOT NULL,
            "交易筆數"	INTEGER,
            "交易金額"	INTEGER,            
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(年月,年收入) ON CONFLICT REPLACE
        );
        '''
    )
    conn.commit()
    cursor.close
    print("年收入類別資料庫建立成功")
        
    
    cursor = conn.cursor()
    cursor.execute(
            '''
            CREATE TABLE  IF NOT EXISTS job(
                "id"	INTEGER,
                "年月"	TEXT NOT NULL,
                "地區"	TEXT NOT NULL,
                "產業別"	TEXT NOT NULL,
                "性別"	INTEGER NOT NULL,
                "職業類別"	INTEGER NOT NULL,
                "交易筆數"	INTEGER,
                "交易金額"	INTEGER,            
                PRIMARY KEY("id" AUTOINCREMENT),
                UNIQUE(年月,職業類別) ON CONFLICT REPLACE
            );
            '''
        )
    conn.commit()
    cursor.close
    print("職業類別資料庫建立成功")

    cursor = conn.cursor()
    cursor.execute(
            '''
            CREATE TABLE  IF NOT EXISTS education(
                "id"	INTEGER,
                "年月"	TEXT NOT NULL,
                "地區"	TEXT NOT NULL,
                "產業別"	TEXT NOT NULL,
                "性別"	INTEGER NOT NULL,
                "教育程度"	INTEGER NOT NULL,
                "交易筆數"	INTEGER,
                "交易金額"	INTEGER,            
                PRIMARY KEY("id" AUTOINCREMENT),
                UNIQUE(年月,教育程度) ON CONFLICT REPLACE
            );
            '''
        )
    conn.commit()
    cursor.close
    print("教育程度類別消費建立成功")
#--------------------------------------------------




#===============建立讀取資料欄位==================

def __insert_data(conn:sqlite3.Connection,values:())->None:
    for item in DataType:
        cursor = conn.cursor(f'{item}.db')    
        sql=   '''
        INSERT INTO f'{item}.db'(年月,地區,產業別,性別,{item},交易筆數,交易金額)VALUES(?,?,?,?,?,?,?)        '''    
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()

    cursor = conn.cursor('job.db')    
    sql=   '''
    INSERT INTO 'income'(年月,地區,產業別,性別,年收入,交易筆數,交易金額)VALUES(?,?,?,?,?,?,?)        '''    
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()

    cursor = conn.cursor('incom.db')    
    sql=   '''
    INSERT INTO 'job'(年月,地區,產業別,性別,職業類別,交易筆數,交易金額)VALUES(?,?,?,?,?,?,?)        '''    
    cursor.execute(sql,values)  
    conn.commit()
    cursor.close()

    cursor = conn.cursor('education.db')    
    sql=   '''
    INSERT INTO 'education'(年月,地區,產業別,性別,教育程度,交易筆數,交易金額)VALUES(?,?,?,?,?,?,?)        '''    
    cursor.execute(sql,values)  
    conn.commit()
    cursor.close()
#--------------------------------------------------


#===============下載並更新資料==================

def updata_sqlite_data()->None:
    
    '''
    下載,並更新資料庫
    '''
    #data = __download_credit_data()
    conn = sqlite3.connect("age.db")
    __create_table(conn) 
    path = "./age"
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            file_directory = os.path.join(path, filename)
            file = open(file_directory)            
            reader = csv.reader(file_directory)
            for item in reader:
                __insert_data(conn,(item('年月'),item('地區'),item('產業別'),item('性別'),item('交易筆數'),item('交易金額')))
            conn.close()
        else:
            continue 
    
    conn = sqlite3.connect("job.db")
    __create_table(conn) 
    path = "./job"
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            file_directory = os.path.join(path, filename)
            file = open(file_directory)
            reader = csv.reader(file)
            for item in reader:
                __insert_data(conn,(item('年月'),item('地區'),item('產業別'),item('職業類別'),item('信用卡交易筆數'),item('信用卡交易金額[新台幣]')))
            conn.close()
        else:
            continue
        
    conn = sqlite3.connect("income.db")
    __create_table(conn) 
    path = "./income"
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            file_directory = os.path.join(path, filename)
            file = open(file_directory)
            reader = csv.reader(file)
            for item in reader:
                __insert_data(conn,(item('年月'),item('地區'),item('產業別'),item('收入類別'),item('信用卡交易筆數'),item('信用卡交易金額[新台幣]')))
            conn.close()
        else:
            continue 

    conn = sqlite3.connect("education.db")
    __create_table(conn) 
    path = "./education"
    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            file_directory = os.path.join(path, filename)
            file = open(file_directory)
            reader = csv.reader(file)
            for item in reader:
                __insert_data(conn,(item('年月'),item('地區'),item('產業別'),item('教育程度類別'),item('信用卡交易筆數'),item('信用卡交易金額[新台幣]')))
            conn.close()
        else:
            continue
    

#--------------------------------------------------