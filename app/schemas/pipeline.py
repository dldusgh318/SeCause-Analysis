from typing import Any, Optional

from pydantic import Field

from app.schemas.base import AnalysisRequestPayload
from app.schemas.finding import Finding


class AnalysisJobContext(AnalysisRequestPayload):
    repo_path: Optional[str] = None
    raw_findings: list[dict[str, Any]] = Field(default_factory=list)
    normalized_findings: list[Finding] = Field(default_factory=list)
    enriched_findings: list[Finding] = Field(default_factory=list)

    @classmethod
    def from_job_payload(cls, payload: dict[str, Any]) -> "AnalysisJobContext":
        return cls.model_validate(payload)
