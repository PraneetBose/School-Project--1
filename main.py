 # Python3 Program to find the
#  net amount of products after 10% discount on the articles

# storing the amount of 1 Article in  "num"
num = int(input("cost of 1 articles is = "))

# storing the number of articles in x and the multiplying it with the amount of 1 article
x = int(input("Quantity of articles - "))
print("Total price of the Articles=", x * num)
# storing the value of x*num in y
y = x * num
# finding the amount after 10% of discount on the total
print("Your net amount after 10% Discount =", y - 10 / 100 * y)
