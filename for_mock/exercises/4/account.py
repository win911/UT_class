# account.py

def get_user(user_id):
    pass


def display_user_info(user_id):
    user = get_user(user_id)
    html = ""
    html += "<h1>{} ({})</h1>".format(user.username, "Adult" if user.is_adult() else "Child")
    return html