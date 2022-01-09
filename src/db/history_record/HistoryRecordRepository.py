from typing import Iterable

from src.db.history_record.HistoryRecord import HistoryRecord, get_session


def get_all() -> Iterable[HistoryRecord]:
    session = get_session()
    return session.query(HistoryRecord).all()


def save(historyRecord: HistoryRecord) -> None:
    session = get_session()
    session.add(historyRecord)
    session.commit()


def get_top_ten() -> Iterable[HistoryRecord]:
    records = get_all()
    records = sorted(records, key=lambda record: (record.get_points(), record.get_player_name()), reverse=True)
    while len(records) < 10:
        records.append(HistoryRecord(points=0,
                                     player_name=""))
    return records[:10]
