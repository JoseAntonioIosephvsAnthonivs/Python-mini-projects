from faker import Faker
from faker.providers import internet

fake = Faker('pt_BR') #pt_BR
fake.add_provider(internet)


for i in range(10): #printar 10 nomes, endereços, telefones e ips

    print('Nome: ',fake.name())
    print("Endereço:",fake.address())
    print("Telefone:", fake.phone_number())
    print('ipv4:',fake.ipv4_private())



