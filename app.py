from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, I am Victoria Robin, a Data Scientist and AI Automation Specialist!"

@app.route('/status')
def status():
    return {"status": "success", "message": "Docker container is running in Codespaces!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
