from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "CI/CD Pipeline is Working Successfully v2.0 Automation is awesome!"

# Move this OUTSIDE the if __name__ block
@app.route('/health')
def health():
    return {"status": "healthy", "version": "2.0"}, 200

if __name__ == "__main__":
    # app.run must be the VERY LAST line
    app.run(host='0.0.0.0', port=5000)