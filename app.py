from db import app

@app.route('/')
def check():
    return 'Flask is working!'

if __name__ == '__main__':
    app.run(debug=True)