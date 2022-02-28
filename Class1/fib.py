'''
Author: Boredcui
Date: 2022-02-28 16:14:27
LastEditors: Boredcui
LastEditTime: 2022-02-28 16:14:27
FilePath: \PythonCourse\fib.py
Description: 

Copyright (c) 2022 by boredcui, All Rights Reserved. 
'''
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
