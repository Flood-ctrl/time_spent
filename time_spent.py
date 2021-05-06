#!/usr/bin/env python3

import time
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# def spentTime(input_function):
#     start_time = time.time()
#     input_function()
#     spent_time = time.time()
#     spent_time = spent_time - start_time
#     spent_time = time.strftime('%H:%M:%S', time.gmtime(spent_time))
#     function_name = sys._getframe().f_code.co_name
#     print (f"Time spent in {function_name} is: ", spent_time)


def sleepFucn():
    start_time = time.time()
    n = 3
    while n > 0:
        n = n - 1
        time.sleep(3)
        spent_time = time.time()
        spent_time = spent_time - start_time
        spent_time = time.strftime('%H:%M:%S', time.gmtime(spent_time))
        function_name = sys._getframe().f_code.co_name
        print (f"{bcolors.WARNING}Time spent in {function_name} : {spent_time}")

sleepFucn()