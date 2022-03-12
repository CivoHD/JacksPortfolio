import time
import random
import pyfiglet

# five games in total
# select sports or achedmic games
# select indivuals or a team

# sports games: Football, Basketball, Volleyball, Swimming, Running
# achemic games: Math, Spelling, Reading, Science Experiments.

Selections = True
Games = 0
postions = [1, 2, 3]


goal1 = 0
goal2 = 0

Team = "team"
TEAMS = ["Team 1", "Team 2", "Team 3", "Team 4"]

Individual = "individual"
INDIVIDUALS = ["leah", "mike", "jack", "terry", "april", "max", "ted", "bob", "jerry", "michale", "batman", "harry", "god", "turtle" ,"june" ,"tobi" ,"tony" ,"greece" ,"tom" ,"alfie"]

teams = ['team1', 'team2', 'team3', 'team4']
events = ['Football Game', "Basketball Game", "Volletball Game", "Spelling", "Math"]

places = {
    '1st': 10,
    '2nd': 8,
    '3rd': 6,
    '4th': 4
}
points = {
    'team1': 0,
    'team2': 0,
    'team3': 0,
    'team4': 0
}

while Selections:
    selection = input("How do you want to enter the tourniment as a 'Team' or a 'individual': ").lower()

    if selection == Team:
        print("Teams are playing")
        break
    elif selection == Individual:
        print("Individuals are playing")
        break
    elif selection != Team or Individual:
        play_again = input("Invalid Please make sure you entered 'team' or 'individual' (type y to restart): ")
        if play_again.lower() != "y":
            break
    else:    
        break

# Adding your name to your list
if selection == Individual:
    while len(INDIVIDUALS):
        name = input("There are 19 individuals: type your name: ")
        INDIVIDUALS.append(name)
        break
    print("your players are")
    print(INDIVIDUALS)
time.sleep(2)

# TEAMMMS Football game
if selection == Team:

    ascii_banner = pyfiglet.figlet_format("Football Games")
    print(ascii_banner)

    print(f"The football games are starting with {selection}s")
    time.sleep(1)

    redside = "Team1"
    print(f"{redside} Scores a goal..")
    goal1 = goal1 + 2
    time.sleep(2)

    blueside = "Team3"
    print(f"{blueside} Scores a goal..")
    goal2 = goal2 + 1
    time.sleep(2)

    print(f"{redside} has just shot the final shot!!")
    time.sleep(2)
    print(f"The winner is: {redside} with a total of {goal1} Goals!!")
    time.sleep(2)
    print(
        f"{redside} Came in {postions[0]}st \n{blueside} Came in {postions[1]}nd")

    print(f"\nSecond football match")
    time.sleep(1)

    redside = "Team2"
    print(f"{redside} Scores a goal..")
    goal1 = goal1 + 2
    time.sleep(2)

    blueside = "Team4"
    print(f"{blueside} Scores a goal..")
    goal2 = goal2 + 1
    time.sleep(2)

    print(f"{redside} has just shot the final shot!!")
    time.sleep(2)
    print(f"The winner is: {redside} with a total of {goal1} Goals!!")
    time.sleep(2)
    print(
        f"{redside} Came in {postions[0]}st \n{blueside} Came in {postions[1]}nd")


    #Final games
    print("\nThe losers go against each other")
    time.sleep(1)
    print("\nTeam 2 vs Team 3")
    time.sleep(1)
    print("\nTeam 3 won!")
    time.sleep(1)
    print("\nTeam 1 vs Team 4")
    time.sleep(2)
    print("Team 1 won!")
    print("\nResults are..")
    print("""\n1st Team 1
2st Team 4
3rd Team 3
4th Team 2""")

    #Basketball game
    ascii_banner = pyfiglet.figlet_format("Basketball Games")
    print(ascii_banner)

    print("Team 1 vs Team 2")
    time.sleep(2)
    print("\nTeam 1 won!")
    time.sleep(2)
    print("\nTeam 3 vs Team 4")
    time.sleep(1)
    print("\nTeam 4 won!")
    print("\nTeam 2 and team 3 go agains each other...")
    time.sleep(2)
    print("\nTeam 2 won!")
    time.sleep(1)
    print("Team 1 vs Team 4")
    time.sleep(2)
    print("Team 1 won!")
    time.sleep(2)
    print("\nResults are..")
    print("""1st: Team1
2nd: Team4
3rd: Team3
4th: Team2""")

    #Volleyball game
    ascii_banner = pyfiglet.figlet_format("Vollyball Games")
    print(ascii_banner)

    print("Team 3 vs Team 1")
    time.sleep(2)
    print("\nTeam 3 won!")
    time.sleep(2)
    print("\nTeam 2 vs Team 4")
    time.sleep(1)
    print("\nTeam 2 won!")
    print("\nTeam 4 and team 1 go agains each other...")
    time.sleep(2)
    print("\nTeam 4 won!")
    time.sleep(1)
    print("Team 3 vs Team 2")
    time.sleep(2)
    print("Team 2 won!")
    time.sleep(2)
    print("\nResults are..")
    print("""1st: Team2
2nd: Team3
3rd: Team4
4th: Team1""")

    ascii_banner = pyfiglet.figlet_format("Spelling")
    print(ascii_banner)

    print("Team 2 vs Team 4")
    time.sleep(2)
    print("\nTeam 2 won!")
    time.sleep(2)
    print("\nTeam 1 vs Team 3")
    time.sleep(1)
    print("\nTeam 1 won!")
    print("\nTeam 3 and team 4 go agains each other...")
    time.sleep(2)
    print("\nTeam 4 won!")
    time.sleep(1)
    print("Team 4 vs Team 2")
    time.sleep(2)
    print("Team 2 won!")
    time.sleep(2)
    print("\nResults are..")
    print("""1st: Team2
2nd: Team4
3rd: Team3
4th: Team1""")

    ascii_banner = pyfiglet.figlet_format("Math")
    print(ascii_banner)

    print("Team 3 vs Team 1")
    time.sleep(2)
    print("\nTeam 3 won!")
    time.sleep(2)
    print("\nTeam 2 vs Team 4")
    time.sleep(1)
    print("\nTeam 2 won!")
    print("\nTeam 4 and team 1 go agains each other...")
    time.sleep(2)
    print("\nTeam 4 won!")
    time.sleep(1)
    print("Team 3 vs Team 2")
    time.sleep(2)
    print("Team 3 won!")
    time.sleep(2)
    print("\nResults are..")
    print("""1st: Team3
2nd: Team2
3rd: Team4
4th: Team1""")

    def run_events():
        for event in events:
            for place in places:
                print("Enter " + place + " place for " + event + ": ")
                team = input().lower()
                points[team] += places[place]


    def main():
        run_events()
        print("\nFinal Scores:\n")
        for team in teams:
            print(team + ": " + str(points[team]) + " points")
            print()


    main()








# INDIVIDUALS
if selection == Individual:
    print(f"The football games are starting with {selection}s")
    print("\nThe individuals are split up into two teams")
    time.sleep(2)


    redside = INDIVIDUALS[0:10]
    print(f"Team 1\n {redside}")
    print(f"Team 2\n {INDIVIDUALS[11:20]}")
    time.sleep(2)
    print(f"\n{random.choice(redside)} Scores a goal..")
    goal1 = goal1 + 2
    time.sleep(2)

    blueside = INDIVIDUALS[11:20]
    time.sleep(2)
    print(f"\n{random.choice(blueside)} Scores a goal..")
    goal1 = goal1 + 1
    time.sleep(2)

    print(f"\n{random.choice(blueside)} has just shot the final shot!!")

    time.sleep(2)
    print(f"\nThe winner team is: {redside} with a total of {goal1} Goals!!")
    time.sleep(2)
    print(
        f"\n{blueside} All Came in {postions[0]}st \n{redside} All Came in {postions[1]}nd")






