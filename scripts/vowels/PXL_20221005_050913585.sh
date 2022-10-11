output_parent_dir="datasets/split/vowels/PXL_20221005_050913585"
input_file="datasets/raw/PXL_20221005_050913585.mp4"
clips=(
  'ា-00:00:07-00:00:08'
  'ិ-00:00:10-00:00:12'
  'ី-00:00:15-00:00:17'
  'ឹ-00:00:19-00:00:21'
  'ឺ-00:00:23-00:00:25'
  'ុ-00:00:28-00:00:29'
  'ូ-00:00:31-00:00:33'
  'ួ-00:00:35-00:00:37'
  'ើ-00:00:40-00:00:41'
  'ឿ-00:00:43-00:00:44'
  'ៀ-00:00:50-00:00:51'
  'េ-00:00:53-00:00:55'
  'ែ-00:00:57-00:00:58'
  'ៃ-00:01:01-00:01:02'
  'ោ-00:01:04-00:01:05'
  'ៅ-00:01:07-00:01:09'
  'ុំ-00:01:12-00:01:13'
  'ំ-00:01:15-00:01:16'
  'ាំ-00:01:19-00:01:21'
  'ះ-00:01:23-00:01:24'
  'ុះ-00:01:27-00:01:28'
  'េះ-00:01:30-00:01:31'
  'ោះ-00:01:41-00:01:42'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
