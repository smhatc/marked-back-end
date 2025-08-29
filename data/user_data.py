from models.user import UserModel


def create_test_users():
    user1 = UserModel(username="User")
    user1.set_password("password")

    user2 = UserModel(username="Test")
    user2.set_password("password")

    return [user1, user2]


user_list = create_test_users()
