from PIL import Image

def shorten_gif(input_path, output_path):
    # 1. Open the original GIF
    img = Image.open(input_path)
    
    # 2. Extract all frames
    frames = []
    try:
        while True:
            frames.append(img.copy())
            img.seek(img.tell() + 1)
    except EOFError:
        pass # Reached the end of the GIF

    # 3. Drop every 10th frame (keeps 90% of the frames)
    shortened_frames = [frame for i, frame in enumerate(frames) if (i + 1) % 10 != 0]

    # 4. Save the new, shorter GIF
    original_duration = img.info.get("duration", 100) # Fallback to 100ms if not found
    
    shortened_frames[0].save(
        output_path,
        save_all=True,
        append_images=shortened_frames[1:],
        duration=original_duration,
        loop=img.info.get("loop", 0) # Keep the original loop settings
    )
    
    print(f"Done! Original frames: {len(frames)} | New frames: {len(shortened_frames)}")

from PIL import Image, ImageSequence

# 1. Open the image
img = Image.open("pipeTrack.gif")

# 2. Extract frames cleanly, dropping every 10th frame
frames = [frame.copy() for i, frame in enumerate(ImageSequence.Iterator(img)) if (i + 1) % 2 != 0]

# 3. Save with optimization turned ON
frames[0].save(
    "output.gif",
    save_all=True,
    append_images=frames[1:],
    duration=img.info.get("duration", 100),
    loop=img.info.get("loop", 0),
    optimize=True # <--- This is the magic word that keeps the file size small
)

print("Done! Shorter and compressed.")

# Run the function
# shorten_gif("pipeTrack.gif", "output.gif")