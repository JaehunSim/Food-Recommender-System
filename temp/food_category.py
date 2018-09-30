# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame, Series
import numpy as np

foodData = pd.read_csv("food_data_old.csv",encoding="euc-kr")
foodCategoryList = list(foodData["구분"].unique())
foodData = foodData.sort_values("구분")

