# create a function discount that takes two arguments cost and d 'discount percentage' as input,and it should return the cost after reducing the discounted price from the original price

# Test cases
# ip : discount(100,50)
# op : 50

# ip : discount(200,20)
# op: 160

acc_cost = int(input())

dis_cost = int(input())

def discount(acc_cost, dis_cost):
    print(acc_cost - dis_cost)

discount(acc_cost, dis_cost)