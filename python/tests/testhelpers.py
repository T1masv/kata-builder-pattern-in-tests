from Shop import User

def create_user_with_age_verified(age:int=25, vefified:bool=True, name:str="bob", email:str="bob@gmail.com", address:str="1 boulevard jean jaures"):
  return User(
      name=name,
      email=email,
      age=age,
      address=address,
      verified=verified
  )
    
