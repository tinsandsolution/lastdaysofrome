import random
import time

confusion = 0
damages = 0
thinking = 0
gameOvers = {}

def sprint(s, indents = 1):
    # time.sleep(1)
    # indents = "\t" * indents
    # print(f"{indents}{s}")
    pass

def ig(s):
    global gameOvers
    if s in gameOvers:
        gameOvers[s] += 1
    else:
        gameOvers[s] = 1

def iconfusion():
    global confusion
    confusion += 1
    if sum(nd6(3)) == 18:
        ig("Feverish Moment of Dire Clarity")
        return (True, "\t +1 Confusion \nYou finally decipher what the mastodon was trying to tell you.\n" \
                "You live the rest of your life in a satte of blissful enlightenment, " \
                "in harmony with your new friend. \nYou're also a vegan now.")
    return (False, "\t+1 Confusion")

def idamages():
    global damages
    damages += 1
    return (False, "\t+1 Damages")
def ithinking():
    global thinking
    thinking += 1
    return (False, "\t+1 Thinking")

def nd6(n):
    return [random.choice([1,2,3,4,5,6]) for i in range(n)]

def d6():
    return random.choice([1,2,3,4,5,6])

def day():
    event = d6()
    cases = {
        1 : [iconfusion],
        2 : [idamages],
        3 : [ithinking],
        4 : [iconfusion, idamages],
        5 : [iconfusion, iconfusion],
        6 : [idamages, idamages],
    }
    messages = {
        1 : "The mastodon tells you a secret about your family it could not possibly know.",
        2 : "Your mastodon decentralizes all over the carpet.",
        3 : "You take the mastodon on a walk in your gated neighborhood.",
        4 : "The mastodon federates violently through a window, which now needs replacing",
        5 : "The mastodon won't move unless you know the password. You do not know the password.",
        6 : "The mastodon bashes a hole in your roof, and now claims to have a much better view of other mastodon.",
    }
    logs = []
    logs.append(messages[event])
    for infliction in cases[event]:
        (end, inflictM) = infliction()
        if end:
            logs.append(inflictM)
            return (end, logs)
        else:
            logs.append(inflictM)

    return (False, logs)

def evening():
    event = d6()
    cases = {
        1 : [ithinking],
        2 : [iconfusion],
        3 : [iconfusion],
        4 : [iconfusion, ithinking],
        5 : [iconfusion, ithinking],
        6 : [idamages],
    }
    messages = {
        1 : "The mastodon trumpets ERROR at you. You ponder your mistake.",
        2 : "It wears so many hats. How will you wash all these hats?.",
        3 : "It reads moral philosophy and particle physics. All day. It will not let you read with it.",
        4 : "Your friends tell you how wonderful their mastodons are. You burn with envy.",
        5 : "Before the mastodon will sleep, you must clean its many gears and whistles.",
        6 : "During the night, your mastodon holds not one, not two, but a third party. There is a platform. And servers.",
    }
    logs = []
    logs.append(messages[event])
    for infliction in cases[event]:
        (end, inflictM) = infliction()
        if end:
            logs.append(inflictM)
            return (end, logs)
        else:
            logs.append(inflictM)

    return (False, logs)

def anger():
    pass

for x in range(1000):
    days = 1
    while True:
        event = d6()
        if event in [1,2,3]:
            sprint(f"Day {days}: A day with your mastodon", 0)
            (endGame, logs) = day()
            for log in logs:
                sprint(log)
            if endGame: break
        elif event in [4,5]:
            sprint(f"Day {days}: An evening at home", 0)
            (endGame, logs) = evening()
            for log in logs:
                sprint(log)
            if endGame: break
        elif event == 6:
            sprint(f"Day {days}:", 0)
            sprint("You anger your mastodon with your questions, and it sits on you.")
            if d6() == 6:
                sprint("You never emerge.")
                ig("Sit Ending")
                break


        if confusion >= 10:
            sprint("You finally lose your temper with the wretched creature and confront it.")
            sprint("The argument is brief, because you have no idea what it is trying to tell you,")
            sprint("and eventually it crushes you to death using its trunk.")
            ig("Confusion Ending")
            break
        elif damages >= 10:
            sprint("You lose all your money and your livelihood is destroyed,")
            sprint("reduced to gigantic footprints in the ashes.")
            sprint("The mastodon abandons you in search of someone else to inconvenience.")
            ig("Damages Ending")
            break
        elif thinking >= 10:
            sprint("You decide that mastodons are not for you.")
            sprint("You slip away into the night with the last of your remaining savings, faking your death.")
            sprint("Perhaps you'll build a gigantic pillowfort. Or collect tumblers. Something quiet.")
            ig("Thinking Ending")
            break
        days += 1
    sprint("GAME OVER")
    confusion = 0
    damages = 0
    thinking = 0

print(gameOvers)

total = 0
gameOvers = sorted(gameOvers.items())
for item in gameOvers:
    (title, freq) = item
    total += freq
for item in gameOvers:
    (title, freq) = item
    print(f"{title} : {round((freq / total)*100, 2)}%")
