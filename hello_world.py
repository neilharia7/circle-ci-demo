from flask import Flask

app = Flask(__name__)


def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:80px;'>
            <center>
                <image height="563" width="426" src="https://i.pinimg.com/564x/1a/04/21/1a04212aaf419b8951ddb4ab434589bd.jpg">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html


@app.route('/')
def hello_world():
    message = 'Bella Caio!'
    html = wrap_html(message)
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7001)
