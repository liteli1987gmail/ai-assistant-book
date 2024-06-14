document.getElementById('input-box').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        let question = this.value;
        this.value = '';
        document.getElementById('chat-window').innerHTML += 'You: ' + question + '<br>';
        fetch('/get_answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({question: question}),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('chat-window').innerHTML += 'Bot: ' + data.answer + '<br>';
        });
    }
});

document.getElementById('clear-button').addEventListener('click', function() {
    document.getElementById('chat-window').innerHTML = '';
});