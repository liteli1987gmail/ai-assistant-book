<script setup>
defineProps({
	messageItem: Object,
})

</script>

<template>
	<div v-if="messageItem.role === 'user'" class="mb-5 flex items-center justify-end">
		<div class="content max-w-[85%] leading-normal px-5 py-3 bg-gray-200 rounded-3xl rounded-br-none">
			{{ messageItem.content }}
		</div>
	</div>
	<div v-else class="mb-5 flex items-center justify-start">
		<div
			class="content max-w-[85%] leading-normal px-5 py-3 bg-blue-200 rounded-3xl rounded-bl-none whitespace-pre-wrap"
			:class="messageItem.status === 'waiting' || messageItem.status === 'streaming' ? 'animate-cursor-flashing' : ''"
		>
			{{ messageItem.content }}
		</div>
	</div>
</template>

<style scoped>
/* 为 animate-cursor-flashing 这个类定义动画效果 */
/* 需要有一个与文字同色的方块光标紧随着文本后面闪烁 */
/* 光标与文字之间有少量空隙 */
@keyframes cursorFlashing {
	0%, 100% {
		opacity: 1;
	}
	50% {
		opacity: 0;
	}
}

.animate-cursor-flashing::after {
	content: '';
	display: inline-block;
	/* 下沉 0.15rem */
	transform: translateY(0.15rem);

	margin-left: 0.2rem;
	width: 0.75rem;
	height: 1rem;
	background-color: currentColor;
	animation: cursorFlashing 0.5s infinite;
}
/* 当元素为空时，光标左侧不留空隙 */
.animate-cursor-flashing:empty::after {
	margin-left: 0;
}

</style>
