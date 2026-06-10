import logging
from typing import Any

logger = logging.getLogger(__name__)


def run_analysis_job(payload: dict[str, Any]) -> dict[str, Any]:
    analysis_id = payload["analysis_id"]
    repository_id = payload["repository_id"]
    repository_url = payload["repository_url"]
    branch = payload["branch"]

    logger.info(
        "Analysis job started. analysis_id=%s repository_id=%s repository_url=%s branch=%s",
        analysis_id,
        repository_id,
        repository_url,
        branch,
    )

    return {
        "analysis_id": analysis_id,
        "repository_id": repository_id,
        "status": "QUEUED",
    }
