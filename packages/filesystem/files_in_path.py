# coding: utf-8
import os


def main():
    dir = './'
    print(os.listdir(dir))
    file_paths = []
    for file_name in os.listdir(dir):
       file_paths.append(os.path.join(dir, file_name))
    print(file_paths)


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
