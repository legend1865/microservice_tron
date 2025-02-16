from datetime import datetime, timezone

from sqlalchemy import ForeignKey, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class Tron(Base):
    __tablename__ = "tron"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(unique=True)
    bandwidth: Mapped[float | None]
    energy: Mapped[float | None]
    balance: Mapped[float]
