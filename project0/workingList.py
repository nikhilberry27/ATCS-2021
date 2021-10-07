careers = ["doctor", "programmer", "truck driver", "flight attendent"]
print ("index of 'programmer' = ", careers.index("programmer"))
print ("programmer" in careers)
careers.append("waiter")
careers.insert(0, "scientist")
for career in careers:
    print(career)