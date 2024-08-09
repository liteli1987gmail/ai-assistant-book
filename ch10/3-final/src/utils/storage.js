// 这个文件用于操作 localStorage
// 保存在 localStorage 中的数据通常是对象或数组，因此在存储和读取时需要使用 JSON.stringify 和 JSON.parse 进行转换

// 保存数据
export function save(key, data) {
	localStorage.setItem(key, JSON.stringify(data))
}

// 读取数据
export function load(key) {
	const data = localStorage.getItem(key)
	return data ? JSON.parse(data) : null
}

// 删除数据
export function remove(key) {
	localStorage.removeItem(key)
}
