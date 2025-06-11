from flask import Flask,render_template, request, redirect, url_for, session

# 객체생성
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        
        # 리다이렉트 success 표시
        session['success'] = True
        return redirect(url_for('contact'))
    # get요청시 success 표시 후 초기화
    success = session.pop('success', False)
    return render_template('contact.html', success=success)


if __name__ == '__main__':
    app.run(debug=True)