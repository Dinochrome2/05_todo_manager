from pathlib import Path
from sqlmodel import create_engine, Session, SQLModel

# Build absolute path to the SQLite database so it works
# regardless of the current working directory.
BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "tasks.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables() -> None:
    """Создаёт таблицы в БД, если их нет."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Генерирует сессию для работы с БД."""
    with Session(engine) as session:
        yield session
