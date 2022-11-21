from faker import Faker

from apps.pelicula.models import Pelicula

faker=Faker()

class PeliculaFactory:

    url2='/api/v1/personaje/'
    def build_pelicula_JSON(self):
       
        return {
                "id":faker.random_number(digits=2),
                "name":faker.name(),
                "apertura":faker.name(),
                "director":faker.name(),
                "prodcutora":faker.name(),
                "personaje":1,
                "active":True
                
            }
    def create_pelicula(self):
        return Pelicula.objects.create(**self.build_pelicula_JSON())

    def build_pelicula_update_JSON(self,id):
  
        return {
                "id":faker.random_number(digits=2),
                "name":faker.name(),
                "apertura":faker.name(),
                "director":faker.name(),
                "prodcutora":faker.name(),
                "personaje_id":id,
                "active":True
                
            }
    def create_pelicula_update(self,id):
        return Pelicula.objects.create(**self.build_pelicula_update_JSON(id))