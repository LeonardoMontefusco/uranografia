import requests, time

if __name__ == "__main__1":
    url = "https://theskylive.com/sky/constellations/"
    body = requests.get(url).content.__str__()
    n = body.count("<a href=")
    a = 0
    for i in range(n):
        a = body.find("<a href=", a)
        b = body.find(">", a)
        uri = body[a + 9:b - 1]
        if uri.count("constellation") > 1 : print(uri)
        a = b

if __name__ == "__main__2":
    url = "https://theskylive.com/sky/constellations/andromeda-constellation"
    body = requests.get(url).content.__str__()
    n = body.count("<a href=")
    a = 0
    for i in range(n):
        a = body.find("<a href=", a)
        b = body.find(">", a)
        uri = body[a + 9:b - 1]
        if uri.count("star") > 1 : print(uri)
        a = b

if __name__ == "__main__3":
    file = open("./uri.txt")
    exit = open("./out.txt", "w")
    for i in range(88):
        uri = file.readline()[:-1]
        body = requests.get(uri).content.__str__()
        time.sleep(0.2)

        n = body.count("<a href=")
        a = 0
        for i in range(n):
            a = body.find("<a href=", a)
            b = body.find(">", a)
            uri = body[a + 9:b - 1]
            if uri.count("star") > 1 : exit.write(uri + "\n")
            a = b
    else:
        file.close()
        exit.close()

if __name__ == "__main__":
    file = open("./stars.txt")
    exit = open("./out.txt", "w")
    for i in range(1755):
        uri = file.readline()[:-1]
        body = requests.get(uri).content.__str__()
        time.sleep(0.2)

        n = body.count("J2000")
        a = body.find("Right Ascension</label>")
        # a = body.find("Right Ascension", a + 10)
        a = body.find("Right Ascension</label>", a + 10)
        b = body.find("</ar>", a)
        exit.write(body[a + 41:b] + "\n")

        a = body.find("<label>Declination</label>", a)
        b = body.find("</ar>", a)
        exit.write(body[a + 42:b - 1] + "\n")
        print(i)
    else:
        file.close()
        exit.close()

if __name__ == "__main__5":
    file = open("./stars.txt")
    exit = open("./out.txt", "w")
    for i in range(1755):
        uri = file.readline()[:-1]
        body = requests.get(uri).content.__str__()
        time.sleep(0.2)

        n = body.count("J2000")
        
        # a = body.find("Spectral Class")
        a = 0
        a = body.find("Magnitude</", a)
        b = body.find("</ar>", a)
        exit.write(body[a + 42:b - 0] + "\n")
        # print(a, b)

        a = body.find("Spectral Type</", a)
        b = body.find("</ar>", a)
        exit.write(body[a + 41:b - 0] + "\n")
        # print(a, b)

        a = body.find("Index (B-V)</", a)
        b = body.find("</ar>", a)
        exit.write(body[a + 39:b] + "\n")
        # print(a, b)
        print(i)
    else:
        file.close()
        exit.close()
