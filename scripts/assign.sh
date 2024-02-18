#!/bin/bash

# 문지영 송성우 양승혜 이서연 주지찬 최재선 홍지훈

# 사용법 확인
if [ $# -lt 1 ]; then
    echo "사용법: $0 <주차> [빠진인원...]"
    exit 1
fi

# 변수 설정
exclude_members=("$@")
all_members=("문지영" "송성우" "양승혜" "이서연" "주지찬" "최재선" "홍지훈")

# 인자로 전달한 인원을 멤버에서 제외
for member in "${exclude_members[@]}"; do
  all_members=("${all_members[@]//$member}")
done
all_members=($(echo "${all_members[@]}" | tr -s ' ' '\n' | grep -v '^$'))

# 인원 수 확인
num_members=${#all_members[@]}
num_problems=$((num_members > 2 ? 2 : num_members))

add_member=()
for i in {1..$num_members}; do
  random_index=$((RANDOM % ${#all_members[@]}))
  add_member+=("${all_members[random_index]}")
done

all_members+=("${add_member[@]}")

# 스크립트 파일이 위치한 디렉토리 경로
script_dir=$(dirname "$(readlink -f "$0")")

# 프로젝트의 루트 디렉토리 경로
root_dir=$(dirname "$script_dir")

current_week=$(date +%U)
study_week=$((current_week + 11))
file="$root_dir/scripts/problems.txt"

# 파일을 한 줄씩 읽어 배열에 담기
IFS=$'\n' read -d '' -r -a lines < "$file"

problems=()

# 배열 순회하여 각 줄 출력
for link in "${lines[@]}"; do
  problem_number=$(echo $link | cut -d '/' -f5 )
  problem_title=$(python $script_dir/crawling.py $problem_number)
  problems+=("${problem_number}_${problem_title}")
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