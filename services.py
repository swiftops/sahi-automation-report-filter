from flask import Flask, request
from filterUtil import getSahiReportURL
from logger_util import get_logger

app = Flask(__name__)
logger = get_logger()


@app.route("/sahifailedresult", methods=['POST'])
def _sahi_filter():
    request_values = request.json
    data = getSahiReportURL(request_values)
    return data


if __name__ == "__main__":
    app.run('0.0.0.0', port=7778, debug=True)

