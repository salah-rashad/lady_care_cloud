import datetime

from firebase_admin.firestore import firestore

from models import SalonService, ServiceCategory

db = firestore.Client(project="lady-care-ksa")


# def duration(hours=0, minutes=0, seconds=0):
#     return int(datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds() * 1000000)


categories = [
    ServiceCategory(
        id="make_up",
        icon_url="service_category_icons/Makeup.png",
        name="ميك اب",
        services=[
            SalonService(
                id="service-1",
                name="Service 1",
                description="Service desc",
                duration=datetime.timedelta(minutes=30),
                price=50,
            ),
        ],
    ),
    ServiceCategory(
        id="skin_care",
        icon_url="service_category_icons/Skin Care.png",
        name="العناية بالبشرة",
        services=[
            SalonService(
                id="service-1",
                name="Service 1",
                description="Service desc",
                duration=datetime.timedelta(minutes=30),
                price=50,
            ),
        ],
    ),
    ServiceCategory(
        id="hair_styling",
        icon_url="service_category_icons/Hair Styling.png",
        name="تصفيف الشعر",
        services=[
            SalonService(
                id="service-1",
                name="Service 1",
                description="Service desc",
                duration=datetime.timedelta(minutes=30),
                price=50,
            ),
        ],
    ),
    ServiceCategory(
        id="nails_care",
        icon_url="service_category_icons/Nails Care.png",
        name="العناية بالأظافر",
        services=[
            SalonService(
                id="service-1",
                name="Service 1",
                description="Service desc",
                duration=datetime.timedelta(minutes=30),
                price=50,
            ),
        ],
    ),
    ServiceCategory(
        id="hair_coloring",
        icon_url="service_category_icons/Hair Coloring.png",
        name="صبغ الشعر",
        services=[
            SalonService(
                id="service-1",
                name="Service 1",
                description="Service desc",
                duration=datetime.timedelta(minutes=30),
                price=50,
            ),
        ],
    ),
    ServiceCategory(
        id="spa",
        icon_url="service_category_icons/Spa.png",
        name="سبا",
        services=[
            SalonService(
                id="service-1",
                name="Service 1",
                description="Service desc",
                duration=datetime.timedelta(minutes=30),
                price=50,
            ),
        ],
    ),
    ServiceCategory(
        id="massage",
        icon_url="service_category_icons/Massage.png",
        name="مساج",
        services=[
            SalonService(
                id="service-1",
                name="Service 1",
                description="Service desc",
                duration=datetime.timedelta(minutes=30),
                price=50,
            ),
        ],
    ),
]


def add_categories_to_firebase(categories: list[ServiceCategory]):
    for category in categories:
        # Add the category to the `categories` collection.
        category_ref = db.collection('TPL_service_categories').document(category.id)
        category_ref.set(category.to_json())

        # Create a sub-collection for the category's services.
        services_ref = category_ref.collection('TPL_services')

        # Add the category's services to the sub-collection.
        for service in category.services:
            service_ref = services_ref.document(service.id)
            service_ref.set(service.to_json())


if __name__ == '__main__':
    add_categories_to_firebase(categories)
