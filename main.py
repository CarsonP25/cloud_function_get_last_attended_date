from flask import Request, Response


def get_last_attended_date(request):
    print(request)
    print("Hello, World!")
    return ("OK", 200)
