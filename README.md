# pairwise-dependency-check

## 题面

接入第三方旧客户端后依赖校验形同虚设：下载依赖未校验校验和可被替换；版本使用开放范围易漂移到脆弱版本；锁定文件可被本地配置绕过；依赖来源未限制可指向任意地址；未校验签名与发布者身份。supply/depcheck.py 是核心，tests/test_depcheck.py 15个红。要修的是：强制比对校验和；锁定精确版本禁止范围漂移；锁定文件不可被旁路；校验依赖来源域名白名单；校验包签名与发布者身份。

## 运行方式

```bash
python -m pytest tests -q
```

初始状态应为 `15 failed`，无 collection error；`tests/` 目录不可修改。

## 字段

- 所属领域：安全
- 子方向：其他
- 任务类型：Bugfix
- 语言/框架：Python 3, pytest
- 环境可复现等级：无外部依赖
