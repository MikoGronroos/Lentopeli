import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth

import os

os.system('cls' if os.name == 'nt' else 'clear')

if auth.Authenticate():
    while True:
        gameLoop.GameLoop()
