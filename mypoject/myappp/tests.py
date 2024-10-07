from django.test import TestCase

# Create your tests here.
from myappp.models import Shop

class ShopTestCase(TestCase):
    def setUpp(self):
        Shop.objects.create(name="vasa", cost=100, proz=0.3)
        Shop.objects.create(name="cape", cost=1000, proz=0.5)
    def test_shop_can_check123(self):
        vasa = Shop.objects.get(name="vasa")
        cape = Shop.objects.get(name="cape")
        self.assertEqual(vasa.check123(12, 0.3), 30)
        self.assertEqual(cape.check123(20, 0.5), 10)

        #kjhgkjhgkjghgk