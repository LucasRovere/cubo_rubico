

def main():
    print_faces = True
    current_track = []
    track_pos = 0
    c = cubo(3)

    while True:
        if print_faces:
            print("")
            c.printFaces()
            print("")

        if len(current_track) > 0:
            track_text = '    '
            for pos in current_track[0:track_pos]:
                track_text += pos + ' '

            track_text += '\033[0;30;47m' + \
                current_track[track_pos] + '\033[0;37;40m '

            for pos in current_track[track_pos + 1:]:
                track_text += pos + ' '

            print(track_text)

            text = input()

            if text == 'q':
                current_track = []
                text = ''
            elif text == 'r':
                text = ''
                if track_pos > 0:
                    track_pos -= 1
                    if len(current_track[track_pos]) == 2:
                        text = current_track[track_pos][0]
                    else:
                        text = current_track[track_pos] + "'"
            else:
                text = ''
                if track_pos < len(current_track) - 1:
                    text = current_track[track_pos]
                    track_pos += 1

        else:
            text = input()

        if len(text) == 0:
            print()
        elif text[0:7] == "restart":
            c.restart(text[8:])
        elif text[0:5] == "track":
            c.track(text[6:])
            print(c.tracks)
        elif text[0:3] == "run":
            current_track = c.run(text[4:])
            current_track.append(' ')
            track_pos = 0

        elif text[0:2] == "u'":
            c.moveU_(text[2:])
        elif text[0] == "u":
            c.moveU(text[1:])

        elif text[0:2] == "d'":
            c.moveD_(text[2:])
        elif text[0] == "d":
            c.moveD(text[1:])

        elif text[0:2] == "f'":
            c.moveF_(text[2:])
        elif text[0] == "f":
            c.moveF(text[1:])

        elif text[0:2] == "b'":
            c.moveB_(text[2:])
        elif text[0] == "b":
            c.moveB(text[1:])

        elif text[0:2] == "r'":
            c.moveR_(text[2:])
        elif text[0] == "r":
            c.moveR(text[1:])

        elif text[0:2] == "l'":
            c.moveL_(text[2:])
        elif text[0] == "l":
            c.moveL(text[1:])

class cubo:
    def __init__(self, size):
        self.size = size

        self.tracking = []
        self.tracks = {}

        self.faceUp = []
        self.faceDown = []
        self.faceFront = []
        self.faceBack = []
        self.faceRight = []
        self.faceLeft = []

        for i in range(size*size):
            self.faceUp.append('\033[1;33;40my\033[0;37;40m')
            self.faceDown.append('\033[1;37;40mw\033[0;37;40m')
            self.faceFront.append('\033[1;34;40mb\033[0;37;40m')
            self.faceBack.append('\033[1;32;40mg\033[0;37;40m')
            self.faceRight.append('\033[1;31;40mr\033[0;37;40m')
            self.faceLeft.append('\033[1;35;40mo\033[0;37;40m')

    def restart(self, size):
        self.size = int(size)

        self.faceUp = []
        self.faceDown = []
        self.faceFront = []
        self.faceBack = []
        self.faceRight = []
        self.faceLeft = []

        self.tracking = []

        for i in range(self.size*self.size):
            self.faceUp.append('\033[1;33;40my\033[0;37;40m')
            self.faceDown.append('\033[1;37;40mw\033[0;37;40m')
            self.faceFront.append('\033[1;34;40mb\033[0;37;40m')
            self.faceBack.append('\033[1;32;40mg\033[0;37;40m')
            self.faceRight.append('\033[1;31;40mr\033[0;37;40m')
            self.faceLeft.append('\033[1;35;40mo\033[0;37;40m')

            # Números para debug
            # self.faceUp.append('\033[1;33;40m' + str(i) + '\033[0;37;40m')
            # self.faceDown.append('\033[1;37;40m' + str(i) + '\033[0;37;40m')
            # self.faceFront.append('\033[1;34;40m' + str(i) + '\033[0;37;40m')
            # self.faceBack.append('\033[1;32;40m' + str(i) + '\033[0;37;40m')
            # self.faceRight.append('\033[1;31;40m' + str(i) + '\033[0;37;40m')
            # self.faceLeft.append('\033[1;35;40m' + str(i) + '\033[0;37;40m')

    def run(self, name):
        if(self.tracks[name]):
            return self.tracks[name]

        return []

    def track(self, name):
        print(self.tracking)

        if(name != ''):
            self.tracks[name] = self.tracking

        self.tracking = []

    def printFaces(self):
        spaces = '                                           '
        lines = '------------------------------------------------------------'
        counter = 0

        print(spaces[0:self.size*2 + 1] +
              lines[0:self.size*2 + 1] + spaces[0:4*self.size + 2])

        # face de cima
        for i in range(self.size):
            line = spaces[0:(1 + 2*self.size)]
            for j in range(self.size):
                line += '|' + self.faceUp[counter]
                counter += 1
            line += '|'

            print(line)

        counter = 0

        print(lines[0:4*(2*self.size + 1)])

        # faces laterais
        for i in range(self.size):
            counter = i * self.size
            line = ''

            for j in range(self.size):
                line += '|' + self.faceLeft[counter]
                counter += 1
            line += '|'

            counter = i * self.size

            for j in range(self.size):
                line += '|' + self.faceFront[counter]
                counter += 1
            line += '|'

            counter = i * self.size

            for j in range(self.size):
                line += '|' + self.faceRight[counter]
                counter += 1
            line += '|'

            counter = i * self.size

            for j in range(self.size):
                line += '|' + self.faceBack[counter]
                counter += 1
            line += '|'

            print(line)

        print(lines[0:4*(2*self.size + 1)])
        counter = 0

        # face de baixo
        for i in range(self.size):
            line = spaces[0:(1 + 2*self.size)]
            for j in range(self.size):
                line += '|' + self.faceDown[counter]
                counter += 1
            line += '|'

            print(line)

        print(spaces[0:self.size*2 + 1] +
              lines[0:self.size*2 + 1] + spaces[0:4*self.size + 2])

    def moveU(self, shift):
        if(len(shift) == 0):
            self.faceUp = self.rotateFace2(self.faceUp, True)

        positionsF = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))
        positionsR = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))
        positionsB = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))
        positionsL = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))

        faces = self.rotateSides([self.faceFront, self.faceRight, self.faceBack, self.faceLeft],
                                 [positionsF, positionsR, positionsB, positionsL])

        self.faceFront = faces[0]
        self.faceRight = faces[1]
        self.faceBack = faces[2]
        self.faceLeft = faces[3]

        self.tracking.append('u' + shift)

    def moveU_(self, shift):
        if(len(shift) == 0):
            self.faceUp = self.rotateFace2(self.faceUp, False)

        positionsF = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))
        positionsR = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))
        positionsB = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))
        positionsL = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))

        faces = self.rotateSides([self.faceFront, self.faceLeft, self.faceBack, self.faceRight],
                                 [positionsF, positionsL, positionsB, positionsR])
        self.faceFront = faces[0]
        self.faceLeft = faces[1]
        self.faceBack = faces[2]
        self.faceRight = faces[3]

        self.tracking.append("u'" + shift)

    def moveD(self, shift):
        if(len(shift) == 0):
            self.faceDown = self.rotateFace(self.faceDown, False)

        positionsF = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsR = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsB = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsL = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))

        faces = self.rotateSides([self.faceFront, self.faceRight, self.faceBack, self.faceLeft],
                                 [positionsF, positionsR, positionsB, positionsL])
        self.faceFront = faces[0]
        self.faceRight = faces[1]
        self.faceBack = faces[2]
        self.faceLeft = faces[3]

        self.tracking.append('d' + shift)

    def moveD_(self, shift):
        if(len(shift) == 0):
            self.faceDown = self.rotateFace(self.faceDown, True)

        positionsF = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsR = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsB = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsL = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))

        faces = self.rotateSides([self.faceFront, self.faceLeft, self.faceBack, self.faceRight],
                                 [positionsF, positionsL, positionsB, positionsR])
        self.faceFront = faces[0]
        self.faceLeft = faces[1]
        self.faceBack = faces[2]
        self.faceRight = faces[3]

        self.tracking.append("d'" + shift)

    def moveF(self, shift):
        if(len(shift) == 0):
            self.faceFront = self.rotateFace(self.faceFront, False)

        positionsU = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsR = []
        positionsL = []
        positionsD = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))

        for i in range(self.size):
            positionsL.append((i+1)*self.size - 1 - len(shift))
            positionsR.append(i*self.size + len(shift))

        faces = self.rotateSidesInverting([self.faceUp, self.faceRight, self.faceDown, self.faceLeft],
                                          [positionsU, positionsR, positionsD, positionsL], [1, 3])
        self.faceUp = faces[0]
        self.faceRight = faces[1]
        self.faceDown = faces[2]
        self.faceLeft = faces[3]

        self.tracking.append('f' + shift)

    def moveF_(self, shift):
        if(len(shift) == 0):
            self.faceFront = self.rotateFace(self.faceFront, True)

        positionsU = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size * len(shift), range(self.size)))
        positionsR = []
        positionsL = []
        positionsD = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))

        for i in range(self.size):
            positionsL.append((i+1)*self.size - 1 - len(shift))
            positionsR.append(i*self.size + len(shift))

        faces = self.rotateSidesInverting([self.faceUp, self.faceLeft, self.faceDown, self.faceRight],
                                          [positionsU, positionsL, positionsD, positionsR], [0, 2])
        self.faceUp = faces[0]
        self.faceLeft = faces[1]
        self.faceDown = faces[2]
        self.faceRight = faces[3]

        self.tracking.append("f'" + shift)

    def moveB(self, shift):
        if(len(shift) == 0):
            self.faceBack = self.rotateFace(self.faceBack, False)

        positionsD = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size*len(shift), range(self.size)))
        positionsR = []
        positionsL = []
        positionsU = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))

        positionsU.reverse()

        for i in range(self.size):
            positionsR.append((i+1)*self.size - 1 - len(shift))
            positionsL.append(i*self.size + len(shift))

        faces = self.rotateSidesInverting([self.faceUp, self.faceLeft, self.faceDown, self.faceRight],
                                          [positionsU, positionsL, positionsD, positionsR], [2, 3])
        self.faceUp = faces[0]
        self.faceLeft = faces[1]
        self.faceDown = faces[2]
        self.faceRight = faces[3]

        self.tracking.append("b" + shift)

    def moveB_(self, shift):
        if(len(shift) == 0):
            self.faceBack = self.rotateFace(self.faceBack, True)

        positionsD = list(map(lambda x: x + self.size *
                              (self.size - 1) - self.size*len(shift), range(self.size)))
        positionsR = []
        positionsL = []
        positionsU = list(map(lambda x: x + self.size *
                              len(shift), range(self.size)))

        positionsU.reverse()

        for i in range(self.size):
            positionsR.append((i+1)*self.size - 1 - len(shift))
            positionsL.append(i*self.size + len(shift))

        faces = self.rotateSidesInverting([self.faceUp, self.faceRight, self.faceDown, self.faceLeft],
                                          [positionsU, positionsR, positionsD, positionsL], [0, 1])
        self.faceUp = faces[0]
        self.faceRight = faces[1]
        self.faceDown = faces[2]
        self.faceLeft = faces[3]

        self.tracking.append("b'" + shift)

    def moveR(self, shift):
        if(len(shift) == 0):
            self.faceRight = self.rotateFace(self.faceRight, True)

        positionsU = []
        positionsF = []
        positionsD = []
        positionsB = []

        for i in range(self.size):
            positionsU.append((i+1)*self.size - 1 - len(shift))
            positionsF.append((i+1)*self.size - 1 - len(shift))
            positionsD.append((i+1)*self.size - 1 - len(shift))
            positionsB.append(i*self.size + len(shift))

        positionsB.reverse()

        faces = self.rotateSides([self.faceUp, self.faceFront, self.faceDown, self.faceBack],
                                 [positionsU, positionsF, positionsD, positionsB])
        self.faceUp = faces[0]
        self.faceFront = faces[1]
        self.faceDown = faces[2]
        self.faceBack = faces[3]

        self.tracking.append("r" + shift)

    def moveR_(self, shift):
        if(len(shift) == 0):
            self.faceRight = self.rotateFace(self.faceRight, False)

        positionsU = []
        positionsF = []
        positionsD = []
        positionsB = []

        for i in range(self.size):
            positionsU.append((i+1)*self.size - 1 - len(shift))
            positionsF.append((i+1)*self.size - 1 - len(shift))
            positionsD.append((i+1)*self.size - 1 - len(shift))
            positionsB.append(i*self.size + len(shift))

        positionsB.reverse()

        faces = self.rotateSides([self.faceUp, self.faceBack, self.faceDown, self.faceFront],
                                 [positionsU, positionsB, positionsD, positionsF])
        self.faceUp = faces[0]
        self.faceBack = faces[1]
        self.faceDown = faces[2]
        self.faceFront = faces[3]

        self.tracking.append("r'" + shift)

    def moveL(self, shift):
        if(len(shift) == 0):
            self.faceLeft = self.rotateFace(self.faceLeft, False)

        positionsU = []
        positionsF = []
        positionsD = []
        positionsB = []

        for i in range(self.size):
            positionsU.append(i*self.size + len(shift))
            positionsF.append(i*self.size + len(shift))
            positionsD.append(i*self.size + len(shift))
            positionsB.append((i+1)*self.size - 1 - len(shift))

        positionsB.reverse()

        faces = self.rotateSides([self.faceUp, self.faceFront, self.faceDown, self.faceBack],
                                 [positionsU, positionsF, positionsD, positionsB])
        self.faceUp = faces[0]
        self.faceFront = faces[1]
        self.faceDown = faces[2]
        self.faceBack = faces[3]

        self.tracking.append("l" + shift)

    def moveL_(self, shift):
        if(len(shift) == 0):
            self.faceLeft = self.rotateFace(self.faceLeft, True)

        positionsU = []
        positionsF = []
        positionsD = []
        positionsB = []

        for i in range(self.size):
            positionsU.append(i*self.size + len(shift))
            positionsF.append(i*self.size + len(shift))
            positionsD.append(i*self.size + len(shift))
            positionsB.append((i+1)*self.size - 1 - len(shift))

        positionsB.reverse()

        faces = self.rotateSides([self.faceUp, self.faceBack, self.faceDown, self.faceFront],
                                 [positionsU, positionsB, positionsD, positionsF])
        self.faceUp = faces[0]
        self.faceBack = faces[1]
        self.faceDown = faces[2]
        self.faceFront = faces[3]

        self.tracking.append("l'" + shift)

    def c_pos(self, i, j):
        return self.size * i + j

    def rotateFace2(self, face, invert):
        for i in range(self.size*self.size):
            posi = int(i % self.size)
            posj = int(i / self.size)

            next_posi = posi
            next_posj = posj

            i0 = posi
            j0 = posj
            i1 = posi
            j1 = posj
            i2 = posi
            j2 = posj
            i3 = posi
            j3 = posj

            if posi == posj and posi < (self.size - 1)/2:
                # cantos
                i1 = self.size - i0 - 1
                j1 = j0
                i2 = i1
                j2 = self.size - j1 - 1
                i3 = self.size - i2 - 1
                j3 = j2
            elif posi < posj and posi < self.size - posj - 1:
                print("# arestas")
                i1 = j0
                j1 = i0
                i2 = self.size - j1 - 1
                j2 = i1
                i3 = self.size - j2 - 1
                j3 = i2
                

            aux = face[self.c_pos(i0, j0)]
            face[self.c_pos(i0, j0)] = face[self.c_pos(i1, j1)]
            face[self.c_pos(i1, j1)] = face[self.c_pos(i2, j2)]
            face[self.c_pos(i2, j2)] = face[self.c_pos(i3, j3)]
            face[self.c_pos(i3, j3)] = aux

            # elif posi < posj and posi < self.size - posj - 1:
            #     # triangulo superior
            #     next_posi = posj
            #     next_posj = posi
            # elif posi > posj and posi > self.size - posj - 1:
            #     # triangulo inferior
            #     next_posi = posj
            #     next_posj = self.size - posi - 1
            # elif posi < posj and posi > self.size - posj - 1:
            #     # triangulo direito
            #     next_posi = self.size - posj - 1
            #     next_posj = posi
            # elif posi > posj and posi < self.size - posj - 1:
            #     # triangulo esquerdo
            #     next_posi = self.size - posj - 1
            #     next_posj = posi

            print("===== " + str(posi) + "  " + str(posj))
            print("===== " + str(next_posi) + "  " + str(next_posj))

            if invert:
                print(invert)
                print(str(face[self.size*posi + posj]) + " " + str(face[self.size*next_posi + next_posj]))
                aux = face[self.size*posi + posj]
                face[self.size*posi + posj] = face[self.size*next_posi + next_posj]
                face[self.size*next_posi + next_posj] = aux
            else:
                print(invert)
                print(str(face[self.size*posi + posj]) + " " + str(face[self.size*next_posi + next_posj]))
                aux = face[self.size*next_posi + next_posj]
                face[self.size*next_posi + next_posj] = face[self.size*posi + posj]
                face[self.size*posi + posj] = aux

        return face            

    def rotateFace(self, face, invert):
        if invert == False:
            # rotaciona cantos
            aux = face[0]
            face[0] = face[self.size - 1]
            face[self.size - 1] = face[self.size*self.size - 1]
            face[self.size*self.size - 1] = face[self.size*self.size - self.size]
            face[self.size*self.size - self.size] = aux

            # rotaciona arestas
            for i in range(self.size - 2):
                j = (self.size - 3) - i  # oposto
                aux = face[i + 1]
                face[i + 1] = face[(i + 2) * (self.size) - 1]
                face[(i + 2) * (self.size) -
                     1] = face[self.size*self.size - 2 - j]
                face[self.size*self.size - 2 - j] = face[self.size * (j + 1)]
                face[self.size * (j + 1)] = aux
        else:
            aux = face[0]
            face[0] = face[self.size*self.size - self.size]
            face[self.size*self.size - self.size] = face[self.size*self.size - 1]
            face[self.size*self.size - 1] = face[self.size - 1]
            face[self.size - 1] = aux

            for i in range(self.size - 2):
                aux = face[i + 1]
                face[i + 1] = face[self.size * (i + 1)]
                face[self.size * (i + 1)] = face[self.size*self.size - 2 - i]
                face[self.size*self.size - 2 -
                     i] = face[(i + 2) * (self.size) - 1]
                # face[(i + 2) * (self.size - 1) + 1] = aux
                face[(i + 2) * (self.size) - 1] = aux

        return face

    def rotateSides(self, faces, face_positions):
        for i in range(self.size):
            pos0 = face_positions[0][i]
            pos1 = face_positions[1][i]
            pos2 = face_positions[2][i]
            pos3 = face_positions[3][i]

            aux = faces[0][pos0]
            faces[0][pos0] = faces[1][pos1]
            faces[1][pos1] = faces[2][pos2]
            faces[2][pos2] = faces[3][pos3]
            faces[3][pos3] = aux

        return faces

    def rotateSidesInverting(self, faces, face_positions, invert_faces):
        for i in range(self.size):
            pos0 = face_positions[0][i]
            pos1 = face_positions[1][i]
            pos2 = face_positions[2][i]
            pos3 = face_positions[3][i]

            aux = faces[0][pos0]
            faces[0][pos0] = faces[1][pos1]
            faces[1][pos1] = faces[2][pos2]
            faces[2][pos2] = faces[3][pos3]
            faces[3][pos3] = aux

        for f in invert_faces:
            for i in range(int(self.size/2)):
                pos = face_positions[f][i]
                posi = face_positions[f][self.size - i - 1]

                aux = faces[f][pos]
                faces[f][pos] = faces[f][posi]
                faces[f][posi] = aux

        return faces


if __name__ == '__main__':
    main()
