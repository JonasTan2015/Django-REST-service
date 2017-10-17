from django.test import TestCase
from .models import CreditCard
from DBAPI import Session

# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        self.name = "John"
        self.creditCard = CreditCard(name=self.name, deposit=100.0)

    def test_model_can_create_creditCard(self):
        old_count = CreditCard.objects.count()
        self.creditCard.save()
        new_count = CreditCard.objects.count()
        self.assertNotEqual(old_count, new_count)


from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.creditCardData = {'ID': 'ID1', 'name': 'Jack', 'deposit': 200}
        self.invalidCardData = {'deposit': 100}


    def test_api_can_create_a_creditCard(self):
        """Test the api has bucket creation capability."""
        response = self.client.post(reverse('create_credit_card'),
                         self.creditCardData,
                         format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_create_invalid_creditCard(self):
        '''Input an invalid credit card data, it should return 400 status code'''
        response = self.client.post(reverse('create_credit_card'),
                                    self.invalidCardData,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    '''
    Test sqlalchemy create AlchemyCreditCard and save it to DB
    '''
    def test_api_create_AlchemyCreditCard(self):
        # count how many records before inserting a credit card
        from .models import AlchemyCreditCard
        from sqlalchemy import func
        session = Session()
        old_count = session.query(AlchemyCreditCard.ID).count()
        session.commit()
        session.close()

        # make a http request to insert a credit card
        response = self.client.post(reverse('create_alchemyCreditCard'),
                         self.creditCardData,
                         format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # count how many credit cards records in the table
        session = Session()
        new_count = session.query(AlchemyCreditCard.ID).count()
        session.commit()
        session.close()

        self.assertNotEqual(old_count, new_count)

        # try to insert a wrong record to database
        response = self.client.post(reverse('create_alchemyCreditCard'),
                                    self.invalidCardData,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




