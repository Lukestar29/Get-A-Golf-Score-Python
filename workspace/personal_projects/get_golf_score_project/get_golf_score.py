letterkenny_index = [5, 7, 11, 15, 17, 1, 9, 13, 3, 6, 12, 14, 8, 16, 2, 18, 4, 10]
letterkenny_par = [4 ,5, 4, 4, 3, 4, 5, 3, 4, 4, 5, 4, 3, 4, 4, 3, 4, 5]
def get_golf_score(hole_score, hole_par, hole_index, handicap):
    course_par = 0
    for hole in letterkenny_par:
        course_par += letterkenny_par[hole]
    dict_1 = {}
    dict_2 = {}
    hole_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    for index1 in range(len(hole_score)):
        value = hole_score[index1]
        actual_index = index1 + 1
        dict_1[actual_index] = value
    for index2 in range(len(hole_par)):
        value2 = hole_par[index2]
        actual_index = index2 + 1
        dict_2[actual_index] = value2
    diff_in_score = []
    score_with_handicap = []
    stableford_points_dict = {}
    total_stableford_points = 0
    shots_over_par = 0
    over_or_under_par = "over"
    for num in hole_num:
        stableford_points_for_hole = 2
        diff_in_score.append(dict_1[num] - dict_2[num])
        if handicap >= 18:
            extra_shot_index = handicap - 18
            if hole_index[num - 1] <= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 2)
            elif hole_index[num - 1] >= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 1)
        elif handicap <= 18:
            extra_shot_index = handicap - 0
            if hole_index[num - 1] <= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 1)
            elif hole_index[num - 1] >= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 0)
        stableford_points_for_hole -= score_with_handicap[num - 1]
        if stableford_points_for_hole < 0:
            stableford_points_for_hole = 0
        stableford_points_dict[num] = stableford_points_for_hole
        total_stableford_points += stableford_points_for_hole
        shots_over_par += diff_in_score[num - 1]
    if shots_over_par < 0:
        over_or_under_par = "under"
        random_variable = shots_over_par ** 2
        shots_over_par = math.sqrt(random_variable)
        
    total_shots = 0
    for hole in hole_score:
        total_shots += hole
    return_string = f"Stableford points for each hole:\nHole: Amount Of Points\n{stableford_points_dict}\nTotal Amount Of Points: {total_stableford_points}!\nTotal Shots in Round: {total_shots}!\nIn Total, you were {shots_over_par} shots {over_or_under_par} par!"
    return return_string
 
hole_score = []
hole_names = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth"]

for index3 in range(len(hole_names)):
    value3 = hole_names[index3]
    hole_name = hole_names[index3]
    try:
        hole_score.append(int(input(f"What score did you get on the {hole_name} hole?")))
    except ValueError:
        print("only whole numbers please.")
        try:
            hole_score.append(int(input(f"What score did you get on the {hole_name} hole?")))
        except ValueError:
            print("only whole numbers please. Restart and try again.")
try:
    handicap = int(input("What is your handicap?(whole number)"))
except ValueError:
    print("only whole numbers please. Restart the software")
def get_golf_score_with_prompt(hole_par, hole_index):
    course_par = 0
    for hole in letterkenny_par:
        course_par += letterkenny_par[hole]
    dict_1 = {}
    dict_2 = {}
    hole_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    for index1 in range(len(hole_score)):
        value = hole_score[index1]
        actual_index = index1 + 1
        dict_1[actual_index] = value
    for index2 in range(len(hole_par)):
        value2 = hole_par[index2]
        actual_index = index2 + 1
        dict_2[actual_index] = value2
    diff_in_score = []
    score_with_handicap = []
    stableford_points_dict = {}
    total_stableford_points = 0
    shots_over_par = 0
    over_or_under_par = "over"
    for num in hole_num:
        stableford_points_for_hole = 2
        diff_in_score.append(dict_1[num] - dict_2[num])
        if handicap >= 18:
            extra_shot_index = handicap - 18
            if hole_index[num - 1] <= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 2)
            elif hole_index[num - 1] >= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 1)
        elif handicap <= 18:
            extra_shot_index = handicap - 0
            if hole_index[num - 1] <= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 1)
            elif hole_index[num - 1] >= extra_shot_index:
                score_with_handicap.append(diff_in_score[num - 1] - 0)
        stableford_points_for_hole -= score_with_handicap[num - 1]
        if stableford_points_for_hole < 0:
            stableford_points_for_hole = 0
        stableford_points_dict[num] = stableford_points_for_hole
        total_stableford_points += stableford_points_for_hole
        shots_over_par += diff_in_score[num - 1]
    if shots_over_par < 0:
        over_or_under_par = "under"
        random_variable = shots_over_par ** 2
        shots_over_par = math.sqrt(random_variable)
        
    total_shots = 0
    for hole in hole_score:
        total_shots += hole
    return_string = f"""
    Stableford points for each hole:\n
    Points on the first:{stableford_points_dict[1]}
    Points on the second:{stableford_points_dict[2]}
    Points on the third:{stableford_points_dict[3]}
    Points on the fourth:{stableford_points_dict[4]}
    Points on the fifth:{stableford_points_dict[5]}
    Points on the sixth:{stableford_points_dict[6]}
    Points on the seventh:{stableford_points_dict[7]}
    Points on the eighth:{stableford_points_dict[8]}
    Points on the ninth:{stableford_points_dict[9]}
    Points on the tenth:{stableford_points_dict[10]}
    Points on the eleventh:{stableford_points_dict[11]}
    Points on the twelth:{stableford_points_dict[12]}
    Points on the thirteenth:{stableford_points_dict[13]}
    Points on the fourteenth:{stableford_points_dict[14]}
    Points on the fifteenth:{stableford_points_dict[15]}
    Points on the sixteenth:{stableford_points_dict[16]}
    Points on the seventeenth:{stableford_points_dict[17]}
    Points on the eighteenth:{stableford_points_dict[18]}
    Total Amount Of Points: {total_stableford_points}!\n
    Total Shots in Round: {total_shots}!\nIn Total, you were {shots_over_par} shots {over_or_under_par} par!
    """
    return return_string





#1 Points on the first:{stableford_points_dict[1]}
#2 Points on the second:{stableford_points_dict[2]}
#3 Points on the third:{stableford_points_dict[3]}
#4 Points on the fourth:{stableford_points_dict[4]}
#5 Points on the fifth:{stableford_points_dict[5]}
#6 Points on the sixth:{stableford_points_dict[6]}
#7 Points on the seventh:{stableford_points_dict[7]}
#8 Points on the eighth:{stableford_points_dict[8]}
#9 Points on the ninth:{stableford_points_dict[9]}
#10 Points on the tenth:{stableford_points_dict[10]}
#11 Points on the eleventh:{stableford_points_dict[11]}
#12 Points on the twelth:{stableford_points_dict[12]}
#13 Points on the thirteenth:{stableford_points_dict[13]}
#14 Points on the fourteenth:{stableford_points_dict[14]}
#15 Points on the fifteenth:{stableford_points_dict[15]}
#16 Points on the sixteenth:{stableford_points_dict[16]}
#17 Points on the seventeenth:{stableford_points_dict[17]}
#18 Points on the eighteenth:{stableford_points_dict[18]}









print(get_golf_score_with_prompt(letterkenny_par, letterkenny_index))
