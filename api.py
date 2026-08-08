from flask import Flask, request, jsonify
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/generate-graph', methods=["POST"])
def generate_graph():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON."}), 400
    
    # Check to make sure all properties were included
    if "x_data" in data and "y_data" in data and "graph_title" in data:

        # To prevent plotly error
        if len(data["x_data"]) == len(data["y_data"]):

            # Empty graph no point
            if len(data["x_data"]) > 0:
                fig = px.scatter(x=data['x_data'], y=data['y_data'], title = data['graph_title'])
                fig_json = fig.to_json()

                return app.response_class(fig_json, mimetype="application/json"), 200

            else:
                return jsonify({"error":"Bad Request: No points for data."}), 400
                
        else:
            return jsonify({"error":"Bad Request: X and Y data length mismatch."}), 400

    else:
        return jsonify({"error":"Bad Request: Missing x data, y data, or title."}), 400

if __name__ == '__main__':
    app.run(debug=True)