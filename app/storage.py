from app.models import Pet
from datetime import datetime
from uuid import uuid4

pets = {
    str(uuid4()): Pet(
        id=str(uuid4()),
        name="Buddy",
        type="Dog",
        age=3,
        created_at=datetime.utcnow()
    ),
    str(uuid4()): Pet(
        id=str(uuid4()),
        name="Mittens",
        type="Cat",
        age=2,
        created_at=datetime.utcnow()
    )
}
