from PIL import Image
import numpy as np

def normalize_to_10_levels(image_path, output_path):
    # Load the image and convert to grayscale
    img = Image.open(image_path).convert("L")
    img_array = np.array(img)

    # Step 1: Normalize to 10 discrete levels (0–9)
    levels_0_9 = (img_array / 255.0 * 9).round().astype(np.uint8)

    # Step 2: Scale those 10 levels to range 0–225
    levels_0_225 = (levels_0_9 * (225 // 9)).astype(np.uint8)

    # Convert back to an image and save
    result_img = Image.fromarray(levels_0_225)
    print("Saving image now...")
    result_img.save(output_path)
    print(f"✅ Saved normalized image to {output_path}")

# --- CALL THE FUNCTION ---
normalize_to_10_levels(
    r"C:\Users\VIVOBOOK\Desktop\ddrfh\image1.png",
    r"C:\Users\VIVOBOOK\Desktop\out\processed_image_10_levels_0_225.png"
)