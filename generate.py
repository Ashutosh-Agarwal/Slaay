import Augmentor
import os


def generation(source_folder, dest_folder):
    dest_folder = os.path.dirname(os.path.realpath(__file__)) + '/' + dest_folder
    print(dest_folder)

    # Get folder with images
    p = Augmentor.Pipeline(source_folder, output_directory=dest_folder, save_format='jpg')

    # Apply some operations on it with specific probabilities
    # -> Rotation
    p.rotate(probability=0.1, max_left_rotation=10, max_right_rotation=10)
    p.rotate90(probability=0.5)
    p.rotate180(probability=0.5)
    p.rotate270(probability=0.5)

    # -> Skewing
    p.skew_tilt(probability=0.5, magnitude=0.7)

    # -> Distortion
    p.random_distortion(probability=0.1, grid_height=16, grid_width=16, magnitude=6)

    # Generate a specific amount of samples
    p.sample(50)


if __name__ == '__main__':
    folder = 'images/product'
    for files in os.listdir(folder):
        print(files)
        source = folder+'/'+files
        dest = 'rawdata/' + files
        print(source)
        generation(source, dest)
