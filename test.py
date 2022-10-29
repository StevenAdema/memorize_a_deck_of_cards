from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table

CONN_STR = 'mysql://admin:1234@localhost:3306/deck_mem'
engine = create_engine(CONN_STR, echo=True)
metadata = MetaData()
card_system = Table('card_system', metadata, autoload=True,
                           autoload_with=engine)
cols = card_system.c


with engine.connect() as conn:

    query = (
        select([cols.CardId, cols.CardRank, cols.CardSuit, cols.CardPerson, cols.CardAction, cols.CardObject])
    )
    for row in conn.execute(query):
        print(row)
