from app.database import RepController


db = RepController()

def test_increase_rep():
    if not db.get_user(1):
        db.add_new_user(1)

    rep_old = db.get_user(1).reputation
    db.increase_rep(1)
    rep_new = db.get_user(1).reputation
    
    assert rep_new > rep_old