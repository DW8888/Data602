days_of_the_week=["Monday","Tuesday","Wednesday","Thurday","Friday","Saturday","Sunday"]
sales_of_the_week=[]

for day in days_of_the_week:
    sale=int(input (f"Pleease enter the sales for {day}:\n"))
    sales_of_the_week.append(sale)

weekly_sales=sum(sales_of_the_week)
print(sales_of_the_week, f"\nThe total sales for the week are $10{weekly_sales}")