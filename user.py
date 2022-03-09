# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User_cls:
    def __init__( self , data ):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']
    
    @classmethod # Now we use class methods to query our database
    def get_all(cls):
        q = "SELECT * FROM user;"
        rez = connectToMySQL('users_sch').query_db(q) # make sure to call the connectToMySQL function with the schema you are targeting.
        userList = [] # Create an empty list to append our instances of friends
        for rec in rez: # Iterate over the db results and create instances of friends with cls.
            userList.append( cls(rec) )
        return userList
            
    @classmethod # this method enables save/commit to db
    def save(cls, data ):
        q = "INSERT INTO user ( firstName , lastName , email , createdAt, updatedAt ) VALUES ( %(clr_firstName)s , %(clr_lastName)s , %(clr_email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_sch').query_db(q, data )
