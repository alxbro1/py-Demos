allowed_keys = {"id","name", "category", "price", "stock", "description", "image_url"}
products = [
    {
        "id": 1,
        "name": "Shampoo Revitalizante",
        "category": "Cuidado Capilar",
        "price": 15.99,
        "stock": 25,
        "description": "Un shampoo que revitaliza y da brillo al cabello.",
        "image_url": "https://example.com/shampoo.jpg"
    },
    {
        "id": 2,
        "name": "Acondicionador Hidratante",
        "category": "Cuidado Capilar",
        "price": 12.49,
        "stock": 30,
        "description": "Acondicionador que hidrata profundamente.",
        "image_url": "https://example.com/acondicionador.jpg"
    },
    {
        "id": 3,
        "name": "Gel de Peinado Fijación Extra",
        "category": "Cuidado Capilar",
        "price": 8.99,
        "stock": 15,
        "description": "Gel de peinado con fijación extra fuerte.",
        "image_url": "https://example.com/gel.jpg"
    },
    {
        "id": 4,
        "name": "Cera Moldeadora",
        "category": "Estilizado",
        "price": 10.99,
        "stock": 20,
        "description": "Cera moldeadora ideal para un acabado mate.",
        "image_url": "https://example.com/cera.jpg"
    },
    {
        "id": 5,
        "name": "Aceite Reparador",
        "category": "Tratamiento",
        "price": 18.75,
        "stock": 10,
        "description": "Aceite reparador para puntas dañadas.",
        "image_url": "https://example.com/aceite.jpg"
    }
]

class IDGenerator:
    def __init__(self):
        self.current_id = 6

    def generate_id(self):
        self.current_id += 1
        return self.current_id
