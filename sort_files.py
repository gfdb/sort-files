# Written by Gianfranco Dumoulin Bertucci

import random
import shutil
import string
from datetime import datetime
from os import listdir, mkdir, rename, walk
from os.path import exists, getctime, getmtime, isdir
from time import time

from tqdm import tqdm

dates = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}


def id_generator(size: int = 6, 
            chars: str = string.ascii_uppercase + string.digits) -> str:
    """Generates random 6 character alphanumeric string

    Args:
        size (int, optional): size of returned string. Defaults to 6.
        chars (str, optional): characters to choose from. Defaults to string.ascii_uppercase+string.digits.

    Returns:
        str: 6 character alphanumeric string
    """
    
    return ''.join(random.choice(chars) for _ in range(size))

def get_date(path_to_file: str, lmod: bool = False) -> str:
    """Given a path to a file, function will return the date the file 
       was created as a string of the form 'Month Day Year'

    Args:
        path_to_file (str): A path to a file
        sort_by_lmod (bool, optional): pass true to sort by last modified. Defaults to False.

    Returns:
        [str]: The date in the form 'Month Day Year'
    """
    date_from_file = None

    if lmod:
        date_from_file = datetime.fromtimestamp(getctime(path_to_file))
    else:
        date_from_file = datetime.fromtimestamp(getmtime(path_to_file))

    return str(dates[date_from_file.month]) + ' ' + str(date_from_file.day) + ' ' + str(date_from_file.year)

def move_to_new(src_path: str, dest_path: str) -> int:
    """[Moves all files in a src_path and all of it's subdirectories to destination folder]

    Args:
        src_path ([string]): [Path to folder to be sorted]
        dest_path ([string]): [Path to folder the sorted pictures will end up in]

    Returns:
        [int]: [Number of files that have been moved]
    """
    num_pics = 0
    mkdir(dest_path)
    for subdir, dirs, files in tqdm(walk(src_path), desc = "Unpacking Files", ncols=50):
        subdir = subdir.replace('\\', '/')
        for file in files:
            num_pics = num_pics + 1
            try:
                shutil.move(subdir + f'/{file}', dest_path)
            except:
                # if thousands of files are being organized, it is 
                # possible that two files have the same name.
                # if so, append random unqiue str
                x = id_generator()
                file1 = file.replace('.', x + '.')
                rename(subdir + f'/{file}', subdir + f'/{file1}')
                shutil.move(subdir + f'/{file1}', dest_path)
    return num_pics

def organize_month_day_year(file_path: str, lmod: bool = False) -> None:
    """Organizes a directory(file_path) by creating a directory 
    of all files created/motified(whichever is passed) on a given 
    day and moving them into that directory

    Args:
        file_path (str): the path to a file
        lmod (bool, optional): pass true to organize by last modified. Defaults to False.
    """
    for file in tqdm(listdir(file_path), desc = "Sorting Files", ncols=100):
        name_date = file_path + '/' + get_date(file_path + '/' + file, lmod)
        if not isdir(name_date):
            mkdir(name_date)
        shutil.move((file_path + '/' + file), name_date)


def organize_by_year(file_path: str) -> None:
    """Organizes directories created in organize_month_day_year by grouping 
    directories of the same year into directories labeled by that year. 
    Ex: Aug 10 2020 and Sep 27 2020 --> 2020
    """
    for dirs in tqdm(listdir(file_path), desc = "Organizing Directories", ncols=100):
        if isdir(file_path + '/' + dirs):
            the_year = file_path + '/' + dirs.split(' ')[2]
            if not exists(the_year):
                mkdir(the_year)
            shutil.move(file_path + '/' + dirs, the_year)


def main():
    source_path = input("Enter the path to the folder you want to sort: ")
    destination_path = source_path + "-Sorted"
    if exists(destination_path):
        cntr = 1
        while exists(destination_path + "(" + str(cntr) + ")"):
            cntr += 1
        destination_path = destination_path + "(" + str(cntr) + ")"


    cdate_or_lmod = ''
    while True:
        cdate_or_lmod = input("How would you like to sort\n\t- Creation Date (c)\n\t- Last Modified (l)\nChoice: ")
        if cdate_or_lmod != 'l' or cdate_or_lmod != 'c':
            break
        else:
            print('Invalid Choice...')

    start_time = time()
    num_pics = move_to_new(source_path, destination_path)
    organize_month_day_year(destination_path)
    organize_by_year(destination_path)
    print(f"{num_pics} files sorted successfully to '{destination_path}' in %s seconds" % round((time() - start_time), 3))

if __name__ == '__main__':
    main()