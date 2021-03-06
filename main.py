__author__ = 'ksanjay'

from flask import Flask, render_template, url_for

app = Flask(__name__) # '__main__'

navbar_lines = [
    {"title": "Home", "id": "Home", "link": "home"},
    {"title": "Work Experience", "id": "Work Experience", "link": "work_experience"}, 
    {"title": "Just for Fun", "id": "Just for Fun", "link": "hobbies"}, 
    # {"title": "Coding Projects", "id": "Coding Projects", "link": "project_home"},
    {"title": "Contact", "id": "Contact", "link": "connect"}
    ]
curr_page = "Home"

projects =[
    {'title': 'Citibike Demand Forecasting', 'synopsis': 'Predict demand for bikes at different citibike stations.', 
        'link': 'simpy', 'section_image':'citibike.jpg'},
    {'title': 'Build a Website', 'synopsis': 'I built this website using jinja 2, flask, and bootstrap.', 
        'link': 'simpy', 'section_image':'webdesign2.jpg'},
    {'title': 'Supply Chain Simulation', 'synopsis': 'Using Simpy to recreate a multiechelon supply chain', 
        'link': 'simpy', 'section_image':'supplychain2.jpg'}
]

exper = [
    {
        'title': 'Manager of Analytical Consulting', 
        'company': "Macy's", 
        'timeline': "May 2018-Present",
        'bullets': ["Created a python Simpy simulator to test various Hold and Flow strategies for Macy's supply chain, creating a Proof of Concept and an estimated sales lift of 15% for the inventory strategy", 
                    "Developed a python data pipeline that estimates Average Rate of Sale for each product in Hold and Flow, and then supplies units to stores to avoid stock outs and maximize probability of selling each unit, resulting in a margin increase of 10% for over 40,000 units of product and a profit of over 150,000 dollars in 8 weeks",
                    "Created a Tableau dashboard to show how algorithm was making decisions on where to place the units"
                    ],
        'display_pics': True,
        'pics': ['macys_1.jpg', 'macys_2.jpg']
    },
    {
        'title': 'Marketing Consultant Intern', 
        'company': "IBM", 
        'timeline': "May 2017-August 2017",
        'bullets': ["Streamlined IBM's translation process to 23 languages in order to capitalize on markets with the highest opportunity for IBM, resulting in an estimated 57 thousand additional engaged visits of webpages valued at over 11 million dollars", 
                    "Synthesized language expert interviews with regression analysis of language factors to provide IBM marketing executives with three markets to begin website translation and 15 languages to stop translation",
                    "Developed a regression model using Excel and SPSS to locate variables that explain engaged visits with IBM content in a specific language, identifying key markets where translation was not adding value to IBM's web presence"
                    ],
        'display_pics': True,
        'pics': ['IBM_1.jpg']
    }
]

@app.route('/')
def home():
    curr_page = "Home"
    return render_template('home.html', curr_page=curr_page, navbar_lines = navbar_lines)

@app.route('/connect.html')
def connect():
    curr_page = "Contact"
    return render_template('connect.html', curr_page=curr_page, navbar_lines = navbar_lines)

@app.route('/projects.html')
def project_home():
    curr_page = "Coding Projects"
    return render_template('/project_home.html', projects=projects, curr_page=curr_page, navbar_lines = navbar_lines)

@app.route('/work_experience.html')
def work_experience():
    curr_page = "Work Experience"
    return render_template('/work_experience.html', df=exper, curr_page=curr_page, navbar_lines = navbar_lines)

@app.route('/projects/<project>')
def project_page(project):
    curr_page = "Projects"
    return render_template('/projects/{}.html'.format(project), curr_page=curr_page, navbar_lines = navbar_lines)

@app.route('/hobbies.html')
def hobbies():
    curr_page = "Just for Fun"
    return render_template('/hobbies.html', df=exper, curr_page=curr_page, navbar_lines = navbar_lines)


if __name__ == '__main__':
    app.run(port=4995)