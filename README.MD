# Gordon AI - Powered by GPT-4

Gordon AI is an interactive chatbot web application designed for dynamic user interaction. This application leverages OpenAI's GPT-4 model for generating responses, providing enhanced contextual understanding and conversational depth.

With its recent updates, Gordon AI now supports advanced features, including **continuous voice input**, **toggleable text-to-speech**, and an improved user interface for a seamless and intuitive user experience.

---

## **Key Features**

### 🧠 **Powered by GPT-4**
- Enhanced language understanding and response generation.
- Offers nuanced, context-aware answers.

### 🎤 **Continuous Voice Input**
- Users can now enable hands-free operation with continuous speech recognition.
- Automatically restarts listening after each input for uninterrupted interaction.
- A toggle button allows users to start/stop voice input dynamically.

### 🔊 **Toggleable Text-to-Speech**
- Enable or mute audio responses dynamically during the session.
- Visual indicators (🔊 for enabled, 🔇 for muted) enhance usability.

### 💬 **Interactive Chatbox**
- A responsive and aesthetically pleasing chat interface.
- Syntax-highlighted responses for better readability of code outputs.
- Dynamic resizing for chat input.

### 🌐 **Integrated Project Links**
- Includes quick-access links to related tools and resources:
  - Medication Service
  - BGP Monitor
  - GeoIP Lookup
  - ChatGPT Detector
  - Gordon AI Source Code

### 🛠️ **Modern Tech Stack**
- Frontend:
  - **HTML5** and **CSS3** for responsive design.
  - **Bootstrap 5** for styling and layout.
  - **jQuery** for streamlined DOM manipulation.
  - **Highlight.js** for syntax highlighting.
- Backend:
  - Flask for handling server-side logic.
  - Gunicorn for production-ready WSGI HTTP serving.
- OpenAI GPT-4 for intelligent response generation.

---

## **Recent Updates**
### **Version 2.0**
1. **Upgraded LLM Backend**
   - Migrated to OpenAI's **GPT-4** for better conversational quality and depth.
   - Improved API request handling for faster response times.

2. **New Continuous Voice Input Feature**
   - Hands-free interaction with automatic speech recognition.
   - Uses the Web Speech API to continuously listen and process speech input.

3. **Enhanced Audio Output Toggle**
   - Users can toggle text-to-speech output during a session.
   - Clear visual feedback with toggleable buttons.

4. **Improved User Interface**
   - Redesigned chatbox for better readability.
   - Integrated project links for quick navigation to related tools.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/chrisjchandler/GordonAI.git

Note
Gunicorn is only compatible with UNIX-based environments. If you are deploying on a Windows server, you will need to use a different WSGI server that is compatible with Windows.


## Configuration

- You can adjust the `total_tokens` and other parameters in the `app.py` file to customize the behavior of the chatbot.

## Open AI Key
import your open AI key
export OPENAI_API_KEY="your key name here"

You can get one from Openai.com

## Deployment

Use gunicorn instead of flask to allow for remote connections. 


gunicorn -w 4 -t 120 app:app


## License

[MIT License](LICENSE)

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- This project is powered by [OpenAI](https://openai.com/).
- Flask, a Python web framework, is used for the backend implementation.


---

Made with ♥ by [Chris](https://about.me/chrisjchandler)






import your open AI key
export OPENAI_API_KEY="your key name here"
Runs on a flask or gunicorn backend
demo site @ https://msitproject.site
