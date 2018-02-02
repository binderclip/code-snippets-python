# coding: utf-8
import xmltodict


def parse_f():
    print('=== parse_f ===')
    with open('demo.xml') as fd:
        doc = xmltodict.parse(fd.read())
        print(doc['mydocument']['@has'])  # == u'an attribute'
        print(doc['mydocument']['and']['many'])  # == [u'elements', u'more elements']
        print(doc['mydocument']['plus']['@a'])  # == u'complex'
        print(doc['mydocument']['plus']['#text'])  # == u'element as well'


def parse_s():
    print('=== parse_s ===')
    xml = """<mydocument has="an attribute">
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a="complex">
    element as well
  </plus>
</mydocument>"""
    doc = xmltodict.parse(xml)
    print(doc['mydocument']['@has'])  # == u'an attribute'
    print(doc['mydocument']['and']['many'])  # == [u'elements', u'more elements']
    print(doc['mydocument']['plus']['@a'])  # == u'complex'
    print(doc['mydocument']['plus']['#text'])  # == u'element as well'


def main():
    parse_f()
    parse_s()


if __name__ == '__main__':
    main()
