def analyse(orders):
    revenue = {}
    product_count = {}
    customers = set()
    for order in orders:
        customer = order['customer']
        status = order['status']
        customers.add(customer)
        # Ignore cancelled orders
        if status != 'CANCELLED':
for product, quantity, price in order['items']:
# Calculate customer revenue
revenue[customer] = revenue.get(customer, 0) + quantity * price
# Count product quantity
product_count[product] = product_count.get(product, 0) + quantit
# Find customers whose all orders are delivered
fully_delivered = sorted([
customer for customer in customers
if all(order['status'] == 'DELIVERED'
for order in orders if order['customer'] == customer)
])
# Find top 2 selling products
top_products = sorted(
product_count.items(),
key=lambda x: (-x[1], x[0])
)[:2]
return {
'revenue': revenue,
'top_products': top_products,
'fully_delivered': fully_delivered
}
# Order details
orders = [
{
'id': 101,
'customer': 'Asha',
'status': 'DELIVERED',
'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
},
{
'id': 102,
'customer': 'Ravi',
'status': 'CANCELLED',
'items': [('monitor', 1, 10999.0)]
},
{
'id': 103,
'customer': 'Asha',
'status': 'DELIVERED',
'items': [('cable', 5, 199.0)]
},
{
'id': 104,
'customer': 'Meera',
'status': 'SHIPPED',
'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
},
{
'id': 105,
'customer': 'Ravi',
'status': 'DELIVERED',
'items': [('mouse', 3, 599.0)]
    }
]
print(analyse(orders))
