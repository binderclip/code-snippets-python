# coding: utf-8
import os


def main():
    file_path = 'temp.txt'
    print('file <{}> exists: {}'.format(file_path, os.path.exists(file_path)))
    try:
        os.remove(file_path)
    except OSError as e:
        print(e)


if __name__ == '__main__':
    main()

# ref Python Delete/Remove a File If Exists On Disk – nixCraft https://www.cyberciti.biz/faq/python-delete-remove-file-if-exists-on-disk/
# python - How to delete a file or folder? - Stack Overflow https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder