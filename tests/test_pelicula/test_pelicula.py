from rest_framework import status
from tests.factories.pelicula.pelicula_factories import PeliculaFactory
from tests.factories.personaje.personaje_factories import PersonajeFactory
from tests.test_setup import TestSetUp
from faker import Faker

class PeliculaTestCase(TestSetUp):
    
    url='/api/v1/pelicula/'
    url2='/api/v1/personaje/'
    
    faker=Faker()
    def test_peliculas(self):
        
        response=self.client.get(self.url+'list/',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    


    def test_create_pelicula(self):
        personajes=PersonajeFactory().build_personaje_JSON()
        response=self.client.post(self.url2+'list/',
           personajes,
           format='json'
        )
        responses=self.client.post(self.url+'list/',
           
             {
                "name":self.faker.name(),
                "apertura":self.faker.name(),
                "director":self.faker.name(),
                "prodcutora":self.faker.name(),
                "personaje":response.data['id'],
                "active":True},
           format='json'
        )
        
        self.assertEqual(responses.status_code,status.HTTP_201_CREATED)
    
    def test_update_pelicula(self):
        personajes=PersonajeFactory().build_personaje_JSON()
        response=self.client.post(self.url2+'list/',
           personajes,
           format='json'
        )
        pelidula=PeliculaFactory().create_pelicula_update(int(response.data['id']))
        responses=self.client.put(self.url+'detail/'+str(pelidula.id),
           
             {  "name":"test1",
                "apertura":"test1",
                "director":"test1",
                "prodcutora":"test1",
                 "personaje":str(pelidula.personaje_id),
                "active":True},
           format='json'
        )
        self.assertEqual(responses.status_code,status.HTTP_200_OK)
    
    def test_delete_pelicula(self):
        personajes=PersonajeFactory().build_personaje_JSON()
        response=self.client.post(self.url2+'list/',
           personajes,
           format='json'
        )
        pelidula=PeliculaFactory().create_pelicula_update(int(response.data['id']))
        responses=self.client.delete(self.url+'detail/'+str(pelidula.id),format='json')
        self.assertEqual(responses.status_code,status.HTTP_204_NO_CONTENT)