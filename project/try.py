from rest_framework import status
from rest_framework.reverse import reverse

from project.models import Owner
from django.test import TestCase

class OwnerTestCase(TestCase):

    def setUp(self):
        self.owner_name = "rakaz noar"
        self.owner = Owner(name=self.owner_name)
        super(OwnerTestCase, self).setUp()

    # def test_owner_created(self):
    #     old_count = Owner.objects.count()
    #     self.owner.save()
    #     new_count = Owner.objects.count()
    #     self.assertNotEqual(old_count, new_count)

    def test_api_can_get_an_owner(self):
        #Test the api can get a given owners name.
        self.owner.save()
        owner = Owner.objects.get(name= self.owner_name)
        response = self.client.get("/owners/{}".format(owner.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, owner)
    #
    # def test_api_can_update_owner(self):
    #     #Test the api can update a given owner.
    #     change_owner = {'name': 'new rakaz'}
    #     response = self.client.put(
    #         reverse('details', kwargs={'pk': owner.id}),
    #         change_owner, format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_api_can_delete_owner(self):
    #     #Test the api can delete a owner.
    #     owner = Owner.objects.get()
    #     response = self.client.delete(
    #         reverse('details', kwargs={'pk': owner.id}),
    #         format='json',
    #         follow=True)
    #
    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
