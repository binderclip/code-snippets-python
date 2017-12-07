# coding: utf-8
import imghdr


def get_image_type_of_file(file_name):
    type_ = imghdr.what(file_name) or ''
    if type_ == 'jpeg':
        type_ = 'jpg'
    return type_


def get_image_type_of_file_data(file_data):
    type_ = imghdr.what('', file_data) or ''
    if type_ == 'jpeg':
        type_ = 'jpg'
    return type_


def main():
    file_name = '../../models/common_img/google.jpg'
    file_name2 = '../../models/common_img/google.jpg.png'
    print(get_image_type_of_file(file_name))
    print(get_image_type_of_file(file_name2))
    with open(file_name) as f:
        print(get_image_type_of_file_data(f.read()))
    with open(file_name2) as f2:
        print(get_image_type_of_file_data(f2.read()))

if __name__ == '__main__':
    main()
