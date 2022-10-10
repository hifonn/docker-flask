from flask import render_template,request,redirect,url_for, flash
from app import app 
#表示部分の作成

@app.route('/')
def index():
        return render_template('/index.html')