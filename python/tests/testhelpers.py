from shop import User

def create_user(age:int=25, vefified:bool=True, name:str="bob", email:str="bob@gmail.com", address:str="1 boulevard jean jaures", verified: bool=True):
  return User(
      name=name,
      email=email,
      age=age,
      address=address,
      verified=verified
  )
    
