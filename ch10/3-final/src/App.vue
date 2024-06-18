<!--
	这个项目是一个网页版的智能对话机器人。
	整个项目采用 TailwindCSS 作为样式库。
	我们会在这个文件中一步一步地构建整个页面。
-->

<script setup>
import { ref, nextTick, onMounted } from 'vue'
import MessageItem from '@/components/MessageItem.vue'
import ConfigDialog from '@/components/ConfigDialog.vue'
import { mockDataMessages } from '@/utils/mock.js'
import { getMockResponse, getResponse } from '@/utils/message.js'
import { hasValidConfig } from '@/utils/config.js'

const $messages = ref([])
const $messageList = ref(null)

const $inputContent = ref('')
const $inputElement = ref(null)

const $isLoading = ref(false)
const $shouldShowDialog = ref(false)

// 这个变量用来保存配置完整性的检查结果
const $hasValidConfig = ref(hasValidConfig())

function scrollToBottom() {
	// 消息列表滚动到底部，需要平滑滚动
	$messageList.value.scrollTo({
		top: $messageList.value.scrollHeight,
		behavior: 'smooth',
	})
}

function onCloseDialog() {
	$shouldShowDialog.value = false
	// 当配置弹框关闭时，重新检查配置完整性
	$hasValidConfig.value = hasValidConfig()
}

async function onSubmit() {
	// 先把输入框中的内容保存到 content 变量中
	const content = $inputContent.value.trim()
	// 如果 content 为空，不做任何处理
	if (!content) return

	// 把用户消息添加到消息列表中
	$messages.value.push({
		role: 'user',
		content: content,
	})
	// 清空输入框
	$inputContent.value = ''
	// 聚焦输入框
	$inputElement.value.focus()
	// 滚动到消息列表的底部
	nextTick(() => {
		scrollToBottom()
	})

	// 为机器人回复的消息提前占个位
	$messages.value.push({
		role: 'assistant',
		content: '',
		status: 'waiting',
	})

	// 设置加载状态
	$isLoading.value = true
	// 获取机器人回复的内容
	const stream = await getResponse($messages.value)
	// 遍历事件流
	for await (const chunk of stream) {
		onReceiveDelta(chunk.choices[0]?.delta?.content || '')
	}
	// 事件流结束，更新最后一条消息的状态
	$messages.value[$messages.value.length - 1].status = 'done'
	// 恢复状态
	$isLoading.value = false
}

function onReceiveDelta(delta) {
	const lastMessageIndex = $messages.value.length - 1
	// 如果最后一条消息是占位状态
	if ($messages.value[lastMessageIndex].status === 'waiting') {
		// 把占位内容清空
		$messages.value[lastMessageIndex].content = ''
		// 消息进入 streaming 状态
		$messages.value[lastMessageIndex].status = 'streaming'
	}

	// 更新最后一条消息的内容
	$messages.value[lastMessageIndex].content += delta
	// 滚动到消息列表的底部
	nextTick(() => {
		scrollToBottom()
	})
}

// 页面加载完成后，消息列表滚动到底部
onMounted(() => {
	scrollToBottom()
})

</script>

<template>
	<!--
		首先这里需要一个容器，用来包裹主体区域。
		它的高度撑满整个页面，最大宽度为 640px，并且居中显示。
		我们一步一步来，暂时不需要考虑它的内容。
	-->
	<div class="mx-auto max-w-[640px] h-full overflow-hidden bg-white flex flex-col relative">
		<!--
			这里需要仿手机 App 的聊天界面布局形式：
			* 顶部是标题栏，高度固定。
			* 底部是操作栏，高度固定。
			* 中间区域是对话区，高度占据剩余空间，当内容超长时可以出现垂直滚动条。
		-->
		<header class="h-11 bg-gray-100 border-b flex-none flex items-center justify-center relative">
			<h1 class="font-bold text-lg">Simple Chat</h1>
			<div class="absolute top-0 right-0 h-full flex items-center justify-center">
				<button
					class="px-5 h-full flex items-center justify-center text-blue-500 hover:text-blue-600"
					@click="$shouldShowDialog = true"
				>配置</button>
			</div>
		</header>
		<div ref="$messageList" class="p-5 pb-10 flex-auto overflow-y-auto">
			<div v-if="!$hasValidConfig">
				<div class="text-gray-400 text-center mt-5">
					（您还没有配置模型）
				</div>
				<button
					class="block mt-5 mx-auto py-3 w-[6em] text-blue-500 rounded border hover:text-blue-600 hover:border-blue-500"
					@click="$shouldShowDialog = true"
				>点此配置
				</button>
			</div>
			<div v-else-if="$messages.length === 0" class="text-gray-400 text-center mt-5">
				（您还没有发过消息）
			</div>
			<template v-else>
				<MessageItem
					v-for="message of $messages"
					:messageItem="message"
				></MessageItem>
			</template>
		</div>
		<footer
			class="h-12 border-t flex-none flex items-stretch justify-between"
			v-if="$hasValidConfig"
		>
			<div class="flex-auto">
				<input
					class="px-4 w-full h-full bg-white outline-0 border-transparent border-2 focus:border-blue-300"
					placeholder="请输入消息内容"
					v-model="$inputContent"
					autofocus
					ref="$inputElement"
					@keydown.enter="onSubmit"
				/>
			</div>
			<div class="flex-none">
				<button
					class="px-4 size-full bg-blue-500 text-white hover:bg-blue-600 disabled:bg-gray-300 disabled:text-gray-500 disabled:cursor-not-allowed"
					@click="onSubmit"
					:disabled="$isLoading"
				>发送</button>
			</div>
		</footer>

		<ConfigDialog
			v-if="$shouldShowDialog"
			@close="onCloseDialog"
		></ConfigDialog>
	</div>
</template>

<style scoped>

</style>
