output_parent_dir="$1"
input_file="$2"
clips=("$@")

mkdir -p $output_parent_dir

function execute() {
  start_time="$1"  # 00:01:00
  end_time="$2"    # 00:02:00
  output_file="$3" # ក.mp4

  ffmpeg -ss $start_time -to $end_time -i $input_file -c copy $output_file
}

function trim() {
  for clip in ${clips[@]}; do
    IFS=-
    set $clip

    output_file="$output_parent_dir/$1.mp4"
    start_time="$2"
    end_time="$3"

    execute $start_time $end_time $output_file
  done
}

trim $@
