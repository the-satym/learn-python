import json

jsonfile=open("data.json",'r+')

data=(json.load(jsonfile))
userlist = data["users"]

user_name = {user["id"]: user["name"] for user in userlist}

for user in userlist:
    user['friends'] = [user_name[friendid] for friendid in user["friends"] ]
    print(f'id:{user["id"]} name: {user["name"]} friends: {user["friends"]}')