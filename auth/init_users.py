from user_docs import *

def init_users():
    userCredentials = [
        {"username": "Cristi", "passwd": 'Sima', "isAdmin": True},
        {"username": "Jul", "passwd": 'Sjlv', "isAdmin": True}
    ]
    for cred in userCredentials:
        username = cred["username"]
        passw = makePassHash(cred["passwd"])
        isAdmin = cred["isAdmin"]
        user = UserDocument(username=username, passw=passw, isAdmin=isAdmin)
        user.save()

if __name__ == "__main__":
    init_users()