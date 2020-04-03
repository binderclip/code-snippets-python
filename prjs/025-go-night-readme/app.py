import re
import os
import json


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + '/bilibili.json') as f:
        b_data = json.load(f)
    # print(data)
    with open(os.path.dirname(os.path.realpath(__file__)) + '/ytb.json') as f:
        y_data = json.load(f)
    replace_s(s1, b_data, y_data)


def replace_s(s, b_data, y_data):
    new_lines = []
    for line in s.splitlines():
        m = re.search(r'第 (\d+)', line)
        if not m:
            new_lines.append(line)
            continue
        n = m.group(1)
        new_b_url = b_data.get(n)
        new_y_url = y_data.get(n)
        new_line = line
        if not new_b_url:
            # todo here
            print("error no bilibili url n: " + str(n))
        else:
            new_line = re.sub(r'\[Bilibili\]\(https://space.bilibili.com/326749661\)', f'[Bilibili]({new_b_url})', new_line)
        if not new_y_url:
            print("error no youtube url n: " + str(n))
        else:
            new_line = re.sub(r'\[YouTube\]\(https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q\?sub_confirmation=1\)', f'[YouTube]({new_y_url})', new_line)
        new_lines.append(new_line)
    print('\n'.join(new_lines))


s1 = """| 第 79 期 | Go-Micro Part 3: 运行时工具集                                  | 舒先                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 78 期 | Go Schedular 源码阅读                                          | 饶全成                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 77 期 | 阅读 Go 源码带来的收益                                         | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 76 期 | Kubernetes Scheduler 设计与实现                                | Draven                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 75 期 | 2020 年 Go 的一些发展计划                                      | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 74 期 | time.Timer 源码分析                                            | 欧长坤                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 73 期 | 趣头条在长链接方面的实践（qrpc）                               | 徐志强                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 72 期 | Go-Micro Part 2: 微服务框架实战                                | 舒先                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 71 期 | go-ini 配置库评析                                              | 无闻                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 70 期 | Go 中不常注意的各种细节集锦                                    | 老貘                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 69 期 | 基于 Go 语言周边生态打造的行业技术中台                         | 杨晖                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 68 期 | 网络知识十全大补丸                                             | 刘楠                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 67 期 | Go database/sql 数据库连接池分析                               | 邹文通                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 66 期 | CSP 理解顺序进程间通信                                         | 欧长坤                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 65 期 | Go 原生网络模型 vs 异步 Reactor 模型                           | 潘建锋                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 64 期 | 深入浅出 Golang Runtime                                        | 郝以奋                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 63 期 | Go 编码风格阅读与讨论                                          | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 62 期 | Go-Micro Part 1: 微服务框架介绍                                | 舒先                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 61 期 | Go Modules、Go Module Proxy 和 goproxy.cn                      | 盛傲飞                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 60 期 | IPFS 星际文件系统                                              | xcshuan                                  | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 59 期 | Real-world Go Concurrency Bugs                                 | 欧长坤                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 58 期 | What's new in Go 1.13？                                        | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 57 期 | sync/semaphore 源码浅析                                        | Felix                                    | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 56 期 | channel & select 源码分析                                      | 欧长坤                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 55 期 | Go&WebAssembly 简介                                            | 柴树彬                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 54 期 | Go 夜读之 TiDB SQL 兼容性测试工具简介                          | PingCAP                                  | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 53 期 | Build in func delete from map                                  | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 52 期 | httprouter 简介                                                | 曹春晖                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 51 期 | sync/errgroup 源码阅读                                         | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 50 期 | GoLand Tips & Tricks                                           | Florin & Shengyou Fan                    | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 49 期 | TiDB 源码阅读之 Transaction                                    | zimulala                                 | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 48 期 | TiDB 源码阅读之 Compiler                                       | wangcong                                 | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 47 期 | TiDB 源码阅读之 Executor                                       | chenshuang                               | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 46 期 | TiDB 源码阅读之概览                                            | 龙恒                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 45 期 | goim 架构设计与源码分析                                        | tsingson                                 | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 44 期 | map 源码阅读分析                                               | 饶全成                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 43 期 | gomonkey 框架设计与应用实践                                    | 张晓龙                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 42 期 | An Introduction to Failpoint Design                            | 龙恒                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 41 期 | golint 及 golangci-lint 的介绍和使用                           | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 40 期 | atomic.Value 的使用和源码分析                                  | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 39 期 | init 函数使用分析                                              | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 38 期 | Kubernetes scheduler 源码阅读                                  | John                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 37 期 | 从 serverless 的一个设计说起                                   | 冉小龙                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 36 期 | k8s context 实践源码阅读                                       | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 35 期 | context 源码阅读                                               | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 34 期 | plan9 汇编入门，带你打通应用和底层                             | 曹春晖                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 33 期 | defer 和逃逸分析                                               | 饶全成                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 32 期 | etcd raft 源码阅读                                             | 缪昌新                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 31 期 | flag 包源码阅读                                                | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 30 期 | go mod 源码阅读 Part 4                                         | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 29 期 | Opentracing jaeger 集成及源码分析                              | jukylin                                  | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 28 期 | go mod 源码阅读 Part 3                                         | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 27 期 | go mod 源码阅读 Part 2                                         | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 26 期 | 手把手教你基于 Github+Netlify 构建自动化持续集成的技术团队博客 | John                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 25 期 | TSDB 引擎介绍，对比及存储细节                                  | yuyang                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 24 期 | go mod 源码阅读 Part 1                                         | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 23 期 | Drone 简单介绍和部分源码分析                                   | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 22 期 | Go 开发工具讨论                                                | 杨文/John                                | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 21 期 | errors 处理及 zap 源码分析                                     | 叶飞／阙坦                               | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 20 期 | go test 及测试覆盖率                                           | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 19 期 | 如何开发一个简单高性能的 http router 及 gorouter 源码分析      | 徐佳军                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 18 期 | 去中心化加密通信框架 CovenantSQL/DH-RPC的设计                  | 王鹏程                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 17 期 | grpc 开发及 grpcp 的源码分析                                   | 林益帆                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 16 期 | OpenFass 介绍及源码分析                                        | Lucas                                    | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 15 期 | 多路复用资源池组件剖析                                         | 李亚川                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 14 期 | sync.Pool 源码分析及适用场景                                   | 杨文                                     | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 13 期 | Kubernetes 入门指南                                            | 李森森                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 12 期 | Go 中 Goroutine 的调度                                         | 郑宝杨                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 11 期 | Go 代码质量持续检测实践                                        | 吴雨豪                                   | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 10 期 | http 包源码阅读 part3 2018-06-28 线下活动                      |                                          | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 9 期  | （未录制）2018-06-14 线下活动                                  |                                          | |
| 第 8 期  | http 包源码阅读 part2 2018-05-31 线下活动                      |                                          | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |
| 第 7 期  | http 包源码阅读 part1 2018-05-24 线下活动                      |                                          | [YouTube](https://www.youtube.com/channel/UCZwrjDu5Rf6O_CX2CVx7n8Q?sub_confirmation=1) [Bilibili](https://space.bilibili.com/326749661) |"""


if __name__ == '__main__':
    main()
