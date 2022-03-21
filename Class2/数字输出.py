'''
Author: Boredcui
Date: 2022-03-07 16:19:23
LastEditors: Boredcui
LastEditTime: 2022-03-07 16:22:11
FilePath: \PythonCourse\Class2\数字输出.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
a = int(input())
for i in range(5):
    print(a % 10)
    a = a//10
