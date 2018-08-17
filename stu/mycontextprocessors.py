#coding=utf-8

def getSesson(request):
    username=request.session.get('username')
    return {'username':username}