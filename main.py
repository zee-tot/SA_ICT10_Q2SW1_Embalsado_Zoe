from pyscript import document

def result_checker(e):
    club_members = ['Hariette Onofre','David Barretto', 'Sianna Santiago', 'Nyle Gutierrez', 'Sophia Pedro', 'Eliesha Bulo', 'Mikaela Cuevas', 'Ethan Park', 'Zoe Embalsado', 'Stefan Pada', 'Oslyn Donato', 'Kyrene Leonardo', 'Allain Magsino']

    #Retrieves the first and last name from the input fields
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    #Concatenates the first and last name to create a candidate variable and checks if the candidate is in the club_members list
    candidate = first_name + ' ' + last_name
    member_checker = candidate.title() in club_members

    #Messages: index 0 = not a member, index 1 = member
    messages = (f'Sorry {candidate.title()}, you are not a member of Glee club.', f'Congratulations {candidate.title()}, you are now a member of Glee club!')

    #Displays the message according to the member_checker boolean value
    document.getElementById('output').innerHTML = messages[member_checker]