from Shop import User

def create_user_with_age_verified(age:int, vefified:bool):
  return User(
      name="bob",
      email="bob@gmail.com",
      age=age,
      address="1 boulevard jean jaures",
      verified=verified
  )
    
