"""Basic example of using threads oar multiprocessing with concurrent.furures module"""

import concurrent.futures
import time


start = time.perf_counter()


def my_func(argument):
    """Function - example"""
    print(f'Start my_func with argument: {argument}')
    time.sleep(argument)
    print(f'Finished my_func with argument {argument}')


# with concurrent.futures.ThreadPoolExecutor() as executor:
with concurrent.futures.ProcessPoolExecutor() as executor:
    arg_list = [3, 4]
    executor.map(my_func, arg_list)

print(f'Spent time: {time.perf_counter() - start}')
