import time
from time_class import TimeClass

# create time class object instance
time_obj = TimeClass()

'''
decorator example
'''
# decorator to some function with or without parameter
@time_obj.func_run_time
def func_run_time_decorator(*args, **kwargs):
    print("Function Params = ", args,kwargs)
    time.sleep(2)

# res = func_run_time_decorator("some args", key_args="some key args")
# print("Total Second Run = ", res)


'''
start/end example
optional - "str_title", return the time with some text before (use it for log or else)
'''
def start_end_time():
    time.sleep(1)

    # write and get start time
    time_obj.start_time_init(str_title="start time")
    
    time.sleep(3)

    # write and get end time
    time_obj.end_time_init(str_title="end time")
    
    # write and get diff time
    res = time_obj.diff_time_init(str_title="diff time")

    print("Diff Time = ", res)

# start_end_time()


'''
multi time
'''
def multi_time():
    # take multi time
    time_obj.take_time_init()
    time.sleep(4)

    time_obj.take_time_init()
    time.sleep(1)

    time_obj.take_time_init()
    time.sleep(2)

    time_obj.take_time_init()

    # return the multi time list
    res = time_obj.take_time_list()
    print("Time List = ", res)

    # calculate the diff between the time and empty the list (return dict with the diff)
    res = time_obj.calc_time_list()
    print("Time List Diff = ", res)


# multi_time()