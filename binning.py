# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:39:49 2018

@author: PS
"""

import  math
list = []
list1 = input("please enter the data:   ").split(",")
bucket = int(input("please enter the number of bin:   "))
for i in list1:
    list.append(int(i))
list.sort()
print ("Sorted data is:  ")
print(list)


def EqualFrquency(list,bucket):
    main_bin = []
    bin_length = int(len(list) / bucket)
    count = 0
    for i in range(bucket):
        bin = []
        for j in range(bin_length):
            bin.append(list[count])
            count = count + 1
        main_bin.append(bin)
    print(main_bin)
    return main_bin


def EqualWidth(list,bucket):
    max =list[len(list)-1]
    width = (max - list[0]) / bucket
    width = math.ceil(width)

    main_bin = []
    bin = []
    for i in list:
        if (i>=0 and i<=width):
            bin.append(i)
    main_bin.append(bin)

    bin = []
    for i in list:
        if (i>=(width+1) and i<=(width+width)):
            bin.append(i)
    main_bin.append(bin)

    bin = []
    for i in list:
        if (i>=(width+width+1)):
            bin.append(i)
    main_bin.append(bin)
    print(main_bin)
    return main_bin


def smoothing_mean(main_bin):
    for i in range(len(main_bin)):
        sum = 0
        for j in range(len(main_bin[i])):
            sum = sum + main_bin[i][j]
        avg = int(sum / len(main_bin[i]))
        for j in range(len(main_bin[i])):
            main_bin[i][j] = avg
    print(main_bin)


def smoothing_median(main_bin):
    for i in range(len(main_bin)):
        mid  = int(len(main_bin[i])/2)
        if (mid != 0):
            for j in range(len(main_bin[i])):
                main_bin[i][j] = main_bin[i][mid]
    print(main_bin)


def bin_boundry(main_bin):
    for i in range(len(main_bin)):
        mid = int(len(main_bin[i])/2)
        near = int(math.fabs(main_bin[i][0] - main_bin[i][mid]))
        nearest = 0
        for j in range(len(main_bin[i])):
            if j != mid:
                dif = int(math.fabs(main_bin[i][mid]- main_bin[i][j]))
                if dif<near:
                    near = dif
                    nearest = j
        main_bin[i][mid] = main_bin[i][nearest]
    print(main_bin)

print()
print("By Equal Frequency:   ")
print("By smoothing mean:   ")
main_bin = EqualFrquency(list,bucket)
smoothing_mean(main_bin)
print("By smoothing median:   ")
main_bin = EqualFrquency(list,bucket)
smoothing_median(main_bin)
print("by bin boundary")
main_bin = EqualFrquency(list,bucket)
bin_boundry(main_bin)

print()
print("By equal width:   ")
print("smooth by mean:")
main_bin = EqualWidth(list,bucket)
smoothing_mean(main_bin)
print("smoothing by median:")
main_bin = EqualWidth(list,bucket)
smoothing_median(main_bin)
print("bin boundary:")
main_bin = EqualWidth(list,bucket)
bin_boundry(main_bin)
