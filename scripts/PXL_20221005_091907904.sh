output_parent_dir="datasets/split"
input_file="datasets/raw/PXL_20221005_091907904.mp4"
clips=(
  'ក-00:00:01-00:00:10'
  'ខ-00:00:10-00:00:25'
  'គ-00:00:25-00:00:45'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
