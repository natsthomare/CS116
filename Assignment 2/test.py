def userid(first_name, middle_name, last_name):
    '''
    Returns the at most 8 chracter user id
    given the first middle and last name

    userid: Str Str Str -> Str
    Requires:
       1 <= len(first_name)
       1 <= len(last_name)

    Examples:
       userid("Harry", "James", "Potter") => "hjpotter"
       userid("Ronald", "Bilius", "Weasley") => "rbweasle"

    '''
    ##YOUR CODE GOES HERE
    if middle_name != "":
        uid = (first_name[0].lower())+(middle_name[0].lower())+last_name[0:6].lower()
    else:
        uid = (first_name[0].lower()) + last_name[0:7].lower()
    print (uid)



userid("Harry", "James", "Potter")
userid("Ronald", "Bilius", "Weasley")
userid("Ronald", "", "Weasley")