output_parent_dir="$1"
input_file="$2"
clips=("$@")

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

function write_to_csv() {
  # remove extra args
  clips=("${clips[@]:1}")
  clips=("${clips[@]:1}")

  IFS=/
  set $output_parent_dir
  type="$3"
  file_name="$4.mp4"
  destination="datasets/csv/$type.csv"

  if [ ! -f "$destination" ]; then
    echo "\"start_at\", \"end_at\", \"name\", \"type\", \"file_name\"" >$destination
  fi

  for clip in ${clips[@]}; do
    echo $clip

    IFS=-
    set $clip

    name="$1"
    start_time="$2"
    end_time="$3"

    echo "\"$start_time\", \"$end_time\", \"$name\", \"$type\", \"$file_name\"" >>$destination
  done
}

mkdir -p $output_parent_dir

write_to_csv $@
# trim $@
