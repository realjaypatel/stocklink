from pymongo import MongoClient

# Replace the connection string with your MongoDB connection string
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/stocklink")

# Access a specific database
db = client['stocklinkdb']

# Access a specific collection
collection = db['stocklinkcl']

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}


data_list = [
    {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Bob', 'age': 22, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 35, 'city': 'San Francisco'}
]

result = collection.insert_many(data_list)
print('Inserted document IDs:', result.inserted_ids)

result = collection.insert_one(data)
print('Inserted document ID:', result.inserted_id)