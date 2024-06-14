# 第九章配套代码

## 文件清单

* `.env.example`：环境变量文件模板。
* `main.py`：脚本文件。
* `main-opt.py`：脚本文件优化后的版本。


## 安装依赖

```shell
$ pip install openai
$ pip install python-dotenv
```

## 配置

把环境变量文件的模板（`.env.example`）复制一份，命令名为真正使用的文件名（`.env`）。

```shell
$ cp .env.example .env
```

编辑 `.env` 文件，配置 LLM API 相关信息。

## 运行

```shell
$ python main.py
```

或在 VS Code 中点击右上角的 ▶️ 按钮运行。
