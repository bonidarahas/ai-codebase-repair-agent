from fastapi import FastAPI, HTTPException, status

from app.schemas.repository import (
    RepositoryScanRequest,
    RepositoryScanResponse,
)
from app.services.repository_scanner import RepositoryScanner


app = FastAPI(
    title="AI Codebase Repair & Migration Agent",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.post(
    "/repositories/scan",
    response_model=RepositoryScanResponse,
)
def scan_repository(
    request: RepositoryScanRequest,
) -> RepositoryScanResponse:
    try:
        result = RepositoryScanner(request.path).scan()
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except NotADirectoryError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return RepositoryScanResponse(**result)

