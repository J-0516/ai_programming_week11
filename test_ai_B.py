'''
아래 명세를 만족하는 함수의 단위 테스트를 pytest로
작성해 주세요. 정상 · 예외 · 경계값을 모두 포함해 주세요.

  ① 무엇을 받나       : 성적 CSV를 읽는 load_scores(path)는 CSV 파일의 경로를 받습니다.
  ② 무엇을 돌려주나   : 유효한 성적 목록과 제외한 행의 기록을 함께 돌려줍니다.
                         성적은 (이름, 정수 점수), 행의 기록은 (줄 번호, 원본 줄, 이유) 형식입니다.
  ③ 실패하면 어떻게 하나 : 파일이 없으면 FileNotFoundError를 그대로 발생시키고, 읽기 오류도 숨기지 않습니다.
                           잘못된 데이터 행은 결과에서 제외하고 행과 이유를 기록합니다.
  ④ 쓰면 안 되는 것   : 표준 라이브러리 외 패키지를 사용하거나 입력 파일을 수정하지 않습니다.
                         잘못된 점수나 행을 임의의 값으로 바꾸지 않습니다.
  ⑤ 예외 상황         : 헤더만 있으면 두 결과 모두 빈 목록입니다. 빈 줄은 기록 없이 건너뜁니다.
                         이름이 중복되어도 해당하는 유효 성적을 모두 남깁니다.
  ⑥ 조건 · 제약       : 첫 줄은 헤더입니다. 이후 행은 열이 정확히 2개이고 이름이 비어 있지 않아야 합니다.
                         점수는 비어 있지 않은 정수이며 0~100 범위입니다. 조건 위반 행은 사유와 함께 기록합니다.
                         파일을 직접 실행하면 명령행 경로의 CSV를 읽고, 요약과 유효·제외 행을 출력합니다.
'''

import csv
import runpy
import sys
from pathlib import Path

import pytest

from load_scores import load_scores


def _쓰기_csv(경로, 행들):
    with open(경로, "w", encoding="utf-8", newline="") as 파일:
        writer = csv.writer(파일)
        writer.writerow(["name", "score"])
        writer.writerows(행들)


def test_잘못된_행을_제외하고_정확한_사유를_기록한다(tmp_path):
    경로 = tmp_path / "잘못된.csv"
    _쓰기_csv(
        경로,
        [
            ["", "90"],
            ["점수없음", ""],
            ["문자점수", "결석"],
            ["범위초과", "101"],
            ["한열"],
            ["열이", "세", "개"],
        ],
    )

    kept, skipped = load_scores(경로)

    assert kept == []
    assert skipped == [
        (2, ",90", "이름이 비어 있음"),
        (3, "점수없음,", "점수가 비어 있음"),
        (4, "문자점수,결석", "점수가 정수가 아님"),
        (5, "범위초과,101", "점수가 0~100 밖"),
        (6, "한열", "열 개수가 2가 아님"),
        (7, "열이,세,개", "열 개수가 2가 아님"),
    ]


def test_경계값에_따라_유효한_성적과_제외_기록을_돌려준다(tmp_path):
    경로 = tmp_path / "경계값.csv"
    _쓰기_csv(경로, [["아래", "-1"], ["최솟값", "0"], ["최댓값", "100"], ["위", "101"]])

    kept, skipped = load_scores(경로)

    assert kept == [("최솟값", 0), ("최댓값", 100)]
    assert skipped == [
        (2, "아래,-1", "점수가 0~100 밖"),
        (5, "위,101", "점수가 0~100 밖"),
    ]


def test_파일_오류를_숨기지_않는다(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores(tmp_path / "없는.csv")

    with pytest.raises(OSError):
        load_scores(tmp_path)


def test_직접_실행하면_결과_요약을_출력한다(tmp_path, monkeypatch, capsys):
    경로 = tmp_path / "실행.csv"
    _쓰기_csv(경로, [["홍길동", "88"], ["오류", "101"]])
    스크립트 = Path(__file__).with_name("load_scores.py")
    monkeypatch.setattr(sys, "argv", [str(스크립트), str(경로)])

    runpy.run_path(str(스크립트), run_name="__main__")

    출력 = capsys.readouterr().out
    assert "읽은 줄 : 1개" in 출력
    assert "홍길동 88" in 출력
    assert "건너뛴 줄 : 1개" in 출력
    assert "오류,101" in 출력