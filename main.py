import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth
import Scripts.Core.startNewGame as start

import os

os.system('cls' if os.name == 'nt' else 'clear')

if auth.Authenticate():
    start.startNewGame()
    #
    #while True:
     #   gameLoop.GameLoop()
