"""Schemas for catalogue search."""

from pydantic import BaseModel, Field

from python_app.core.constants import DEFAULT_TOP_K, MAX_TOP_K


class Book(BaseModel):
    """Represent a library catalogue book."""

    id: int
    title: str
    author: str
    subject: str
    description: str
    isbn: str


class SearchRequest(BaseModel):
    """Represent a catalogue search request."""

    query: str = Field(
        ...,
        min_length=1,
        description="Natural-language catalogue search query.",
    )
    top_k: int = Field(
        default=DEFAULT_TOP_K,
        ge=1,
        le=MAX_TOP_K,
        description="Maximum number of results.",
    )


class SearchResult(BaseModel):
    """Represent a ranked catalogue search result."""

    book: Book
    score: float