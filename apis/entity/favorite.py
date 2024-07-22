from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from entity.base import Base

from entity.user import User
from entity.content import Content


class Favorite(Base):
    __tablename__ = "favorites"  # テーブル名 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める。
    # 新しいレコードが挿入される際に、lambdaで指定する関数の出力をデフォルト値として使う
    user_id = Column(
        String(36),
        ForeignKey(User.id),
        nullable=False,
        primary_key=True,
    )
    content_id = Column(
        String(36),
        ForeignKey(Content.id),
        nullable=False,
        primary_key=True,
    )

    # Relationship with User (optional, but useful for ORM queries)
    user = relationship("User", back_populates="favorites")
    content = relationship("Content", back_populates="favorites")

    def __repr__(self):
        return f"<Favorite(user_id={self.user_id}, content_id={self.content_id})>"

    def __str__(self):
        return f"Favorite(user_id={self.user_id}, content_id={self.content_id})"
