from flask import Flask, redirect, render_template, redirect, request
import os,sys
from formregistry import *
app=Flask(__name__)



@app.route("/", methods=['POST','GET'])
def homepage():
	return render_template("home.html", name="Home", nav1='Members', nav2='SMEs', nav3='Corporates', nav4='News', nav5='Articles', nav6='Tenders')

@app.route ("/Home", methods=['POST','GET'])
def mtaa():
	return redirect("./")

@app.route ("/signup", methods=['POST','GET'])
def signup():
	form=RegisterForm(request.form)
	if request.method=="POST" and form.validate():
		return render_template("signup.html")
	signup_message='Join the club!'
	return render_template("signup.html", form=form, form_message=signup_message, name='Sign Up')

@app.route ("/login", methods=['POST','GET'])
def login():
	form=LoginForm(request.form)
	if request.method=="POST" and form.validate():
		return render_template("login.html")
	login_message='Welcome Back!'
	return render_template("login.html", form=form, form_message=login_message, name ='Log in')

@app.route ("/forgotpassword", methods=['POST','GET'])
def forgotpassword():
	form=ForgotPasswordForm(request.form)
	if request.method=="POST" and form.validate():
		return render_template("forgotpassword.html")
	forgotpassword_message='Say no more'  
	return render_template("forgotpassword.html", form=form, form_message=forgotpassword_message, name='Recover Password')

@app.route("/about",  methods=['POST','GET'])
def aboutpage():
	return render_template("about.html", abouttext=aboutstories)

@app.route("/members",  methods=['POST','GET'])
def memberspage():
	membersstories= []
	with open(os.path.join(sys.path[0], "textmembers.txt"), encoding="utf8") as file:
		for line in file:
			line = line.strip() #or some other preprocessing
			membersstories.append(line)
			print (membersstories)
	name="Members"
	return render_template("members.html", memberstext=membersstories, name=name, nav1='Groups', nav2='Notices', nav3='Chat Forums', nav4='Events', nav5='Profiles', nav6='Notifications')

@app.route("/smes",  methods=['POST','GET'])
def smespage():
	smesstories= []
	with open(os.path.join(sys.path[0], "textsme.txt"), encoding="utf8") as file:
		for line in file:
			line = line.strip() #or some other preprocessing
			smesstories.append(line)
			print (smesstories)
	name="SMEs"
	return render_template("smes.html", smestext=smesstories, name=name, nav1='Get Market Data', nav2='Seek Financing', nav3='Legal Aid', nav4='Events', nav5='Downloads', nav6='Collaborations')


@app.route("/corporates",  methods=['POST','GET'])
def corporatespage():
	corporatesstories=[]
	with open(os.path.join(sys.path[0], "textcorporates.txt"), encoding="utf8") as file:
		for line in file:
			line = line.strip() #or some other preprocessing
			corporatesstories.append(line)
			print (corporatesstories)
	name="Corporates"
	return render_template("corporates.html", corporatestext=corporatesstories, name=name, nav1='Get Market Data', nav2='Financing', nav3='Work Postings', nav4='Events', nav5='Downloads', nav6='Collaborations')


@app.route("/articles",  methods=['POST','GET'])
def articlespage():
	articlesstories=[]
	with open(os.path.join(sys.path[0], "textarticles.txt"), encoding="utf8") as file:
		for line in file:
			line = line.strip() #or some other preprocessing
			articlesstories.append(line)
			print (articlesstories)
	name="Articles"
	return render_template("articles.html", articlestext=articlesstories, name=name, nav1='My Hustle', nav2='Politics', nav3='Industry', nav4='Family & Living', nav5='Health and Fitness', nav6='Motivation')


@app.route("/tenders",  methods=['POST','GET'])
def tenderspage():
	tendersstories=[]
	with open(os.path.join(sys.path[0], "texttenders.txt"), encoding="utf8") as file:
		for line in file:
			line = line.strip() #or some other preprocessing
			tendersstories.append(line)
			print (tendersstories)
	name="Tenders"
	return render_template("tenders.html", tenderstext=tendersstories, name=name, nav1='Postings', nav2='LPO Financing', nav3='Legal Aid', nav4='Institutional Contractors', nav5='Shortlisted', nav6='Prequalify')

@app.route("/news",  methods=['POST','GET'])
def newspage():
	newsstories=[]
	with open(os.path.join(sys.path[0], "textnews.txt"), encoding="utf8") as file:
		for line in file:
			line = line.strip() #or some other preprocessing
			newsstories.append(line)
			print (newsstories)
	name="News"
	return render_template("news.html", newstext=newsstories, name=name, nav1='Business', nav2='Industry', nav3='Politics', nav4='Women in Business', nav5='Africa', nav6='Global')

if __name__=="__main__":
	app.run(debug=True, port=5000)
