from random import randint, sample
from datetime import datetime, timedelta

from models import SalonAmenity

from google.cloud import firestore

db = firestore.Client(project="lady-care-ksa")


def generate_amenity():
    return SalonAmenity(
        id='amenity_id_' + str(randint(1, 100)),
        name='Amenity ' + str(randint(1, 10)),
        icon='amenity_icon'
    )


def main():
    count = 5
    amenities = [generate_amenity() for _ in range(count)]

    for a in amenities:
        db.collection("salon_amenities").add(a.toJson(), document_id=a.id, )


if __name__ == '__main__':
    main()
