user = [
    {"id": 1, "total":100, "coupon": "p20"},
    {"id": 2, "total":150, "coupon": "f20"},
    {"id": 3, "total":90, "coupon": "l20"}
]

discounts = {
    "p20":(0.2,0),
    "f20":(0.5,0),
    "l20":(0,10)
}

for user in user:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discounts = user["total"] * percent + fixed
    print(f"user {user['id']} paid {user['total']} and got discount for next visit of rupees {discounts}")