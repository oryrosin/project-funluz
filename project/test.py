import json
#from django.contrib.auth.models import User
from django.urls import reverse

#from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from project.models import Owner, Calendar



class OwnerTestCase(APITestCase):

    def setUp(self):
        pass
        #self.username = "john"
        #self.email = "john@snow.com"
        #self.password = "you_know_nothing"
        #self.user = User.objects.create_user(self.username, self.email, self.password)
        #self.token = Token.objects.create(user=self.user)
        #self.api_authentication()

    #def api_authentication(self):
        #self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_owner(self):
        #self.owner_name = "rakaz noar"
        self.owner = Owner(name="rakaz")
        self.owner.save()
        response = self.client.post("/owners/", {"name": "rakaz"})
        self.assertEqual(201, response.status_code)

    def test_get_an_owner(self):
        #Test the api can get a given owners name.
        self.owner = Owner(name="rakaz")
        self.owner.save()
        owner = Owner.objects.get(name= "rakaz")
        response = self.client.get("/owners/{}/".format(owner.id))
        self.assertEqual(200, response.status_code)

    def test_get_list_of_owners(self):
        self.owner1 = Owner(name="rakaz.a")
        self.owner1.save()
        self.owner2 = Owner(name="rakaz.b")
        self.owner2.save()
        response = self.client.get("/owners/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 2)
        # verify owner list includes expected owners:
        self.assertEqual({"id": 2 ,"name": "rakaz.b"} in response.json()['results'], True)

    def test_update_owner(self):
        self.owner = Owner(name="rakaz")
        self.owner.save()
        response = self.client.patch("/owners/{}/".format(self.owner.id), {"name": "rakaz hadash"})
        response_data = json.loads(response.content)
        self.assertEqual(response_data,{'id': 1, 'name': 'rakaz hadash'})
        self.assertEqual(response.status_code, 200)

    def test_owner_object_delete(self):
        self.owner = Owner(name="rakaz")
        self.owner.save()
        response = self.client.delete("/owners/{}/".format(self.owner.id))
        self.assertEqual(204, response.status_code)


class CalendarTestCase(APITestCase):

    def setUp(self):
        pass

    def test_creat_new_calendar_for_specific_owner(self):
        self.owner = Owner(name="rakaz")
        self.owner.save()
        self.calendar= Calendar(month="2020-07-23", owner=self.owner )
        self.calendar.save()
        print(self.calendar.id, self.owner.id)
        response = self.client.post("/owners/{}/calendar/{}/".format(self.owner.id, self.calendar.id))
        print(response.status_code)
        #self.assertEqual(201, response.status_code)


    def test_creating_new_calendar_for_no_owner_fails(self):
        pass
    def test_get_calendar(self):
        pass

