import index

def test1():
    actual1 = index.custom_parent_for('Cersei Lannister')
    assert actual1 == 'Tywin Lannister'

    actual2 = index.custom_parent_for('Daenerys Targaryen', 'mother')
    assert actual1 == 'Rhaella Targaryen'
