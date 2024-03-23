from flask import Flask

app = Flask(__name__)

try:
    from controllers import controller
except Exception as e:
        print('Error: {}'.format(e))


