mountains = {"Mount Everest": 8848,
             "K2": 8611,
             "Cho Oyu": 8188,
             "Manaslu": 8163,
             "Nanga Parbat": 8126,
             }

for key_name in mountains.keys():
    print("The mountain name is: ", key_name)

for value_name in mountains.values():
    print("The elevation is: ", value_name)

for k_name, v_name in mountains.items():
    print(k_name, " is ", v_name, " meters tall.")

