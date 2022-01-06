from db.DatabaseSettings import session
import model.Color as Color
import exception.WrongColorNameException


def get_by_name(name: str):
    if name not in Color.COLOR_NAMES:
        raise exception.WrongColorNameException
    return session.query(Color).filter(Color.get_name() == name).first()

