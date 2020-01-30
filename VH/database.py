from model import Base, User


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(input_email, input_username, input_password):
    """
    Add a user to the database, given
    their email 
    """
    user_object = User(
        email=input_email,
        username=input_username,
        password=input_password)
    session.add(user_object)
    session.commit()

# add_user("immail", "imuname", "impass")


def query_all():
   """
   Get all the products
   in the database.
   """
   users = session.query(
      User).all()
   return users



def query_by_mail(prod_mail):
   """
   Find the first product
   in the database, by its id
   """
   user = session.query(
       User).filter_by(
       email=prod_mail).first()
   return user

def delete_user(prod_id):
   """
   Delete user with certain id
   """
   session.query(User).filter_by(
       id=prod_id).delete()
   session.commit()
# print(query_by_mail("ranif"))

# DISPLAYS USERS

for prod in query_all():
  print(prod.email, prod.username, prod.id)

# DELETES USERS DELETES

# for prod in query_all():
#   delete_user(prod.id)

# def update_price (prod_id, price):
#    """
#    Update a product in the database, with price
#    """
#    product = session.query(
#        Product).filter_by(
#        id=prod_id).first()
#    product.price = price
#    session.commit()


# #update_lab_status(0, 250.00)



def delete_all():
   """
   Delete product with certain id
   """
   session.query(
      User).all().delete()
   session.commit()

# def add_to_cart(prod_id):
#     """
#     Add a product to the cart
#     """
#     cart_object = Cart(
#         product_id=prod_id)
#     session.add(cart_object)
#     session.commit()