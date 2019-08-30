
from controle_cubo import controle

def getCommand(text):
    splitted = text.split(" ")

    if text == '':
        splitted = ['empty']
    elif len(splitted[0]) < 3 and not text == '-':
        splitted.insert(0, "move")
    
    return splitted

ctrl = controle()

while True:
    ctrl.print()

    text = input("$ ")

    command = getCommand(text)
    ctrl.run_command(command)
