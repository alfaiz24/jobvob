from flask import Flask, render_template

app = Flask(__name__)




JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
     'location' : 'Delhi, India',
     'salary': 'Rs.3,50,000'
  },
  {
   'id': 2, 
   'title': 'Data Scientist',
   'location': 'Indore, India' ,
   'salary': 'Rs.4,50,000'
  },
  {
   'id': 3, 
   'title': 'Frontend Develoer',
   'location': 'Jaipr, India',
   'salary': 'Rs.5,00,000'
  },
  {
   'id': 4, 
   'title': 'Backend Develoer' ,
   'location': 'Delhi, India',
   'salary': 'Rs.3,70,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)



if __name__ == "__main__":
  app.run(host= '0.0.0.0', debug=True)  

    

