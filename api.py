from flask import Flask, request, jsonify
import plotly.express as px
import pandas as pd

app = Flask(__name__)


@app.route('/generate-graph', methods=["POST"])
def genearte_graph():
    data = request.get_json()

    fig = px.scatter(x=data['x_data'], y=data['y_data'], title = data['graph_title'])

    fig_json = fig.to_json()

    # return data, 200
    return app.response_class(fig_json, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)