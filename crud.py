from sqlalchemy.orm import Session
from . import models, schemas

def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def get_comments_by_task(db: Session, task_id: int):
    return db.query(models.Comment).filter(models.Comment.task_id == task_id).all()

def create_comment(db: Session, comment: schemas.CommentCreate, task_id: int):
    db_comment = models.Comment(content=comment.content, task_id=task_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment(db: Session, comment_id: int, comment: schemas.CommentUpdate):
    db_comment = get_comment(db, comment_id)
    if db_comment:
        db_comment.content = comment.content
        db.commit()
        db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = get_comment(db, comment_id)
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment
