# Chatbot Application

Overview
This chatbot application is designed to interact with users in a friendly and helpful manner. It features an advanced HTML front-end for a seamless user experience and a Python-based Flask backend for processing conversations. The chatbot uses OpenAI's API to generate responses and can also perform additional actions like fetching weather updates.

Features
- **Conversational AI** – Engages in meaningful discussions with users.
- **Advanced Front-End** – Utilizes modern HTML and JavaScript for an interactive UI.
- **Flask Backend** – Handles API requests and response processing.
- **OpenAI Integration** – Generates intelligent responses using OpenAI's API.
- **Utility Functions** – Can perform tasks beyond chatting, such as fetching weather details.

Prerequisites
Before running the chatbot, ensure you have the following installed:
- Python 3.x
- Flask
- OpenAI API key
- Required Python packages (listed in `requirements.txt`)

Installation & Setup
 Clone the Repository
   ```bash
   git clone https://github.com/your-repo/chatbot.git
   cd chatbot
   ```

   Set Up OpenAI API Key
   - Create a file named `openai_key.txt` in the project directory.
   - Copy your OpenAI API key into `openai_key.txt`.

  Run the Flask Application
   ```bash
   python app.py
   ```

Access the Chatbot
   - Open a browser and go to `http://127.0.0.1:5000` to start chatting.

 File Structure
```
chatbot/
│-- static/
│   ├── gifs/  # Folder for GIF files
│-- templates/
│   ├── index.html
│-- app.py
│-- requirements.txt
│-- openai_key.txt  # (User needs to create this file)
```

How It Works
1. **User Input** – The user types a message in the chat UI.
2. **Flask Backend** – The message is sent to the backend via an API call.
3. **OpenAI Processing** – The Flask app retrieves the OpenAI API key, sends the input, and fetches a response.
4. **Dynamic Response** – The response is displayed in the chat interface.
5. **Utility Actions** – If required, the bot can fetch weather updates or perform other actions.

Purpose
This project helps in understanding the basics of OpenAI API integration, Flask-based backend development, and modern front-end design. It serves as a foundation for building more advanced chatbot applications.

Future Enhancements
- Add authentication for secure API usage.
- Integrate database storage for chat history.
- Improve UI with real-time typing indicators.

License
This project is open-source and can be modified or extended as needed.

