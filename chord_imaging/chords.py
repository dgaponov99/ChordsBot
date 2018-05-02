from databases import images
from chord_imaging import chord_validator
from chord_imaging.parsers import multi_parser


def get_chord_files_id(instrument, chord):
    return images.get_files_id(instrument, chord)


def get_chord_urls(instrument, chord):
    if instrument == 'guitar':
        urls_list = images.get_guitar_url(chord)
        if urls_list is not None:
            return urls_list

    chord = chord_validator.validation_chord(chord)
    if chord is None:
        return None

    url_of_page = multi_parser.create_url_of_chord(instrument, chord)
    urls_list = multi_parser.get_images(url_of_page)
    return urls_list


def add_chord(instrument, chord):
    images.add_chord(instrument, chord)
