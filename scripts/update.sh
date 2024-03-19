#!/bin/bash

# 파일 이름과 문제 목록 파일의 경로 설정
md_file="TEST.md"
problems_file="problems.txt"

# 스크립트 파일이 위치한 디렉토리 경로
script_dir=$(dirname "$(readlink -f "$0")")

# 프로젝트의 루트 디렉토리 경로
root_dir=$(dirname "$script_dir")

# 현재 날짜의 주차 정보 가져오기
current_week=$((10#$(date +%U)))
echo "current_week : $current_week"

start_date=$(date -d "$year-01-01 +$((current_week-1))weeks" +%m/%d)
end_date=$(date -d "$year-01-01 +$((current_week))weeks -1 day" +%m/%d)

echo "start_date, end_date : $start_date, $end_date"

# start_date=$(date -v${current_week}w -v1d +%m.%d)
# end_date=$(date -v${current_week}w -v7d +%m.%d)

# start_date=$(date -d "$(date +%Y)-01-01 +$((current_week*7))days" +%m.%d)
# end_date=$(date -d "$(date +%Y)-01-01 +$((current_week*7+6))days" +%m.%d)

study_week=$((current_week + 11))

file="$root_dir/scripts/problems.txt"

# 파일을 한 줄씩 읽어 배열에 담기
IFS=$'\n' read -d '' -r -a lines < "$file"

# 배열 순회하여 각 줄 출력
total_boj=${#lines[@]}
length=$((total_boj - 1))

# 새로운 문제 목록을 담을 변수 초기화
new_schedule="| ${study_week}주차 (${start_date} ~ ${end_date}) |"
problem_title=""

for (( i=0; i<${#lines[@]}; i++ )); do
  link="${lines[$i]}"

  if [[ $i < $length ]]; then
    problem_number=$(echo $link | cut -d '/' -f5 )
    problem_title=$(python $script_dir/crawling.py $problem_number)
  else
    problem_title=$(python ./scripts/crawling_psg.py $link)
  fi

  # Markdown 표 형식에 맞게 새로운 줄 추가
  new_schedule+=" [${problem_title}](${link}) |"
done

echo "new_schedule : ${new_schedule}"

# 새로운 일정표 생성
new_md=$(awk -v new_schedule="$new_schedule" '/3기 일정표/,/17주차/ {if ($0 ~ /^|/) print new_schedule; else print} ' "$md_file")

# 업데이트된 내용을 원래의 파일에 다시 쓰기
echo "$new_md" > "$md_file"

echo "Markdown 파일이 업데이트되었습니다."

# #!/bin/bash

# # 현재 년도와 주차 계산
# current_year=$((10#$(date +%Y)))
# current_week=$((10#$(date +%U)))
# week=$(date +%U)

# echo "current_year : $current_year"
# echo "current_week : $current_week"

# # start_date=$(date -v1d -v-$(($current_week-1))w -v+$((($current_week-1)*7))d -jf "%Y-%m-%d" "$current_year-$week-01" +%m/%d)
# start_date=$(date -v1d -v-$(($current_week-1))w -v+$((($current_week-1)*7))d -jf "%Y-%m-%d" +%m/%d)

# # 주의 시작 날짜 (월요일)
# # start_date=$(date -v -$(($current_week-1))w -v1d +%m/%d)

# # 주의 종료 날짜 (일요일)
# end_date=$(date -v -$(($current_week-1))w -v7d +%m/%d)

# # # 주의 시작 날짜 (월요일)
# # start_date=$(date -d "$current_year-01-01 +10#$(($current_week-1))weeks" +%m/%d)

# # # 주의 종료 날짜 (일요일)
# # end_date=$(date -d "$current_year-01-01 +10#$(($current_week))weeks -1 day" +%m/%d)

# echo "이번 주 월요일: $start_date"
# echo "이번 주 일요일: $end_date"