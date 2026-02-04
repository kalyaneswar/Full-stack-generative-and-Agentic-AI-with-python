from functools import wraps

def required_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied Only Admins!")
        else:
            return func(user_role)
    return wrapper

@required_admin
def access_to_inventory(role):
    print("Access granted to Inventory")

access_to_inventory("user")
access_to_inventory("admin")