'''Displays the field that was generated by first__issue_generate_field.
What it do:
1. import generate_field
2. Numerate a columns in alphabetical.
3. Numerate a rows in digital.
4. Align first row (alphabetical)
5. Align first column of the field (digital).
6. Print the final look of the field (You can append print_field() into the to display field).
Attention!!!
Function "generate_field" consist function "change_field"
Quote:
    Function for making changes in field.
    It's created for future development. For now it's doing nothing.
    It just take the list and return it back without changes'''


from generate_field import generate_field, change_field, create_list_alphabet, generate_dig_list


def align_first_row():
    l = create_list_alphabet()
    '''List begins with " ", its align first symbol'''
    l.insert(0, "  " * (len(str(max(generate_dig_list()))) - len(l[0])))
    '''It\'s cut the list to appropriate size for print'''
    l = l[0: len(generate_field()[0]) + 1]
    return l


def add_first_element_to_list(l):
    ''' Adding a first element to the nested list.
     As a result we get numbered zero elements in nested lists'''
    count = 1
    for i in l:
        '''Separate ordinary lists (type will be != list) from nested lists'''
        if type(i) == list:
            for j in align_first_column(generate_dig_list()):
                if int(j) == count:
                    i.insert(0, j)
            count += 1
    return l


def align_first_column(l):
    '''Function makes alignment of first column in field output
    It add spaces to element if needed'''
    l = generate_dig_list()
    l_new = []
    for i in l:
        if len(str(i)) <= len(str(max(l))):
            '''Count's number of spaces that we need to write before element,
            that they have the same length.'''
            spaces_number = len(str(max(l))) - len(str(i))
            i = " " * spaces_number + str(i)
            l_new.append(i)
    return l_new


def print_field():
    print(*align_first_row())
    '''It's print the field generated by generate_field'''
    for i in add_first_element_to_list(change_field(generate_field())):
        x = i
        print(*x)

