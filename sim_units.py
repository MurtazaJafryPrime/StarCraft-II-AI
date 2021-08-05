"""
This program is where all of the stats for the StarCraft II units simulation
are stored.
Units is a dictionary with the keys being 'Terran', 'Protoss', and 'Zerg', and
the values being dictionaries with the stats of the units of those respective
races.
The primary function that will be called is the get_Units function
"""


def get_Units():
    """
    Returns a dictionary where the key is a race name,
    value is that race's dictionary of units
    """
    Units = {}
    Units['Terran'] = build_Terran()
    Units['Protoss'] = build_Protoss()
    Units['Zerg'] = build_Zerg()

    return Units


def build_Terran():
    """
    Returns the dictionary of the stats of all Terran units
    """
    Terran_Units = {}

    Marine = {}
    # Combat stats
    Marine['hp'] = 45
    Marine['dps'] = 9.8
    Marine['ranged'] = True
    Marine['armor'] = 0
    Marine['attributes'] = {'Biological', 'Light', 'Ground'}
    Marine['type'] = {'Ground'}
    Marine['targetable'] = {'Ground', 'Air'}
    Marine['bonuses'] = {}
    Marine['bonus_dps'] = 0
    Marine['healer'] = False
    # Resource stats
    Marine['mineral'] = 50
    Marine['gas'] = 0
    Marine['time'] = 18
    Marine['supply'] = 1
    Terran_Units['Marine'] = Marine

    SCV = {}
    # Combat stats
    SCV['hp'] = 45
    SCV['dps'] = 4.67
    SCV['ranged'] = False
    SCV['armor'] = 0
    SCV['attributes'] = {'Biological', 'Light', 'Mechanical', 'Ground'}
    SCV['targetable'] = {'Ground'}
    SCV['type'] = {'Ground'}
    SCV['bonuses'] = {}
    SCV['bonus_dps'] = 0
    SCV['healer'] = True
    # Resource stats
    SCV['mineral'] = 75
    SCV['gas'] = 0
    SCV['time'] = 12
    SCV['supply'] = 1
    Terran_Units['SCV'] = SCV

    Medivac = {}
    # Combat stats
    Medivac['hp'] = 150
    Medivac['dps'] = 0
    Medivac['ranged'] = False
    Medivac['armor'] = 1
    Medivac['attributes'] = {'Armored', 'Mechanical', 'Air'}
    Medivac['targetable'] = {}
    Medivac['type'] = {'Air'}
    Medivac['bonuses'] = {}
    Medivac['bonus_dps'] = 0
    Medivac['healer'] = True
    # Resource stats
    Medivac['mineral'] = 100
    Medivac['gas'] = 100
    Medivac['time'] = 30
    Medivac['supply'] = 2
    Terran_Units['Medivac'] = Medivac

    Hellion = {}
    # Combat stats
    Hellion['hp'] = 90
    Hellion['dps'] = 4.48*5
    Hellion['ranged'] = True
    Hellion['armor'] = 0
    Hellion['attributes'] = {'Light', 'Mechanical', 'Ground'}
    Hellion['targetable'] = {'Ground'}
    Hellion['type'] = {'Ground'}
    Hellion['bonuses'] = {'Light'}
    Hellion['bonus_dps'] = 3.4*5
    Hellion['healer'] = False
    # Resource stats
    Hellion['mineral'] = 100
    Hellion['gas'] = 0
    Hellion['time'] = 21
    Hellion['supply'] = 2
    Terran_Units['Hellion'] = Hellion

    return Terran_Units


def build_Protoss():
    """
    Returns a dictionary with all of the Protoss units
    """
    Protoss_Units = {}

    Probe = {}
    # Combat stats
    Probe['hp'] = 20+20
    Probe['dps'] = 4.67
    Probe['ranged'] = False
    Probe['armor'] = 0
    Probe['attributes'] = {'Light', 'Mechanical', 'Ground'}
    Probe['targetable'] = {'Ground'}
    Probe['type'] = {'Ground'}
    Probe['bonuses'] = {}
    Probe['bonus_dps'] = 0
    Probe['healer'] = False
    # Resource stats
    Probe['mineral'] = 50
    Probe['gas'] = 0
    Probe['time'] = 12
    Probe['supply'] = 1
    Protoss_Units['Probe'] = Probe

    Zealot = {}
    # Combat stats
    Zealot['hp'] = 100+50
    Zealot['dps'] = 18.6
    Zealot['ranged'] = False
    Zealot['armor'] = 1
    Zealot['attributes'] = {'Light', 'Biological', 'Ground'}
    Zealot['targetable'] = {'Ground'}
    Zealot['type'] = {'Ground'}
    Zealot['bonuses'] = {}
    Zealot['bonus_dps'] = 0
    Zealot['healer'] = False
    # Resource stats
    Zealot['mineral'] = 100
    Zealot['gas'] = 0
    Zealot['time'] = 27
    Zealot['supply'] = 2
    Protoss_Units['Zealot'] = Zealot

    Stalker = {}
    # Combat stats
    Stalker['hp'] = 80+80
    Stalker['dps'] = 9.7
    Stalker['ranged'] = True
    Stalker['armor'] = 1
    Stalker['attributes'] = {'Armored', 'Mechanical', 'Ground'}
    Stalker['targetable'] = {'Ground', 'Air'}
    Stalker['type'] = {'Ground'}
    Stalker['bonuses'] = {'Armored'}
    Stalker['bonus_dps'] = 3.7
    Stalker['healer'] = False
    # Resource stats
    Stalker['mineral'] = 125
    Stalker['gas'] = 50
    Stalker['time'] = 30
    Stalker['supply'] = 2
    Protoss_Units['Stalker'] = Stalker

    Sentry = {}
    # Combat stats
    Sentry['hp'] = 40+40
    Sentry['dps'] = 8.4
    Sentry['ranged'] = True
    Sentry['armor'] = 1
    Sentry['attributes'] = {'Light', 'Mechanical', 'Psionic', 'Ground'}
    Sentry['targetable'] = {'Ground', 'Air'}
    Sentry['type'] = {'Ground'}
    Sentry['bonuses'] = {}
    Sentry['bonus_dps'] = 0
    Sentry['healer'] = False
    # Resource stats
    Sentry['mineral'] = 50
    Sentry['gas'] = 100
    Sentry['time'] = 26
    Sentry['supply'] = 2
    Protoss_Units['Sentry'] = Sentry

    Adept = {}
    # Combat stats
    Adept['hp'] = 70+70
    Adept['dps'] = 6.2
    Adept['ranged'] = True
    Adept['armor'] = 1
    Adept['attributes'] = {'Light', 'Biological', 'Ground'}
    Adept['targetable'] = {'Ground'}
    Adept['type'] = {'Ground'}
    Adept['bonuses'] = {'Light'}
    Adept['bonus_dps'] = 7.45
    Adept['healer'] = False
    # Resource stats
    Adept['mineral'] = 100
    Adept['gas'] = 25
    Adept['time'] = 30
    Adept['supply'] = 2
    Protoss_Units['Adept'] = Adept

    HighTemplar = {}
    # Combat stats
    HighTemplar['hp'] = 40+40
    HighTemplar['dps'] = 3.2
    HighTemplar['ranged'] = True
    HighTemplar['armor'] = 0
    HighTemplar['attributes'] = {'Light', 'Biological', 'Psionic', 'Ground'}
    HighTemplar['targetable'] = {'Ground'}
    HighTemplar['type'] = {'Ground'}
    HighTemplar['bonuses'] = {}
    HighTemplar['bonus_dps'] = 0
    HighTemplar['healer'] = False
    # Resource stats
    HighTemplar['mineral'] = 50
    HighTemplar['gas'] = 150
    HighTemplar['time'] = 39
    HighTemplar['supply'] = 2
    Protoss_Units['HighTemplar'] = HighTemplar

    DarkTemplar = {}
    # Combat stats
    DarkTemplar['hp'] = 40+80
    DarkTemplar['dps'] = 37.2
    DarkTemplar['ranged'] = False
    DarkTemplar['armor'] = 1
    DarkTemplar['attributes'] = {'Light', 'Biological', 'Psionic', 'Ground'}
    DarkTemplar['targetable'] = {'Ground'}
    DarkTemplar['type'] = {'Ground'}
    DarkTemplar['bonuses'] = {}
    DarkTemplar['bonus_dps'] = 0
    DarkTemplar['healer'] = False
    # Resource stats
    DarkTemplar['mineral'] = 125
    DarkTemplar['gas'] = 150
    DarkTemplar['time'] = 39
    DarkTemplar['supply'] = 2
    Protoss_Units['DarkTemplar'] = DarkTemplar

    Immortal = {}
    # Combat stats
    Immortal['hp'] = 200+100
    Immortal['dps'] = 19.2
    Immortal['ranged'] = True
    Immortal['armor'] = 1
    Immortal['attributes'] = {'Armored', 'Mechanical', 'Ground'}
    Immortal['targetable'] = {'Ground'}
    Immortal['type'] = {'Ground'}
    Immortal['bonuses'] = {'Armored'}
    Immortal['bonus_dps'] = 28.9
    Immortal['healer'] = False
    # Resource stats
    Immortal['mineral'] = 275
    Immortal['gas'] = 100
    Immortal['time'] = 39
    Immortal['supply'] = 4
    Protoss_Units['Immortal'] = Immortal

    Colossus = {}
    # Combat stats
    Colossus['hp'] = 300+200
    Colossus['dps'] = 18.7
    Colossus['ranged'] = True
    Colossus['armor'] = 1
    Colossus['attributes'] = {'Armored', 'Mechanical', 'Massive', 'Ground'}
    Colossus['targetable'] = {'Ground'}
    Colossus['type'] = {'Ground', 'Air'}
    Colossus['bonuses'] = {'Light'}
    Colossus['bonus_dps'] = 9.3
    Colossus['healer'] = False
    # Resource stats
    Colossus['mineral'] = 300
    Colossus['gas'] = 200
    Colossus['time'] = 54
    Colossus['supply'] = 6
    Protoss_Units['Colossus'] = Colossus

    Archon = {}
    # Combat stats
    Archon['hp'] = 10+350
    Archon['dps'] = 20
    Archon['ranged'] = True
    Archon['armor'] = 0
    Archon['attributes'] = {'Psionic', 'Massive', 'Ground'}
    Archon['targetable'] = {'Ground', 'Air'}
    Archon['type'] = {'Ground'}
    Archon['bonuses'] = {}
    Archon['bonus_dps'] = 0
    Archon['healer'] = False
    # Resource stats
    # Assumes Archon is from two HT merged
    Archon['mineral'] = 50*2
    Archon['gas'] = 150*2
    Archon['time'] = 39*2+8.57
    Archon['supply'] = 4
    Protoss_Units['Archon'] = Archon

    Pheonix = {}
    # Combat stats
    Pheonix['hp'] = 120+60
    Pheonix['dps'] = 12.7
    Pheonix['ranged'] = True
    Pheonix['armor'] = 0
    Pheonix['attributes'] = {'Light', 'Mechanical', 'Air'}
    Pheonix['targetable'] = {'Air'}
    Pheonix['type'] = {'Air'}
    Pheonix['bonuses'] = {'Light'}
    Pheonix['bonus_dps'] = 12.7
    Pheonix['healer'] = False
    # Resource stats
    Pheonix['mineral'] = 150
    Pheonix['gas'] = 100
    Pheonix['time'] = 25
    Pheonix['supply'] = 2
    Protoss_Units['Pheonix'] = Pheonix

    VoidRay = {}
    # Combat stats
    VoidRay['hp'] = 150+100
    VoidRay['dps'] = 16.8
    VoidRay['ranged'] = True
    VoidRay['armor'] = 0
    VoidRay['attributes'] = {'Armored', 'Mechanical', 'Air'}
    VoidRay['targetable'] = {'Air', 'Ground'}
    VoidRay['type'] = {'Air'}
    VoidRay['bonuses'] = {'Armored'}
    VoidRay['bonus_dps'] = 11.2
    VoidRay['healer'] = False
    # Resource stats
    VoidRay['mineral'] = 200
    VoidRay['gas'] = 150
    VoidRay['time'] = 37
    VoidRay['supply'] = 4
    Protoss_Units['VoidRay'] = VoidRay

    Oracle = {}
    # Combat stats
    Oracle['hp'] = 100+60
    Oracle['dps'] = 24.4
    Oracle['ranged'] = True
    Oracle['armor'] = 0
    Oracle['attributes'] = {'Armored', 'Mechanical', 'Psionic', 'Air'}
    Oracle['targetable'] = {'Ground'}
    Oracle['type'] = {'Air'}
    Oracle['bonuses'] = {'Light'}
    Oracle['bonus_dps'] = 11.5
    Oracle['healer'] = False
    # Resource stats
    Oracle['mineral'] = 150
    Oracle['gas'] = 150
    Oracle['time'] = 37
    Oracle['supply'] = 3
    Protoss_Units['Oracle'] = Oracle

    Tempest = {}
    # Combat stats
    Tempest['hp'] = 200+100
    Tempest['dps'] = 16.97+12.73
    Tempest['ranged'] = True
    Tempest['armor'] = 2
    Tempest['attributes'] = {'Armored', 'Mechanical', 'Massive', 'Air'}
    Tempest['targetable'] = {'Ground', 'Air'}
    Tempest['type'] = {'Air'}
    Tempest['bonuses'] = {'Massive'}
    Tempest['bonus_dps'] = 9.32
    Tempest['healer'] = False
    # Resource stats
    Tempest['mineral'] = 250
    Tempest['gas'] = 175
    Tempest['time'] = 43
    Tempest['supply'] = 5
    Protoss_Units['Tempest'] = Tempest

    Mothership = {}
    # Combat stats
    Mothership['hp'] = 350+350
    Mothership['dps'] = 22.7
    Mothership['ranged'] = True
    Mothership['armor'] = 2
    Mothership['attributes'] = {'Armored', 'Mechanical', 'Massive', 'Psionic', 'Heroic', 'Air'}
    Mothership['targetable'] = {'Ground', 'Air'}
    Mothership['type'] = {'Air'}
    Mothership['bonuses'] = {}
    Mothership['bonus_dps'] = 0
    Mothership['healer'] = False
    # Resource stats
    Mothership['mineral'] = 400
    Mothership['gas'] = 400
    Mothership['time'] = 114
    Mothership['supply'] = 8
    Protoss_Units['Mothership'] = Mothership

    Interceptor = {}
    # Combat stats
    Interceptor['hp'] = 40+40
    Interceptor['dps'] = 4.7
    Interceptor['ranged'] = True
    Interceptor['armor'] = 0
    Interceptor['attributes'] = {'Light', 'Mechanical', 'Air'}
    Interceptor['targetable'] = {'Ground', 'Air'}
    Interceptor['type'] = {'Air'}
    Interceptor['bonuses'] = {}
    Interceptor['bonus_dps'] = 0
    Interceptor['healer'] = False
    # Resource stats
    # Interceptors are only built as a part of a Carrier
    Interceptor['mineral'] = 15
    Interceptor['gas'] = 0
    Interceptor['time'] = 9
    Interceptor['supply'] = 0
    Protoss_Units['Interceptor'] = Interceptor

    Carrier = {}
    # Combat stats
    Carrier['hp'] = 300+150
    Carrier['dps'] = 0
    Carrier['ranged'] = False
    Carrier['armor'] = 2
    Carrier['attributes'] = {'Armored', 'Mechanical', 'Massive', 'Air'}
    Carrier['targetable'] = {}
    Carrier['type'] = {'Air'}
    Carrier['bonuses'] = {}
    Carrier['bonus_dps'] = 0
    Carrier['healer'] = False
    # Resource stats
    # Additional Mineral cost to adjust for the fact that
    # Interceptors will be built automatically
    Carrier['mineral'] = 350+15*4
    Carrier['gas'] = 250
    Carrier['time'] = 64
    Carrier['supply'] = 6
    Protoss_Units['Carrier'] = Carrier

    return Protoss_Units


def build_Zerg():
    """
    Returns a dictionary of all of the Zerg units
    """
    Zerg_Units = {}

    return Zerg_Units