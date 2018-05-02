from res.riffspot.chords_general import chords_general
from res.riffspot.chords_type import chords_type


def validation_chord(chord):
    general, length = validation_general_part(chord)
    if general is None:
        return None
    if len(chord) == length:
        if general[-1] == '-':
            return general + 'major'
        return general + '-major'
    type_of_chord = validation_type(chord[length:])
    if type_of_chord is None:
        return None
    if general[-1] == type_of_chord[0] == '-':
        return general + type_of_chord[1:]
    return general + type_of_chord


def validation_general_part(chord):
    if chord == '':
        return None, None
    result = chords_general.get(chord[:2])
    length = 2
    if result is None:
        result = chords_general.get(chord[0])
        length = 1
    return result, length


def validation_type(type_part_of_chord):
    return chords_type.get(type_part_of_chord)

