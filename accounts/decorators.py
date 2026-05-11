from django.http import HttpResponse


def allowed_users(allowed_roles=[]):

    def decorator(view_func):

        def wrapper_func(request, *args, **kwargs):

            if request.user.is_authenticated:

                role = request.user.userprofile.role

                if role in allowed_roles:

                    return view_func(request, *args, **kwargs)

                else:

                    return HttpResponse(
                        "You are not authorized to view this page."
                    )

            return HttpResponse(
                "Login Required"
            )

        return wrapper_func

    return decorator