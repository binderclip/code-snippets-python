# code-snippets-python

## 为什么要收集这些代码

因为害怕。

记性不好。好不容易写了一个东西，之后又遇到类似场景的时候搞半天之前解决过的问题是会令人崩溃的。
相反，如果能随手找到之前的代码，并在它的基础上扩展扩展就实现了新的需求，那么几乎是正向的循环了。

另外一下子搞明白一个东西非常非常的困难，但弄明白又可能只是一次一次的应付。那么就结合一下两者，先应付应付，久了觉得有必要再去深入理解。
为了实现这个想法，应付的时候多留下点东西是不错的。

大概就是这样。

## 环境配置

### 安装 Conda

Linux

```
$ wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
$ bash Miniconda2-latest-Linux-x86_64.sh
```

macOS

```
$ wget https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
$ bash Miniconda2-latest-MacOSX-x86_64.sh
```

### 创建和启动虚拟环境

下载代码，并创建虚拟环境

```
$ git clone git@github.com:binderclip/code-snippets-python.git

$ conda env create -f code-snippets-python/environment.yml
$ source activate cspy2
```

### 之后更新虚拟环境

开发环境导出：

```
$ conda env export | grep -v "^prefix: " > environment.yml
```

线上对应更新：

```
$ conda env update -f environment.yml
```
