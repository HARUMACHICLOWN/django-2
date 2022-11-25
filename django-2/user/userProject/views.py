from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>Path: {path}</p> 
    <p>User-agent: {user_agent}</p>
    """)


def error_page(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")



def user_info(request, login='Samir', post_name='django project', post_number='1'):
    return HttpResponse(f"""Login: {login}<br>
                            Post name: {post_name}<br> 
                            Post number: {post_number}
                            """)
