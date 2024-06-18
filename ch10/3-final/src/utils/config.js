import * as storage from '@/utils/storage.js'

// 配置信息有以下几个字段：
// - apiKey: OpenAI API Key (必填)
// - baseURL: OpenAI API Base URL (必填)
// - modelName: OpenAI Model Name (必填)
// - systemPrompt: 系统提示词 (可选)

// 保存在 localStorage 中的配置信息的 key
const STORAGE_KEY = 'config'

// 默认的系统提示词
const DEFAULT_SYSTEM_PROMPT = '你是一个名叫 “Simple Chat” 的智能对话机器人。你可以回答关于编程、设计、科技、生活等方面的问题。默认使用简体中文回答。'

// 初始化配置信息
// 有默认值的字段写入默认值，没有默认值的字段设置为空字符串
function initConfig() {
	return {
		apiKey: '',
		baseURL: '',
		modelName: '',
		systemPrompt: DEFAULT_SYSTEM_PROMPT,
	}
}

// 从 localStorage 中读取配置信息
// 如果没有保存过配置信息，则初始化一个配置信息，并保存到 localStorage
export function loadConfig() {
	const config = storage.load(STORAGE_KEY)
	if (!config) {
		const newConfig = initConfig()
		saveConfig(newConfig)
		return newConfig
	}
	return config
}

// 保存配置信息到 localStorage
export function saveConfig(config) {
	// 这里需要防止存入的系统提示词为空字符串
	if (!config.systemPrompt) {
		config.systemPrompt = DEFAULT_SYSTEM_PROMPT
	}

	storage.save(STORAGE_KEY, config)
}

// 判断是否已经保存了必填字段
export function hasValidConfig() {
	const config = loadConfig()
	return config.apiKey && config.baseURL && config.modelName
}
