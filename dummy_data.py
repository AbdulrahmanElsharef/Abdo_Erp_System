import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
import random
from ErpApp.models import Item,Category


# def seed_brand(n):
#     fake=Faker()
#     images=['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14jpeg']
#     for _ in range(n):
#         Brand.objects.create(
#             name=fake.name(),
#             image=f"brand/{images[random.randint(1,12)]}"
#         )
#     print(f"{n} brands seed ")

# def seed_item(n):
#     fake=Faker()
#     images=['image (1).jpg','image1 (2).jpg','image1 (3).jpg','image1 (4).jpg','image1 (5).jpg','image1 (6).jpg','image1 (7).jpg','image1 (8).jpg','image1 (9).jpg','image1 (10).jpg','image1 (11).jpg','image1 (12).jpg','image1 (13).jpg']
#     STATUS = [ 'Available','Sold','Returns']
#     COLORS=['Black','Grey','White','Blue','Brown','Red']
#     Active=['True','False']

#     for _ in range(n):
#         Item.objects.create(
#             name=fake.name(),
#             image=f"Items/{images[random.randint(0,12)]}",
#             quantity=random.randint(1,10),
#             price=round(random.uniform(999.99,9999.99),2),
#             details=fake.text(max_nb_chars=500),
#             active=Active[random.randint(0,1)],
#             status=STATUS[random.randint(0,2)],
#             colors=COLORS[random.randint(0,5)],
#             category=Category.objects.get(id=random.randint(1,7)),
#         )
#     print(f"{n} items seed ")
    
# seed_item(250)


def seed_item_price(n):
    fake=Faker()

    for _ in range(n):
            item=Item.objects.get(id=random.randint(2,250))
            price=item.price+2000
            item.price_sales=price
            item.save()
    print(f"{n} items seed ")
    
seed_item_price(200)