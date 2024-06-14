/* 
本程序是一个用于清除浏览器缓存的 Chrome 扩展程序。
处理按钮点击事件：
- ID 为 "allHistory" 的按钮用于清除所有缓存历史记录
- ID 为 "pastMonth" 的按钮用于清除过去一个月的缓存历史记录
- ID 为 "pastWeek" 的按钮用于清除过去一周的缓存历史记录
- ID 为 "pastDay" 的按钮用于清除过去一天的缓存历史记录
- ID 为 "pastHour" 的按钮用于清除过去一小时的缓存历史记录
- ID 为 "pastMinute" 的按钮用于清除过去一分钟的缓存历史记录

创建函数以实现：
- 将日期和时间转换为人类可读的格式
- 在 ID 为 "lastCleared" 的段落中添加 "成功清除缓存" 及日期和时间
*/

document.getElementById('allHistory').addEventListener('click', () => {
    chrome.browsingData.remove({}, {
        "appcache": true,
        "cache": true,
        "cookies": true,
        "downloads": true,
        "fileSystems": true,
        "formData": true,
        "history": true,
        "indexedDB": true,
        "localStorage": true,
        "pluginData": true,
        "passwords": true,
        "serviceWorkers": true,
        "webSQL": true
    }, () => {
        console.log('Cache Cleared');
        document.getElementById('lastCleared').innerHTML = 'Successfully cleared cache: ' + new Date().toLocaleString();
    });
}
);

document.getElementById('pastMonth').addEventListener('click', () => {
    chrome.browsingData.remove({
        "since": (new Date().getTime() - 2592000000)
    }, {
        "appcache": true,
        "cache": true,
        "cookies": true,
        "downloads": true,
        "fileSystems": true,
        "formData": true,
        "history": true,
        "indexedDB": true,
        "localStorage": true,
        "pluginData": true,
        "passwords": true,
        "serviceWorkers": true,
        "webSQL": true
    }, () => {
        console.log('Cache Cleared');
        document.getElementById('lastCleared').innerHTML = 'Successfully cleared cache: ' + new Date().toLocaleString();
    });
}
);

document.getElementById('pastWeek').addEventListener('click', () => {
    chrome.browsingData.remove({
        "since": (new Date().getTime() - 604800000)
    }, {
        "appcache": true,
        "cache": true,
        "cookies": true,
        "downloads": true,
        "fileSystems": true,
        "formData": true,
        "history": true,
        "indexedDB": true,
        "localStorage": true,
        "pluginData": true,
        "passwords": true,
        "serviceWorkers": true,
        "webSQL": true
    }, () => {
        console.log('Cache Cleared');
        document.getElementById('lastCleared').innerHTML = 'Successfully cleared cache: ' + new Date().toLocaleString();
    });
}
);

document.getElementById('pastDay').addEventListener('click', () => {
    chrome.browsingData.remove({
        "since": (new Date().getTime() - 86400000)
    }, {
        "appcache": true,
        "cache": true,
        "cookies": true,
        "downloads": true,
        "fileSystems": true,
        "formData": true,
        "history": true,
        "indexedDB": true,
        "localStorage": true,
        "pluginData": true,
        "passwords": true,
        "serviceWorkers": true,
        "webSQL": true
    }, () => {
        console.log('Cache Cleared');
        document.getElementById('lastCleared').innerHTML = 'Successfully cleared cache: ' + new Date().toLocaleString();
    });
}
);

document.getElementById('pastHour').addEventListener('click', () => {
    chrome.browsingData.remove({
        "since": (new Date().getTime() - 3600000)
    }, {
        "appcache": true,
        "cache": true,
        "cookies": true,
        "downloads": true,
        "fileSystems": true,
        "formData": true,
        "history": true,
        "indexedDB": true,
        "localStorage": true,
        "pluginData": true,
        "passwords": true,
        "serviceWorkers": true,
        "webSQL": true
    }, () => {
        console.log('Cache Cleared');
        document.getElementById('lastCleared').innerHTML = 'Successfully cleared cache: ' + new Date().toLocaleString();
    });
}
);

document.getElementById('pastMinute').addEventListener('click', () => {
    chrome.browsingData.remove({
        "since": (new Date().getTime() - 60000)
    }, {
        "appcache": true,
        "cache": true,
        "cookies": true,
        "downloads": true,
        "fileSystems": true,
        "formData": true,
        "history": true,
        "indexedDB": true,
        "localStorage": true,
        "pluginData": true,
        "passwords": true,
        "serviceWorkers": true,
        "webSQL": true
    }, () => {
        console.log('Cache Cleared');
        document.getElementById('lastCleared').innerHTML = 'Successfully cleared cache: ' + new Date().toLocaleString();
    });
}
);

function humanReadableDate(date) {
    return date.toLocaleString();
}

function humanReadableTime(date) {
    return date.toLocaleTimeString();
}

function humanReadableDateTime(date) {
    return date.toLocaleString() + ' ' + date.toLocaleTimeString();
}

function humanReadableDateTimeParagraph(date) {
    return 'Successfully cleared cache: ' + humanReadableDateTime(date);
}

// Path: build-a-browser-extension/manifest.json

    