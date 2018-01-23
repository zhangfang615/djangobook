class TokenModel:
    def __init__ (self, userId, token):
        self.__userId = userId
        self.__token = token

    def getUserId (self):
        return self.__userId

    def setUserId(self, __userId) :
        self.__userId = __userId

    def getToken(self):
        return self.__token

    def setToken (self, __token):
        self.__token = __token