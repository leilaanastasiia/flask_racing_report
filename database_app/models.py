import peewee
from peewee import Model, CharField
from settings import PATH_ABB, PATH_START, PATH_END, PATH_DB

db = peewee.SqliteDatabase(PATH_DB)


class BaseModel(Model):
    class Meta:
        database = db


class Report(BaseModel):  # database table name
    abbreviation = CharField(unique=True)
    name = CharField()
    car = CharField()
    start = CharField(null=True)
    end = CharField(null=True)


def parse_abb() -> None:
    """
    Parse abbreviation.txt & add to the database 3 fields:
    abbreviation, name, car
    """
    with open(PATH_ABB, encoding='utf-8') as abb_file:
        abb_list = [line[:-1].split('_') for line in abb_file]
        for item in abb_list:
            try:
                Report.create(abbreviation=item[0],  # but there are a faster way with insert_many()
                              name=item[1],
                              car=item[2])
            # TODO Is it ok to catch an err like this?
            except peewee.IntegrityError:  # if data has already been added
                pass


def parse_start() -> None:
    """
    Parse abbreviation.txt & add to the database start field:
    """
    with open(PATH_START) as start_file:
        for line in start_file:
            if line != '\n':
                query = Report.update(start=line[3:-1]).where(Report.abbreviation == line[:3])
                query.execute()


def parse_end() -> None:
    """
    Parse abbreviation.txt & add to the database end field:
    """
    with open(PATH_END) as end_file:
        for line in end_file:
            if line != '\n':
                query = Report.update(end=line[3:-1]).where(Report.abbreviation == line[:3])
                query.execute()


def init_db():
    db.connect(reuse_if_open=True)
    db.create_tables([Report], safe=True)

    parse_abb()
    parse_start()
    parse_end()
