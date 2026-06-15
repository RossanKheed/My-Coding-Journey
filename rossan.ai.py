print ("ROSSAN'S AI")
user_name = input ("What is your username :").upper()
print (f"A bot to help students. And if you ain't ready {user_name}.  Just type 'exist' to stop")
while True:
    question = input("Ask :").lower()
    
    if question == "exist":
        print ("Welcome to ROSSAN'S AI, have a nice day")
        break
    elif "matter" in question :
        print ("Well, Matter is the anything that has mass or weight and occupies space. So examples of matter are like Books,Sun,Pond of water,person, etc")
    elif "photosynthesis" in question :
         print ("Actually, Photosynthesis is the process where green plants make their own foods through sunlight 🌞")
    elif "atom" in question :
         print ("Atom is the smallest unit of a matter  ")
    elif "cell" in question :
         print("Cell is the smallest unit of life. Every living thing has a cell, there is plant cell and animal cell")
    elif "environment" in question :
        print ("Actually Environment is the everything that sorounds us. Everything sorounds us is Environment, when you talk about plants,animals,Pond of water, sky, air ,etc") 
    else :
          print (f"Sorry! {user_name} but ROSSAN'S AI have no access and don't know that yet, Welcome to ROSSAN'S AI")