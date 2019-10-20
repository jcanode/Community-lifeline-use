from ws import login_manager, mongoDB, models

def getUserById(id):
    user_data = mongoDB.users.find_one({"_id": id})
    if user_data == None:
        return None
    user = models.User()
    user.load(user_data)
    return User.get(id)

@login_manager.user_loader
def getUserByName(name):
    user_data = mongoDB.users.find_one({"name": name})
    if user_data == None:
        return None
    user = models.user()
    user.load(user_data)
    return user

@login_manager.user_loader
def getUserByEmail(email):
    user_data = mongoDB.users.find_one({"email": email})
    if user_data == None:
        return None
    user = models.User()
    user.load(user_data)
    return user