output_parent_dir="datasets/split/sub_vowels/PXL_20221005_061812917"
input_file="datasets/raw/PXL_20221005_061812917.mp4"
clips=(
  '៊-00:00:02-00:00:03'
  '៉-00:00:07-00:00:08'
  '៌-00:00:11-00:00:12'
  '់-00:00:14-00:00:15'
  '័-00:00:18-00:00:19'
  'ៗ-00:00:22-00:00:23'
  '៚-00:00:26-00:00:27'
  '៖-00:00:35-00:00:36'
  '៘-00:00:40-00:00:41'
  '៏-00:00:46-00:00:47'
  '!-00:00:55-00:00:56'
  '?-00:00:59-00:01:00'
  '។-00:01:07-00:01:09'
  '+-00:01:13-00:01:14'
  # '៍-00:00:49-00:00:52'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
