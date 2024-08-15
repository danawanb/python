
def get_formatted_name(first :str, last:str, middle='') -> str:
    if middle:
        full_name = f"{first} {middle} {last}"
        return  full_name.title()
    else:
        full_name = f"{first} {last}"
        return full_name.title()


def test_get_format_name():
    formated_name  = get_formatted_name('Joni', 'Depp', 'Robi')
    assert formated_name == 'Joni Depp'
