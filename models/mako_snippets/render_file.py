# coding: utf-8
from mako.template import Template


def main():
    mytemplate = Template(filename='mytmpl.txt')
    print(mytemplate.render(name='Jack'))


if __name__ == '__main__':
    main()
