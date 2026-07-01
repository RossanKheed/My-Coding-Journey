# chatbot for simple science definitions 
print ("=======💀ROSSAN'S AI💀=======")
user_name = input ("What is your username :").upper()
print (f"Im here to help you with some science definitions. And if you ain't ready {user_name}.  Just type 'exit' to stop")

    
print("I only know some of some science definitions including ; matter, photosynthesis, waste, atom,laboratory, cell, environment as well as library.So I only know about these !. So I'll only help you with one of these stuffs !")

while True:
    question = input("Ask :").lower()
# stop / break the codes     
    if question == "exit":
        print ("Welcome to ROSSAN'S AI, have a nice day")
        break 
    
    elif "matter" in question :
        print ("Well, Matter is the anything that has mass or weight and occupies space. So examples of matter are like Books,Sun,Pond of water,person, etc")
        
    elif "photosynthesis" in question :
         print ("Actually, Photosynthesis is the process where green plants make their own foods through sunlight 🌞")
    elif "waste" in question :
        print("Waste is the unwanted material that are no longer needed. Eg; broken glass, used plastics, dirty water")    
    elif "library" in question :
        print("Actually, Library is the room or place where books are kept")    
    elif "atom" in question :
         print ("Atom is the smallest unit of a matter  ")
    elif "cell" in question :
         print("Cell is the smallest unit of life. Every living thing has a cell, there is plant cell and animal cell")
    elif "laborat" in question :
        print ("Laboratory is the room or building specifically used for performing experiments")
         
    elif "environment" in question :
        print ("Actually Environment is the everything that sorounds us. Everything sorounds us is Environment, when you talk about plants,animals,Pond of water, sky, air ,etc") 
# don't know the clarification yet   
    else :
          print (f"Sorry! {user_name} but ROSSAN'S AI have no access and don't know {question} yet, Welcome to ROSSAN'S AI")