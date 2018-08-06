from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<int:num_1>/<int:num_2>')
def show_post(num_1, num_2):
    ans = num_1*num_2
    return '%d' % ans


@app.errorhandler(404)
def page_not_found(error):
    return 'only int is accepted'
