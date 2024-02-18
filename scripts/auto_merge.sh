#!/bin/bash

export $(grep -v '^#' .env | xargs)

# GitHub 사용자 이름
USERNAME="$1"

# GitHub Personal Access Token (PAT)
PAT="$GITHUB_TOKEN"

# 대상 저장소
REPO="Stendhalsynd/baekjoon-algorithm-study"

# main 브랜치 이름
MAIN_BRANCH="main"

# PR 상태 필터 (예: open, closed, all)
PR_STATE="open"

# PAT 설정
echo "$PAT" | gh auth login --with-token

# 현재 브랜치 확인
CURRENT_BRANCH=$(git branch --show-current)

# main 브랜치로 이동
git checkout "$MAIN_BRANCH"

# 모든 PR 목록 가져오기
PRs=$(gh pr list --repo "$REPO" --state "$PR_STATE" --author "$USERNAME" --json url)

# PR 루프
for PR_URL in $PRs; do
  # PR 번호 추출
  PR_NUMBER=$(echo "$PR_URL" | sed -n 's/.*\/pull\/\([0-9]*\).*/\1/p')

  # PR 정보 출력
  echo "## PR #$PR_NUMBER"

  # PR 체크아웃
  git checkout "$PR_NUMBER"

  # PR 변경 사항 저장
  git add -A

  # PR rebase
  git rebase "$MAIN_BRANCH"

  # PR merge
  git merge --squash "$MAIN_BRANCH"

  # PR 삭제
  gh pr close "$PR_NUMBER"

  # main 브랜치로 이동
  git checkout "$MAIN_BRANCH"
done

# 변경 사항 푸시
git push

# 현재 브랜치로 돌아가기
git checkout "$CURRENT_BRANCH"

echo "## 완료"