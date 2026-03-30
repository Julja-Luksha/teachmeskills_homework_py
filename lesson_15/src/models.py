from datetime import datetime

from sqlalchemy import String, Integer, Boolean, ForeignKey, Text, BigInteger, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    points: Mapped[int] = mapped_column(Integer, default=0)

    def __str__(self):
        return f"User<{self.username}, points={self.points}>"

    @staticmethod
    def is_exist(session, username:str) -> bool:
        user = session.query(User).filter(User.username == username).first()
        return user is not None

    def orders(self, session):
        result = (
            session.query(Order, Product)
            .join(Product, Order.product_id == Product.id)
            .filter(Order.user_id == self.id)
            .order_by(Order.order_date.desc())
            .all()
        )
        return result

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable= True)

    def __str__(self):
        status = "доступен" if self.available else "был использован"
        return f"Ticket<{self.uuid}, {status}"

    @staticmethod
    def valid_ticket(session, ticket_uuid: str):
        ticket = (
            session.query(Ticket)
            .filter(
                Ticket.uuid == ticket_uuid,
                Ticket.available == True,
            )
            .first()
        )
        return ticket

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    cost: Mapped[int] = mapped_column(BigInteger, default=0)
    count: Mapped[int] = mapped_column(BigInteger, default=0)

    def __str__(self):
        return f"{self.id:<3} {self.name:<25} цена: {self.cost:<5} количество: {self.count}"

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="RESTRICT"))
    count: Mapped[int] = mapped_column(BigInteger, default=0)
    order_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __str__(self):
        return f"Order<{self.id}, user={self.user_id}, product={self.product_id}, count={self.count}>"