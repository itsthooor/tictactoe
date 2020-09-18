#Credits: https://github.com/itsthooor/tictactoe

import  os
import time

class plays:
    fields = ['1','2','3','4','5','6','7','8','9']
    p1 = 'x'
    p2 = 'o'
    move = 1
    selfield = 0
    rounds = 1

    def chgmove(self, ply):
        self.move = ply

    def chground(self):
        self.rounds += 1

inst = plays()
playstate = True
while playstate:

    def check():
        if 'x' == inst.fields[0] == inst.fields[3] == inst.fields[6] or 'x' == inst.fields[1] == inst.fields[4] == inst.fields[7] or 'x' == inst.fields[2] == inst.fields[5] == inst.fields[8] or 'x' == inst.fields[0] == inst.fields[1] == inst.fields[2] or 'x' == inst.fields[3] == inst.fields[4] == inst.fields[5] or 'x' == inst.fields[6] == inst.fields[7] == inst.fields[8] or 'x' == inst.fields[0] == inst.fields[4] == inst.fields[8] or 'x' == inst.fields[2] == inst.fields[4] == inst.fields[6]:
            print("Player 1 wins!")
            quit()
        elif 'o' == inst.fields[0] == inst.fields[3] == inst.fields[6] or 'o' == inst.fields[1] == inst.fields[4] == inst.fields[7] or 'o' == inst.fields[2] == inst.fields[5] == inst.fields[8] or 'o' == inst.fields[0] == inst.fields[1] == inst.fields[2] or 'o' == inst.fields[3] == inst.fields[4] == inst.fields[5] or 'o' == inst.fields[6] == inst.fields[7] == inst.fields[8] or 'o' == inst.fields[0] == inst.fields[4] == inst.fields[8] or 'o' == inst.fields[2] == inst.fields[4] == inst.fields[6]:
            print("Player 2 wins!")
            quit()
        elif inst.rounds > 9:
            print("It's a tie!")
            quit()

    def gameui():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(inst.fields[0] + ' | ' + inst.fields[1] + ' | ' + inst.fields[2] + '\n' +
            inst.fields[3] + ' | ' + inst.fields[4] + ' | ' + inst.fields[5] + '\n' +
            inst.fields[6] + ' | ' + inst.fields[7] + ' | ' + inst.fields[8])

    def move():
        gameui()
        check()
        inst.selfield = int(input('\nPlayer ' + str(inst.move) + ', choose a field (1-9): '))
        if inst.move == 1:
            if inst.fields[inst.selfield-1] not in ('x','o'):
                inst.fields[inst.selfield-1] = inst.p1
                inst.chgmove(2)
                inst.chground()
            else:
                print("Field already used!")
                time.sleep(1)
                move()
        elif inst.move == 2:
            if inst.fields[inst.selfield-1] not in ('x','o'):
                inst.fields[inst.selfield-1] = inst.p2
                inst.chgmove(1)
                inst.chground()
            else:
                print("Field already used!")
                time.sleep(1)
                move()
        else:
            print("Something is wrong!")
            quit()

    move()
