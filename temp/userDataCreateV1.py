# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

#my library
from pickFunctionV2  import pick_main, pick_random_from_list, yes_or_no_loop

def load_id_db():
    id_data = pd.read_excel("id_db_log.xlsx",dtype=np.dtype(str))
    return id_data

def main():
    data = load_id_db()
    while True:
        ID = input("<회원가입을 하려면 0을 입력, 종료하려면 exit을 입력>.\nID를 입력하세요.\nID: ")
        if ID == "exit":
            return
        if ID not in data.id.values:
            while True:
                print("등록되지 않은 ID입니다")
                ID = input("<회원가입을 하려면 0을 입력, 종료하려면 exit을 입력>.\nID를 다시 입력하세요.\nID: ")
                if ID in data.id.values:
                    break
                if ID  == "exit":
                    return
        if ID in data.id.values:    
            info = data.loc[data['id']==ID]
            password = input("비밀번호를 입력하세요\nPassword: ")
            if password == "exit":
                return
            if password == info["password"][0]:
                login = "success"
            while password != info["password"][0]:
                print("Wrong Password")
                print("<시작으로 돌아가려면 start를 입력, 종료하려면 exit을 입력>")
                password = input("비밀번호를 다시 입력하세요\nPassword: ")
                if password in ["start","exit"]:
                    break
                if password == info["password"][0]:
                    login = "success"
                    break                
            if password == "exit":
                return
        if login =="success":
            break
        
                
                
w = load_id_db()

main()

