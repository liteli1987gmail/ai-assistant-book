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
		<div class="content max-w-[85%] leading-normal px-5 py-3 bg-blue-200 rounded-3xl rounded-bl-none whitespace-pre-wrap">
			{{ messageItem.content }}
		</div>
	</div>
</template>
