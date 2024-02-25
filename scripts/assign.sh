#!/bin/bash

# 변수 설정
exclude_members=("$@")
all_members=("송성우" "양승혜" "최재선" "홍지훈")

# 인자로 전달한 인원을 멤버에서 제외
for member in "${exclude_members[@]}"; do
  all_members=("${all_members[@]//$member}")
done
all_members=($(echo "${all_members[@]}" | tr -s ' ' '\n' | grep -v '^$'))

# 인원 수 확인
num_members=${#all_members[@]}
num_problems=$((num_members > 2 ? 2 : num_members))

add_member=()

for ((i = 0; i < 7 - $num_members; i++)); do
  random_index=$((RANDOM % ${#all_members[@]}))
  add_member+=("${all_members[random_index]}")
done

all_members+=("${add_member[@]}")

# 스크립트 파일이 위치한 디렉토리 경로
script_dir=$(dirname "$(readlink -f "$0")")

# 프로젝트의 루트 디렉토리 경로
root_dir=$(dirname "$script_dir")

current_week=$((10#$(date +%U)))
study_week=$((current_week + 11))
file="$root_dir/scripts/problems.txt"

# 파일을 한 줄씩 읽어 배열에 담기
IFS=$'\n' read -d '' -r -a lines < "$file"

total_boj=${#lines[@]}
length=$((total_boj - 1))

problems=()

# 배열 순회하여 각 줄 출력
for ((i = 0; i < ${#lines[@]}; i++)); do
  link=${lines[$i]}
  if [[ $i < $length ]]; then
    problem_number=$(echo $link | cut -d '/' -f5 )
    problem_title=$(python ./scripts/crawling.py $problem_number)
    problems+=("${problem_number}_${problem_title}")
  else
    problem_title=$(python ./scripts/crawling_psg.py $link)
    problems+=("${problem_title}")
  fi
done

# exclude_members가 비어있는 경우
if [[ -z "$exclude_members" ]]; then
  # 랜덤 숫자로 선택된 문제 추가
  random_problem_index=$((RANDOM % 7))
  problems+=("${problems[$random_problem_index]}")
fi

# Fisher-Yates 알고리즘 -> 인원 랜덤 섞기
for i in "${!all_members[@]}"; do
  j=$((RANDOM % ($i + 1)))
  temp=${all_members[$i]}
  all_members[$i]=${all_members[$j]}
  all_members[$j]=$temp
done

# 결과 출력
echo "# $study_week 주차 문제 배정 결과" > weekly_assign.md
echo "" >> weekly_assign.md

# 문제의 수에 따라 표를 생성합니다.
printf "|" >> weekly_assign.md

for problem in "${problems[@]}"; do
  printf "%s" " $problem |" >> weekly_assign.md
done

echo "" >> weekly_assign.md

printf "|" >> weekly_assign.md

for problem in "${problems[@]}"; do
  printf "%s" " --- |" >> weekly_assign.md
done

echo "" >> weekly_assign.md

printf "|" >> weekly_assign.md

for member in "${all_members[@]}"; do
  printf "%s" " $member |" >> weekly_assign.md
done