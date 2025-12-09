# Multithreading
# threading.Thread(target = my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finished walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You took out the trash")

def get_mail():
    time.sleep(4)
    print("You got the mail")

# We are multi-tasking, we are starting everything at the same time

chore1 = threading.Thread(target = walk_dog, args = ("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target = take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

#with join method, we wait for the thread tasks to finish to go on to the next statements
chore1.join()
chore2.join()
chore3.join()

print("All chores are completed!")

