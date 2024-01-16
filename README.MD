# Chatbot Implementation using Flask and OpenAI's GPT-3.5-turbo

This repository contains a simple yet powerful chatbot implementation using Flask, a popular web framework in Python, and OpenAI's GPT-3.5-turbo model. The chatbot is designed to provide conversational interactions, leveraging the advanced natural language processing capabilities of GPT-3.5-turbo.

## Features

- Flask-based web application.
- Integration with OpenAI's GPT-3.5-turbo for generating conversational responses.
- Interactive chat interface.

## Requirements

- Python 3.6 or higher.
- Flask
- Requests library
- Access to OpenAI's API.

## Installation

1. Clone the repository:
git clone https://github.com/your-username/your-repository.git
cd your-repository

pip install Flask requests

3. Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY='your-api-key'
(get one for free from openai)


## Running the Chatbot in Flask locally for testing

1. Start the Flask server:
python app.py
2. Open your web browser and navigate to `http://localhost:5000`.

3. Start interacting with the chatbot through the web interface.

## Running the Chatbot in Gunicorn for production

For production deployment, it is recommended to use a more robust WSGI server like Gunicorn. Gunicorn is a pre-fork worker model server that is designed to serve various web applications including Flask. It is particularly advantageous for handling multiple simultaneous requests, which is a common scenario in a production environment.

### Installing Gunicorn

You can install Gunicorn via pip:

```bash
pip install gunicorn

Running the Application with Gunicorn
Once Gunicorn is installed, you can start your Flask application with it. For example:
gunicorn -w 4 -b 127.0.0.1:8000 app:app

In this command:

-w 4 means that Gunicorn will use 4 worker processes for handling requests.
-b 127.0.0.1:8000 binds Gunicorn to listen on localhost at port 8000.
app:app tells Gunicorn to load the app module and use the app callable within that module to start the Flask application.
Using Gunicorn can significantly improve your application's performance and reliability in production. It's also compatible with various deployment environments, including both traditional servers and container-based environments.

Note
Gunicorn is only compatible with UNIX-based environments. If you are deploying on a Windows server, you will need to use a different WSGI server that is compatible with Windows.


## Configuration

- You can adjust the `total_tokens` and other parameters in the `app.py` file to customize the behavior of the chatbot.

## License

[MIT License](LICENSE)

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- This project is powered by [OpenAI](https://openai.com/).
- Flask, a Python web framework, is used for the backend implementation.

## Contact

For any queries or suggestions, please contact [Your Name](mailto:your-email@example.com).

---

Made with ♥ by [Chris](https://riotdoor.com)






import your open AI key
export OPENAI_API_KEY="your key name here"
Runs on a flask or gunicorn backend
demo site @ http://gordon.msitproject.site
