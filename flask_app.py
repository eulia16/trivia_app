from flask import Flask
import trivia_requests

app = Flask(__name__)

# we will create a home landing page, that will not return any real functionality

# we will create a few endpoints, each returning separate, yet similar functionalities
# such as a random question, 5 random questions, or 10 random questions, and maybe some
# more endpoints as needed, for now probably just those 3 though

@app.route('/home', methods = ['GET', 'POST'])
def home_page():
    return "this will be the home page"#maybe add a render template html flask thing here

@app.route('/random/single_question', methods=['GET','POST'])
def single_random_question():
    return trivia_requests.send_request(1)

@app.route('/random/multiple_questions/<int:num>')
def multiple_random_questions(num):
    return trivia_requests.send_request(num)

    #return str(num+5)



# return trivia_requests.send_request(5)


if __name__ == '__main__':
    # in debug mode now
    app.run(debug = True, port = 5000)