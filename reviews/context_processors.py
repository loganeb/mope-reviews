def user_authenticated(request):
    return {'user_authenticated': request.user.is_authenticated}