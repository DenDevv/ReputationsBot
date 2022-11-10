import pytest

from app.database import RepController, drop_tables


db = RepController()


@pytest.mark.usefixtures("drop_tables")
def test_add_new_user():
    if not db.get_user(1):
        db.add_new_user(1)

    assert db.get_user(1)