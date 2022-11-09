from app.database import RepController


db = RepController()


def test_add_new_user():
    db.add_new_user(2)
    assert db.get_rep(2)