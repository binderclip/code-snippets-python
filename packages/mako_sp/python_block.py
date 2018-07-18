from mako.template import Template


tpl = """
a, b = ${a}, ${b}
<%
show_max = not (a < 0 and b < 0)
%>
% if show_max:
max(a, b) = ${max(a, b)}
% else:
min(a, b) = ${min(a, b)}
% endif
"""


def main():
    mytemplate = Template(tpl)
    print(mytemplate.render(a=1, b=2))
    print(mytemplate.render(a=-1, b=2))
    print(mytemplate.render(a=-1, b=-2))


if __name__ == '__main__':
    main()
