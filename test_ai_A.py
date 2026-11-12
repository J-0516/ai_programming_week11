'''
아래 함수의 단위 테스트를 pytest로 작성해 주세요.
정상 · 예외 · 경계값을 모두 포함해 주세요.

import csv

MIN_SCORE = 0
MAX_SCORE = 100


def load_scores(path):
    """성적 CSV를 읽어 (유효한 목록, 건너뛴 줄 기록) 을 돌려준다."""
    kept = []
    skipped = []

    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for line_no, row in enumerate(reader, start=1):
            if line_no == 1:              # 헤더
                continue
            if not row:                   # 빈 줄 — 기록하지 않는다
                continue

            원본 = ",".join(row)

            if len(row) != 2:
                skipped.append((line_no, 원본, "열 개수가 2가 아님"))
                continue

            name = row[0].strip()
            raw = row[1].strip()

            if name == "":
                skipped.append((line_no, 원본, "이름이 비어 있음"))
                continue
            if raw == "":
                skipped.append((line_no, 원본, "점수가 비어 있음"))
                continue

            try:
                score = int(raw)
            except ValueError:
                skipped.append((line_no, 원본, "점수가 정수가 아님"))
                continue

            if score < MIN_SCORE or score > MAX_SCORE:
                skipped.append((line_no, 원본, "점수가 0~100 밖"))
                continue

            kept.append((name, score))

    return kept, skipped


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else "scores.csv"
    kept, skipped = load_scores(path)
    print(f"읽은 줄 : {len(kept)}개")
    for name, score in kept:
        print(f"  {name} {score}")
    print(f"건너뛴 줄 : {len(skipped)}개")
    for line_no, 원본, 이유 in skipped:
        print(f"  {line_no}행  {원본}   ← {이유}")
'''

import csv

from load_scores import load_scores


def _쓰기_csv(경로, 행들):
    with open(경로, "w", encoding="utf-8", newline="") as 파일:
        writer = csv.writer(파일)
        writer.writerow(["name", "score"])
        writer.writerows(행들)


def test_중복_이름과_쉼표가_포함된_이름을_그대로_읽는다(tmp_path):
    경로 = tmp_path / "정상.csv"
    _쓰기_csv(경로, [["김하나", "88"], ["김하나", "91"], ["최,네번", "77"]])

    kept, skipped = load_scores(경로)

    assert kept == [("김하나", 88), ("김하나", 91), ("최,네번", 77)]
    assert skipped == []


def test_빈_줄은_제외_기록에_넣지_않는다(tmp_path):
    경로 = tmp_path / "빈줄.csv"
    _쓰기_csv(경로, [["학생", "80"], [], ["다른학생", "90"]])

    kept, skipped = load_scores(경로)

    assert kept == [("학생", 80), ("다른학생", 90)]
    assert skipped == []


def test_입력_파일을_수정하지_않는다(tmp_path):
    경로 = tmp_path / "입력.csv"
    _쓰기_csv(경로, [["학생", "80"], ["오류", "101"]])
    원본 = 경로.read_bytes()

    load_scores(경로)

    assert 경로.read_bytes() == 원본