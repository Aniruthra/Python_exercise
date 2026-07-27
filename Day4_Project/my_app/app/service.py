from .repository import UserRepository
from .models import User

class UserService:
    def __init__(self, repo:UserRepository | None=None):
        self.repo=repo or UserRepository()

    def deactivate_user(self, user_id:int)->User:
        user=self.repo.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")

        user.is_active=False
        self.repo.save(user)
        return user

