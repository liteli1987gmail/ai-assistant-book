import OpenAI from 'openai'
import { BASE_URL, API_KEY, MODEL_NAME } from './config.js'

// 一个休眠函数，让程序等待一段时间（单位 ms）
function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms))
}

// 这个函数用来模拟一个 API 请求，一秒钟后返回字符串
export async function getMockResponse() {
	await sleep(1000)
	return '这是一条模拟的回复'
}

// 先创建一个 OpenAI 的 JS SDK 实例，以备稍后调用大模型的 API
const client = new OpenAI({
	apiKey: API_KEY,
	baseURL: BASE_URL,
	timeout: 60_000,
	dangerouslyAllowBrowser: true,
})

const SYSTEM_PROMPT = '你是一个名叫 “Simple Chat” 的智能对话机器人。你可以回答关于编程、设计、科技、生活等方面的问题。你的回答尽量简洁。默认使用简体中文回答。如果用户提出的问题超出了你的知识库范围，请不要编造答案，可以回复 “我不知道”。'

export async function getResponse(question) {
	const completion = await client.chat.completions.create({
		messages: [
			{ role: 'system', content: SYSTEM_PROMPT },
			{ role: 'user', content: question },
		],
		model: MODEL_NAME,
	})
	return completion.choices[0]?.message?.content || ''
}
