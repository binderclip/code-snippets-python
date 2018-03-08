import imghdr


def get_image_type_of_file(file):
    type_ = imghdr.what(file) or ''
    if type_ == 'jpeg':
        type_ = 'jpg'
    return type_


def get_image_type_of_file_data(file_data):
    type_ = imghdr.what('', file_data) or ''
    if type_ == 'jpeg':
        type_ = 'jpg'
    return type_


def main():
    file_name = '../_common_img/google.jpg'
    file_name2 = '../_common_img/google.jpg.png'
    file_name3 = '../_common_img/xxx.png'

    # use file name
    print(get_image_type_of_file(file_name))
    print(get_image_type_of_file(file_name2))
    print(get_image_type_of_file(file_name3))

    # use file obj
    with open(file_name, 'rb') as f:
        print(get_image_type_of_file(f))

    # use file stream
    with open(file_name, 'rb') as f:
        print(get_image_type_of_file_data(f.read()))
    with open(file_name2, 'rb') as f2:
        print(get_image_type_of_file_data(f2.read()))


if __name__ == '__main__':
    main()


# https://docs.python.org/3.6/library/imghdr.html
