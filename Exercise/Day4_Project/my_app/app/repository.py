from typing import Optional
from .models import User

_USER_DB_={
    1: User(id=1,name="Ani",email="ani123@gmail.com"),
    2: User(id=2,name="Gopi",email="gopi321@gmail.com")
}

class UserRepository:
    def get_by_id(self, user_id:int)->Optional[User]:
        return _USER_DB_.get(user_id)

    def save(self, user:User)->None:
        _USER_DB_[user.id]=user
