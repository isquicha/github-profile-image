from src import get_user_image_link

if __name__ == "__main__":
    username = input(
        "Type the github username to get a link to profile image: "
    )
    image_link = get_user_image_link(username=username)
    print(f"Link to {username} github profile image is {image_link}")
