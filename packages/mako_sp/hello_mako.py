# coding: utf-8
from mako.template import Template


def simple_render():
    mytemplate = Template("hello world!")
    print(mytemplate.render())


def render_arg():
    mytemplate = Template("hello, ${name}!")
    print(mytemplate.render(name="jack"))


def main():
    simple_render()
    render_arg()


if __name__ == '__main__':
    main()

