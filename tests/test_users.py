from killranswers import User

def test_create():
    user = User.create("something")
    assert user.user_id == "something"
