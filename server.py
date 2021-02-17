from flask import Flask, render_template,url_for, request, redirect
import csv

app = Flask(__name__)

def write_to_file(data):
    file1 = open('database.txt','a')
    email, subject, message = data['email'], data['subject'], data['message']
    file1.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    file1 = open('database.csv','a',newline='')
    email, subject, message = data['email'], data['subject'], data['message']
    csv_writer = csv.writer(file1,delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database!!'
    else:
        return 'something is wrong!!!'

# import csv

# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})