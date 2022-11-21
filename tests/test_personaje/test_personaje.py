from rest_framework import status
from tests.factories.personaje.personaje_factories import PersonajeFactory
from tests.test_setup import TestSetUp

class PersonajeTestCase(TestSetUp):
    
    url='/api/v1/personaje/'
    
    def test_personajes(self):
        personaje=PersonajeFactory().create_personaje()
        response=self.client.get(self.url+'list/',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_name_personaje(self):
        personaje=PersonajeFactory().create_personaje()
        response=self.client.get(self.url+'list/?',{'full_name':personaje.full_name},format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data[0]['full_name'],personaje.full_name) 
    
    def test_name_personaje_error(self):
        personaje=PersonajeFactory().create_personaje()
        response=self.client.get(self.url+'list/?full_name=dssdsgsd',format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(personaje.full_name,"dssdsgsd")

    def test_create_personaje(self):
        personaje=PersonajeFactory().build_personaje_JSON()
        response=self.client.post(self.url+'list/',
           personaje,
           format='json'
        )
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'],personaje['full_name'])
    def test_update_personaje(self):
        personaje=PersonajeFactory().create_personaje()
        response=self.client.put(self.url+'detail/'+str(personaje.id),
           {"full_name":"test1",
            "active":False},
           format='json'
        )
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_delete_personaje(self):
        personaje=PersonajeFactory().create_personaje()
        response=self.client.delete(self.url+'detail/'+str(personaje.id),
           format='json'
        )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        # self.assertEqual(response.data['full_name'],personaje['full_name'])