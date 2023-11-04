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


def userinformation(userid): # Retrieve additional details about the user
    response = requests.get(f"https://users.roblox.com/v1/users/{userid}", headers=headers)

    if response.ok:
        content = response.json()
        
        username = content["name"]
        displayname = content["displayName"]
        isbanned = content["isBanned"]
        joindate = content["created"]
        hasVerifiedBadge = content["hasVerifiedBadge"]
        accountstatus = ""
        verified_developer = ""
        display_message = ""

        if not hasVerifiedBadge:
            verified_developer = "not"
        
        if not isbanned:
            accountstatus = "not"

        if displayname == username:
            display_message = "And also it seems like you didn't set a displayname yet.."
        else:
            display_message = f"And also I know your displayname is {displayname}"

        toconclude = f"Hello {username}, how dare you? I know you were starting to play roblox back in {joindate[:4]}, and I know your account is {accountstatus} banned, and also you are {verified_developer} a verified dev., {display_message}"

        print(toconclude)



def categories(): # Many people have asked about the names of all the Roblox categories, so here's your answer.
    response = requests.get("https://catalog.roblox.com/v1/categories", headers=headers)

    if response.ok:
        content = response.json()
        categories = ", ".join(x for x in content)
    else:
        print("Encountering Error, with status code", response.status_code)
    print(f"The categories are: {categories}, \n\n have a great day.")


# * ------ How can we use the functions? ------


# getusername(userid_here) -- to call this function, you simply set the argument "userid_here".
# userinformation(userid_here) -- to call this function, you simply set the argument "userid_here".
# categories() -- to call this function, you simply just need to define the function somewhere, without any additionals parameters.


# * ------ Arguments details ------

# "userid_here" stands for the roblox roblox user ID
# "limit_number" The number of the details results.
