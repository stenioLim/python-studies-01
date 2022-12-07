class Connection : 
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls , user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def connection_log(msg):
        print('LOG', msg)

c1 = Connection.create_with_auth('stenio', '123')
print(Connection.connection_log('This menssagen is from log'))
print(c1.user)
print(c1.password)