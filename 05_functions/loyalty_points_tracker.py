loyalty_points = 0

def process_transactions(transactions: list[int]) -> int:
    total = 0
    def apply_bonus():
        nonlocal total
        if transactions > 1000:
            total += 50
            global loyalty_points
            loyalty_points = (total / 100) * 1
        return total



#
# def process_transactions(transactions: list[int]) -> int:
#     # Write your code below this line
#     def apply_bonus():
#         nonlocal total
#         if total > 1000:
#             total += 50  # bonus for high spenders
#
#     total = 0
#
#     for amount in transactions:
#         total += amount
#
#     apply_bonus()
#
#     # update global loyalty_points
#     global loyalty_points
#     loyalty_points += total // 100  # earn 1 point per ₹100
#
#     return total