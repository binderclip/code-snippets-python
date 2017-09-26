# coding: utf-8
import simplejson
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


def parse_whole_html():
    print("=== parse_whole_html ===")
    html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())
    print("soup.title: {}".format(soup.title))
    print("soup.title.name: {}".format(soup.title.name))
    print("soup.title.string: {}".format(soup.title.string))
    print("soup.title.parent.name: {}".format(soup.title.parent.name))


def parse_part_html():
    print("=== parse_part_html ===")
    html_para = """<p>just <b>click</b> <a href="http://example.com">here</a>.</p>"""
    soup = BeautifulSoup(html_para, 'html.parser')
    for s in soup.strings:
        print(s)
    print("".join(soup.strings))
    for content in soup.contents:
        print_content(content)


def print_content(content, level=0):
    print("{}{}".format("\t" * level, content))
    if isinstance(content, NavigableString):
        return
    for sub_content in content.contents:
        print_content(sub_content, level + 1)
    print('{}<<< end'.format("\t" * level))


def parse_part_html2():
    print("=== parse_part_html2 ===")
    html_para = """<p>just <b>click</b> <a href="http://example.com">here</a>.</p>"""
    soup = BeautifulSoup(html_para, 'html.parser')
    print(simplejson.dumps(parse_soup_to_markup(soup)))


def parse_soup_to_markup(soup):
    m = {
        "text": "".join(soup.strings),
    }
    markups, _ = get_markups(soup)
    m["markups"] = markups
    return m


def get_markups(content, start_index=0):
    if isinstance(content, NavigableString):
        start_index += len(content)
        return [], start_index
    _start_index = start_index
    markups = []
    for child in content.children:
        new_markups, start_index = get_markups(child, start_index)
        markups.extend(new_markups)
    if isinstance(content, Tag) and content.name in ('a', 'b'):
        markup = {
            "name": content.name,
            "start_index": _start_index
        }
        markup['end_index'] = start_index
        markups.append(markup)
    return markups, start_index


def main():
    parse_whole_html()
    parse_part_html()
    parse_part_html2()


if __name__ == '__main__':
    main()


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
