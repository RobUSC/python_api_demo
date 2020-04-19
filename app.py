from flask import Flask
from service.HelloWorldService import HelloWorldService

app = Flask(__name__)


@app.route('/')
def hello_world(self):
    return hello_world()


if __name__ == '__main__':
    app.run()
