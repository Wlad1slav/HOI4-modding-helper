tags = """CZE
SLO
BUL
LAT
EST
LIT
UKR
BLR
SER
MOL
FIN
MAC
BOS
ROM
POL
AUS
CRO
GRE
HUN
SLV
GER
ITA
FRA""".split("\n")
z = '{'
x = '}'

for tag in tags:
    code = f"""
{tag}_gas_supplies = {z}

    icon = generic_political_rally

    allowed = {z} tag = SOV {x}
    
    visible = {z}
        {tag} = {z} has_country_flag = refused_pay_in_rubles {x}
   {x}

    fire_only_once = yes

    cost = 80
    
    complete_effect = {z}
        {tag} = {z} country_event = {z} id = rus.7 {x} {x}
        add_opinion_modifier = {z} target = {tag} modifier = embargo {x}
        {tag} = {z} add_opinion_modifier = {z} target = SOV modifier = embargo {x} {x}
   {x}
{x}
    """
    print(code)

for tag in tags:
    loc = f"""
 {tag}_gas_supplies:0 "Прекратить поставки газа в £{tag}_small"
"""
    print(loc, end='')

d = input()