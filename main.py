import requests, df_up, datetime
from flask import Flask, render_template, url_for, request

class FileWork():
    def get_file_ind_lst(): #возвращает список индустрий для фильтра
        with open("db_folder/ind_file.txt", "r") as file:
            ind_txt = file.read()
        ind_lst = list()
        for ind in ind_txt.split("\n"):
            ind_lst.append(ind)
        return(ind_lst)  
      
    
    def up_file(): # если вы запускаете код в первый раз, файл автоматически будет загружен в нужную директорию
        url_file = "https://www.dropbox.com/s/ru96yt1m92xdltx/stocks_price_final.csv?dl=1"
        fl = requests.get(url_file)
        with open("db_folder/DB_file.csv", "wb") as file:
            file.write(fl.content)


    def fltr(s = False, e = False, ind = False, cou = 100): #возвращает таблицу для вывода на сайте
        cou = int(cou)
    
        if "False" == ind:
            ind = False

        if s or e:
            if datetime.datetime.strptime(s, "%Y-%m-%d") > datetime.datetime.strptime(e, "%Y-%m-%d"): # если даты выбраны не корректно, отправит на страницу ошибки
                return "dataER"
        
        df = df_up.getDF(start_data = s, end_data = e, industry = ind).head(cou)

        if len(df) == 0:
            return "fileER"
        
        return df
    
