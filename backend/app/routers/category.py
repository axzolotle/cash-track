from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.crud.category import (
    create_category,
    get_categories,
    delete_category,
    update_category
)

router = APIRouter(prefix="/categories", tags=["categories"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoryResponse, status_code=201)
def category_create(
    data: CategoryCreate,
    db: Session = Depends(SessionLocal)
):
    return create_category(db, data)

@router.get("/", response_model=list[CategoryResponse])
def categories_list(
    db: Session = Depends(SessionLocal)
):
    return get_categories(db)

@router.put("/{category_id}", response_model=CategoryResponse)
def category_update(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(SessionLocal)
):
    updated = update_category(db, category_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@router.delete("/{category_id}", response_model=CategoryResponse)
def category_delete(
    category_id: int,
    db: Session = Depends(SessionLocal)
):
    deleted = delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted

