import requests,json
from datetime import date
import configuration
import uuid  
 
headers = {
       "Authorization": "Bearer " + configuration.notion_token,
       "accept": "application/json",
       "Notion-Version": "2022-06-28",
       "content-type": "application/json"
    }
  
def readDatabase(headers):
    
    readUrl = f"https://api.notion.com/v1/databases/{configuration.databaseId}/query"
    
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    # DS return users_data=[
    # user_data={
    # keys:values}]
    users_data=[]
    records=data["results"]
    today = date.today()
  
     
    for record in records:
        record_date=record["properties"].get("Order Date").get("date")
        user_data={}
        if record_date is not None:
            if str(today)==str(record_date.get("start")):
                for key, value in record["properties"].items():
                    if value.get("type")=="rich_text" and value.get("rich_text"):
                        user_data[key]=value.get("rich_text")[0].get("text").get("content")
                    elif value.get("type")=="date" and value.get("date") is not None:
                        user_data[key]=value.get("date").get("start")
                    elif value.get("type")=="title" and value.get("title"): 
                        user_data[key]=value.get("title")[0].get("text").get("content")
                    elif value.get("type")=="phone_number" and value.get("phone_number") is not None:     
                        user_data[key]=value.get("phone_number")
                    elif value.get("type")=="select" and value.get("select") is not None:     
                        user_data[key]=value.get("select").get("name")
                    elif value.get("type")=="multi_select" and value.get("multi_select"):
                        user_data[key]=value.get("multi_select")[0].get("name")
                    elif value.get("type")=="checkbox":
                        user_data[key]=value.get("checkbox")
                    elif value.get("type")=="email" and value.get("email") is not None:
                        user_data[key]=value.get("email")
                    elif value.get("type")=="number" and value.get("number") is not None:
                        user_data[key]=value.get("number")    
                    elif value.get("type")=="status" and value.get("status") is not None:
                        user_data[key]=value.get("status").get("name")
                    elif value.get("type")=="url" and value.get("url") is not None:
                        user_data[key]=value.get("url")     
                users_data.append(user_data) 
        
    return  users_data

def get_data():
    form_data=readDatabase(headers)
    print(form_data)
    return form_data 

# get_data()