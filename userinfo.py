import requests
import json
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='userinfodb')
except mysql.connector.Error as e:
    print("db connection error",e)
mycursor=mydb.cursor()
data=requests.get("https://reqres.in/api/users?page=1").text
data_info=json.loads(data)
for j in data_info['data']:
    try:
        #sql='INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ("'+j['API']+'","'+j['Description']+'","'+j['Auth']+'","'+http+'","'+j['Cors']+'","'+j['Link']+'","'+j['Category']+'")'
        #sql="INSERT INTO `papi`(`api`, `description`, `auth`, `https`, `cors`, `link`, `category`) VALUES ('"+j['API']+"','"+j['Description']+"','"+j['Auth']+"','"+http+"','"+j['Cors']+"','"+j['Link']+"','"+j['Category']+"')"
        sql="INSERT INTO `userinfo`(`email`, `firstname`, `lastname`) VALUES  (%s,%s,%s)"
        data=(j['email'],j['first_name'],j['last_name'])
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully",j['first_name'])
    except mysql.connector.Error as e:
        print("error is",e)
    

        