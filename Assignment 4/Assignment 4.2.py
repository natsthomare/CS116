sample_rock_positions = ["041Y1","209R1","389Y1","596R1",\
                         "045Y2","198R2","376R2","380R2","415R2","606R2",\
                         "043Y3","071Y3","108R3","400Y3","402Y3",\
                         "042Y4","075Y4","076Y4","422R4"]

sample1_rock_positions = ["041Y1","209R1","389Y1","596R1",\
                         "045Y2","198R2","376R2","380R2","415R2","606R2",\
                         "043R3","071Y3","108R3","400Y3","402Y3",\
                         "042R4","075Y4","076Y4","422R4"]
sample2_rock_positions = ["100Y1",	"100Y2",	"100Y3",	"100Y4",	"100Y5",	"100Y6",	"100Y7",	"100Y8",\
                          "100Y9",	"100Y10",	"100Y11",	"100Y12",	"100Y13",	"100Y14",	"100Y15",	"100Y16",\
                          "100Y17",	"100Y18",	"100Y19",	"100Y20",	"100Y21",	"100Y22",	"100Y23",	"100Y24",\
                          "100Y25",	"100Y26",	"100Y27",	"100Y28",	"100Y29",	"100Y30",	"100Y31",	"100Y32",\
                          "100Y33",	"100Y34",	"100Y35",	"100Y36",	"100Y37",	"100Y38",	"100Y39",	"100Y40",\
                          "100Y41",	"100Y42",	"100Y43",	"100Y44",	"100Y45",	"100Y46",	"100Y47",	"100Y48",\
                          "100Y49",	"100Y50",	"100R51",	"100R52",	"100R53",	"100R54",	"100R55",	"100R56",\
                          "100R57",	"100R58",	"100R59",	"100R60",	"100R61",	"100R62",	"100R63",	"100R64",\
                          "100R65",	"100R66",	"100R67",	"100R68",	"100R69",	"100R70",	"100R71",	"100R72",\
                          "100R73",	"100R74",	"100R75",	"100R76",	"100R77",	"100R78",	"100R79",	"100R80",\
                          "100R81",	"100R82",	"100R83",	"100R84",	"100R85",	"100R86",	"100R87",	"100R88",\
                          "100R89",	"100R90",	"100R91",	"100R92",	"100R93",	"100R94",	"100R95",	"100R96",\
                          "100R97",	"100R98",	"100R99"]
flag1 = False

def check_next(k,M,colour):
    global flag1

    if flag1 == True:
        #print(k)
        if k +1 == len(M):
            return False
        #print(M[k][3],M[k+1][3])
        if M[k][3] == colour and M[k+1][3] ==colour:
            #print ("flag1=", flag1)
            #print(True)
            return True
        else:
            flag1 = False
            return False
    else:
        return False

def calculate_score_for_the_end(M,colour):
    #print("M=",M)
    N= list(filter(lambda k: check_next(k,M,colour), range(len(M))))
    #print("N=",N, "len of N=", len(N))
    return len(N)
    ##filter for consecutive colour i_colour = i+1+colour if not blank for range (l-1)
    ##calculate  score by summing int of score for each string



def check_end_number(j,i):
    ##print(i,j)
    if int(j[4:]) == i:
        return j
    else:
        return ""

'''
def check_not_space(M,a):
    if M[a] != "":
        return True
    else:
        return False
'''
def score_from_each_end (colour, rock_positions, i, end_score):
    global flag1
    #print(i)
    Q = list(map(lambda j: check_end_number(j,i),rock_positions))
    M= list(filter(lambda a: a !="" ,Q))
    #print(M)
    flag1 =False
    if M == []:
        return 0
    if M[0][3] == colour:
        end_score= 1
        flag1 = True
        end_score= end_score+calculate_score_for_the_end(M,colour)
        #print("endscore",end_score)
        return end_score
        ##calculate score for the end
    else:
        return end_score

def sort_order(s):
    return s[4] +  s[0:2]




def score(colour, rock_positions):
    '''

    :param colour:
    :param rock_positions:
    :return:
    Requires there is no tie on any of the ends
             0 < number of ends < 100

    '''
    if rock_positions != []:
        rock_positions.sort(key=sort_order)
        number_of_ends = int(rock_positions[-1][4:])
        #print(number_of_ends)
        L = list(map(lambda i: score_from_each_end(colour, rock_positions, i, 0), range(1,number_of_ends+1)))
        #print(L)
        return sum(L)
    else:
        return 0


print("No rocks in the house and check for Red score:", score("R", []))
print("No rocks in the house and check for Yellow score:", score("Y", []))
print("1 Red rock in the house and check for Red score:", score("R", ["101R1"]))
print("1 Red and 1 Yellow rock in the house for different ends and check for Red score:", \
      score("R", ["101R1", "101Y2"]))
print("1 Red and 1 Yellow rock in the house for different ends and check for Yellow score:", \
      score("Y", ["101R1", "101Y2"]))
print("Only Red rocks win with one in each end and check for Red score:", \
      score("R", ["101R1", "115R2", "115R3", "114R5"] ))
print("Only Red rocks win with one in each end and check for Yellow score:", \
      score("R", ["101R1", "115R2", "115R3", "114R5"] ))
print("Only Red rocks win more than one rock for an end and check for Red score:",
      score("R", ["101R1", "115R3", "115R1", "114R1", "116R1", "012R3", "222R8"]))
print("Only Red rocks win more than one rock for an end and check for Yellow score:", \
      score("Y", ["101R1", "115R3", "115R1", "114R1", "116R1", "012R3", "222R8"]))
print("Red rocks win with one end and some yelllow rocks before red in the house and check for Red score:",\
      score("R", ["113R1", "114R1", "115R1", "116Y1", "117R1"]))
print("Red rocks win with one end and some yelllow rocks before red in the house and check for Yellow score:", \
      score("Y", ["113R1", "114R1", "115R1", "116Y1", "117R1"]))
print("Red rocks win more than one end with some yelllow rocks before red in the house and check for Red score:", \
      score("R", ["113R1", "114R1", "115R1", "116Y1", "117R1", "100R2", "100Y3"]))
print("Multiple end with only Yellow wins and check for Red score: ", score("R", sample_rock_positions))
print("Multiple end with only Yellow wins and check for Yellow score: ", score("Y", sample_rock_positions))
print("Multiple end wins for Red and Yellow and check for Red score:", score("R", sample1_rock_positions))
print("Multiple end wins for Red and Yellow and check for Yellow score:", score("R", sample1_rock_positions))
print("99 ends with multiple end wins for Red and Yellow and check for Red score:", \
      score("R", sample2_rock_positions))
print("99 ends with multiple end wins for Red and Yellow and check for Yellow score:", \
      score("Y", sample2_rock_positions))
