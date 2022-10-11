output_parent_dir="datasets/split/sub_vowels/PXL_20221005_060957166"
input_file="datasets/raw/PXL_20221005_060957166.mp4"
clips=(
  '៊-00:00:06-00:00:08'
  '៉-00:00:11-00:00:14'
  '៌-00:00:17-00:00:19'
  '់-00:00:22-00:00:24'
  '័-00:00:29-00:00:30'
  'ៗ-00:00:36-00:00:38'
  '៚-00:00:41-00:00:43'
  '៖-00:00:47-00:00:50'
  '៘-00:00:54-00:00:56'
  '៏-00:01:06-00:01:09'
  '!-00:01:14-00:01:17'
  '?-00:01:32-00:01:34'
  '។-00:01:39-00:01:41'
  '+-00:01:54-00:01:56'
  # '៍-00:00:49-00:00:52'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
