def total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['cost']*item['quantity']
    return total_cost
cart=[
    {'name':'banana','cost':2,'quantity':5},
    { 'name':'apple','cost':200,'quantity':0.5},
    { 'name':'grapes','cost':80,'quantity':1}
    ]
print(total_cost(cart))