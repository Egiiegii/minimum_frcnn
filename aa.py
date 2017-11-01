testset_path = "data/3_only_slipper_in_sss/shoesSamples/forTest/"

weight_name = "model_frcnn_1"
print("mkdir imgs/"+weight_name)
print(
		"python with_output_dir_test_frcnn.py" + 
		" -p "+ testset_path +
		" --output_config_filename configs/" + weight_name + ".pickle" +
		" --img_output imgs/"+ weight_name
		)