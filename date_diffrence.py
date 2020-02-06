"""   Python challenge 1
Given two timestamps, in different time zones of the format:
        >>>  Day dd Mon yyyy hh:mm:ss +xxxx
where +xxxx represents the time zone.
Following program prints the absolute difference (in seconds) between them.
"""
from datetime import datetime

def solution(time_1, time_2):
    """
    Takes two valid dates and computes the difference in seconds
    :param time_1: start date
    :param time_2: end date
    :return: absolute difference in seconds
    """
    time_1 = datetime.strptime(time_1, "%a %d %b %Y %H:%M:%S %z")
    time_2 = datetime.strptime(time_2, "%a %d %b %Y %H:%M:%S %z")
    return int(abs(time_1 - time_2).total_seconds())


# Driver Code
if __name__ == '__main__':
    time_in_sec = ""
    N = int(input("Number of test cases : "))

    for i in range(N):
        print("{} Pair".format(i + 1))
        t1 = input("Enter first date: ")
        t2 = input("Enter second date: ")
        time_in_sec = time_in_sec + "\n" + str(solution(t1, t2))

    print("Output: {}".format(time_in_sec))
