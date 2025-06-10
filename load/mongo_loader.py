from pymongo import MongoClient
from config import settings

def load_to_mongo(data):
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB_NAME]
    collection = db[settings.MONGO_COLLECTION]

    filtered_data = []
    for record in data:
        email = record.get("email")
        phone = record.get("phone")

        if not email or not phone:
            continue

        existing = collection.find_one({
            "email": email,
            "phone": phone
        })

        if existing:
            print(f"Đã tồn tại trong DB: {email} - {phone}")
        else:
            filtered_data.append(record)

    if filtered_data:
        collection.insert_many(filtered_data)
        print("thành công.")
    else:
        print("không thành công")

    client.close()
