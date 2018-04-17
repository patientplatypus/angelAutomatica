from pymongo import MongoClient

# mongodb://<dbuser>:<dbpassword>@ds157499.mlab.com:57499/angel_list_names


class DBHandler(object):
    def __init__(self):
        self.database = None

    def init_db(self):
        print('inside init_db of DBHandler')
        connection = MongoClient('mongodb://<dbuser>:<dbpassword>@ds157499.mlab.com:57499/MONGO_DB_NAMES')
        self.database=connection.angel_list_names

    def add_name(self, name):
        print('inside add_business of DBHandler')
        business = {
            'name' : name
        }
        self.database.angel_list_names.insert_one(business)

    def check_name(self, name):
        print('inside check_name of DBHandler')
        output = []
        dbInstance = self.database.angel_list_names
        for item in dbInstance.find():
            output.append({'name' : item['name']})
        for x in range(0, len(output)):
            if(output[x]['name']==name):
                return True
        return False
