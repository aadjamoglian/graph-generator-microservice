from flask import Flask, request, jsonify
import plotly.express as px
import pandas as pd

app = Flask(__name__)


@app.route('/generate-graph', methods=["POST"])
def genearte_graph():
    data = request.get_json()

    if "x_data" in data and "y_data" in data and "graph_title" in data:
        if len(data["x_data"]) == len(data["x_data"]):
            if len(data["x_data"]) > 0:
                fig = px.scatter(x=data['x_data'], y=data['y_data'], title = data['graph_title'])

                fig_json = fig.to_json()

                # return data, 200
                return app.response_class(fig_json, mimetype="application/json"), 200
            else:
                return "Bad Request: No points for data.", 401
        else:
            return "Bad Request: X and Y data length mismatch.", 401

    else:
        return "Bad Request: Missing x data, y data, or title.", 401

if __name__ == '__main__':
    app.run(debug=True)