# The Skin Disease Classification Network

### TRAINING

To fine-tune the Inception model:
```
python retrain.py --image_dir <trainfolder>
```

The complete set of parameters that can be passed are as follows:
```
python {$your-working_directory}/retrain.py
--bottleneck_dir=/{$your-working_directory}/bottlenecks         
--how_many_training_steps <steps>
--model_dir=/{$your-working_directory}/inception
--output_graph=/{$your-working_directory}/retrained_graph.pb
--output_labels=/{$your-working_directory}/retrained_labels.txt
--image_dir /{$your-working_directory}/${your_training_data_path}
```

To test the model:
```
python test.py test_image
```
