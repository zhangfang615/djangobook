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

    def getToken(authentication):
        if authentication == None or len(authentication) == 0 :
            return None
        params = authentication.split("_")
        if len(params) != 2:
            return None

        userId = int(params[0])
        return TokenModel( userId, params[1])

    def checkToken(tokenModel):
        if tokenModel == None:
            return False
        token = cache.get(tokenModel.getUserId())
        print(token)
        print(tokenModel.getToken())
        if token == None or token != tokenModel.getToken():
            return False
        cache.set(tokenModel.getUserId(), token, TOKEN_EXPIRE_TIME)
        return True

    def deleteToken(tokenModel):
        cache.delete(tokenModel.getUserId())

if __name__ == '__main__':
    authentication = "1_c747c8c373b3474e81341faa3ab6c613"
    tokenModel = RedisTokenManager.getToken(authentication)
    # cModel = RedisTokenManager.createToken(1)
    result = RedisTokenManager.checkToken(tokenModel)
    print(result)
