
### generator

- 用了 generator 之后会懒生成，使用更少的内存从而提升了性能
- 懒生成不用等元素都生成好了再用
- 懒生成和 iterator 提供的好处类似，只是用 generator 使得创建 iterator 更简单 
- 对于演示目的用了 generator 的 firstn 足够好，但是有和他等同的内建函数 range，内建函数通常会更快
- list comprehension 很像把一个 generator expression 传递给了一个 list constructor
- 需要用不止一次 generated values 的时候可以看看是不是保存到一个 list 中再用两次，比较计算和存储的开销

[Generators - Python Wiki](https://wiki.python.org/moin/Generators)

### coroutine

- x

[Charming Python: Implementing "weightless threads" with Python generators](https://www.ibm.com/developerworks/library/l-pythrd/)


[协程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000)

## ref

- [Generators Are Not Coroutines](http://wiki.c2.com/?GeneratorsAreNotCoroutines)
- [Python yield 使用浅析](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)
- [生成器 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681965108490cb4c13182e472f8d87830f13be6e88000)
