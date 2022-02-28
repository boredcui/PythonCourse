'''
Author: Boredcui
Date: 2022-02-28 16:24:03
LastEditors: Boredcui
LastEditTime: 2022-02-28 16:25:24
FilePath: \PythonCourse\datetime.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime("%x"))
print(now.strftime("%X"))
