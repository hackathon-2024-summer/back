from sqlalchemy import Boolean, Column, ForeignKey, String, text,Date
from sqlalchemy.orm import relationship
from entity.base import Base
import uuid
from entity.user import User


class Content(Base):
    __tablename__ = "contents"  # テーブル名 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める。
    # 新しいレコードが挿入される際に、lambdaで指定する関数の出力をデフォルト値として使う
    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    user_id = Column(String(36), ForeignKey(User.id), nullable=False)
    content_date = Column(Date, server_default=text("(CURRENT_DATE)"), nullable=False)

    
    is_public = Column(Boolean, nullable=False, default=False)
    content = Column(String(256), nullable=False)
    is_accepted = Column(Boolean, nullable=False, default=False)

    # Relationship with User (optional, but useful for ORM queries)
    user = relationship("User", back_populates="contents")
    
    def __repr__(self):
        return f"<Content(id={self.id}, user_id={self.user_id}, content_date={self.content_date}, is_public={self.is_public}, content={self.content}, is_accepted={self.is_accepted})>"

    def __str__(self):
        return f"Content(id={self.id}, user_id={self.user_id}, content_date={self.content_date}, is_public={self.is_public}, content={self.content}, is_accepted={self.is_accepted})"
