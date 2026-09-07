"""API endpoints for catalogue search."""

from fastapi import APIRouter, HTTPException

from python_app.services.search_service import search_catalogue


router = APIRouter(
    prefix="/api/v1",
    tags=["Catalogue Search"],
)


@router.get("/search")
def search_catalogue_endpoint(
    query: str,
    top_k: int = 10,
) -> dict:
    """Search the library catalogue."""
    try:
        results = search_catalogue(
            query=query,
            top_k=top_k,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error

    return {
        "query": query,
        "count": len(results),
        "results": results,
    }