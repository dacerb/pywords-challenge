import pymongo
import config

con = pymongo.MongoClient(config.MONGO_HOST, config.MONGO_PORT)
db = con[config.MONGO_DB]
db.authenticate(config.MONGO_USER, config.MONGO_PASS)

print(db)
input()

##https://stackoverflow.com/questions/42718547/how-to-connect-remote-mongodb-with-pymongo