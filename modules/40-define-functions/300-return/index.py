from hexlet.code_basics import parent_for

# BEGIN
def get_parent_names_total_length(child):
    mother = parent_for(child, 'mother')
    father = parent_for(child, 'father')
    return len(mother) + len(father)
# END
