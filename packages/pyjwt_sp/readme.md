# pyjwt usage

## jwt 里一些字段的含义

- iat，Issued At，授权的时间
- exp，Expiration Time，失效时间
- nbf，Not Before Time，生效时间
- iss，Issuer，授权者
- sub，Subject，授权目的
- jti，JWT ID，ID

上面的时间都是用时间戳

## refs

- [RFC 7519 - JSON Web Token (JWT)](https://tools.ietf.org/html/rfc7519)
- [JSON Web Token - Wikipedia](https://en.wikipedia.org/wiki/JSON_Web_Token)
- [Welcome to PyJWT — PyJWT 1.6.1 documentation](https://pyjwt.readthedocs.io/en/latest/)
- [Flask + PyJWT 实现基于Json Web Token的用户认证授权 – 那时那你](https://www.thatyou.cn/flask-pyjwt-%E5%AE%9E%E7%8E%B0%E5%9F%BA%E4%BA%8Ejson-web-token%E7%9A%84%E7%94%A8%E6%88%B7%E8%AE%A4%E8%AF%81%E6%8E%88%E6%9D%83/)
- [IBM Knowledge Center - 用于 OAuth 客户机授权的 JSON Web 令牌 (JWT)](https://www.ibm.com/support/knowledgecenter/zh/SSEQTP_8.5.5/com.ibm.websphere.wlp.doc/ae/cwlp_jwttoken.html)
