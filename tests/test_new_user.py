from test_database import TestRepController


db = TestRepController()

def test_add_new_user():
    if not db.get_user(1):
        db.add_new_user(1)
    
    assert db.get_user(1)