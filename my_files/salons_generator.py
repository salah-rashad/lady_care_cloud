from random import randint, sample
from datetime import datetime, timedelta

from google.cloud import firestore

db = firestore.Client(project="lady-care-ksa")

# Function to generate a random TimeOfDay
def generate_work_hours_range():
    startHour = randint(8, 10)
    return {
        'start': {
            'hour': startHour,  
            'minute': 0
        },
        'end': {
            'hour': startHour + 8, # 8 hours work day
            'minute': 0
        }
    }

# Function to generate a SalonAmenity
def generate_salon_amenity():
    return {
        'id': 'amenity_id_' + str(randint(1, 100)),
        'name': 'Amenity ' + str(randint(1, 10)),
        'icon': 'amenity_icon_url'
    }

# Function to generate a SalonService
def generate_salon_service():
    return {
        'id': 'service_id_' + str(randint(1, 100)),
        'name': 'Service ' + str(randint(1, 10)),
        'description': 'Service description',
        'price': round(randint(10, 100), 2),
        'duration': randint(30, 120)
    }

# Function to generate a ServiceCategory
def generate_service_category():
    num_services = randint(1, 5)
    services = [generate_salon_service() for _ in range(num_services)]

    return {
        'id': 'category_id_' + str(randint(1, 100)),
        'iconUrl': 'category_icon_url',
        'name': 'Category ' + str(randint(1, 5)),
        'services': services
    }

# Function to generate a Salon
def generate_salon() -> tuple[dict, list[dict],list[dict]]:
    num_service_categories = randint(1, 4)
    service_categories = [generate_service_category() for _ in range(num_service_categories)]

    num_salon_amenities = randint(1, 5)
    salon_amenities = [generate_salon_amenity() for _ in range(num_salon_amenities)]

    random_amenities = sample(salon_amenities, randint(1,num_salon_amenities))

    return {
        'name': 'Salon ' + str(randint(1, 10)),
        'description': 'Salon description',
        'profileImageUrl': 'salon_image_url',
        'locations': ['Location 1', 'Location 2'],
        'images': ['image_url_1', 'image_url_2'],
        'amenities': [item['id'] for item in random_amenities],
        'workDays': {
            'sunday': generate_work_hours_range(),
            'monday': generate_work_hours_range(),
            'tuesday': generate_work_hours_range(),
            'wednesday': generate_work_hours_range(),
            'thursday': generate_work_hours_range(),
            'friday': generate_work_hours_range(),
            'saturday': generate_work_hours_range(),
        },
        'rating': round(randint(1, 5) + (randint(0, 9) / 10), 1),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now() - timedelta(days=randint(1, 365))
    }, service_categories, salon_amenities

# Function to add a Salon document to Firestore with subcollections
def add_salon_to_firestore(salon_data, service_categories, salon_amenities):
    _, salon_ref = db.collection('salons').add(salon_data)
    print(f'Salon added with ID: {salon_ref.id}')

    # Add service categories as subcollections
    for category_data in service_categories:
        salon_ref.collection('service_categories').add(category_data)
    for amenity_data in salon_amenities:
        db.collection('salon_amenities').add(amenity_data)

# Generate and add sample Salon data
for _ in range(5):  # Change the number as per your requirement
    salon_data, service_categories, salon_amenities = generate_salon()
    add_salon_to_firestore(salon_data, service_categories, salon_amenities)

print("Sample data added to Firestore with subcollections.")
