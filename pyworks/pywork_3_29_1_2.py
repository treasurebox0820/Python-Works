def month(input_year=0, input_month=0):
    print(input_year, input_month)
    return """
{}     M T W T F S S
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaa
aaaaaaaaa
""".format(input_month)