import urllib.request
value = input("Please enter an integer: \n") # input the number to test
weburl = urllib.request.urlopen('http://localhost:8080/romannumeral?query='+str(value)) # run the URL queru
data = weburl.read() #Read the data
print(data) # print the data

