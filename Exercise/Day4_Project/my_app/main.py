from app import UserService, UserRepository

def main():
    service=UserService()
    updated_user=service.deactivate_user(user_id=1)
    print(f"Updated the status of the user: {updated_user.name}")


if __name__ == "__main__":
    main()
