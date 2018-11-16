from flask import Flask
from containers import getcontainers,containersToTable
from socketfinder import getlocalcidr

app = Flask(__name__)
@app.route("/")
def hello():
    containers = getcontainers()
    print(containers)
    output = "<html><body>{}</body></html>".format(containersToTable(containers))
    return output

if __name__ == '__main__':
    ip, _ = getlocalcidr()
    app.run(host=ip)
