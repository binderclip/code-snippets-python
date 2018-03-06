## package and module 


- module 是一个 python 文件
- package 是一个一些 python 文件的集合
- import 了 package 的时候更像是 import 了 package 的 `__init__.py`
- import package 的结果也是一个 module 对象
- package 不可以被 `python -m` 执行
- import package 中内容的时候 package 中的 `__init__.py` 会先加载 
- 命名空间首先是当前执行脚本所在的目录，然后是 `PYTHONPATH` 中的目录

### name

- `__name__` 在 `python xxx.py` 以及直接在 python 解释器中的时候都是 `__main__`
- 其他时候比如 `python -m xxx.py`，或者被其他文件中 `import` 的时候一个文件中的 `__name__` 是 module 或者 package 的名字
- `__name__` 是 `__main__` 的时候是不可以有相对引用的

## ref

- [6. Modules — Python 3.6.4rc1 documentation](https://docs.python.org/3/tutorial/modules.html)
- [PEP 366 -- Main module explicit relative imports | Python.org](https://www.python.org/dev/peps/pep-0366/)
- [PEP 328 -- Imports: Multi-Line and Absolute/Relative | Python.org](https://www.python.org/dev/peps/pep-0328/)
- [What's the difference between a Python module and a Python package? - Stack Overflow](https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package)
- [python - How to fix "Attempted relative import in non-package" even with __init__.py - Stack Overflow](https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py)
- [Execute an installed Python package as a script? - Stack Overflow](https://stackoverflow.com/questions/4050120/execute-an-installed-python-package-as-a-script)