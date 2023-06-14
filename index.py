import cv2
import os
import argparse


def generate_masks(input_dir, output_dir, brightness_threshold):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through the files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load the image
            input_path = os.path.join(input_dir, filename)
            image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

            # Apply brightness thresholding to create the mask
            _, mask = cv2.threshold(
                image, brightness_threshold, 255, cv2.THRESH_BINARY)

            # Save the mask image
            output_filename = os.path.splitext(filename)[0] + ".mask.png"
            output_path = os.path.join(output_dir, output_filename)
            cv2.imwrite(output_path, mask)

            print(f"Generated mask for {filename}")

    print("Mask generation completed.")


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Automatic mask generation")

    # Add arguments
    parser.add_argument(
        "--input", "-i", help="Path to the input directory containing the images")
    parser.add_argument(
        "--output", "-o", help="Path to the output directory to save the generated masks")
    parser.add_argument("--brightness_threshold", type=int, default=100,
                        help="Brightness threshold value for masking (default: 100)")

    # Parse the arguments
    args = parser.parse_args()

    # Generate masks using the provided arguments
    generate_masks(args.input, args.output, args.brightness_threshold)
