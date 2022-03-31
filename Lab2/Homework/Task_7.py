# Author: Jakub Szwedowicz
# Date: 17.03.2022
# e-mail: kuba.szwedowicz@gmail.com
import time
import os


def task():
    dir_path = input_dir_path()
    if not dir_path:
        return

    filename = input_filename()
    full_path = os.path.join(dir_path, filename)

    print('Date of last modification:', time.localtime(os.path.getmtime(full_path)))
    print('Date of file creation:', time.localtime(os.path.getctime(full_path)))
    print('Date of last access:', time.localtime(os.path.getatime(full_path)))
    print('Size in bytes:', time.localtime(os.path.getsize(full_path)))


def input_dir_path() -> str:
    path = input('Enter the path to the dir: ')
    # path = 'Homework'
    if not os.path.isdir(path):
        print('Not a dir path! closing!')
        path = ''
    return path


def input_filename() -> str:
    filename = input('Enter name of the file: ')
    # filename = 'Task_1.py'
    return filename
