#!/usr/bin/env python

prices = {
    "GOOG" : 490.10,
    "AAPL" : 123.50,
    "IBM"  : 91.50,
    "MSFT" : 52.13
}

if "GOOG" in prices:
    p = prices["GOOG"]
else:
    p = 'NA'
print p

s = prices.get("SOX", 'NA')
print s
