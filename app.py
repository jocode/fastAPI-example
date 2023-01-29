from fastapi import FastAPI, HTTPException
from models.post import Post
from uuid import uuid4 as uuid
from typing import List

app = FastAPI()

posts = [
    {
        "id": "1",
        "title": "First post",
        "content": "This is my first post",
        "author": "John Doe",
    },
]

@app.get("/")
def read_root():
    return {"welcome": "Welcome to the FastAPI"}


@app.get("/posts", response_model=List[Post])
def get_posts():
    return posts

@app.post("/posts", response_model=Post)
def create_post(post: Post):
    post.id = str(uuid())
    # print(post.dict())
    posts.append(post.dict())
    return posts[-1]

@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = updatedPost.title
            posts[index]["content"] = updatedPost.content
            posts[index]["author"] = updatedPost.author
            return posts[index]
    
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post deleted"}
    
    raise HTTPException(status_code=404, detail="Post not found")
