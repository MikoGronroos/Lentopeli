import Scripts.Core.gameLoop as gameLoop
import Scripts.Core.authentication as auth

if auth.Authenticate():
    while True:
        gameLoop.GameLoop()
