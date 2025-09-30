import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth

while True:
    auth.Authenticate()
    gameLoop.GameLoop()
