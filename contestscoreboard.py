"""
Problem: Contest Scoreboard
Simulate a contest scoreboard where each submission is processed to update the team's score and penalty. Each submission has a team number, problem number, submission time, and result (C: correct, I: incorrect, R/U/E: ignored). For each team, output the team number, number of problems solved, and total penalty.

Input:
- Each line: team_number problem_number submission_time result
- Input ends when an empty line or EOF is encountered.

Output:
- For each team, print a list: [team_number, number_of_problems_solved, total_penalty]

Sample Input:
1 2 10 I
1 2 20 C
2 1 15 C
2 1 25 I

Sample Output:
[1, 1, 40]
[2, 1, 15]

Explanation:
- Team 1: 1 incorrect (20 penalty), then correct (20+20=40 penalty, 1 problem solved)
- Team 2: correct on first try (15 penalty, 1 problem solved)

Time Complexity: O(n), where n is the number of submissions.
Space Complexity: O(t), where t is the number of teams.
"""

Board = {}
Final_score = {}
Teams = []
Useless = ['R','U','E']
temp = input().split(" ")
n = 0

Correct = dict()
Repeat = dict()
while(True):                    #Take input until user enters
    try:
        temp[1]
    except:
        break
    Board[n] = temp
    n = n+1
    temp = input().split(" ")

for i in range(0,n):
    for j in range(0,3):
        Board[i][j] = int(Board[i][j]) #convert to int and add to repeat
    Repeat[Board[i][0]] = False
    Correct[Board[i][0]] = False
 

for i in range(0,n):
        if(Board[i][3] in Useless):
            continue
        elif(Board[i][3] == 'I' and Correct[Board[i][0]] == False):
            if(Repeat[Board[i][0]] == True):
                Final_score[Board[i][0]][2] += 20
                if(Board[i][1] > Final_score[Board[i][0]][1]):
                    Final_score[Board[i][0]][1] = Board[i][1]
            else:
                Repeat[Board[i][0]] = True
                Board[i][2] = 20
                Final_score[Board[i][0]] = Board[i]
        elif(Board[i][3] == 'C'):
            if(Repeat[Board[i][0]] == True):
                Final_score[Board[i][0]][2] += Board[i][2]
                if(Board[i][1] > Final_score[Board[i][0]][1]):
                    Final_score[Board[i][0]][1] = Board[i][1]
            else:
                Repeat[Board[i][0]] = True
                Correct[Board[i][0]] = True    #to avoid 'I' after 'C'
                Final_score[Board[i][0]] = Board[i]

for i in Final_score:
    print(str(Final_score[i][:3]))