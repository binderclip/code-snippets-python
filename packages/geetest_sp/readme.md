# geetest

## 验证流程

- 用 id 和 key 初始化 geetest lib
- 发送 user_id 获得 status（geetest 是否宕机）和 challenge
- status 和 user_id 写入 session，challenge 信息发给客户端
- ...
- 从客户端读取 challenge、validate 和 seccode，从 session 读取 status 和 user_id
- 如果是正常情况用 geetest 的在线测试，geetest 宕机情况则使用普通模式

## 实际应用

### 做发帖限制

- 客户端默认的请求不需要验证
- 服务器中记录用户的发帖情况
- 服务器接收请求之后判断是否超过限制，如果超过且没有 geetest 信息则报错
- 客户端接收到错误之后提示验证
- 验证后重新提交请求，验证通过则提交，不通过则返回错误

## refs

- [geetest-start](https://docs.geetest.com/install/overview/start/)
- [geetest-guide](https://docs.geetest.com/install/overview/guide)
- [geetest-flowchart](https://docs.geetest.com/install/overview/flowchart)
