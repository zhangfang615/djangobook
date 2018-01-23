from models.TokenManager import TokenManager
from models.TokenModel import TokenModel
from django.core.cache import cache
from djangobook.settings import TOKEN_EXPIRE_TIME
import uuid
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangobook.settings'
class RedisTokenManager(TokenManager):
    def createToken(userId):
        token = str(uuid.uuid4()).replace("-", "");
        model = TokenModel(userId, token)
        cache.set(model.getUserId(),  model.getToken(), TOKEN_EXPIRE_TIME)
        return model

    def checkToken(tokenModel):
        if tokenModel == None:
            return False
        token = cache.get(tokenModel.getUserId())
        if token == None or token != tokenModel.getToken():
            return False
        cache.set(tokenModel.getUserId(), token, TOKEN_EXPIRE_TIME)
        return True

    def deleteToken(tokenModel):
        cache.delete(tokenModel.getUserId())

if __name__ == '__main__':

    tokenModel = RedisTokenManager.createToken(1)
    result = RedisTokenManager.deleteToken(tokenModel)
    print(result)
