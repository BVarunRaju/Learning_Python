#Program for: Cover price of book is $24.95 with a 40% discount. Shipping cost is $3 for the first book and $0.75 for rest of the books.
#What is the total wholesale cost of 60 copies?
book_price=24.95
discount=0.6
shipping_first=3
shipping_rest=0.75
total_books=60
total_cost=(book_price*discount*total_books)+shipping_first+(total_books-1)*shipping_rest
print("The total cost for 60 books is:$",total_cost)