from shop import Address, User

def create_user(is_major:bool=True, name:str="bob", email:str="bob@gmail.com", has_address_local:bool=True, is_verified: bool=True):
  address= Address(
    line1="",
    line2="",
    city="",
    zip_code="",
    country= "USA" if has_address_local else "France"
    )
  return User(
      name=name,
      email=email,
      age=25 if is_major else 12,
      address=address,
      is_verified=is_verified
  )
