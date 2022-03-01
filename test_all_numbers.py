import urllib.request

#weburl = urllib.request.urlopen('http://localhost:8080/romannumeral?query=50')
#data = weburl.read()
#print(data)
#weburl = urllib.request.urlopen('http://localhost:8080/romannumeral?query=10')
#data = weburl.read()
#print(data)
#i = 1
#str(i)
#weburl = urllib.request.urlopen('http://localhost:8080/romannumeral?query='+str(i))
#data = weburl.read()
#print(data)
i = 1
while(i < 256): # same concept as test_1_number.py but for all the numebrs in the range
    weburl = urllib.request.urlopen('http://localhost:8080/romannumeral?query='+str(i))
    data = weburl.read()
    print(data)
    i +=1


