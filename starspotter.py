import requests, time, threading, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
folder = "C:/Users/oleon/Documents/Python/SkyView"
uri = "https://theskylive.com"

def run(filename, url):
    text = requests.get(url, verify=False).content.__str__()
    n_info = text.count('<div class="keyinfobox"')
    i = 0
    

    with open(filename, "w") as ofile:
        for c in range(n_info):
            x = text.find('<div class="keyinfobox"', i)
            if x == -1: break
            y = text.find('</div>', x)
            clean_version = f"{text[x:(y + 6)]}\n".replace("\\n", "").replace("\\t", "").replace("&#", "")
            ofile.write(clean_version)
            i = y
    return 0

def stars():
    with open(f"{folder}/starspotter.txt", "r") as ifile:
        for counter, line in enumerate(ifile.readlines()):
            spec = 6
            if counter < spec: continue
            # if counter > spec + 5: break
            print(counter, line[:-1])
            new_thread = threading.Thread(target = run, args = (f"{folder}/stars/{counter}.txt", f"{uri}{line[:-1]}"))
            new_thread.start()
            time.sleep(0.2)
        else:
            print("ALL")
    return 1

def main():
    # req_thread = threading.Thread(target = stars)
    # req_thread.start()
    # req_thread.join()

    with open(f"{folder}/starspotter.htm", "w") as ofile:
        ofile.write("<table>")
        for i in range(8500, 8994):
            try: ifile = open(f"{folder}/stars/{i}.txt", "r")
            except FileNotFoundError: print(f"Erro no {i}.txt")
            else:
                ofile.write("<tr>")
                ofile.write(ifile.read().replace("<div", "<td").replace("</div", "</td").replace("<br>", ""))
                ofile.write("</tr>")
                print(i)
        else:
            ofile.write("</table>")
    return 2

if __name__ == "__main__": main()