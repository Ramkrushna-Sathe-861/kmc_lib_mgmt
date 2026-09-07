"""API endpoints for the library conversational assistant."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from python_app.services.assistant_service import process_question

router = APIRouter(
    prefix="/api/v1/assistant",
    tags=["Assistant"],
)


class AssistantRequest(BaseModel):
    """Request model for the library assistant."""

    question: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Natural-language question asked by the user.",
    )


class AssistantResponse(BaseModel):
    """Response model for the library assistant."""

    question: str
    answer: str


@router.post("", response_model=AssistantResponse)
def ask_assistant(request: AssistantRequest) -> AssistantResponse:
    """Process a user's library question.

    Args:
        request: User's assistant request.

    Returns:
        Assistant response containing the question and answer.

    Raises:
        HTTPException: If the question cannot be processed.
    """
    try:
        # Service integration will be added in the next step.
        assistant_result = process_question(request.question)

        

        return AssistantResponse(
            question=assistant_result["question"],
            answer=assistant_result["answer"],
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Unable to process the assistant request.",
        ) from error