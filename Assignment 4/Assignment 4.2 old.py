sample_rock_positions = ["041Y1","209R1","389Y1","596R1",\
                         "045Y2","198R2","376R2","380R2","415R2","606R2",\
                         "043Y3","071Y3","108R3","400Y3","402Y3",\
                         "042Y4","075Y4","076Y4","422R4"]


calculate score for the end
    filter for consecutive colour i_colour = i+1+colour if not blank for range (l-1)
    calculate  score by summing int of score for each string

def score_from_each_end (colour, rock_positions, i, end_score):
    M = list filter for each end so M has only one end
    if M[0].colour = colour
        calculate score for the end
    return end_score

def sort_order(s):
    return s[4] + s[0:2]

def score(colour, rock_positions):
    rock_positions.sort(key=sort_order)
    #print(rock_positions)
    #N= create_loL(rock_positions.sort(key=sort_order), 0)
    #print(N)
    #N = list(map(lambda i: create_row(rock_positions.sort(key = sort_order)), rock_positions.sort(key = sort_order)))
    Number_of_ends = 99
    L = list(filter(lambda i: score_from_each_end(colour, rock_positions, i, 0), range(Number_of_ends))
    final_score = sum all L
    return final_score

print(score("R", ["101R1", "115R3", "116R1", "012R3", "222R8"]))