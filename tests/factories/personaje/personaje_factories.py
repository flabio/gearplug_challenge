from faker import Faker

from apps.personaje.models import Personaje

faker=Faker()

class PersonajeFactory:
    
        
    def build_personaje_JSON(self):
        return {
                "id":faker.random_number(digits=2),
                "full_name":faker.name(),
                "active":True
                
            }
    def create_personaje(self):
        return Personaje.objects.create(**self.build_personaje_JSON())