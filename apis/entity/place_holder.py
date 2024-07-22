from sqlalchemy import Column, String
from entity.base import Base
import uuid


class PlaceHolder(Base):
    __tablename__ = "place_holders"  # テーブル名 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める。
    # 新しいレコードが挿入される際に、lambdaで指定する関数の出力をデフォルト値として使う
    id = Column(
        String(36),
        nullable=False,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    place_holder = Column(String(256), unique=True, nullable=False)

    # printで表示するための関数
    def __repr__(self):
        return f"<PlaceHolder(id={self.id}, place_holder={self.place_holder})>"

    def __str__(self):
        return f"PlaceHolder(id={self.id}, place_holder={self.place_holder})"

