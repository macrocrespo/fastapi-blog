import uuid
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageOps

PROFILE_PICS_DIR = Path("media/profile_pics")

# Processes an uploaded profile image: fixes orientation, crops/resizes it to
# a 300x300 JPEG, saves it with a random name and returns that filename.
def process_profile_image(content: bytes) -> str:
    # Open the image from the in-memory bytes; "with" closes it when done
    with Image.open(BytesIO(content)) as original:
        # Fix rotation based on EXIF metadata (e.g. sideways phone photos)
        img = ImageOps.exif_transpose(original)

        # Crop and resize to a 300x300 square without distorting the image
        img = ImageOps.fit(img, (300, 300), method=Image.Resampling.LANCZOS)

        # JPEG doesn't support transparency or palettes: convert to RGB
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")

        # Random unique name to avoid collisions and untrusted user filenames
        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = PROFILE_PICS_DIR / filename

        # Create the destination folder if it doesn't exist
        PROFILE_PICS_DIR.mkdir(parents=True, exist_ok=True)

        # Save as JPEG with good quality and optimized file size
        img.save(filepath, "JPEG", quality=85, optimize=True)

    # Return only the filename (to be stored in the database)
    return filename

# Deletes a profile image file from disk given its filename.
# Does nothing if no filename is given or the file doesn't exist.
def delete_profile_image(filename: str | None) -> None:
    # Nothing to delete (e.g. user has no profile picture)
    if filename is None:
        return

    # Build the full path to the image inside the profile pics folder
    filepath = PROFILE_PICS_DIR / filename
    # Only delete if the file actually exists, to avoid errors
    if filepath.exists():
        filepath.unlink()