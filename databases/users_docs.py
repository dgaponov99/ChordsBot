def new_user(chat_id, first_name, mode='guitar'):
    return {'_id': chat_id,
            'first_name': first_name,
            'mode': mode}


def user(chat_id):
    return {'_id': chat_id}


def user_mode(mode):
    return {'mode': mode}
