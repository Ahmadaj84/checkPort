import urllib3 as u
import csv

"""url = "http://**.**.***.**:****/"
http = u.PoolManager()
r = http.request('GET',url)
print (r.status)
"""



def checkport (port):
  
    add = "http://**.**.***.**:"+port+"/"
    statu = ""
    try:
        http = u.PoolManager().request('POST', add)
        statu = http.status       
    except:
        statu = "no page status"
        
    return statu

temp = []
with open('C:\\****\\******\\*******\\portsOf39.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')    
    for row in csv_reader:
        print (row[0],checkport(row[0]))
        temp.append((row[0],checkport(row[0])))
with open('C:\\****\\******\\*******\\portsOf39x.csv', 'w') as csv_file:
    csv.writer(csv_file).writerows(temp)
    
print ('End of the file')
