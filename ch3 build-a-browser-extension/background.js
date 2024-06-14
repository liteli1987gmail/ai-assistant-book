/*
服务工作线程用于 Google Chrome 扩展程序
需处理扩展程序安装时的情况
需处理接收到消息时的情况
*/

// When extension is installed
chrome.runtime.onInstalled.addListener(() => {
    console.log('Extension Installed');
});

// When message is received
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log('Message Received');
    console.log(message);
    sendResponse('Message Received');
});


