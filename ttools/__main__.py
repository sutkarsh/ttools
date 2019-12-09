"""Executable entrypoints."""
import argparse
import imageio


def im2vid():
    parser = argparse.ArgumentParser(description="converts a series of image frames to a video.")
    parser.add_argument("images", nargs="+")
    parser.add_argument("output")
    args = parser.parse_args()

    images = []
    print("loading", len(args.images), "images")
    for filename in sorted(args.images):
        images.append(imageio.imread(filename))
        print(".")
    print("saving video")
    imageio.mimsave(args.output, images)