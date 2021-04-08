#
# Disclaimer: It's not pretty but it works. 
#
import os
import random
import shutil
import string
import time
from datetime import date
from os import listdir, makedirs, mkdir, walk
from os.path import isfile, join
from sys import platform
from time import sleep

from PIL import Image
from tqdm import tqdm

dates = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    '''
        Generates random 6 character alphanumeric string
    '''
    return ''.join(random.choice(chars) for _ in range(size))

def get_date(path_to_file, max_age = None):
    '''
    Returns(String) the date the target file was created or modified, whichever is older, as Month Day Year
    '''
    date_from_file = []
    date_from_file.append(time.ctime(os.path.getctime(path_to_file))) #creation date & time
    date_from_file.append(time.ctime(os.path.getmtime(path_to_file))) #last modified date & time
    if path_to_file.endswith('.jpg'):
        print(Image.open(path_to_file)._getexif()[36867])
        print(time.ctime(os.path.getctime(path_to_file)))
        print(time.ctime(os.path.getmtime(path_to_file)))
        exit()
        # date_from_file.append(Image.open(path_to_file)._getexif()[36867])


    date_dictionaries = []
    oldest = ''

    for the_date in date_from_file:
        the_date = the_date.replace('  ', ' ')
        date_dict = dict()
        date_dict['day'] = the_date.split(' ')[2]
        date_dict['month'] = the_date.split(' ')[1]
        date_dict['year'] = the_date.split(' ')[4]
        date_dictionaries.append(date_dict)
    for dic1 in date_dictionaries:
        for dic2 in date_dictionaries:
            if max_age:
                if int(dic1['year']) < int(max_age):
                    dic1['year'] = float('inf')
                if int(dic2['year']) < int(max_age):
                    dic2['year'] = float('inf')
            day1 = date(int(dic1['year']), dates[dic1['month']], int(dic1['day']))
            day2 = date(int(dic2['year']), dates[dic2['month']], int(dic2['day']))
            if day1 < day2:
                oldest = dic1['month'] + ' ' + dic1['day'] + ' ' + dic1['year']
            else:
                oldest = dic2['month'] + ' ' + dic2['day'] + ' ' + dic2['year']
    return oldest
    
        


def move_to_new(src_path, dest_path):
    """[Moves all files in a src_path and all of it's subdirectories to destination folder]

    Args:
        src_path ([string]): [Path to folder to be sorted]
        dest_path ([string]): [Path to folder the sorted pictures will end up in]

    Returns:
        [int]: [Number of files that have been moved]
    """
    num_pics = 0
    mkdir(dest_path)
    for subdir, dirs, files in os.walk(src_path):
        subdir = subdir.replace('\\', '/')
        for file in files:
            num_pics = num_pics + 1
            try:
                shutil.move(subdir + f'/{file}', dest_path)
            except:
                x = id_generator()
                file1 = file.replace('.', x + '.')
                os.rename(subdir + f'/{file}', subdir + f'/{file1}')
                shutil.move(subdir + f'/{file1}', dest_path)
    return num_pics

def organize_month_day_year(file_path, max_age = None):
    '''
    Organizes a directory(file_path) by creating a directory of all files created/motified(whichever is older) on a given day
    and moving them into that directory
    '''
    for file in os.listdir(file_path):
        name_date = file_path + '/' + get_date(file_path + '/' + file, max_age)
        if not os.path.isdir(name_date):
            mkdir(name_date)
        shutil.move((file_path + '/' + file), name_date)


def organize_by_year(file_path):
    '''
    Organizes directories created in organize_month_day_year by grouping directories of the same year
    into directories labeled by that year. Ex: Aug 10 2020 and Sep 27 2020 --> 2020
    '''
    for dirs in os.listdir(file_path):
        if os.path.isdir(file_path + '/' + dirs):
            the_year = file_path + '/' + dirs.split(' ')[2]
            if not os.path.exists(the_year):
                mkdir(the_year)
            shutil.move(file_path + '/' + dirs, the_year)


def main(): 
    # max_age = ''
    # source_path = input("Enter the path to the folder you want to sort: ")
    # yes_no = input("Are these recovered files with potentially corrupted metadata? (y/n): ")
    # if yes_no == "y":
    #     max_age = input("What is the year created/modified of the oldest file? (Example: I know none of the files are from before 1999, so I would enter 1999. Go older if you're not sure): ")
    # destination_path = source_path + " - Sorted"

    # start_time = time.time()
    # num_pics = move_to_new(source_path, destination_path)
    # sleep(2)
    # organize_month_day_year(destination_path, max_age)
    # sleep(2)
    # organize_by_year(destination_path)
    # sleep(2)
    # print(f"{num_pics} pictures sorted successfully to '{destination_path}' in %s seconds" % round((time.time() - start_time), 3))
    get_date('D:/pics - Copy- Sorted/2002/Jan 9 2002/DSCF0002.jpg')


main()

# print(get_date(destination_path + '/IMG_0004 (2).JPG'))

# print(get_date(destination_path + '/IMG_0004 (2).JPG'))
