names = ["Bryn", "Nikhil", "Sean", "Salma", "Tommy"]

def crowd_test(names):
    if(len(names) > 3):
        print ("The room is crowded, it has more than 3 people.")
crowd_test(names)
del names[0:2]
crowd_test(names)