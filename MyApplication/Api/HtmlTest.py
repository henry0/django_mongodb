from django.http import HttpResponse
from django.template import loader

from MyApplication.MongoDbManager import MongoDbManager


def specific_user(request, username):
    def get():
        dbUserData = MongoDbManager().get_users_from_collection({'name': username})

        userData = dbUserData[0]
        del userData['_id']

        template = loader.get_template('User.html')
        return HttpResponse(template.render({'userData': [userData]}, request))

    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)


def all_users(request):
    def get():
        dbUserData = MongoDbManager().get_users_from_collection({})

        userData = []
        for user in dbUserData:
            del user['_id']
            userData.append(user)

        template = loader.get_template('User.html')
        return HttpResponse(template.render({'userData': userData}, request))

    if request.method == 'GET':
        return get()
    else:
        return HttpResponse(status=405)
