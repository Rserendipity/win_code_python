from urllib.request  import urlretrieve

file = open("./1.txt", "r")


url = file.readlines()

cnt = 1

for i in url:
    urlretrieve(i, "./pic/" + str(cnt) + ".jpg")
    cnt += 1
