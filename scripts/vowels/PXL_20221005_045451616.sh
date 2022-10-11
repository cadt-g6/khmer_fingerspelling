output_parent_dir="datasets/split/vowels/PXL_20221005_091907904"
input_file="datasets/raw/PXL_20221005_091907904.mp4"
clips=(
  'ា-00:00:00-00:00:05'
  'ិ-00:00:06-00:00:09'
  'ី-00:00:10-00:00:13'
  'ឹ-00:00:14-00:00:18'
  'ឺ-00:00:19-00:00:22'
  'ុ-00:00:23-00:00:25'
  'ូ-00:00:27-00:00:30'
  'ួ-00:00:31-00:00:34'
  'ើ-00:00:35-00:00:38'
  'ឿ-00:00:39-00:00:42'
  'ៀ-00:00:44-00:00:48'
  'េ-00:00:49-00:00:52'
  'ែ-00:00:53-00:00:56'
  'ៃ-00:00:58-00:01:01'
  'ោ-00:01:02-00:01:06'
  'ៅ-00:01:07-00:01:10'
  'ុំ-00:01:11-00:01:14'
  'ំ-00:01:15-00:01:19'
  'ាំ-00:01:20-00:01:23'
  'ះ-00:01:25-00:01:28'
  'ុះ-00:01:29-00:01:32'
  'េះ-00:01:33-00:01:35'
  'ោះ-00:01:38-00:01:41'
)

./scripts/base/trim_video.sh $output_parent_dir $input_file ${clips[@]}
