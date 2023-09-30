from google.cloud import firestore

db = firestore.Client(project="lady-care-ksa")

data = db.collection('customer_reviews').order_by(field_path= 'rating', direction="DESCENDING").order_by(field_path= 'salon_id', direction="DESCENDING").limit(5).get()
for item in data:
    print(item._data)