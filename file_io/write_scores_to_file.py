#!/usr/bin/env python

f = open('scores.txt', 'r')

while True:
    participant = input('Participant name > ')

    if participant == 'quit':
        print('Quitting ...')
        break

    score = input('Score for ' + participant + '> ')
    f.write(participant + ',' + score + '\n')

f.close()
