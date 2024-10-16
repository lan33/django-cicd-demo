# from django.test import TestCase

import pytest

def fizz_buzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0 :
        return 'Fizz'

def test_fizz():
    number = 3

    result = fizz_buzz(number)

    assert result == 'Fizz'

def test_fizz_with_another_number():
    number = 12

    result = fizz_buzz(number)

    assert result == 'Fizz'

def test_buzz():
    number = 5

    result = fizz_buzz(number)

    assert result == 'Buzz' 

def test_fizzbuzz():
    number = '15'

    result = fizz_buzz(number)

    assert result == 'FizzBuzz'


# class DemoTestCase(TestCase):
        # def test_simple(self):
        #       self.assertEqual(1+2, 2)


        # def test_model_InventoryItem(self):
		# # 1. Préparer les données de test
		#     self.user = User.objects.create_user(username='testuser', password='password')
		#     self.category = Category.objects.create(name='Test Category')
              
		# # 2. Exécution de l'action
        #     inventory_item = InventoryItem.objects.create(
        #         name='Test Item',
        #         quantity=10,
        #         user=self.user,
        #         category=self.category
		#     )
        
		# # 3. Assertions
        #     self.assertEquals(str(inventory_item), 'Test Item')
        #     self.assertTrue(isinstance(inventory_item, InventoryItem))


    # def test_fizz(self):
    #     number = 3

    #     result = fizz_buzz(number)

    #     self.assertEqual(result, 'Fizz')

    # def test_fizz_with_another_number(self):
    #     number = 12

    #     result = fizz_buzz(number)

    #     self.assertEqual(result, 'Fizz')

    # def test_buzz(self):
    #     number = 5

    #     result = fizz_buzz(number)

    #     self.assertEqual(result, 'Buzz')

    # def test_fizzbuzz(self):
    #     number = 15

    #     result = fizz_buzz(number)

    #     self.assertEqual(result, 'FizzBuzz')




       
