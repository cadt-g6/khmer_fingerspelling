output_parent_dir="datasets/split/independent_vowels/PXL_20221005_064056229"
input_file="datasets/raw/PXL_20221005_064056229.mp4"
clips=(
  'ឥ-00:00:01-00:00:03'
  'ឦ-00:00:06-00:00:08'
  'ឧ-00:00:11-00:00:14'
  'ឪ-00:00:30-00:00:32'
  'ឫ-00:00:54-00:00:56'
  'ឬ-00:01:00-00:01:02'
  'ឭ-00:01:09-00:01:10'
  'ឮ-00:01:13-00:01:15'
  'ឯ-00:01:21-00:01:24'
  'ឰ-00:01:36-00:01:37'
  'ឱ-00:01:50-00:01:51'
  'ឳ-00:01:55-00:01:57'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
