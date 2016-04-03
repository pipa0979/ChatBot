'''
import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input("Enter your message >> "))
'''

import aiml
import os
import requests,json


kernel = aiml.Kernel()
sessionId = 1
sessionData = kernel.getSessionData(sessionId)
url='http://api.openweathermap.org/data/2.5/weather?q=Boulder,CO,USA&appid=83364ebafb88eff14f89615a7067812f'
# Get session info as dictionary. Contains the input
# and output history as well as any predicates known
data = requests.get(url)
data=data.json()
data=str(data)





if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
# kernel now ready for use

kernel.setPredicate("dog", "Brandy", sessionId)
clients_dogs_name = kernel.getPredicate("dog", sessionId)


'''
kernel.setBotPredicate("hometown", data)
bot_hometown = kernel.getBotPredicate("hometown")
'''
kernel.setPredicate("hometown", data, sessionId)
bot_hometown = kernel.getPredicate("hometown",sessionId)


while True:
    message = raw_input("Enter your message to the bot: ")

    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message, sessionId)

        print bot_response
        # Do something with bot_response