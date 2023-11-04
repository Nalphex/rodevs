import requests

# definition

headers = {"Content-Type": "application/json; charset=utf-8"}
main_userid = 12345678 # replace it with your own roblox userid



def getusername(userid): # How do I convert any Roblox user ID to its own username?

    response = requests.get(f"https://users.roblox.com/v1/users/{userid}", headers=headers)
    
    if response.ok:
        content = response.json()
        username = content["name"]
    else:
        print("Encountering Error, with status code", response.status_code)
    return username

def oldusernames(userid, limitnumber): # How do we actually retrieve our old Roblox usernames?, Here is your answer.
    username = getusername(userid)
    response = requests.get(f"https://users.roblox.com/v1/users/{userid}/username-history?limit={limitnumber}&sortOrder=Asc", headers={"Content-Type": "application/json; charset=utf-8"})

    print(response.status_code)
    if response.ok:
        content = response.json()
        usernames = ", ".join([x['name'] for x in content['data']])

        print(f"Hello {username}, okay so here are the past usernames that u had, {usernames}")



def gamesdetails(userid, limit): # This is how can we fetch our game details: eg gameid, game_name


    response = requests.get(f"https://games.roblox.com/v2/users/{userid}/games?accessFilter=2&limit={limit}&sortOrder=Asc", headers=headers)

    gamesinfo = {}

    if response.ok:
        content = response.json()

        for game in content['data']:
            gamesinfo[f"{game['name']}"] = game['id']
    else:
        print("Encountering Error, with status code", response.status_code)
    print(gamesinfo)
    return gamesinfo


# * ------ How can we use the functions? ------


# getusername(userid_here) -- to call this function, you simply set the argument "userid_here".
# oldusernames(userid_here, limit_number) - to call this function, you have to call it within 2 arguments, the arguments are "userid_here", "limit_number".
# gamesdetails(userid_here, limit_number) -to call this function, you have to call it within 2 arguments, the arguments are "userid_here", "limit_number".


# * ------ Arguments details ------

# "userid_here" stands for the roblox roblox user ID
# "limit_number" The number of the details results.

