#!/usr/bin/env python
# requires portfolio.csv in the same directory as this script.

# File containing lines of the form "name,shares,price"
filename = "portfolio.csv"
portfolio = []
for line in open(filename):
    fields = line.split(",")       # Split each line into a list
    name   = fields[0]             # Extract and convert individual fields
    shares = int(fields[1])
    price  = float(fields[2])
    stock  = (name,shares,price)   # Create a tuple (name, shares, price)
    portfolio.append(stock)        # Append to list of records

print 
print 'portfolio 2 is:', portfolio[1]
print 'stock price of portfolio 2 is:', portfolio[1][2]

total = 0.0
for name, shares, price in portfolio:
    total += shares * price
print 'total portfolio value is:', str(total)
print
