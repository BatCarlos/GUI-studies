from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/question/', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        return redirect(url_for('drive'))
    return render_template('question.html')

@app.route('/navigation/',  methods=['GET', 'POST'])
def drive():
    return render_template('navigation.html')

# @app.route('/test/', methods=['GET', 'POST'])
# def submit():
#     global data
#     if request.method == 'POST':
#         data = request.form['data']
#         # Process the data from the POST request
#         print(f"Received POST request with data: {data}")
#         return redirect(url_for('drive'))
#     else:
#         return render_template('question.html')

if __name__ == '__main__':
    app.run(debug=True)
