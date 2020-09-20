from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)  # instantiate app
'''
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject},{message}')

'''

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save!'
    else:
        return "Error submitting form."

@app.route('/favicon.ico')
def favicon_page():
    return render_template('favicon.html')

# Note, to use debug mode: enter at terminal:  export FLASK_ENV=development
# To simply run the server, enter at terminal:  export FLASK_APP=hello.py
# To start server, enter:  flask run
