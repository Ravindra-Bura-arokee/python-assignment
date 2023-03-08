from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['python']
print("Connection Successful")
# print("List of databases")
# print(client.list_database_names())
client.close()