output_parent_dir="datasets/split/independent_vowels/PXL_20221005_063616958"
input_file="datasets/raw/PXL_20221005_063616958.mp4"
clips=(
  'ឥ-00:00:03-00:00:05'
  'ឦ-00:00:07-00:00:09'
  'ឧ-00:00:14-00:00:17'
  'ឪ-00:00:33-00:00:35'
  'ឫ-00:00:52-00:00:55'
  'ឬ-00:01:12-00:01:14'
  'ឭ-00:01:20-00:01:21'
  'ឮ-00:01:24-00:01:26'
  'ឯ-00:01:32-00:01:35'
  'ឰ-00:01:40-00:01:43'
  'ឱ-00:01:57-00:01:58'
  'ឳ-00:02:00-00:02:02'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}