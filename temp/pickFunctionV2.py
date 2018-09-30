# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

RECOMMEND_LIST = "food_recommendV2.xlsx"
OUTPUT = "output_log.xlsx"
FOOD_DATA = "food_data.xlsx"

def pick_random_from_list(list1):
    "from list1 pick random value"
    randIndex = np.random.randint(0,len(list1))
    return list1[randIndex]

def yes_or_no_loop(data):
    "append column names from data"
    data_category_list=[]
    for name in data:
        data_category_list.append(name)
    
    noChoiceList = []    
    
    choice = 0
    while(choice ==0):
        pickedCategory = pick_random_from_list(data_category_list)
        categoryData = data[pickedCategory]
        categoryData = categoryData.dropna()
        randomFood = list(categoryData.sample(1))[0]
        print(pickedCategory,"-",randomFood)
        while(True):
            choice = input("yes or No? ")
            choice = choice.upper()
            if choice in ["Y","YES","EXIT"]:
                break
            elif choice in ["N", "NO"]:
                print()
                choice = 0
                noChoiceList.append(randomFood)
                break
            else:
                print("Wrong Input")
    if choice == "EXIT":
        randomFood = "Dump"
    return randomFood, noChoiceList

def pick_main(id_code):
    recommend_data = pd.read_excel(RECOMMEND_LIST)
    food_data = pd.read_excel(FOOD_DATA)
    try:
        log_data= pd.read_excel(OUTPUT)    
    except:
        log_data = pd.DataFrame(columns=["id_code","food_id","choice","time","gps","weather","temp"])
    randomFood, noChoiceList = yes_or_no_loop(recommend_data)
    if randomFood == "Dump":
        pass
    else:
        food_id = food_data.loc[food_data["food"]==randomFood]["food_id"].values[0]
        log_data = log_data.append({"id_code":id_code,"food_id":food_id},ignore_index=True)
    #return log_data
    log_data.to_excel('output_log.xlsx', index=None)
    return log_data

w = pick_main()

