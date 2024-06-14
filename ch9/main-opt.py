# 我们正在编写一个脚本，通过 OpenAI SDK 调用 LLM 的 API，对英文文稿进行翻译。
# 待翻译的文件在 input 目录中，翻译结果将保存在 output 目录中。
# 每次读取一个输入文件，翻译结果保存到输出目录中。
# 我们会逐步完成整个脚本，通过多个函数的配合来完成整个任务。

import os
from typing import Optional

# 引入依赖包 openai 和 python-dotenv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

"""
我在 .env 文件中定义的环境变量如下：
BASE_URL
API_KEY
MODEL_NAME
"""

# 现在把它们引入到当前脚本中
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# 我的系统提示词
system_prompt_for_essay = "你是一个精通中英文翻译的智能助手。用户发来的消息都是待翻译的文本。你不需要问候、不需要解释、不需要总结，直接按照原文的格式输出译文即可。"
system_prompt_for_tech_doc = "……"
system_prompt_for_blog = "……"

# 创建 OpenAI 实例
client = OpenAI(base_url = BASE_URL, api_key = API_KEY)

# 先实现一个简单的翻译函数，通过 OpenAI SDK 调用大模型 API
def translate(text: str, system_prompt: str) -> Optional[str]:
	print("SDK requesting...")
	try:
		completion = client.chat.completions.create(
			model = MODEL_NAME,
			messages = [
				{"role": "system", "content": system_prompt},
				{"role": "user", "content": text}
			]
		)
		print("SDK done!")
		# print(completion.choices[0].message.content)
		return completion.choices[0].message.content
	except Exception as e:
		print(f"SDK error occurred: {e}")
		return None

# 检查目录是否存在，如果不存在则创建
output_dir = "output"
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

# 写一个函数，用于读取文件内容。参数是文件路径，返回文件内容
def read_file(file_path):
	with open(file_path, "r") as f:
		return f.read()

# 写一个函数，用于保存文件内容。参数是文件路径和内容，将内容保存到文件中
def save_file(file_path, content):
	with open(file_path, "w") as f:
		f.write(content)

# 写一个函数，用于读取指定目录下的文件，返回文件路径列表
def list_files(dir):
	return [os.path.join(dir, f) for f in os.listdir(dir)]

# test
# print(list_files("input"))

files = list_files("input")
for file in files:
	text = read_file(file)
	output = translate(text, system_prompt_for_essay)
	if output != "":
		save_file(file.replace("input", "output"), output)
		print(f"{file} done")
	else:
		print(f"{file} failed")
