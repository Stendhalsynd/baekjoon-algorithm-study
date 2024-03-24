#!/bin/bash
 
# 형식 : ./create.sh {이름} {확장자} -> 확장자를 전달하지 않으면 py 파일을 생성합니다.
# 위의 명령어를 실행하면 현재 주차에 해당하는 자신이 생성해야 할 파일과 폴더들을 생성합니다.

# 스크립트 파일이 위치한 디렉토리 경로
script_dir=$(dirname "$(readlink -f "$0")")

# 프로젝트의 루트 디렉토리 경로
root_dir=$(dirname "$script_dir")

# 현재 날짜의 주차 정보 가져오기
current_week=$((10#$(date +%U)))
study_week=$((current_week + 11))
week_folder="$root_dir/week$study_week"
mkdir -p "$week_folder"

file="$root_dir/scripts/problems.txt"
executor_name="$1"
expansion="$2"  # 두 번째 인자로 받은 확장자

# 파일을 한 줄씩 읽어 배열에 담기
IFS=$'\n' read -d '' -r -a lines < "$file"

# 배열 순회하여 각 줄 출력
total_boj=${#lines[@]}
length=$((total_boj - 1))

for (( i=0; i<${#lines[@]}; i++ )); do
  link="${lines[$i]}"
  
  # TODO: 19주차부터 지울 부분
  problem_number=$(echo $link | cut -d '/' -f5 )
  problem_title=$(python $script_dir/crawling.py $problem_number)
  problem_folder="${week_folder}/BOJ_${problem_number}"

  # # TODO: 19주차부터 PSG 에 적용
  # if [[ $i < $length ]]; then
  #   problem_number=$(echo $link | cut -d '/' -f5 )
  #   problem_title=$(python $script_dir/crawling.py $problem_number)
  #   problem_folder="${week_folder}/BOJ_${problem_number}"
  # else
  #   problem_title=$(python ./scripts/crawling_psg.py $link)
  #   problem_folder="${week_folder}/PSG_${problem_title}"
  # fi

  mkdir -p "$problem_folder"

  # 두 번째 인자가 주어졌을 때 해당 확장자로 파일 생성
  if [ -n "$expansion" ]; then
    touch "${problem_folder}/${problem_title}_${executor_name}.${expansion}"
  else
    # 두 번째 인자가 주어지지 않았을 때 기본적으로 py 확장자로 파일 생성
    touch "${problem_folder}/${problem_title}_${executor_name}.py"
  fi
done