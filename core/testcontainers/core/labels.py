from uuid import uuid4
from typing import Optional

from .images import REAPER_IMAGE


SESSION_ID: str = str(uuid4())
LABEL_SESSION_ID = "org.testcontainers.session-id"


def create_labels(image: str, labels: Optional[dict]) -> dict:
    if labels is None:
        labels = {
            "org.testcontainers.lang": "python",
        }

    if image == REAPER_IMAGE:
        return labels

    labels[LABEL_SESSION_ID] = SESSION_ID
    return labels