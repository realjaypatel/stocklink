from pymongo import MongoClient
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/stocklink")
db = client['stocklinkdb']
collection = db['stocklink_async']
# data = {
#     'name': 'John Doe',
#     'age': 30,
#     'city': 'New York'
# }
# result = collection.insert_one(data)
# print('Inserted document ID:', result.inserted_id)

async def store(x):
    try:
        q =  b.getQuote(x)
        await collection.insert_one(q)


    except:
        print(b.verifyScripCode(x))
        print('err')


from bsedata.bse import BSE
b = BSE()
print(b)

b = BSE(update_codes = True)

k = b.getScripCodes()
for x,y in k.items():
    store(x)
    

print('end')