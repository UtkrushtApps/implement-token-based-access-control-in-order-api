import os

UPLOAD_FOLDER = 'uploaded_images'

def save_profile_image(user_id: str, file_obj) -> str:
    """Save uploaded image to disk for the user and return path to file."""
    # TODO: Save image data to disk under unique filename for user
    # Return full image path
    pass

def get_profile_image_path(user_id: str) -> str:
    """Return path to user's profile image if exists else None."""
    # TODO: Return file path if it exists, else None
    pass
