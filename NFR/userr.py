import os
import getpass


def get_current_user():
    try:
        # Get the username of the current logged-in user
        username = getpass.getuser()

        # Get the user ID using environment variables
        user_profile = os.environ.get('USERPROFILE')

        # Return both username and user ID
        return username, user_profile
    except Exception as e:
        print(f"Error retrieving current user: {str(e)}")
        return None, None


# Example usage
if __name__ == "__main__":
    username, user_profile = get_current_user()
    if username and user_profile:
        print(f"Username: {username}")
        print(f"User Profile Directory: {user_profile}")
    else:
        print("Unable to retrieve current user information.")
