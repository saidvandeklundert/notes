import copy

tests = [
    {
        "competitions": [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
        "results": [0, 0, 1],
    },
]
# from biglists import tests


def tournamentWinner(competitions, results):
    winners_d = {}

    for index, value in enumerate(results):
        if value == 1:
            winner = competitions[index][0]
        else:
            winner = competitions[index][1]

        if winner in winners_d:
            winners_d[winner] += 1
        else:
            winners_d[winner] = 1

    champ = ["", 0]
    for team, wins in winners_d.items():
        if wins > champ[1]:
            champ = [team, wins]
    return champ[0]


# Better

HOME_TEAM_WON = 1


def tournamentWinner_better(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winingTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winingTeam, 3, scores)

        if scores[winingTeam] > scores[currentBestTeam]:
            currentBestTeam = winingTeam

    return currentBestTeam


def updateScores(team, points, scores):

    if team not in scores:
        scores[team] = 0

    scores[team] += points


if __name__ == "__main__":
    print("num1")
    i = 0
    for d in tests:
        i += 1
        print(f"Test number {i}")
        print(tournamentWinner(competitions=d["competitions"], results=d["results"]))
    print("num2")
    i = 0
    for d in tests:
        i += 1
        print(f"Test number {i}")
        print(
            tournamentWinner_better(
                competitions=d["competitions"], results=d["results"]
            )
        )
