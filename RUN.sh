#!/usr/bin/bash

python3 test.py --dataset_root ../coarse_v1/ --trained_model "$1.pth" --visual_threshold 0.50 --cuda True --exp_name "test_$1" --test_data validation_data --suffix "_512" --model_type 512 --cfg hboxes512 --padding 0 2 --kernel 1 5 --batch_size 8

python3 gtdb/stitch_patches_pdf.py --data_file ../coarse_v1/coarse_data_pdf --output_dir "eval/stitched_$1" --math_dir "eval/test_$1/" --stitching_algo equal --algo_threshold 50 --num_workers 8 --postprocess True --home_images ../coarse_v1/images/

cd ../../

python3 TFD-ICDAR2019v2/Evaluation/IOULib/IOUevaluater.py --ground_truth ScanSSD-Project/coarse_v1/gt/ --detections "ScanSSD-Project/ssd/eval/stitched_$1" > 217000.txt

python3 TFD-ICDAR2019v2/VisualizationTools/visualize_annotations.py --img_dir ScanSSD-Project/coarse_v1/images/ --out_dir visual217000 --math_dir "ScanSSD-Project/ssd/eval/stitched_$1"
