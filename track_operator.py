
class track_operator:
    def run(self, operation, track, arg0 = ''):
        if operation == 'remove-oposites' or operation == 'ro':
            return self.remove_oposites(track)
        else:
            return []

    def remove_oposites(self, track):
        redo = True

        while redo and len(track) > 3:
            redo = False

            for i in range(len(track) - 2):
                if len(track) <= 3:
                    break

                current = track[i]
                next = track[i+1]

                if self.reverse_move(current) == next:
                    track.remove(current)
                    track.remove(next)
                    redo = True
                    break
            
        return track
    
    def reverse_move(self, move):
        if move == ['start'] or move == ['end']:
            return None

        new_move = move.copy()
        print(move)
        
        if move[1].__contains__("'"):
            new_move[1].replace("'", "")
        else:
            new_move[1] += "'"

        return new_move
