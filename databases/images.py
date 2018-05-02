from databases.db import Database
from databases.db_config import INST_COLLECTION
from databases.db_config import GUITAR_CHORDS_URL
from databases.docs import chords_docs

inst = INST_COLLECTION


def get_guitar_url(chord):
    database = Database(GUITAR_CHORDS_URL)
    doc = database.get_one_doc(chord)
    if doc is None:
        return None
    return doc['urls']


def get_files_id(instrument, chord):
    database = Database(inst[instrument])
    doc = database.get_one_doc(chord)
    if doc is None:
        return None
    return doc['files_id']


def add_chord(instrument, chord, files_id):
    doc = chords_docs.chords(chord, files_id)
    database = Database(inst[instrument])
    database.add_doc(doc)
