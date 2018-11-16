import podman


def getcontainers():
    with podman.Client() as client:
        return client.containers.list()

def containersToTable(containers):
    output = "<table border=1><tr>"
    ctr = 0
    for i in containers:
        print(i)
        if ctr % 5 == 0:
            output += "</tr><tr>"
        color = "green"
        if i.status != "running":
            color = "blue"
        output += "<td align='center'><img src='static/{}.png'><br>{}</td>".format(color, i.names)
        ctr = ctr +1
    output += "</tr></table>"
    return output
