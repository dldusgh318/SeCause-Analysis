from fastapi import APIRouter, BackgroundTasks, status

from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.post( # 공통 응답 처리 코드 필요?
    "/internal/analyze",
    response_model=AnalyzeResponse,
    status_code=status.HTTP_202_ACCEPTED, 
)
async def analyze(request: AnalyzeRequest, _background_tasks: BackgroundTasks):
    """
    분석 요청을 수신하고 백그라운드 태스크로 등록.
    Spring Boot는 이 응답을 받으면 즉시 클라이언트에게 analysis_id 반환
    """
    # 추후: background_tasks.add_task(run_pipeline, request)

    return AnalyzeResponse(
        accepted=True,
        analysis_id=request.analysis_id,
        message="Analysis queued for processing",
    )
