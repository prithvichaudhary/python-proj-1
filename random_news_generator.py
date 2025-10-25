import random 

subjects=["Rahul Gandhi",
          "Prithvi Chaudhary",
          "Virat Kohli",
          "Ronaldo Kumari",
          "Messi Devi",
          "Modi Don",
          "Arnav Singh",
          "Sritika Choudhary"]

actions=["makes momos",
        "watches anime",
        "eats golgappe",
        "marches ",
        "flies  ",
        "declared war ",
        "is boxing",
        "is dancing"]

place_or_things = ["at white house",
                  "in stadium",
                  "near shimla mall road",
                  "in surajkund mela",
                  "near srm college",
                  "at upper bazar road"]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)
    headline = f" Breaking News : {subject} {action} {place_or_thing} "
    print("\n"+ headline)
    response = input("Do you want to continue generating the headlines (yes/no)").strip().lower()
    if response == 'no':
        break
print("Thankyou for generating this headline have a nice day !!!!!!! ")

