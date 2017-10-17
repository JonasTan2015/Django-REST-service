from DBAPI import Session

class AlchemyCRUDMixin(object):
    def __create__(self, alchemyModelObject):
        session = Session()
        session.add(alchemyModelObject)
        session.flush()
        session.commit()
        session.close()

    def __update__(self, alchemyModelObject):
        session = Session()
