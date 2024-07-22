from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from entity.base import Base
import uuid
from entity.user import User


class Setting(Base):
    __tablename__ = "settings"  # テーブル名 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める。

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    user_id = Column(String(36), ForeignKey(User.id), nullable=False)
    view_count = Column(Integer, nullable=False)

    # Relationship with User (optional, but useful for ORM queries)
    user = relationship("User", back_populates="settings")

    def __repr__(self):
        return f"<Setting(id={self.id}, user_id={self.user_id}, view_count={self.view_count})>"

    def __str__(self):
        return f"Setting(id={self.id}, user_id={self.user_id}, view_count={self.view_count})"
