from flask import Flask, request, Response, sessions

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def jupyter_lab():
    return Response('"Hello JupyterLab"', mimetype='application/json', status=200)


if __name__ == '__main__':
    port = 8080
    hostname = '0.0.0.0'
    app.run(host=hostname, port=port)
