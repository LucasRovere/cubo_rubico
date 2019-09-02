
from modelo_cubo import modelo_cubo
from track_operator import track_operator
import os

class controle_cubo:
    def __init__(self):
        self.tracks = {}
        self.states = {}
        self.last_moves = []
        self.current_track = []
        self.current_track_pos = 0
        self.cubo = modelo_cubo(3)
        self.message = ''
        self.track_op = track_operator()

    def run_command(self, command):
        if command[0] == "empty" and len(self.current_track) > 0:
            command = ['step']
        elif command[0] == "-" and len(self.current_track) > 0:
            command = ['step', '-']

        # move o cubo
        if command[0] == "move":
            try:
                self.move_cubo(command)
                self.last_moves.append(command)
            except:
                self.message = "Error on move"

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
            self.restart(command)

        # reinicia o tracking / salva o tracking atual
        elif command[0] == "track":
            if len(command) > 1:
                self.last_moves.append(['end'])
                self.last_moves.insert(0, ['start'])
                self.tracks[command[1]] = self.last_moves

                self.message = "Saved track: " + command[1]
            else:
                self.message = "Missing arguments: [name]"

            self.last_moves = []

        # salva o estado atual
        elif command[0] == "state":
            if len(command) > 1:
                state_name = command[1]
                self.states[state_name] = [self.cubo.faceUp, self.cubo.faceDown,
                                           self.cubo.faceFront, self.cubo.faceBack,
                                           self.cubo.faceRight, self.cubo.faceLeft]

                self.message = "Saved state: " + command[1]
            else:
                self.message = "Missing arguments: [name]"

        # mostra tracks e states
        elif command[0] == "show":
            show_tracks = True
            show_states = True

            if len(command) > 1:
                if command[1] == "tracks":
                    show_states = False
                elif command[1] == "states":
                    show_tracks = False

            i = 1
            if show_states:
                self.message += "States:\n"
                for name in self.states:
                    self.message += "  " + str(i) + ". " + name + "\n"
                    i += 1

            i = 1
            if show_tracks:
                self.message += "Tracks:\n"
                for name in self.tracks:
                    self.message += "  " + str(i) + ". " + name + "\n"
                    i += 1

        # carrega track ou state
        elif command[0] == "load":
            if len(command) == 1:
                self.message = "Missing arguments: [track/state] [name]"
            elif len(command) == 2:
                self.message = "Missing arguments: [name]"
            elif command[1] == "track":
                try:
                    self.current_track = self.tracks[command[2]]
                    self.message = "Loaded track " + command[2]
                    self.current_track_pos = -1
                except:
                    self.message = "Couldn't load track " + command[2]
            elif command[1] == "state":
                try:
                    state = self.states[command[2]]
                    self.cubo.setState(state)
                    self.message = "Loaded state " + command[2]
                except:
                    self.message = "Couldn't load state " + command[2]

        # roda 1 passo da track atual
        elif command[0] == "step":
            if len(self.current_track) == 0:
                self.message = "No track loaded"
                return

            if self.current_track_pos == -1:
                self.current_track_pos += 1
                return

            if len(command) > 1 and command[1] == "-":
                self.move_cubo_inverted(
                    self.current_track[self.current_track_pos])
                if self.current_track_pos > 0:
                    self.current_track_pos -= 1
            else:
                if self.current_track_pos < len(self.current_track) - 1:
                    self.current_track_pos += 1
                    self.move_cubo(self.current_track[self.current_track_pos])

        # roda a track atual completa
        elif command[0] == "run":
            self.run(command)
        elif command[0] == "close":
            self.current_track = []

        elif command[0] == "undo":
            if len(self.last_moves) == 0:
                self.message = "No moves to undo"
                return

            move = self.last_moves.pop()
            self.move_cubo_inverted(move)

        elif command[0] == "trackop" or command[0] == "top":
            operation = ''
            track = ''

            try:
                operation = command[1]
            except:
                self.message = "Missing argument [operation]"
                return

            try:
                track = self.tracks[command[2]]
            except:
                if len(self.current_track) > 0:
                    track = self.current_track
                else:
                    self.message = "Couldn't load track"
                    return

            self.current_track = self.track_op.run(operation, track)
            self.current_track_pos = -1

        elif command[0] != "empty":
            self.message = "Unknown command"

    def print(self):
        os.system('clear')
        if self.message == '' or self.message == "Unknown command":
            self.cubo.printFaces()
            print("")
            # print("last moves: " + str(self.last_moves))
            if len(self.current_track) > 0:
                ctrack = "current track: \n   "
                for i in range(len(self.current_track)):
                    selected = (i == self.current_track_pos)
                    move = self.current_track[i]

                    for s in move:
                        if not s == 'move':
                            if selected:
                                ctrack += "\033[0;30;47m" + s + "\033[0;37;40m"
                            else:
                                ctrack += s

                    ctrack += " "

                print(ctrack)

        if not self.message == '':
            print("")
            print(self.message)
            self.message = ''

    def restart(self, command, size_param = 0):
        size = self.cubo.size
        debug = False

        if size_param == 0:
            try:
                size = int(command[1])
            except:
                pass

            try:
                debug = (command[2] == "debug")
            except:
                debug = False
        else:
            size = size_param
            debug = False

        self.last_moves = []
        self.cubo.restart(size, debug)
        self.message = "Restarting cube with size: " + str(size)

    def run(self, command, is_track = False):
        track = []
        if not is_track:
            try:
                invert = False
                track = self.tracks[command[1]].copy()
                if len(command) > 2:
                    if command[2] == "-":
                        invert = True
                        track.reverse()
            except:
                self.message = "Couldn't load track"
                return
        else:
            track = command

        for move in track:
            if not invert:
                self.move_cubo(move)
            else:
                self.move_cubo_inverted(move)
        
    def get_state(self):
        return [self.cubo.faceUp, self.cubo.faceDown,
                self.cubo.faceFront, self.cubo.faceBack,
                self.cubo.faceRight, self.cubo.faceLeft]

    def move_cubo_inverted(self, command):
        if command[0] == 'end' or command[0] == 'start':
            return

        new_command = command.copy()
        
        if command[1].__contains__("'"):
            new_command[1].replace("'", "")
        else:
            new_command[1] += "'"

        self.move_cubo(new_command)

    def move_cubo(self, command):
        if command[0] == 'end' or command[0] == 'start':
            return

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
            else:
                self.last_moves.pop()
