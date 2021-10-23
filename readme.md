# Sort Files

This script will sort a directory of your choosing. You can choose to sort by either creation date or last modified. This is espcially useful for drives/directories that contain thousands of unsorted pictures. The script will unpack all files from the passed directory and it's sub directories. It will then move them into a new directory, which it will then sort.

How to Run (or follow the example):

1. Clone Repo
2. Navigate to some/file/path/sort-files
3. If you do not have pipenv installed, install it using ```$ pip install pipenv```
4. ```$ pipenv install```
5. ```$ pipenv run python sort_files.py```

Enjoy your sorted files.

Note: There is a 0% chance of your files being deleted. No deleting occurs at any point during the sorting of your files. As a result you will be left with two directories:
1. Source_Dir
2. Source_Dir-Sorted

Your source dir will contain a bunch of empty directories (if it had any within it), as all files will have been moved to the new sorted directory, feel free to delete the source dir once the script is done.

Example of file structure after sort:

 +-- 2021

&emsp; +-- Jan 18 2021

&emsp;&emsp; +-- file1.txt

&emsp;&emsp; +-- file2.txt

&emsp; +-- Jan 19 2021

&emsp; +-- Jan 20 2021

&emsp; +-- Jan 21 2021


## Step by Step

1. Clone Repo
2. Navigate to some/file/path/sort-files
3. If you do not have pipenv installed, install it using 

```$ pip install pipenv``` - installs pipenv

```$ pipenv install``` - installs dependencies

4. Navigate to the directory that you want to sort, in this case "/Volumes/LEXAR\ MEDIA/DCIM/100CANON" (contains 672 images)

![terminal](https://github.com/gfdb/sort-files/blob/main/example_pics/unsorted.png?raw=true)

![terminal](https://github.com/gfdb/sort-files/blob/main/example_pics/terminal.png?raw=true)

5. Copy directory path
6. Run the script using pipenv

```$ pipenv run python sort_files.py```

7. Paste directory path from your clipboard and choose whether you want to sort by creation date or last modified.

![terminal](https://github.com/gfdb/sort-files/blob/main/example_pics/output.png?raw=true)

8. Go check out your sorted files.

![terminal](https://github.com/gfdb/sort-files/blob/main/example_pics/sorted.png?raw=true)