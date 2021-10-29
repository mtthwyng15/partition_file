#!/bin/env python3

import sys
import re
import os

# count number of arguments
count_args = len(sys.argv)

# variables

student = {
    "name": "Matthew",
    "surname": "Yeung",
    "id_number": "13789641",
    "date_completed": "15 October 2021"
    }

# function

def get_option():
    return sys.argv[1]

def get_file_system_type():
    file_size = os.path.getsize(sys.argv[2])
    file_system_types = []

    if file_size > 0:
        print("the file system types in use: ",  end = " ")
       # print(open_file)
        for line in open(open_file):
            line.rstrip('\n')
            fields = re.split(' ', line)
            #  print(fields[2], end = " ")
            value = fields[2]
            
            if value not in file_system_types:
                file_system_types.append(value)

        print(file_system_types)
    else:
        print("No file system types found in argument file")

def get_available_size():
    count = 0;
    for line in open(open_file):
        fields = re.split(' ', line)
        if fields[3] == 'rw':
            count = count + int(fields[4])
            count = count - int(fields[5])

    print("Overall space available in read-write partitions: " + str(int(count)))

def is_partition_found(partition_found):

    if not partition_found:
        print('no partition found')

def partition():
    get_partition = sys.argv[2]
    open_file = sys.argv[3]

    # print(get_partition)
    # print(open_file)

    if os.access(open_file, os.R_OK):

        partition_found = False

        for line in open(open_file):
            fields = re.split(' ', line)
            
            if get_partition == fields[0]:
                partition_found = True
                file_type = fields[3]
                count = int(fields[4]) - int(fields[5])
                if file_type == 'rw':
                    file_type = 'read-write'
                    print('Partition ' + get_partition + ' is ' + file_type + ' and has ' + str(int(count)) + ' available space')
                elif file_type == 'ro':
                    file_type = 'read-only'
                    print('Partition ' + get_partition + ' is ' + file_type + ' and has ' + str(int(count)) + ' available space')

        is_partition_found(partition_found)
    else:
        print("Error: file reading not possible")

option = get_option()

if count_args <= 2:
    print('missing argument')
elif count_args == 3:
    
    open_file = sys.argv[2]

    if os.access(open_file, os.R_OK):

        if option == '-f':
            get_file_system_type()
        elif option == '-a':
            get_available_size()
        elif option == '-v':
            print(student)
        else:
            print('wrong option')
    else:
        print("Error: file reading not possible")

elif count_args == 4:
    if option == '-p':
        partition()
    else:
        print('wrong option')
else:
    print('too many arguments')

