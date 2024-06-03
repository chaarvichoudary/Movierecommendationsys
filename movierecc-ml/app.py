from flask import Flask, request, jsonify, render_template, redirect, url_for
from movie_recommendation_system import get_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id'))
    num_recommendations = int(request.args.get('num_recommendations', 5))
    recommendations = get_recommendations(user_id, num_recommendations)
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return jsonify(recommendations)
    else:
        return render_template('recommendations.html', user_id=user_id, recommendations=recommendations)

@app.route('/submit', methods=['POST'])
def submit():
    user_id = int(request.form['user_id'])
    return redirect(url_for('recommend', user_id=user_id))

from flask import Flask

app = Flask(__name__)

# Your Flask routes and other application setup code here...

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

