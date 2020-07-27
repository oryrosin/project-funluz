import json
#from django.contrib.auth.models import User
from django.urls import reverse

#from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from project.models import Owner



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
        response = self.client.get("/owners/{}".format(owner.id))
        self.assertEqual(200, response.status_code)

    # def test_get_group(self):
    #     # get one group
    #     group = GroupF()
    #
    #     url = reverse('group-detail', kwargs={'pk': group.pk})
    #     res = self.client.get(url)
    #     content = json.loads(res.content)
    #     self.assertEqual(res.status_code, 200)

    # def test_get_groups(self):
    #     # one group available
    #     url = reverse('group-list')
    #     res = self.client.get(url)
    #     content = json.loads(res.content)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(len(content['results']), 0)


    def test_update_owner(self):
        self.owner = Owner(name="rakaz")
        self.owner.save()
        response = self.client.put("/owners/", {"name": "new rakaz"})
        response_data = json.loads(response.content)
        owner = Owner.objects.get(id=self.owner.id)
        self.assertEqual(response_data.get("name"), owner.name)

    def test_owner_object_delete(self):
        self.owner = Owner(name="rakaz")
        self.owner.save()
        response = self.client.delete("/owners/{}".format(self.owner.id))
        self.assertEqual(204, response.status_code)
