class TokenModel:
    def __init__ (self, userId, token):
        self.__secretuserId = userId
        self.__secrettoken = token

    def getUserId (self):
        return self.__secretuserId

    def setUserId(self, __secretuserId) :
        self.__secretuserId = __secretuserId

    def getToken(self):
        return self.__secrettoken

    def setToken (self, __secrettoken):
        self.__secrettoken = __secrettoken