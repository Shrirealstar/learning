function askQuestion() {
    var userInput = document.getElementById("userInput").value;

    // Clear input field
    document.getElementById("userInput").value = '';

    // Append user question to chat box
    var chatBox = document.getElementById("chatBox");
    var userQuestionDiv = document.createElement("div");
    userQuestionDiv.className = "user-question";
    userQuestionDiv.innerHTML = "<strong>You:</strong> " + userInput;
    chatBox.appendChild(userQuestionDiv);

    // Send user question to server and get answer
    fetch('/ask', {
        method: 'POST',
        body: new URLSearchParams({
            'question': userInput
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Append answer to chat box
        var answerDiv = document.createElement("div");
        answerDiv.className = "bot-answer";
        answerDiv.innerHTML = "<strong>Bot:</strong> " + data.answer;
        chatBox.appendChild(answerDiv);

        // Scroll to bottom of chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error('Error:', error));
}
