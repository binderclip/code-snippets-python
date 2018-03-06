# coding: utf-8
import misaka as m
from misaka import Markdown, HtmlRenderer


def main():
    rndr = HtmlRenderer()
    md = Markdown(rndr)
    print md('some text')

    print m.html('some other text')


if __name__ == '__main__':
    main()
