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
root.geometry("400x400")import requests
import json
from urllib import request
from tkinter import *
from PIL import ImageTk
from PIL import Image
import pickle
import os

global label1,imagephoto,imagephoto2
global txt_detalie, txtbox, client_secret, HEADERS, origin, data_location, image_location

data_location = './data/'
image_location = './image/'

client_secret = "428d72e8d59140d89a4d9e4ee234e10f"
HEADERS = {"X-API-Key": client_secret}
origin = 'https://www.bungie.net'

#폴더랑 기본파일 확인용, ddd.json 확인....

root = Tk()
root.title("데스티니 2")
root.geometry("400x400")
#프레임/윈도우/창 크기 조절 허용 여부
root.resizable(False, False)
root.iconbitmap(data_location+"destiny-2.ico")

def btndef():
    global names
    print(txtbox.get())
    names = findhash()

    #txt_detalie.insert(END,find_hash)
    #name.clear()
    return

def findhash():
    gettxt = txtbox.get()
    list1.delete(0,END)
    ss = '/Platform/Destiny2/Armory/Search/DestinyInventoryItemDefinition/'+gettxt+'?lc=ko'
    r = requests.get(origin + ss, headers=HEADERS);
    print(r.json())
    touch = r.json()

    with open('./data/touch.pickle','wb') as fw:
        pickle.dump(touch, fw)

    totalResult = touch.get("Response").get("results").get("totalResults")
    name = [0] * totalResult
    for i in range(totalResult):
        name[i] = touch.get("Response").get("results").get("results")[i].get("displayProperties").get("name")
    for ii in range(totalResult):
        list1.insert(ii,name[ii])
    return name

def findinformation():
    anchor = list1.get(ANCHOR)
    in_to = int(names.index(anchor))

    with open('./data/touch.pickle','rb') as f:
        data = pickle.load(f)

    getyou = data.get("Response").get("results").get("results")[in_to].get("hash")
    print(getyou)
    ss = '/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/'+ str(getyou) +'?lc=ko'
    r = requests.get(origin + ss, headers=HEADERS);
    rjson = r.json()
    print(rjson)
    image_upload = rjson.get("Response").get("displayProperties").get("icon")
    phtoimage_down(image_upload)
    phtoimage_setup()


def phtoimage_down(urldown):
    #os.system("curl " + origin +urldown + " > "+data_location+"icons2.jpg")
    request.urlretrieve(origin+urldown,data_location+'icons2.jpg')
    return

def phtoimage_setup():
    image_change = ImageTk.PhotoImage(Image.open(data_location+"icons2.jpg"))
    label1.config(image=image_change)
    label1.image = image_change


def scaled(event):
    print()
    #label1.configure(image=imagephoto2)

imagephoto = ImageTk.PhotoImage(Image.open(data_location+"main.jpg"))
label1 = Label(root, image=imagephoto)
txtbox = Entry(root, width=20)
txtbox.insert(END, "내일")
btn1 = Button(root, text="검색", command=btndef)
#txt_detalie = Text(root, width=30, height=10)
list1 = Listbox(root, selectmode='extended',height=0)
btn2 = Button(root, text="검색", command=findinformation)

#label1.bind("<Button-1>",scaled)

if __name__ == "__main__":
    txtbox.pack()
    btn1.pack()
    #txt_detalie.pack()
    list1.pack()
    btn2.pack()
    label1.pack()
    root.mainloop()
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
