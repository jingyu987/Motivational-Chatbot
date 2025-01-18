import React, { useState, useRef, useEffect } from 'react';
import './global.css';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  // Ref for the chat box
  const chatBoxRef = useRef(null);

  const handleSend = () => {
    if (input.trim() === '') return;

    // Add user's message
    setMessages((prev) => [...prev, { sender: 'user', text: input }]);

    // Mock bot response
    const botResponse = "That's a great point! Keep going!";
    setMessages((prev) => [...prev, { sender: 'bot', text: botResponse }]);

    setInput(''); // Clear the input
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault(); // Prevent default Enter behavior
      handleSend();
    }
  };

  // Automatically scroll to the bottom when messages update
  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="chat-container">
      <div className="chat-box" ref={chatBoxRef}>
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.sender === 'user' ? 'user-message' : 'bot-message'}`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
          autoFocus
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default Chat;
