import pytest
from app.database import RepController, drop_tables


db = RepController()


@pytest.mark.usefixtures("drop_tables")
def test_increase_rep():
    if not db.get_user(1):
        db.add_new_user(1)

    rep_old = db.get_user(1).reputation
    db.reduce_rep(1, "some reason")
    rep_new = db.get_user(1).reputation

    assert rep_new < rep_old
    assert db.get_reduce_rep_history(1)