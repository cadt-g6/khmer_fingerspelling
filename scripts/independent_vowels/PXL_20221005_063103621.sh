output_parent_dir="datasets/split/independent_vowels/PXL_20221005_063103621"
input_file="datasets/raw/PXL_20221005_063103621.mp4"
clips=(
  'ឥ-00:00:06-00:00:07'
  'ឦ-00:00:12-00:00:13'
  'ឧ-00:00:18-00:00:21'
  'ឪ-00:00:32-00:00:34'
  'ឫ-00:00:38-00:00:41'
  'ឬ-00:00:44-00:00:47'
  'ឭ-00:00:55-00:00:56'
  'ឮ-00:01:02-00:01:05'
  'ឯ-00:01:12-00:01:17'
  'ឰ-00:01:26-00:01:27'
  'ឱ-00:01:35-00:01:37'
  'ឳ-00:01:44-00:01:47'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
