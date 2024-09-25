from flask import Flask, render_template, request, jsonify
from code_explanation.main import explain_code, save_feedback
import traceback
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.debug("Request received: %s", request.method)
    if request.method == 'POST':
        try:
            data = request.get_json()
            app.logger.debug("Received data: %s", data)
            code = data['code']
            explanation = explain_code(code)
            app.logger.debug("Explanation generated: %s", explanation)
            return jsonify({'explanation': explanation})
        except Exception as e:
            app.logger.error("An error occurred: %s", str(e))
            app.logger.error(traceback.format_exc())
            return jsonify({'error': str(e)}), 500
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        data = request.json
        save_feedback(data['code'], data['explanation'], data['rating'], data['comment'])
        return jsonify({'message': 'Feedback saved successfully'})
    except Exception as e:
        app.logger.error("An error occurred while saving feedback: %s", str(e))
        app.logger.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)