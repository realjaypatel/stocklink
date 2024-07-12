from pymongo import MongoClient
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/stocklink")
db = client['stocklinkdb']
collection = db['stocklinkcl']
# data = {
#     'name': 'John Doe',
#     'age': 30,
#     'city': 'New York'
# }
# result = collection.insert_one(data)
# print('Inserted document ID:', result.inserted_id)



from bsedata.bse import BSE
b = BSE()
print(b)

b = BSE(update_codes = True)

k = b.getScripCodes()
for x,y in k.items():
    try:
        q = b.getQuote(x)
        collection.insert_one(q)


    except:
        print(b.verifyScripCode(x))
        print('err')

print('end')