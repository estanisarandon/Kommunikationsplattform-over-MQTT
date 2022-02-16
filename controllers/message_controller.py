from flask_login import current_user
from controllers.user_controller import get_user_by_id


def create_message(body, key_encrypted, receiver_id):
    from models import Message
    user = current_user
    message = Message(body=body, key_encrypted=key_encrypted, sender_id=user.id)
    receiver_id = int(receiver_id)
    receiver = get_user_by_id(receiver_id)
    message.receivers.append(receiver)
    from app import db
    db.session.add(message)
    db.session.commit()


def get_user_messages():
    return current_user.recv_messages


def get_body_and_key(message_id):
    from models import Message
    from app import db
    msg_body = db.session.query(Message).filter(Message.id == message_id).first()
    body_and_key = [msg_body.body, msg_body.key_encrypted]
    msg_body.read = 1
    db.session.commit()
    return body_and_key


def get_unread_msg_count():
    user = current_user
    msg_count = 0

    for msg in user.recv_messages:
        if not msg.read:
            msg_count += 1

    return msg_count
