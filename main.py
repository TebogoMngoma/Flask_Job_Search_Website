# import flask framework
from flask import Flask, render_template, url_for, request, redirect, jsonify

# we need to initialise the flask app using the variable app with Flask(__name__) function
app = Flask(__name__)

#let's create a json file which contains all job listings
JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Johannesburg',
  'salary': 'R30 000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Johannesburg',
  'salary': 'R100 000'
}, {
  'id': 3,
  'title': 'UX Designer',
  'location': 'Cape town',
  'salary': 'R45 000'
}, {
  'id': 3,
  'title': 'Data Engineer',
  'location': 'Polokwane',
  'salary': 'R10 000'
}]

#all our web pages
index_site = 'index.html'


#every time this website it called , it should run a certain function , hence in this case we return the string "hey babe"
@app.route('/')
def index():
  return render_template(index_site, jobs=JOBS)


# to acces some date like we did above with the jobs json file , we can use an api
@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


# if the variable __name__ has the value __main__ , we have to run the app
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
