import normalise as nm
import os

raw_data = 'rawdata'
data_path = 'data'
model_path = 'checkpoints'
height = 100
width = 100
if not os.path.exists(data_path):
    nm.image_normalisation(raw_data, data_path, height, width)
all_classes = os.listdir(data_path)
number_of_classes = len(all_classes)
color_channels = 3
epochs = 10
batch_size = 30
batch_counter = 0
model_save_name = './checkpoints/model'

# batch_size = 30
# epochs = 200
# samples = 4800
