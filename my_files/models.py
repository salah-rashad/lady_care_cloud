import datetime


class ServiceCategory:
    def __init__(self, id, icon_url, name, services):
        self.id = id
        self.icon_url = icon_url
        self.name = name
        self.services = services

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "icon_url": self.icon_url,
        }


class SalonService:
    def __init__(self, id, name, description, price, duration: datetime.timedelta):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.duration = duration

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "duration": self.duration.total_seconds() * 1000000,
        }


class CustomerReview:
    def __init__(self, id, salon_id, customer_id, rating, comment, created_at):
        self.id = id
        self.salon_id = salon_id
        self.customer_id = customer_id
        self.rating = rating
        self.comment = comment

    def toJson(self):
        return {
            "id": self.id,
            "salon_id": self.salon_id,
            "customer_id": self.customer_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": datetime.datetime.now().isoformat(),
        }


class SalonAmenity:
    def __init__(self, id, name, icon):
        self.id = id
        self.name = name
        self.icon = icon

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
        }


class Salon:
    def __init__(
        self,
        name,
        description,
        profile_image_url,
        locations,
        shots,
        amenities,
        work_days,
        rating_average,
    ):
        self.name = name
        self.description = description
        self.profile_image_url = profile_image_url
        self.locations = locations
        self.shots = shots
        self.amenities = amenities
        self.work_days = work_days
        self.rating_average = rating_average

    def toJson(self):
        return {
            "name": self.name,
            "description": self.description,
            "profile_image_url": self.profile_image_url,
            "locations": self.locations,
            "shots": self.shots,
            "amenities": self.amenities,
            "work_days": self.work_days.toJson(),
            "rating_average": self.rating_average,
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": datetime.datetime.now().isoformat(),
        }


class TimeOfDay:
    def __init__(self, h: int, m: int):
        self.h = h
        self.m = m

    def toJson(self):
        return {
            "h": self.h,
            "m": self.m,
        }


class WorkHoursRange:
    def __init__(self, start: TimeOfDay, end: TimeOfDay):
        self.start = start
        self.end = end

    def toJson(self):
        return {
            "start": self.start.toJson(),
            "end": self.end.toJson(),
        }


class WorkDays:
    def __init__(
        self, sunday: WorkHoursRange | None = None, monday: WorkHoursRange | None = None, tuesday: WorkHoursRange | None = None, wednesday: WorkHoursRange | None = None, thursday: WorkHoursRange | None = None, friday: WorkHoursRange | None = None, saturday: WorkHoursRange | None = None
    ):
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday

    def toJson(self):
        return {
            "sunday": self.sunday.toJson() if self.sunday else None,
            "monday": self.monday.toJson() if self.monday else None,
            "tuesday": self.tuesday.toJson() if self.tuesday else None,
            "wednesday": self.wednesday.toJson() if self.wednesday else None,
            "thursday": self.thursday.toJson() if self.thursday else None,
            "friday": self.friday.toJson() if self.friday else None,
            "saturday": self.saturday.toJson() if self.saturday else None,
        }
