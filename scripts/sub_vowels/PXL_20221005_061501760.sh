output_parent_dir="datasets/split/sub_vowels/PXL_20221005_061501760"
input_file="datasets/raw/PXL_20221005_061501760.mp4"
clips=(
  '៊-00:00:02-00:00:04'
  '៉-00:00:09-00:00:10'
  '៌-00:00:17-00:00:19'
  '់-00:00:22-00:00:23'
  '័-00:00:29-00:00:30'
  'ៗ-00:00:51-00:00:52'
  '៚-00:00:57-00:00:58'
  '៖-00:00:50-00:00:53'
  '៘-00:01:08-00:01:10'
  '៏-00:01:15-00:01:17'
  '!-00:01:26-00:01:28'
  '?-00:01:46-00:01:47'
  '។-00:01:51-00:01:52'
  "'+'-00:01:57-00:01:59"
  # '៍-00:00:49-00:00:52'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
