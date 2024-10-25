from fastapi import APIRouter, HTTPException
from app.models import Blog
from app.config import blog_collection
from bson import ObjectId

blog_router = APIRouter()

@blog_router.post("/", response_model=Blog)
async def create_blog(blog: Blog):
    new_blog = await blog_collection.insert_one(blog.dict())
    created_blog = await blog_collection.find_one({"_id": new_blog.inserted_id})
    if created_blog:
        return created_blog
    raise HTTPException(status_code=400, detail="Blog creation failed")

@blog_router.get("/{id}", response_model=Blog)
async def get_blog(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid Blog ID")
    
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@blog_router.put("/{id}", response_model=Blog)
async def update_blog(id: str, blog: Blog):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid Blog ID")
    
    updated_blog = await blog_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": blog.dict()},
        return_document=True
    )
    if updated_blog:
        return updated_blog
    raise HTTPException(status_code=404, detail="Blog not found")

@blog_router.delete("/{id}")
async def delete_blog(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid Blog ID")

    result = await blog_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")
