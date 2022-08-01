import os
from moka_python_sdk.moka import Moka

API_KEY = "test_f7f7955d44cd10dd2bbbdc4381eb8d4c"
SECRET_KEY = "d269d087-25a6-49fa-b17c-22cd1b23c515"
x = Moka(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

merchant = x.Merchant

print("Business Info:")
print(merchant.show_business_info())

print("Customer List:")
print(merchant.get_list_customer(
    business_id=1,
    mobile_device=1,
    page=1,
    per_page=10,
    include_deleted=True,
    include_loyalty=True,
))

print("Business Checkout Setting:")
print(merchant.get_business_checkout_setting(
    business_id=1,
))

print("List Outlets:")
print(merchant.get_list_outlets(
    business_id=1,
))





