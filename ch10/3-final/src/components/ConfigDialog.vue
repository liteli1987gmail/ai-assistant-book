<script setup>
import { ref } from 'vue'
import { loadConfig, saveConfig } from '@/utils/config.js'

// 当前组件声明会抛出 'close' 事件
const emit = defineEmits(['close'])

const config = loadConfig()

const $baseURL = ref(config.baseURL || '')
const $apiKey = ref(config.apiKey || '')
const $modelName = ref(config.modelName || '')
const $systemPrompt = ref(config.systemPrompt || '')

function onClickSave() {
	saveConfig({
		baseURL: $baseURL.value,
		apiKey: $apiKey.value,
		modelName: $modelName.value,
		systemPrompt: $systemPrompt.value,
	})
	emit('close')
}
</script>

<template>
	<!-- 半透明背景遮罩 -->
	<div
		class="mask absolute inset-0 bg-black opacity-50 z-10"
		@click="emit('close')"
	></div>

	<!-- 半屏弹框，包含标题栏和简洁风格的表单 -->
	<div class="dialog absolute left-0 right-0 bottom-0 max-h-3/4 z-20 bg-white overflow-hidden">
		<!-- 标题栏，中间是标题文字，左右各有一个按钮 -->
		<header class="h-11 bg-gray-100 border-b flex-none flex items-center justify-center relative">
			<h1 class="font-bold text-lg">配置</h1>
			<div class="absolute top-0 left-0 h-full flex items-center justify-center">
				<button
					class="px-5 h-full flex items-center justify-center text-gray-500 hover:text-gray-600"
					@click="emit('close')"
				>取消</button>
			</div>
			<div class="absolute top-0 right-0 h-full flex items-center justify-center">
				<button
					class="px-5 h-full flex items-center justify-center text-blue-500 hover:text-blue-600"
					@click="onClickSave"
				>保存</button>
			</div>
		</header>

		<!-- 表单，包含四个字段，前三个输入框必填，最后一个多行输入框可选 -->
		<div class="content overflow-auto p-5">
			<div class="mb-5">
				<label class="block mb-1 text-sm text-gray-500">
					API Base URL
					<span class="text-red-500">*</span>
				</label>
				<input
					type="text"
					v-model.trim="$baseURL"
					class="w-full px-3 py-2 border rounded border-gray-300 focus:outline-none focus:border-blue-500"
				/>
			</div>
			<div class="mb-5">
				<label class="block mb-1 text-sm text-gray-500">
					API Key
					<span class="text-red-500">*</span>
				</label>
				<input
					type="text"
					v-model.trim="$apiKey"
					class="w-full px-3 py-2 border rounded border-gray-300 focus:outline-none focus:border-blue-500"
				/>
			</div>
			<div class="mb-5">
				<label class="block mb-1 text-sm text-gray-500">
					模型名
					<span class="text-red-500">*</span>
				</label>
				<input
					type="text"
					v-model.trim="$modelName"
					class="w-full px-3 py-2 border rounded border-gray-300 focus:outline-none focus:border-blue-500"
				/>
			</div>
			<div class="mb-5">
				<label class="block mb-1 text-sm text-gray-500">
					系统提示词
				</label>
				<textarea
					v-model.trim="$systemPrompt"
					class="w-full h-24 px-3 py-2 leading-snug border rounded border-gray-300 resize-none focus:outline-none focus:border-blue-500"
				></textarea>
			</div>
		</div>
	</div>
</template>
