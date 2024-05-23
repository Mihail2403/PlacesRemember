from django.shortcuts import redirect


def is_not_admin(func):
    """decorator for checking that usr isn't admin"""

    def wrapper(*args, **kwargs):
        current_user = args[0].user if len(args) > 0 else None
        if current_user and not current_user.is_staff:
            return func(*args, **kwargs)
        print(
            "Вам необходимо войти от имени авторизованного через \
                вк пользователя (не root - выйдете из его аккаунта)"
        )
        return redirect("/admin")

    return wrapper
