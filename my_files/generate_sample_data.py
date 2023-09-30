import random
import datetime

from google.cloud import firestore

db = firestore.Client(project="lady-care-ksa")

# Generate 20 salons
salons = []
for i in range(20):
    salon = {
        "id": str(i),
        "name": "Salon " + str(i),
        "description": "This is a sample salon description.",
        "profileImageUrl": "https://example.com/salon-image.png",
        "services": [
            {
                "id": "service-1",
                "name": "Haircut",
                "description": "A haircut service.",
                "price": 100,
                "duration": 60,
                "category": "Hair",
            },
            {
                "id": "service-2",
                "name": "Manicure",
                "description": "A manicure service.",
                "price": 50,
                "duration": 30,
                "category": "Nails",
            },
        ],
        "locations": ["Giza, Egypt"],
        "images": ["https://example.com/salon-image-1.png", "https://example.com/salon-image-2.png"],
        "amenities": [
            {
                "id": "amenity-1",
                "name": "Free Wi-Fi",
                "icon": "https://example.com/wifi-icon.png",
            },
            {
                "id": "amenity-2",
                "name": "Parking",
                "icon": "https://example.com/parking-icon.png",
            },
        ],
        "workDays": {
            "sunday": {
                "start": datetime.time(9, 0),
                "end": datetime.time(18, 0),
            },
            "monday": {
                "start": datetime.time(9, 0),
                "end": datetime.time(18, 0),
            },
            "tuesday": {
                "start": datetime.time(9, 0),
                "end": datetime.time(18, 0),
            },
            "wednesday": {
                "start": datetime.time(9, 0),
                "end": datetime.time(18, 0),
            },
            "thursday": {
                "start": datetime.time(9, 0),
                "end": datetime.time(18, 0),
            },
            "friday": {
                "start": datetime.time(9, 0),
                "end": datetime.time(18, 0),
            },
            "saturday": {
                "start": datetime.time(9, 0),
                "end": datetime.time(18, 0),
            },
        },
        "createdAt": datetime.datetime.now(),
        "updatedAt": datetime.datetime.now(),
    }
    salons.append(salon)

# Generate 100 customer reviews
customer_reviews = []
for i in range(100):
    customer_review = {
        "id": str(i),
        "salonId": random.choice(list(map(lambda salon: salon["id"], salons))),
        "customerId": str(i),
        "rating": random.randint(1, 5),
        "comment": "This is a sample customer review comment.",
        "createdAt": datetime.datetime.now(),
    }
    customer_reviews.append(customer_review)

# Convert datetime.time objects to strings before writing them to Firestore
for salon in salons:
    for day in salon["workDays"]:
        salon["workDays"][day]["start"] = salon["workDays"][day]["start"].strftime("%H:%M")
        salon["workDays"][day]["end"] = salon["workDays"][day]["end"].strftime("%H:%M")

# Write salons and customer reviews to Firebase
for salon in salons:
    db.collection("salons").document(salon['id']).set(salon)

for customer_review in customer_reviews:
    db.collection("customer_reviews").document(customer_review["id"]).set(customer_review)

# Success!
