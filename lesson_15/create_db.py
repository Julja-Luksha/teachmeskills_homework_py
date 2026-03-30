import uuid

from src.db_connector import engine, session
from src.models import *

Base.metadata.create_all(engine)


session.add_all([
    Product(name="Кружка", cost=10, count=5),
    Product(name="Ручка", cost=2, count=20),
    Product(name="Блокнот", cost=15, count=5)
])
session.add_all([
    Ticket(uuid=str(uuid.uuid4())),
    Ticket(uuid=str(uuid.uuid4())),
    Ticket(uuid=str(uuid.uuid4()))
])
session.commit()
