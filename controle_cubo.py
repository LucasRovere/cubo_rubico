
from modelo_cubo import modelo_cubo

class controle:
    def __init__(self):
        self.tracks = {}
        self.states = {}
        self.last_moves = []
        self.current_track = []
        self.cubo = modelo_cubo(3) 

    def run_command(self, command):
        # move o cubo
        if command[0] == "move":
            shifts = []
            
            if len(command) < 3:
                shifts.append(0)
            elif command[2].__contains__('-') or command[2].__contains__('+'):
                for i in range(len(command[2])):
                    if command[2][i] == '+':
                        shifts.append(i)
            else:
                shifts.append(int(command[2]))

            for shift in shifts:
                if command[1] == "u":
                    self.cubo.moveU(shift)
                elif command[1] == "u'":
                    self.cubo.moveU_(shift)
                elif command[1] == "d":
                    self.cubo.moveD(shift)
                elif command[1] == "d'":
                    self.cubo.moveD_(shift)
                elif command[1] == "f":
                    self.cubo.moveF(shift)
                elif command[1] == "f'":
                    self.cubo.moveF_(shift)
                elif command[1] == "b":
                    self.cubo.moveB(shift)
                elif command[1] == "b'":
                    self.cubo.moveB_(shift)
                elif command[1] == "r":
                    self.cubo.moveR(shift)
                elif command[1] == "r'":
                    self.cubo.moveR_(shift)
                elif command[1] == "l":
                    self.cubo.moveL(shift)
                elif command[1] == "l'":
                    self.cubo.moveL_(shift)
            
        elif command[0] == "spin":
            for shift in range(0, self.cubo.size):
                if command[1] == "left":
                    self.cubo.moveU(shift)
                elif command[1] == "right":
                    self.cubo.moveU_(shift)
                elif command[1] == "unclock":
                    self.cubo.moveF(shift)
                elif command[1] == "clock":
                    self.cubo.moveF_(shift)
                elif command[1] == "up":
                    self.cubo.moveR(shift)
                elif command[1] == "down":
                    self.cubo.moveR_(shift)

        # reinicia o cubo com um tamanho escolhido
        elif command[0] == "restart":
            size = self.cubo.size
            debug = False

            try:
                size = int(command[1])
            except:
                pass

            try:
                debug = (command[2] == "debug")
            except:
                debug = False

            self.cubo.restart(size, debug)

        # reinicia o tracking / salva o tracking atual
        elif command[0] == "track":
            pass
        # salva o estado atual
        elif command[0] == "state":
            pass
        # mostra tracks e states
        elif command[0] == "show":
            pass
        # carrega track ou state
        elif command[0] == "load":
            pass
        # roda 1 passo da track atual
        elif command[0] == "step":
            pass
        # roda a track atual completa
        elif command[0] == "run":
            pass

    def print(self):
        self.cubo.printFaces()
        print("")
        print("last moves: " + str(self.last_moves))
        print("current track: " + str(self.current_track))

    def move(self, command):
        pass

    