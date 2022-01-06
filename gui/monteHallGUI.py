from class_definitions.game import Game
from class_definitions.stats import Stats
import tkinter
from random import randint

"""
TO-DO:
make selection active
make switch selection active
"""

m = tkinter.Tk()
m.geometry("470x450")
m.title("Let's Make A Deal!")


def switchDecision(guessedDoorNum):
    change_all_doors("disabled")
    change_automation("disabled")
    game.setLoser(guessedDoorNum)
    loser = game.loser

    switch = game.switch(guessedDoorNum)

    info.config(text=f'Door #{guessedDoorNum} selected. #{loser} removed')
    info.grid(row=3, columnspan=3)
    global switchLabel
    switchLabel = (tkinter.Label(m, text=f"Would you like to switch to door #{switch}?"))
    switchLabel.config(wrap=100)
    switchLabel.grid(row=5, columnspan=1)
    global switchYes
    switchYes = tkinter.Button(m, text="yes", width=10, command=lambda: switchY(guessedDoorNum))
    switchYes.grid(row=5, column=1)
    global switchNo
    switchNo = tkinter.Button(m, text="no",  width=10, command=lambda: switchN(guessedDoorNum))
    switchNo.grid(row=5, column=2)


def switchY(doorNum):
    guess(game.switch(doorNum))
    switchLabel.destroy()
    switchYes.destroy()
    switchNo.destroy()


def switchN(doorNum):
    guess(doorNum)
    switchLabel.destroy()
    switchYes.destroy()
    switchNo.destroy()


def guess(doorNum):
    if game.guess(doorNum):
        info.config(text="YOU WON A CAR!")
        stats.won()
    else:
        info.config(text="YOU LOSE!")
        stats.lost()
    updateStats()
    playAgainBtn = tkinter.Button(m, text="Play Again", width=10, command=lambda: [reset(), playAgainBtn.destroy(), exitBtn.destroy()])
    playAgainBtn.grid(row=7, column=1, pady=(14, 0))
    exitBtn = tkinter.Button(m, text="Exit",  width=10, command=m.destroy)
    exitBtn.grid(row=7, column=2, pady=(14, 0))


def reset():
    print("----------")
    game.reset()
    print(f"Answer: {game.rand}")
    info.config(text="Select a door:")
    change_all_doors("normal")
    change_automation("normal")


def btnDisable(door):
    door.config(state="disabled")


def btnEnable(door):
    door.config(state="enabled")


def change_all_doors(action):
    door1.config(state=action)
    door2.config(state=action)
    door3.config(state=action)


def change_automation(action):
    autoYBtn.config(state=action)
    autoNBtn.config(state=action)


def updateStats():
    winCount.config(text=stats.wins)
    lossesCount.config(text=stats.losses)
    winPCount.config(text=stats.winPercent())


def doorFromNum(doorNum):
    switcher = {
        1: door1,
        2: door2,
        3: door3
    }


def auto(decision):
    i = 500
    while i > 0:
        autoGuess = randint(1, 3)
        switchDecision(autoGuess)
        if decision == 'y':
            switchY(autoGuess)
        else:
            switchN(autoGuess)
        i -= 1


info = tkinter.Label(m, width=30, text="Select a door:")
info.grid(row=3, columnspan=3, pady=(15, 0))

# doors
door1 = tkinter.Button(m, text="1", width=10, height=13, command=lambda: switchDecision(1))
door1.grid(row=4, padx=15, pady=10)
door2 = tkinter.Button(m, text="2", width=10, height=13, command=lambda: switchDecision(2))
door2.grid(row=4, column=1, padx=15, pady=10)
door3 = tkinter.Button(m, text="3", width=10, height=13, command=lambda: switchDecision(3))
door3.grid(row=4, column=2, padx=15, pady=10)

switchLabel = tkinter.Label(m)

# stats
stats = Stats()
wins = stats.wins
losses = stats.losses
winP = stats.winPercent()

winsLbl = tkinter.Label(m, text="Wins")
winsLbl.grid(row=0, column=0)
lossesLbl = tkinter.Label(m, text="Losses")
lossesLbl.grid(row=0, column=1)
winPLbl = tkinter.Label(m, text="Win %")
winPLbl.grid(row=0, column=2)
winCount = tkinter.Label(m, text=wins)
winCount.grid(row=1, column=0)
lossesCount = tkinter.Label(m, text=losses)
lossesCount.grid(row=1, column=1)
winPCount = tkinter.Label(m, text=winP)
winPCount.grid(row=1, column=2)
statsResetBtn = tkinter.Button(m, padx=20, pady=2, text="Reset Stats", command=lambda:  [stats.reset(), updateStats()])
statsResetBtn.grid(row=2, columnspan=3)

# automation
autoLbl = tkinter.Label(m, text='Auto play 500 games:')
autoLbl.config(wrap=100)
autoLbl.grid(row=6, column=0)
autoYBtn = tkinter.Button(m, text='Switch', command=lambda: auto('y'))
autoYBtn.grid(row=6, column=1)
autoNBtn = tkinter.Button(m, text='No Switch', command=lambda: auto('n'))
autoNBtn.grid(row=6, column=2)

game = Game()
print(f"Answer: {game.rand}")


m.mainloop()  # event watcher
