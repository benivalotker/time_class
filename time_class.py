#/path/path/
#title           :TITLE
#description     :script description.
#update date     :01/01/2020 12:10
#version         :1.0
#changes         :veriosn changes description.
#python_version  :3.6  
#==============================================================================

import json
import datetime

'''
three type of time calculate:
    1. function run time - decorator static methods.
    2. block run time (start/end/diff) - instance methods.
    3. multi run time (list of time) - instance methods.

NOTE: the alternative is to inherit from log class and write the time to log.
'''
class TimeClass():
    # constructor
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.diff_time = None
        self.take_time = []


    ''' TYPE 1 - function run time decorator '''
    # calculate function run time
    def func_run_time(self, func):
        def time_warapper(*args, **kwargs):
            # start time (before function run)
            start_time = datetime.datetime.now()

            # function run
            func(*args, **kwargs)

            # end time (before function run)
            end_time = datetime.datetime.now()
            
            # return diff time
            return end_time-start_time
        return time_warapper


    ''' TYPE 2 - start time, end time & diff time '''
    # start time - time start from some position.
    def start_time_init(self, str_title=None):
        self.start_time = datetime.datetime.now()

        if str_title != None:
            return str_title + " - " + str(self.start_time) 
        else:
            return str(self.start_time)

    # end time - time end from some position.
    def end_time_init(self, str_title=None):
        self.end_time = datetime.datetime.now()

        if str_title != None:
            return str_title + " - " + str(self.end_time) 
        else:
            return str(self.end_time)

    # diff time - calculate the diff between end time & start time.
    def diff_time_init(self, str_title=None):
        self.diff_time = self.end_time - self.start_time

        if str_title != None:
            return str_title + " - " + str(self.diff_time) 
        else:
            return str(self.diff_time)
    

    ''' TYPE 3 -  multi time take '''
    # take_time_init   - write the correct time.
    def take_time_init(self):
        time_name = str(datetime.datetime.now())
        
        self.take_time.append(time_name)

    # finish_take_time - return the time list and empty the list.
    def take_time_list(self):
        return self.take_time

    # calc_take_time   - calculate the time list.
    def calc_time_list(self):
        start_end_diff =  self._parse_str_to_datetime(self.take_time[-1]) - self._parse_str_to_datetime(self.take_time[0])
        time_summery = {"Total Diff Time": str(start_end_diff)}

        list_len = len(self.take_time)
        for i in range(list_len):
            try:
                total = self._parse_str_to_datetime(self.take_time[i+1]) - self._parse_str_to_datetime(self.take_time[i])
                time_summery["Diff Time {}".format(i)] = str(total)
            except:
                pass

        self.take_time = []
        return time_summery


    def _parse_str_to_datetime(self, str_time):
        return datetime.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')


