# Moka Python Library

This library is the abstraction of Moka API for access from applications written with Python.

## Table of Contents

- [Moka Python Library](#moka-python-library)
  - [Table of Contents](#table-of-contents)
  - [API Documentation](#api-documentation)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [API Key](#api-key)
    - [Merchant](#merchant)
      - [Show Business Info](#show-business-info)
    - [Transaction](#transaction)
      - [Get latest transaction](#get-latest-transaction)
      - [Get all open bills](#get-all-open-bills)
    - [Report](#report)
      - [Category Sales](#category-sales)
      - [Modifier Sales](#modifier-sales)
      - [Discount Sales](#discount-sales)
      - [Tax Sales](#tax-sales)
  - [License](#license)


## API Documentation
Please check [Moka API Reference](https://api.mokapos.com/docs).

## Requirements

Python 3.7 or later

## Installation

To use the package, run ```pip install moka-python-sdk```

## Usage

### API Key

```python
from moka_python_sdk.moka import Moka

API_KEY = "test_f7f7955d44cd10dd2bbbdc4381eb8d4c"
SECRET_KEY = "d269d087-25a6-49fa-b17c-22cd1b23c515"
x = Moka(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

# Then access each class from x attribute
merchant = x.Merchant
```


### Merchant
Get information about merchant

#### Show Business Info

```python
merchant = x.Merchant
merchant.show_business_info()
```

Usage example:

```python
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
``` 

Reference: https://api.mokapos.com/docs#tag/Business


### Transaction
#### Get latest transaction
```python
transaction = x.Transaction

print("Show Latest Transaction:")
print(transaction.show_latest(
    outlet_id=1,
    per_page=10,
    include_promo=True
))
```
Reference: https://api.mokapos.com/docs#operation/showLatestTransactionsV3

#### Get all open bills
```python
transaction = x.Transaction

print("Get All Open Bill: ")
print(transaction.bill.get(
    outlet_id=1,
    page=1,
    per_page=10,
    dine_in_only=True,
    deep=True
))
```
Reference: https://api.mokapos.com/docs#operation/listBillsV1
### Report
#### Category Sales
```python
report = x.Report
report.show_category_sales(
    outlet_id=1,
    per_page=10,
)
```
Reference: https://api.mokapos.com/docs#operation/showCategorySalesV2

#### Modifier Sales
```python
report = x.Report
report.show_modifier_sales(
    outlet_id=1,
    per_page=10,
)
```
Reference: httpshttps://api.mokapos.com/docs#tag/Modifier-Sales

#### Discount Sales
```python
report = x.Report
report.show_discount_sales(
    outlet_id=1,
    per_page=10,
)
```
Reference: https://api.mokapos.com/docs#tag/Discount-Sales

#### Tax Sales
```python
report = x.Report
report.show_tax_sales(
    outlet_id=1,
    per_page=10,
)
```
Reference: https://api.mokapos.com/docs#tag/Tax-Sales

## License

MIT License