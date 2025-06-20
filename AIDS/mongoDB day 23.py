from pymongo import MongoClient

# Connect to MongoDB (adjust URI if using Atlas or remote server)
client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
db = client['task_manager']
tasks = db['tasks']

# --- CREATE ---
task = {'title': 'Buy groceries', 'status': 'pending'}
tasks.insert_one(task)

# --- READ ---
for t in tasks.find():
    print(t)

# --- UPDATE ---
tasks.update_one({'title': 'Buy groceries'}, {'$set': {'status': 'done'}})

# --- DELETE ---
tasks.delete_one({'title': 'Buy groceries'})