"""
This program is where all of the stats for the StarCraft II units simulation
are stored.
There are four dictionaries, one for each race and one that includes all races
The dictionaries have the unit name as the key, and then a dictionary with
the unit stats as the value.
"""


def get_Units():
    """
    Returns a dictionary where the key is a race name,
    value is that race's dictionary of units
    """
    Units = {}
    Terran = get_Terran()
    Protoss = get_Protoss()
    Zerg = get_Zerg()
    Units.update(Terran)
    Units.update(Zerg)
    Units.update(Protoss)

    return Units


def get_Terran():
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

    Marauder = {}
    # Combat stats
    Marauder['hp'] = 125
    Marauder['dps'] = 9.3
    Marauder['ranged'] = True
    Marauder['armor'] = 1
    Marauder['attributes'] = {'Biological', 'Armored', 'Ground'}
    Marauder['type'] = {'Ground'}
    Marauder['targetable'] = {'Ground'}
    Marauder['bonuses'] = {'Armored'}
    Marauder['bonus_dps'] = 9.3
    Marauder['healer'] = False
    # Resource stats
    Marauder['mineral'] = 100
    Marauder['gas'] = 25
    Marauder['time'] = 21
    Marauder['supply'] = 2
    Terran_Units['Marauder'] = Marauder

    Reaper = {}
    # Combat stats
    Reaper['hp'] = 60
    Reaper['dps'] = 10.1
    Reaper['ranged'] = True
    Reaper['armor'] = 0
    Reaper['attributes'] = {'Biological', 'Light', 'Ground'}
    Reaper['type'] = {'Ground'}
    Reaper['targetable'] = {'Ground'}
    Reaper['bonuses'] = {}
    Reaper['bonus_dps'] = 0
    Reaper['healer'] = False
    # Resource stats
    Reaper['mineral'] = 50
    Reaper['gas'] = 50
    Reaper['time'] = 32
    Reaper['supply'] = 1
    Terran_Units['Reaper'] = Reaper

    Ghost = {}
    # Combat stats
    Ghost['hp'] = 100
    Ghost['dps'] = 9.3
    Ghost['ranged'] = True
    Ghost['armor'] = 0
    Ghost['attributes'] = {'Biological', 'Psionic', 'Ground'}
    Ghost['type'] = {'Ground'}
    Ghost['targetable'] = {'Ground', 'Air'}
    Ghost['bonuses'] = {'Light'}
    Ghost['bonus_dps'] = 9.3
    Ghost['healer'] = False
    # Resource stats
    Ghost['mineral'] = 150
    Ghost['gas'] = 125
    Ghost['time'] = 29
    Ghost['supply'] = 2
    Terran_Units['Ghost'] = Ghost

    Hellbat = {}
    # Combat stats
    Hellbat['hp'] = 135
    Hellbat['dps'] = 12.6*2
    Hellbat['ranged'] = False
    Hellbat['armor'] = 0
    Hellbat['attributes'] = {'Biological', 'Light', 'Mechanical', 'Ground'}
    Hellbat['type'] = {'Ground'}
    Hellbat['targetable'] = {'Ground'}
    Hellbat['bonuses'] = {'Light'}
    Hellbat['bonus_dps'] = 8.4
    Hellbat['healer'] = False
    # Resource stats
    Hellbat['mineral'] = 100
    Hellbat['gas'] = 0
    Hellbat['time'] = 21
    Hellbat['supply'] = 2
    Terran_Units['Hellbat'] = Hellbat

    SiegeTank = {}
    # Combat stats
    SiegeTank['hp'] = 150
    SiegeTank['dps'] = 18.69
    SiegeTank['ranged'] = True
    SiegeTank['armor'] = 1
    SiegeTank['attributes'] = {'Armored', 'Mechanical', 'Ground'}
    SiegeTank['type'] = {'Ground'}
    SiegeTank['targetable'] = {'Ground'}
    SiegeTank['bonuses'] = {'Armored'}
    SiegeTank['bonus_dps'] = 14.02
    SiegeTank['healer'] = False
    # Resource stats
    SiegeTank['mineral'] = 150
    SiegeTank['gas'] = 125
    SiegeTank['time'] = 32
    SiegeTank['supply'] = 3
    Terran_Units['SiegeTank'] = SiegeTank

    Cyclone = {}
    # Combat stats
    Cyclone['hp'] = 120
    Cyclone['dps'] = 25.2
    Cyclone['ranged'] = True
    Cyclone['armor'] = 1
    Cyclone['attributes'] = {'Armored', 'Mechanical', 'Ground'}
    Cyclone['type'] = {'Ground'}
    Cyclone['targetable'] = {'Ground', 'Air'}
    Cyclone['bonuses'] = {}
    Cyclone['bonus_dps'] = 0
    Cyclone['healer'] = False
    # Resource stats
    Cyclone['mineral'] = 150
    Cyclone['gas'] = 100
    Cyclone['time'] = 32
    Cyclone['supply'] = 3
    Terran_Units['Cyclone'] = Cyclone

    Thor = {}
    # Combat stats
    Thor['hp'] = 400
    Thor['dps'] = 65.9+11.2
    Thor['ranged'] = True
    Thor['armor'] = 1
    Thor['attributes'] = {'Armored', 'Mechanical', 'Massive', 'Ground'}
    Thor['type'] = {'Ground'}
    Thor['targetable'] = {'Ground', 'Air'}
    Thor['bonuses'] = {'Light', 'Massive'}
    Thor['bonus_dps'] = 11.2
    Thor['healer'] = False
    # Resource stats
    Thor['mineral'] = 300
    Thor['gas'] = 200
    Thor['time'] = 43
    Thor['supply'] = 6
    Terran_Units['Thor'] = Thor

    Viking = {}
    # Combat stats
    Viking['hp'] = 135
    Viking['dps'] = 14
    Viking['ranged'] = True
    Viking['armor'] = 0
    Viking['attributes'] = {'Armored', 'Mechanical', 'Air'}
    Viking['type'] = {'Air'}
    Viking['targetable'] = {'Air'}
    Viking['bonuses'] = {'Armored'}
    Viking['bonus_dps'] = 5.59
    Viking['healer'] = False
    # Resource stats
    Viking['mineral'] = 150
    Viking['gas'] = 75
    Viking['time'] = 30
    Viking['supply'] = 2
    Terran_Units['Viking'] = Viking

    Liberator = {}
    # Combat stats
    Liberator['hp'] = 180
    Liberator['dps'] = 65.8
    Liberator['ranged'] = True
    Liberator['armor'] = 0
    Liberator['attributes'] = {'Armored', 'Mechanical', 'Air'}
    Liberator['type'] = {'Air'}
    Liberator['targetable'] = {'Ground'}
    Liberator['bonuses'] = {}
    Liberator['bonus_dps'] = 0
    Liberator['healer'] = False
    # Resource stats
    Liberator['mineral'] = 150
    Liberator['gas'] = 150
    Liberator['time'] = 43
    Liberator['supply'] = 3
    Terran_Units['Liberator'] = Liberator

    Banshee = {}
    # Combat stats
    Banshee['hp'] = 140
    Banshee['dps'] = 27
    Banshee['ranged'] = True
    Banshee['armor'] = 0
    Banshee['attributes'] = {'Light', 'Mechanical', 'Air'}
    Banshee['type'] = {'Air'}
    Banshee['targetable'] = {'Ground'}
    Banshee['bonuses'] = {}
    Banshee['bonus_dps'] = 0
    Banshee['healer'] = False
    # Resource stats
    Banshee['mineral'] = 150
    Banshee['gas'] = 100
    Banshee['time'] = 43
    Banshee['supply'] = 3
    Terran_Units['Banshee'] = Banshee

    Battlecruiser = {}
    # Combat stats
    Battlecruiser['hp'] = 550
    Battlecruiser['dps'] = 49.8
    Battlecruiser['ranged'] = True
    Battlecruiser['armor'] = 3
    Battlecruiser['attributes'] = {'Armored', 'Massive', 'Mechanical', 'Air'}
    Battlecruiser['type'] = {'Air'}
    Battlecruiser['targetable'] = {'Ground', 'Air'}
    Battlecruiser['bonuses'] = {}
    Battlecruiser['bonus_dps'] = 0
    Battlecruiser['healer'] = False
    # Resource stats
    Battlecruiser['mineral'] = 400
    Battlecruiser['gas'] = 300
    Battlecruiser['time'] = 64
    Battlecruiser['supply'] = 6
    Terran_Units['Battlecruiser'] = Battlecruiser

    return Terran_Units


def get_Protoss():
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
    Colossus['dps'] = 18.7*2.8
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
    Archon['time'] = 39+8.57
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


def get_Zerg():
    """
    Returns a dictionary of all of the Zerg units
    """
    Zerg_Units = {}

    Drone = {}
    # Combat stats
    Drone['hp'] = 40
    Drone['dps'] = 4.67
    Drone['ranged'] = False
    Drone['armor'] = 0
    Drone['attributes'] = {'Light', 'Biological', 'Ground'}
    Drone['targetable'] = {'Ground'}
    Drone['type'] = {'Ground'}
    Drone['bonuses'] = {}
    Drone['bonus_dps'] = 0
    Drone['healer'] = False
    # Resource stats
    Drone['mineral'] = 50
    Drone['gas'] = 0
    Drone['time'] = 12
    Drone['supply'] = 1
    Zerg_Units['Drone'] = Drone

    Queen = {}
    # Combat stats
    Queen['hp'] = 175
    Queen['dps'] = 12.6
    Queen['ranged'] = True
    Queen['armor'] = 1
    Queen['attributes'] = {'Psionic', 'Biological', 'Ground'}
    Queen['targetable'] = {'Ground', 'Air'}
    Queen['type'] = {'Ground'}
    Queen['bonuses'] = {}
    Queen['bonus_dps'] = 0
    Queen['healer'] = False
    # Resource stats
    Queen['mineral'] = 150
    Queen['gas'] = 0
    Queen['time'] = 36
    Queen['supply'] = 2
    Zerg_Units['Queen'] = Queen

    Zergling = {}
    # Combat stats
    Zergling['hp'] = 35
    Zergling['dps'] = 10
    Zergling['ranged'] = False
    Zergling['armor'] = 0
    Zergling['attributes'] = {'Light', 'Biological', 'Ground'}
    Zergling['targetable'] = {'Ground'}
    Zergling['type'] = {'Ground'}
    Zergling['bonuses'] = {}
    Zergling['bonus_dps'] = 0
    Zergling['healer'] = False
    # Resource stats
    Zergling['mineral'] = 25
    Zergling['gas'] = 0
    Zergling['time'] = 17
    Zergling['supply'] = 0.5
    Zerg_Units['Zergling'] = Zergling

    Baneling = {}
    # Combat stats
    Baneling['hp'] = 30
    Baneling['dps'] = 16*2.2
    Baneling['ranged'] = False
    Baneling['armor'] = 0
    Baneling['attributes'] = {'Biological', 'Ground'}
    Baneling['targetable'] = {'Ground'}
    Baneling['type'] = {'Ground'}
    Baneling['bonuses'] = {'Light'}
    Baneling['bonus_dps'] = 19
    Baneling['healer'] = False
    # Resource stats
    Baneling['mineral'] = 25+25
    Baneling['gas'] = 25
    Baneling['time'] = 17+14
    Baneling['supply'] = 0.5
    Zerg_Units['Baneling'] = Baneling

    Roach = {}
    # Combat stats
    Roach['hp'] = 145
    Roach['dps'] = 11.2
    Roach['ranged'] = True
    Roach['armor'] = 1
    Roach['attributes'] = {'Armored', 'Biological', 'Ground'}
    Roach['targetable'] = {'Ground'}
    Roach['type'] = {'Ground'}
    Roach['bonuses'] = {}
    Roach['bonus_dps'] = 0
    Roach['healer'] = False
    # Resource stats
    Roach['mineral'] = 75
    Roach['gas'] = 25
    Roach['time'] = 19
    Roach['supply'] = 2
    Zerg_Units['Roach'] = Roach

    Ravager = {}
    # Combat stats
    Ravager['hp'] = 120
    Ravager['dps'] = 14.04
    Ravager['ranged'] = True
    Ravager['armor'] = 1
    Ravager['attributes'] = {'Biological', 'Ground'}
    Ravager['targetable'] = {'Ground'}
    Ravager['type'] = {'Ground'}
    Ravager['bonuses'] = {}
    Ravager['bonus_dps'] = 0
    Ravager['healer'] = False
    # Resource stats
    Ravager['mineral'] = 25+75
    Ravager['gas'] = 25+75
    Ravager['time'] = 19+9
    Ravager['supply'] = 2+1
    Zerg_Units['Ravager'] = Ravager

    Hydralisk = {}
    # Combat stats
    Hydralisk['hp'] = 90
    Hydralisk['dps'] = 20.4
    Hydralisk['ranged'] = True
    Hydralisk['armor'] = 0
    Hydralisk['attributes'] = {'Light', 'Biological', 'Ground'}
    Hydralisk['targetable'] = {'Ground', 'Air'}
    Hydralisk['type'] = {'Ground'}
    Hydralisk['bonuses'] = {}
    Hydralisk['bonus_dps'] = 0
    Hydralisk['healer'] = False
    # Resource stats
    Hydralisk['mineral'] = 100
    Hydralisk['gas'] = 50
    Hydralisk['time'] = 24
    Hydralisk['supply'] = 2
    Zerg_Units['Hydralisk'] = Hydralisk

    Lurker = {}
    # Combat stats
    Lurker['hp'] = 200
    Lurker['dps'] = 14
    Lurker['ranged'] = True
    Lurker['armor'] = 1
    Lurker['attributes'] = {'Armored', 'Biological', 'Ground'}
    Lurker['targetable'] = {'Ground'}
    Lurker['type'] = {'Ground'}
    Lurker['bonuses'] = {'Armored'}
    Lurker['bonus_dps'] = 7
    Lurker['healer'] = False
    # Resource stats
    Lurker['mineral'] = 100+50
    Lurker['gas'] = 50+100
    Lurker['time'] = 24+18
    Lurker['supply'] = 2+1
    Zerg_Units['Lurker'] = Lurker

    SwarmHost = {}
    # Combat stats
    SwarmHost['hp'] = 160
    SwarmHost['dps'] = 0
    SwarmHost['ranged'] = False
    SwarmHost['armor'] = 1
    SwarmHost['attributes'] = {'Armored', 'Biological', 'Ground'}
    SwarmHost['targetable'] = {}
    SwarmHost['type'] = {'Ground'}
    SwarmHost['bonuses'] = {}
    SwarmHost['bonus_dps'] = 0
    SwarmHost['healer'] = False
    # Resource stats
    SwarmHost['mineral'] = 100
    SwarmHost['gas'] = 75
    SwarmHost['time'] = 29
    SwarmHost['supply'] = 3
    Zerg_Units['SwarmHost'] = SwarmHost

    Locust = {}
    # Combat stats
    Locust['hp'] = 50
    Locust['dps'] = 23.25
    Locust['ranged'] = True
    Locust['armor'] = 0
    Locust['attributes'] = {'Light', 'Biological', 'Ground'}
    Locust['targetable'] = {'Ground'}
    Locust['type'] = {'Ground'}
    Locust['bonuses'] = {}
    Locust['bonus_dps'] = 0
    Locust['healer'] = False
    # Resource stats
    Locust['mineral'] = 0
    Locust['gas'] = 0
    Locust['time'] = 3.6
    Locust['supply'] = 0
    Zerg_Units['Locust'] = Locust

    Ultralisk = {}
    # Combat stats
    Ultralisk['hp'] = 500
    Ultralisk['dps'] = 57.38
    Ultralisk['ranged'] = False
    Ultralisk['armor'] = 2
    Ultralisk['attributes'] = {'Armored', 'Massive', 'Biological', 'Ground'}
    Ultralisk['targetable'] = {'Ground'}
    Ultralisk['type'] = {'Ground'}
    Ultralisk['bonuses'] = {}
    Ultralisk['bonus_dps'] = 0
    Ultralisk['healer'] = False
    # Resource stats
    Ultralisk['mineral'] = 300
    Ultralisk['gas'] = 200
    Ultralisk['time'] = 39
    Ultralisk['supply'] = 6
    Zerg_Units['Ultralisk'] = Ultralisk

    Mutalisk = {}
    # Combat stats
    Mutalisk['hp'] = 120
    Mutalisk['dps'] = 8.26+2.75+0.92
    Mutalisk['ranged'] = True
    Mutalisk['armor'] = 0
    Mutalisk['attributes'] = {'Light', 'Biological', 'Air'}
    Mutalisk['targetable'] = {'Ground', 'Air'}
    Mutalisk['type'] = {'Air'}
    Mutalisk['bonuses'] = {}
    Mutalisk['bonus_dps'] = 0
    Mutalisk['healer'] = False
    # Resource stats
    Mutalisk['mineral'] = 100
    Mutalisk['gas'] = 100
    Mutalisk['time'] = 24
    Mutalisk['supply'] = 2
    Zerg_Units['Mutalisk'] = Mutalisk

    Corruptor = {}
    # Combat stats
    Corruptor['hp'] = 200
    Corruptor['dps'] = 10.29
    Corruptor['ranged'] = True
    Corruptor['armor'] = 2
    Corruptor['attributes'] = {'Armored', 'Biological', 'Air'}
    Corruptor['targetable'] = { 'Air'}
    Corruptor['type'] = {'Air'}
    Corruptor['bonuses'] = {'Massive'}
    Corruptor['bonus_dps'] = 4.4
    Corruptor['healer'] = False
    # Resource stats
    Corruptor['mineral'] = 150
    Corruptor['gas'] = 100
    Corruptor['time'] = 29
    Corruptor['supply'] = 2
    Zerg_Units['Corruptor'] = Corruptor

    BroodLord = {}
    # Combat stats
    BroodLord['hp'] = 225
    BroodLord['dps'] = 22.4
    BroodLord['ranged'] = True
    BroodLord['armor'] = 1
    BroodLord['attributes'] = {'Armored', 'Massive', 'Biological', 'Air'}
    BroodLord['targetable'] = { 'Ground'}
    BroodLord['type'] = {'Air'}
    BroodLord['bonuses'] = {}
    BroodLord['bonus_dps'] = 0
    BroodLord['healer'] = False
    # Resource stats
    BroodLord['mineral'] = 150+150
    BroodLord['gas'] = 100+150
    BroodLord['time'] = 29+24
    BroodLord['supply'] = 2+2
    Zerg_Units['BroodLord'] = BroodLord

    Broodling = {}
    # Combat stats
    Broodling['hp'] = 30
    Broodling['dps'] = 8.7
    Broodling['ranged'] = False
    Broodling['armor'] = 0
    Broodling['attributes'] = {'Light', 'Biological', 'Ground'}
    Broodling['targetable'] = { 'Ground'}
    Broodling['type'] = {'Ground'}
    Broodling['bonuses'] = {}
    Broodling['bonus_dps'] = 0
    Broodling['healer'] = False
    # Resource stats
    Broodling['mineral'] = 0
    Broodling['gas'] = 0
    Broodling['time'] = 0
    Broodling['supply'] = 0
    Zerg_Units['Broodling'] = Broodling

    return Zerg_Units