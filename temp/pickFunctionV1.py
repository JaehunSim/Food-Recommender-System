# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

def pick_random_from_list(list1):
    "from list1 pick random value"
    randIndex = np.random.randint(0,len(list1))
    return list1[randIndex]

def yes_or_no_loop(data):
    "append column names from data"
    data_category_list=[]
    for name in data:
        data_category_list.append(name)
        
    choice = 0
    
    while(choice ==0):
        pickedCategory = pick_random_from_list(data_category_list)
        categoryData = data[pickedCategory]
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
                break
            else:
                print("Wrong Input")
    if choice == "EXIT":
        pickedCategory = "Dump"
        randomFood = "Dump"
    return pickedCategory, randomFood

def pick_main():
    data = pd.read_excel("대표음식데이터.xlsx")
    logDataOpen = pd.read_table("outputLog.txt")
    logData = logDataOpen.readlines()
    logDataOpen.close()
    
    logging = open("outputLog.txt", "a")
    pickedCategory, randomFood = yes_or_no_loop(data)
    if pickedCategory == "Dump":
        pass
    else:
        logging.write(pickedCategory + "\t" + randomFood + "\n")
    logging.close()

pick_main()

