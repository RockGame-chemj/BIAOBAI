from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 存储表白数据
love_data = {
    'name': '',
    'message': ''
}

@app.route('/')
def index():
    return redirect(url_for('a_side'))

@app.route('/a', methods=['GET', 'POST'])
def a_side():
    if request.method == 'POST':
        love_data['name'] = request.form.get('name', '').strip()
        love_data['message'] = request.form.get('message', '').strip()
        return redirect(url_for('a_success'))
    return render_template('a_side.html')

@app.route('/a/success')
def a_success():
    return render_template('a_success.html', name=love_data['name'])

@app.route('/b', methods=['GET', 'POST'])
def b_side():
    if request.method == 'POST':
        input_name = request.form.get('name', '').strip()
        if input_name.lower() == love_data['name'].lower():
            return redirect(url_for('love_page'))
        else:
            return render_template('b_side.html', error="名字不匹配，请再试一次")
    return render_template('b_side.html')

@app.route('/love')
def love_page():
    if not love_data['name']:
        return redirect(url_for('b_side'))
    return render_template('love.html', name=love_data['name'], message=love_data['message'])

if __name__ == '__main__':
    app.run(debug=True)