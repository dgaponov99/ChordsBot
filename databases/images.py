from databases.db import Database
from databases.db_config import INST_COLLECTION
from databases.db_config import GUITAR_CHORDS_URL
from databases.docs import chords_docs

inst = INST_COLLECTION

database_gui = Database(GUITAR_CHORDS_URL)
databases_inst = {'guitar': Database(inst['guitar']),
                  'ukulele': Database(inst['ukulele']),
                  'banjo': Database(inst['banjo']),
                  'mandolin': Database(inst['mandolin']),
                  'piano': Database(inst['piano'])}


def get_guitar_url(chord):
    doc = database_gui.get_one_doc(chord)
    if doc is None:
        return None
    return doc['urls']


def get_files_id(instrument, chord):
    database = databases_inst[instrument]
    doc = database.get_one_doc(chord)
    if doc is None:
        return None
    return doc['files_id']


def add_chord(instrument, chord, files_id):
    doc = chords_docs.chords(chord, files_id)
    database = databases_inst[instrument]
    database.add_doc(doc)
