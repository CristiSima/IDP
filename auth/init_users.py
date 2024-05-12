from user_docs import *

def init_users():
    userCredentials = [
        {"username": "Cristi", "passwd": 'Sima'},
        {"username": "Jul", "passwd": 'Sjlv'}
    ]
    for cred in userCredentials:
        username = cred["username"]
        passw = makePassHash(cred["passwd"])
        user = UserDocument(username=username, passw=passw)
        user.save()

if __name__ == "__main__":
    init_users()