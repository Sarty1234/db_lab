


from typing import TypeVar, Generic, Type, List, Optional
from sqlalchemy.orm import Session
from domain.general_domain import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseDAO(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, session: Session, id: int) -> Optional[ModelType]:
        return session.get(self.model, id)

    def get_all(self, session: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return session.query(self.model).offset(skip).limit(limit).all()

    def create(self, session: Session, obj_in_data: dict) -> ModelType:
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def update(self, session: Session, db_obj: ModelType, update_data: dict) -> ModelType:
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def delete(self, session: Session, id: int) -> bool:
        db_obj = self.get_by_id(session, id)
        if db_obj:
            session.delete(db_obj)
            session.commit()
            return True
        return False

    