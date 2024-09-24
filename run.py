from flask import Flask, render_template, request, jsonify
from code_explanation.main import explain_code, save_feedback

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        explanation = explain_code(code)
        return jsonify({'explanation': explanation})
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    save_feedback(data['code'], data['explanation'], data['rating'], data['comment'])
    return jsonify({'message': 'Feedback saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)