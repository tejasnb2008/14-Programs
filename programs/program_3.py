def simple_interest(p, t, r):
    si = (p * t * r) / 100
    return si

def compound_interest(p, t, r):
    ci = p * ((1 + r/100)**t) - p
    return ci

p = float(input("Enter principal amount: "))
t = int(input("Enter time period (in years): "))
r = float(input("Enter annual interest rate (in %): "))

si = simple_interest(p, t, r)
ci = compound_interest(p, t, r)
diff = ci - si

print("Simple Interest", si)
print("Compound Interest", ci)
print("Difference between CI and SI:", diff)