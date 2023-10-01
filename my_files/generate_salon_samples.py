from random import randint, sample
from datetime import datetime, timedelta

from models import Salon, WorkDays, WorkHoursRange, TimeOfDay

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from google.cloud.firestore import DocumentReference, CollectionReference

cred = credentials.Certificate('lady-care-ksa-firebase-adminsdk-1vbyo-f7a323eaca.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
bucket = storage.bucket(name="lady-care-ksa.appspot.com")

tpl_categories_ref = db.collection_group("TPL_service_categories")
tpl_categories = tpl_categories_ref.get()

tpl_amenities_ref = db.collection("TPL_amenities")
tpl_amenities = tpl_amenities_ref.get()


def generate_work_hours_range():
    is_work_day = bool(randint(0, 1))
    if is_work_day:
        start_hour = randint(8, 10)
        return WorkHoursRange(
            start=TimeOfDay(start_hour, 0),
            end=TimeOfDay(start_hour+8, 0)
        )
    else:
        return None


def generate_work_days():
    return WorkDays(
        sunday=generate_work_hours_range(),
        monday=generate_work_hours_range(),
        tuesday=generate_work_hours_range(),
        wednesday=generate_work_hours_range(),
        thursday=generate_work_hours_range(),
        friday=generate_work_hours_range(),
        saturday=generate_work_hours_range(),
    )


def generate_salon(index: int):
    amenities_count = randint(1, len(tpl_amenities))
    random_amenities = sample(tpl_amenities, randint(1, amenities_count))
    return Salon(
        name='صالون ' + str(index),
        description='وصف الصالون ' + str(index),
        profile_image_url=None,
        locations=['Location 1', 'Location 2'],
        shots=None,
        amenities=[item._data['id'] for item in random_amenities],
        work_days=generate_work_days(),
        rating_average=min(round(randint(1, 5) + (randint(0, 9) / 10), 1), 5.0),
    )


def get_random_categories():
    categories_count = randint(1, len(tpl_amenities))
    return sample(tpl_categories, randint(1, categories_count))


def get_random_tpl_category_services(tpl_category_path):
    services = db.collection(tpl_category_path+"/TPL_services").get()
    services_count = randint(1, len(services))
    return sample(services, randint(1, services_count))


def main():
    count = 10

    for i in range(count):
        # generate and store salon in cloud
        salon = generate_salon(i)
        _, salon_doc = db.collection("salons").add(salon.toJson())
        salon_doc: DocumentReference = salon_doc

        # create salon storage folder
        blob = bucket.blob("images/salons/{0}/shots/".format(salon_doc.id))
        blob.upload_from_string("")

        # generate and store random services in each salon
        random_categories = get_random_categories()
        for tpl_category in random_categories:
            category_data = tpl_category._data
            _, category_doc = salon_doc.collection("service_categories").add(category_data, document_id=category_data["id"])
            category_doc: DocumentReference = category_doc

            tpl_cat_ref: DocumentReference = tpl_category._reference
            tpl_services = get_random_tpl_category_services(tpl_cat_ref.path)
            for service in tpl_services:
                service_data = service._data
                category_doc.collection("services").add(service_data, document_id=service_data["id"])


if __name__ == '__main__':
    main()
