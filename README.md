# Task Overview
You are tasked with restoring correct and immediate cache invalidation for user profile images in a FastAPI backend used by a SaaS platform. Users expect that uploading a new profile image replaces their old one instantly, but currently, the system sometimes returns outdated or default images after a successful upload due to improper cache handling.

# Guidance
- Consider how and when in-memory cache invalidation or updates should occur for profile images.
- Review the code paths involved in both uploading an image and fetching an image.
- Ensure that all future GET requests show the latest uploaded profile image without delay or inconsistency.
- Focus on consistency of cache and image storage state after uploads.

# Objectives
- Update the cache invalidation and updating logic for profile images to guarantee immediate cache consistency after upload.
- Ensure the GET endpoint never returns a stale or default image after a successful upload.
- Prevent race conditions and ensure correct cache usage in both upload and fetch flows.

# How to Verify
- Upload a new profile image for a user via the upload endpoint and confirm that all GET requests for that user immediately return the new image.
- Check that fetching profile images never serves outdated or default images after a successful upload.
- Validate that the image cache state remains correct and up-to-date after uploads.