inputs = [
    {
        "competitions": [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
        "results": [0, 0, 1],
    },
    {
        "competitions": [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]],
        "results": [0, 1, 1],
    },
    {
        "competitions": [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
        ],
        "results": [0, 1, 1, 1, 0, 1],
    },
    {
        "competitions": [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"],
        ],
        "results": [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    },
    {"competitions": [["Bulls", "Eagles"]], "results": [1]},
    {
        "competitions": [["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bears", "Eagles"]],
        "results": [0, 0, 0],
    },
    {
        "competitions": [
            ["Bulls", "Eagles"],
            ["Bulls", "Bears"],
            ["Bulls", "Monkeys"],
            ["Eagles", "Bears"],
            ["Eagles", "Monkeys"],
            ["Bears", "Monkeys"],
        ],
        "results": [1, 1, 1, 1, 1, 1],
    },
    {
        "competitions": [
            ["AlgoMasters", "FrontPage Freebirds"],
            ["Runtime Terror", "Static Startup"],
            ["WeC#", "Hypertext Assassins"],
            ["AlgoMasters", "WeC#"],
            ["Static Startup", "Hypertext Assassins"],
            ["Runtime Terror", "FrontPage Freebirds"],
            ["AlgoMasters", "Runtime Terror"],
            ["Hypertext Assassins", "FrontPage Freebirds"],
            ["Static Startup", "WeC#"],
            ["AlgoMasters", "Static Startup"],
            ["FrontPage Freebirds", "WeC#"],
            ["Hypertext Assassins", "Runtime Terror"],
            ["AlgoMasters", "Hypertext Assassins"],
            ["WeC#", "Runtime Terror"],
            ["FrontPage Freebirds", "Static Startup"],
        ],
        "results": [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    },
    {
        "competitions": [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"],
        ],
        "results": [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    },
    {"competitions": [["A", "B"]], "results": [0]},
    {
        "competitions": [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
        "results": [0, 0, 1],
    },
    {
        "competitions": [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"],
        ],
        "results": [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    },
    {"competitions": [["A", "B"]], "results": [0]},
]


def add_to_score_dict(teams, score_dict):
    for team in teams:
        if score_dict.get(team) is None:
            score_dict[team] = 0


def tournamentWinner(competitions, results):
    # Write your code here.
    print(competitions)
    print(results)
    score_dict = {}
    winner = ["", 0]
    for idx, c in enumerate(competitions):
        add_to_score_dict(c, score_dict)
        print(c)
        print(score_dict)

        if results[idx] == 1:
            score_dict[c[0]] += 1
            if score_dict[c[0]] > winner[1]:
                winner[0], winner[1] = c[0], score_dict[c[0]]
            elif score_dict[c[1]] > winner[1]:
                winner[0], winner[1] = c[1], score_dict[c[1]]
        else:
            score_dict[c[1]] += 1
            if score_dict[c[0]] > winner[1]:
                winner[0], winner[1] = c[0], score_dict[c[0]]
            elif score_dict[c[1]] > winner[1]:
                winner[0], winner[1] = c[1], score_dict[c[1]]
    print("final score", score_dict)

    return winner[0]


HOME_TEAM_WON = 1


def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points


def better(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        update_scores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


if __name__ == "__main__":
    for test in inputs:
        # print(isValidSubsequence(**test))
        print(tournamentWinner(**test))
        print(better(**test))

        print(50 * "_")
