"""
Name: Mohammad Fakhro
Class: CSCI 1411-004
Due Date: 10/27/2026
Description: Modular programming, creating 6 different functions with different tasks, read_data, compute_sum, compute_mean, compute_sd, display_result
Status: Works
"""
import math

def read_data():
    list_of_nums = []
    while(True):
        num = input("Enter a number(enter 'n' if you'd like to stop)")

        if(num == 'n'):
            return list_of_nums
        else:
            num = int(num)
            list_of_nums.append(num)


def compute_sum(list_of_nums):
    sum = 0
    for i in list_of_nums:
        sum += i
    return sum

def compute_mean(list_of_nums):
    size = len(list_of_nums)
    sum = compute_sum(list_of_nums)
    return sum / size

def compute_sd(list_of_nums):
    sum = 0
    for num in list_of_nums:
        mean = compute_mean(list_of_nums)
        dev = num - mean
        sqr_dev = dev ** 2
        sum+=sqr_dev
    size = len(list_of_nums)
    result = sum / (size -1 )
    SD = math.sqrt(result)
    return SD

def display_result(Sum, Mean, SD):
    print(f"Sum is: {Sum:.2f}")
    print(f"Mean is: {Mean:.2f}")
    print(f"Standard Deviation is: {SD:.2f}")

def main():
    my_list = read_data()
    Sum = compute_sum(my_list)
    Mean = compute_mean(my_list)
    SD = compute_sd(my_list)
    display_result(Sum,Mean,SD)


