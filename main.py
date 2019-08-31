
from controle_cubo import controle_cubo

def getCommand(text):
    splitted = text.split(" ")

    if text == '':
        splitted = ['empty']
    elif len(splitted[0]) < 3 and not text == '-':
        splitted.insert(0, "move")
    
    return splitted

ctrl = controle_cubo()

while True:
    ctrl.print()

    text = input("$ ")

    command = getCommand(text)
    ctrl.run_command(command)
