DATABASE = 'bot'
MONGO_LINK = 'mongodb://{0}:{1}@chordsbot-shard-00-00-ud0ik.mongodb.net:27017,chordsbot-shard-00-01-ud0ik.mongodb.net:27017,chordsbot-shard-00-02-ud0ik.mongodb.net:27017/test?ssl=true&replicaSet=ChordsBot-shard-0&authSource=admin'
USERS = 'users'
GUITAR_CHORDS_URL = 'guitar_chords_url'
INST_COLLECTION = {
    'guitar': 'guitar_chords',
    'ukulele': 'ukulele_chords',
    'mandolin': 'mandolin_chords',
    'piano': 'piano_chords',
    'banjo': 'banjo_chords'}
