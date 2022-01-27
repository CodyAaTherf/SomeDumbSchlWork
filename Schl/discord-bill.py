bill_amt = float(input("Bill Amount: "))

def calc_dis(bill_amt):
    if bill_amt > 2000:
        return bill_amt*(1-.15)
    if bill_amt >= 1501 and bill_amt <= 2000:
        return bill_amt*(1-.08)
    if bill_amt >= 1000 and bill_amt <= 1500:
        return  bill_amt*(1)
    return bill_amt

print(f"Total bill amount = {calc_dis(bill_amt)}")

"""
I HAVE MADE THIS ONE A BIT SIMPLE. I COULD HAVE USED `if __name__ == "__main__":`
"""