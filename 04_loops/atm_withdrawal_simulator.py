withdrawals = []
Amount = 1000
withdrawAmount = 0

while withdrawAmount <= Amount:
    withdrawAmount = int(input("Please enter the amount you want to withdraw"))
    withdrawals.append(f"Withdrawn: {withdrawAmount}")
    Amount -= withdrawAmount
    print(Amount)

print(withdrawals)


# def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
#     # Write your code below this line
#     result = []
#     index = 0
#     while index < len(withdrawals):
#         amount = withdrawals[index]
#         if amount <= balance:
#             balance -= amount
#             result.append(f"Withdrawn: {amount}")
#         else:
#             result.append(f"Insufficient funds for requested amount: {amount}")
#         index += 1
#     result.append(f"Remaining Balance: {balance}")
#     return result
