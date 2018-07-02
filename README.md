# code-snippets-python

## 为什么要收集这些代码

下次用起来方便。

## 环境配置

### 安装 pipenv

```shell
$ pip install pipenv
# or
$ brew install pipenv
```

### 配置（可选）

```shell
# 自动补全
$ eval "$(pipenv --completion)"

# macOS 可能要在 profile 里导出 local 变量
$ export LC_ALL=en_US.UTF-8
$ export LANG=en_US.UTF-8
```

### 创建和启动虚拟环境

```shell
$ git clone git@github.com:binderclip/code-snippets-python.git
$ cd code-snippets-python 
$ pipenv install
$ pipenv shell
```

### 之后更新虚拟环境

```shell
$ pipenv install xxx
```
