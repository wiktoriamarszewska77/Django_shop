import factory
from users.models import User, Company


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("username")
    phone = factory.Faker("123456789")
    address = factory.Faker("address")
    password = factory.Faker("TestPassword123!")


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("Name")
    address = factory.Faker("address")
    nip = factory.Faker("1234567890")
