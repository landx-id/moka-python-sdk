from moka_python_sdk.moka import Moka


API_KEY = "test_f7f7955d44cd10dd2bbbdc4381eb8d4c"
SECRET_KEY = "d269d087-25a6-49fa-b17c-22cd1b23c515"
x = Moka(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

library = x.Library
print("Get All Categories:")
print(library.category.get(
    outlet_id=1,
    page=1,
    per_page=10,
    include_deleted=True
))