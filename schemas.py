from pydantic import BaseModel

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class CommentUpdate(CommentBase):
    pass

class CommentInDBBase(CommentBase):
    id: int
    task_id: int

    class Config:
        orm_mode = True

class Comment(CommentInDBBase):
    pass
