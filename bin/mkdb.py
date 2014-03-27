import sqlite3
import csv
import os

dbconn = sqlite3.connect('pfeebles.sqlite3')
dbconn.text_factory = str
curr = dbconn.cursor()

if not os.path.exists('spells.csv'):
    raise ValueError('download spells.csv first!')

spell_col_names = ( \
        'name', 'school', 'subschool', 'descriptor',
            'spell_level', 'casting_time', 
            'components', 'costly_components',
            'range', 'area', 'effect', 'targets', 'duration', 
            'dismissible', 'shapeable',
            'saving_throw', 'spell_resistence',
            'description',
            'source',
            'full_text',
            'verbal', 'somatic', 'material', 'focus', 'divine_focus',
            'sor', 'wiz', 'cleric', 'druid', 'ranger', 'bard', 'paladin', 'alchemist',
                'summoner', 'witch', 'inquisitor', 'oracle', 'antipaladin', 'magus',
                'adept', 'deity',
            'sla_level',
            'air', 'chaotic', 'cold', 'curse', 'darkness', 'death', 'disease', 'earth',
                'electricity', 'emotion', 'evil', 'fear', 'fire', 'force', 'good',
                'language_dependent', 'lawful', 'light', 'mind_affecting',
                'pain', 'poison', 'shadow', 'sonic', 'water',
            'id',
            'material_costs',
            'bloodline',
            'patron',
            'mythic_text',
            'augmented',
            'mythic'
        )

feat_col_names = ( \
        'id', 'name',
        'type', 'description',
        'prerequisites', 'prerequisite_feats',
        'benefit', 'normal', 'special',
        'source',
        'fulltext',
        'teamwork',
        'critical',
        'grit',
        'style',
        'performance',
        'racial',
        'companion_familiar',
        'race_name',
        'note',
        'goal',
        'completion_benefit',
        'multiples',
        'suggested_traits' )

trait_col_names = ( \
        'name',
        'type',
        'category',
        'prerequisites',
        'pfs_legal',
        'description',
        'source',
        'version' )

def setup_table(colnames, csvname, tablename, translator = {}):
    curr.execute('''
            CREATE TABLE %s
            (%s)
            ''' % (tablename, ', '.join(colnames)))

    data_csv = csv.reader(open(csvname, 'r'))
    data_header = data_csv.next()
    data_rtable = {}
    for n, colname in enumerate(data_header):
        print colname
        if colname.lower() not in translator:
            if colname.lower() in colnames:
                data_rtable[colname.lower()] = n
        else:
            if translator[colname.lower()] in colnames:
                data_rtable[translator[colname.lower()]] = n

    def extract_values(row):
        tr = [ row[data_rtable[colname]] for colname in colnames ]
        print row[data_rtable['name']]
        return tr

    curr.executemany('insert into %s (%s) values (%s)' \
            % ( tablename,
                ','.join(colnames), 
                ', '.join(['?' for n in colnames])),
            ( extract_values(r) for r in data_csv ))

    dbconn.commit()

setup_table(spell_col_names, 'spells.csv', 'spells')
setup_table(feat_col_names, 'feats.csv', 'feats')
setup_table(trait_col_names, 'traits.csv', 'traits',
        translator = {'trait name':'name', 'prerequisite(s)':'prerequisites', \
                'pfs legal':'pfs_legal'})

dbconn.close()

