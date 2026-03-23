from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper():