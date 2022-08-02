from moka_python_sdk.moka import Moka


API_KEY = "test_f7f7955d44cd10dd2bbbdc4381eb8d4c"
SECRET_KEY = "d269d087-25a6-49fa-b17c-22cd1b23c515"
x = Moka(api_key=API_KEY, secret_key=SECRET_KEY, production=False)

report = x.Report

print("Category Sales:")
print(report.show_category_sales(
    outlet_id=1,
    per_page=10,
))

print("Collector Sales: ")
print(report.get_collector_sales(
    outlet_id=1,
    per_page=10
))


print("Modifier Sales:")
print(report.show_modifier_sales(
    outlet_id=1,
    per_page=10
))

print("Discount Sales:")
print(report.show_discount_sales(
    outlet_id=1,
    per_page=10
))

print("Tax Sales: ")
print(report.show_tax_sales(
    outlet_id=1,
    per_page=10
))

print("Gratuity Sales:")
print(report.show_gratuity_sales(
    outlet_id=1,
    per_page=10
))

print("Server Sales: ")
print(report.show_server_sales(
    outlet_id=1,
    per_page=10
))

print("Item Sales: ")
print(report.show_item_sales(
    outlet_id=1,
    per_page=10
))

print("Sales Summary: ")
print(report.show_sales_summary(
    outlet_id=1,
    per_page=10
))

print("Payment Method: ")
print(report.show_payment_methods(
    outlet_id=1,
    per_page=10
))


