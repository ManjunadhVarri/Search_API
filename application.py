from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load videos from the JSON file
with open('data/DataSet.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    videos = data.get('results', [])  # Get the list of videos or an empty list if 'results' key is not present

@app.route('/search', methods=['GET'])
def search_videos():
    if len(request.args) == 0:  # If no parameters are provided in the URL
        return jsonify(videos)
    else:
        # Get search parameters from the request
        title_query = request.args.get('title', '').lower()
        genre_ids_query = request.args.getlist('genre_ids')
        description_query = request.args.get('description', '').lower()

        # Convert genre_ids_query to integers
        genre_ids_query = [int(genre_id) for genre_id in genre_ids_query]

        # Filter videos based on search parameters
        results = []
        for video in videos:
            title_match = title_query in video['title'].lower() if title_query else False
            genre_ids_match = any(genre_id in video.get('genre_ids', []) for genre_id in genre_ids_query) if genre_ids_query else False
            description_match = description_query in video.get('overview', '').lower() if description_query else False

            if title_match or genre_ids_match or description_match:
                results.append(video)

        return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)