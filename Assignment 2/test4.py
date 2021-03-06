def name_change(old, new_last):
    '''
    Changes the old string's last name to the string new_last

    name_change: Str Str -> Str
    Requires:
       old contains at least one space separating first
       and last name.

    Examples:
       name_change("John Doe", "Smith") => "John Smith"
       name_change("Bruce Thomas Wayne", "Willis") => "Bruce Thomas Willis"
    '''
    start = ( old.rfind(" "))
    print(old[start+1:])
    new = old.replace(old[start+1:], new_last)
    print (new)


name_change("John Doe", "Smith")
name_change("Bruce Thomas Wayne", "Willis")

