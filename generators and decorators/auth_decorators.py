from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if (user_role!="admin"):
            print("Access denied!")
        else:
            return func(user_role)
        return wrapper
@require_admin
def access_balanzo_portal():
    print("Access granted to the portal")
    
    access_balanzo_portal("user")
    access_balanzo_portal("admin")
