from fastapi import HTTPException
class BaseRepository:
    def __init__(self, model):
        self.model = model

    def _query(self, session, *_, **kwargs):
        filters = [getattr(self.model, k) == v for k, v in kwargs.items()]
        return session.query(self.model).filter(*filters)

    def get(self, session, *_, **kwargs):
        return self._query(session, **kwargs).one_or_none()

    def get_many(self, session, *_, **kwargs):
        return self._query(session, **kwargs).all()

    def create(self, session, obj_in):
        db_obj = self.model(**obj_in.dict())
        return self.create_obj(session, db_obj)
    
    def create_obj(self, session, db_obj):
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    
    def update(self, session, id, obj_in):
        db_obj = self.get(session, id=id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Object not found")
        for k, v in obj_in.items():
            setattr(db_obj, k, v)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    
    def delete(self, session, id):
        obj = self.get(session, id=id)
        return self.delete_obj(session, obj)
    
    def delete_obj(self, session, obj):
        session.delete(obj)
        return None