import requests
import json
import codecs
from tkinter import *
from PIL import ImageTk
from PIL import Image
import os

global label1
global txt_detalie, txtbox
name = [0]*4

root = Tk()
root.title("데스티니 2")
root.geometry("400x400")
#프레임/윈도우/창 크기 조절 허용 여부
root.resizable(False, False)


def btndef():
    print(txtbox.get())
    find_hash = str(findhash())
    txt_detalie.insert(END,find_hash)
    name.clear()
    return

def findhash():
    client_secret = "428d72e8d59140d89a4d9e4ee234e10f"
    HEADERS = {"X-API-Key": client_secret}
    origin = 'https://www.bungie.net'
    gettxt = txtbox.get()
    ss = '/Platform/Destiny2/Armory/Search/DestinyInventoryItemDefinition/'+gettxt+'?lc=ko'
    r = requests.get(origin + ss, headers=HEADERS);
    print(r.json())
    touch = r.json()
    totalResult = touch.get("Response").get("results").get("totalResults")
    name = [0] * totalResult
    for i in range(totalResult):
        name[i] = touch.get("Response").get("results").get("results")[i].get("displayProperties").get("name")
        print(i)
    return name

def phtoimagedown():
    urldown = "https://www.bungie.net/common/destiny2_content/icons/e2f9671a1864e407537c229c6c3a0d3a.jpg"
    os.system("curl " + urldown + " > icons.jpg")




if __name__ == "__main__":
    imagephoto = ImageTk.PhotoImage(Image.open("icons.jpg"))
    label1 = Label(root, image=imagephoto)
    txtbox = Entry(root, width=20)
    txtbox.insert(END, "회문")
    txt_detalie = Text(root, width=30, height=10)
    btn1 = Button(root, text="검색", command=btndef)

    label1.pack()
    txtbox.pack()
    btn1.pack()
    txt_detalie.pack()

    while TRUE:
        root.mainloop()
