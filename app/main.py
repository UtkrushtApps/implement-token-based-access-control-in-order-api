from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.storage import save_profile_image, get_profile_image_path
from app.cache import image_cache, invalidate_cache_for_user
import os

app = FastAPI()

UPLOAD_FOLDER = 'uploaded_images'
DEFAULT_IMAGE_PATH = 'default_avatar.png'

@app.post('/upload-profile-image')
def upload_profile_image(user_id: str, image: UploadFile = File(...)):
    # TODO: Save the uploaded image to disk and update the image cache to ensure the latest image is used for all future requests
    # You should call save_profile_image and then ensure cache is updated appropriately
    # HINT: You may need to use invalidate_cache_for_user or update image_cache accordingly
    return {"message": "TODO: implement profile image upload and cache update"}

@app.get('/images/{user_id}')
def get_profile_image(user_id: str):
    # TODO: Fetch the image from cache if present, else from storage; return the path to the image
    # If user has no profile image, serve the default avatar image
    return FileResponse(DEFAULT_IMAGE_PATH)
