
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

item_similarity_df = pd.read_csv("movie_similarity.csv", index_col=0)

app = Flask(__name__)
CORS(app)

@app.route("/recms", methods = ["POST"])
def make_rec():
  if request.method == "POST":
        data = request.json
        movie = data["movie_title"]
        try: 
            similar_score = item_similarity_df[movie]
            similar_movies = similar_score.sort_values(ascending=False)[1:10]
            api_recommendations = similar_movies.index.to_list()
        except:
            api_recommendations = ['Movie not found']
        return {"rec_movie":api_recommendations}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)