# coding: utf-8
from misaka import Markdown, HtmlRenderer


class _Renderer(HtmlRenderer):
    """自定义 Markdown 渲染器"""

    def linebreak(self):
        # two space on line tail
        print('>>> linebreak')
        # return '<br>'       # no return no change

    # def paragraph(self, content):
    #     print('>>> paragraph')
    #     print(content)
    #     print('<<<')
    #     # return content


def main():
    md = Markdown(
            # skip-html - 跳过原文中的 HTML 代码
            # hard-wrap - 每个 \n 都渲染为 <br>
            renderer=_Renderer(flags=('hard-wrap', 'skip-html')),
            # space-headers - 只将 # Title 转为 <header>
            #                 #Title 会保持原样
            extensions=('disable-indented-code', 'autolink', 'space-headers'))
    print md('''some text
next line

next para''')


if __name__ == '__main__':
    main()
