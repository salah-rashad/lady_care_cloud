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
            "iconUrl": self.icon_url,
        }


class SalonService:
    def __init__(self, id, name, description, price, duration):
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
            "duration": self.duration,
        }