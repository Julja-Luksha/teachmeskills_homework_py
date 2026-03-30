from .models import User, Ticket, Product, Order
from .settings import TICKET_POINTS
from .db_connector import session


class UserService:
    @staticmethod
    def register(username: str, password: str):
        if User.is_exist(session, username):
            return None
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        return new_user

    @staticmethod
    def login(username: str, password: str):
        user = (
            session.query(User)
            .filter(
                User.username == username,
                User.password == password
            )
            .first()
        )
        return user


class TicketService:
    @staticmethod
    def redeem_ticket(user: User, ticket_uuid: str) -> bool:
        ticket = Ticket.valid_ticket(session, ticket_uuid)
        if not ticket:
            return False
        ticket.available = False
        ticket.user_id = user.id
        user.points += TICKET_POINTS
        session.commit()
        return True


class ProductService:
    @staticmethod
    def get_available_products():
        products = (
            session.query(Product)
            .filter(Product.count > 0)
            .order_by(Product.id)
            .all()
        )
        return products

    @staticmethod
    def get_product_by_id(product_id: int):
        return session.query(Product).filter(Product.id == product_id).first()


class OrderService:
    @staticmethod
    def create_order(user: User, product: Product, count: int):
        if count <= 0:
            return None
        if product.count < count:
            return None
        total_cost = product.cost * count
        if user.points < total_cost:
            return None
        product.count -= count
        user.points -= total_cost
        new_order = Order(
            user_id=user.id,
            product_id=product.id,
            count=count
        )
        session.add(new_order)
        session.commit()
        return new_order
