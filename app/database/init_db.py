from app.database import Session, engine
from app.models import UserReps


session = Session(bind=engine)


class RepController:
    # Add new user, default rep is 10
    def add_new_user(self, user_id):
        new_user = UserReps(user_id=user_id, reputation=10)
        session.add(new_user)
        session.commit()

    # Get user by user_id
    def get_user(self, user_id):
        return session.query(UserReps).filter(UserReps.user_id==user_id).first()

    # Get rep by user_id
    def get_rep(self, user_id):
        return self.get_user(user_id).reputation

    # Increase rep
    def increase_rep(self, user_id):
        user = self.get_rep(user_id)        # getting user by user_id
        user.reputation += 0.1              # increasing rep by 0.1
        session.commit()                    # saving changes

    # Reduce rep
    def reduce_rep(self, user_id):
        user = self.get_rep(user_id)         # getting user by user_id
        user.reputation -= 0.1               # reducing rep by 0.1
        session.commit()                     # saving changes