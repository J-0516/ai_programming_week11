# ai_programming_week11

## ① 무엇을 하나요 (What)

주어진 CVS에서 유효한 성적을 가진 학생들을 선정한다.

## ② 왜 만들었나요 (Why)          ★ AI는 이 칸을 못 씁니다

일반적인 경우에는 범위 외 점수뿐만 아니라, 
빈 칸, 중복 이름, 헤더만 있는 칸과 같은 CVS에서 작동이 안 된다.

## ③ 어떻게 쓰나요 (How)

```bash
# 설치
python -m pip install pytest
# 실행
python load_scores.py scores.csv
```

## ④ 어떻게 테스트하나요

```bash
pytest를 실행하면 다음과 같다.
```

```
==================================== test session starts =====================================
platform win32 -- Python 3.12.6, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\USER\Desktop\AI_programming\week11_files
plugins: cov-7.1.0
collected 17 items                                                                            

test_ai_A.py ...                                                                        [ 17%]
test_ai_B.py ....                                                                       [ 41%]
test_ai_C.py .                                                                          [ 47%]
test_load_scores.py .........                                                           [100%]

===================================== 17 passed in 0.11s ===================================== 
```

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| `load_scores.py` | 성적 CSV를 읽고 유효한 성적과 제외한 행의 기록을 반환한다. |
| `test_load_scores.py` | 성적 읽기의 정상 동작, 파일 예외, 빈 파일, 점수 경계값을 테스트한다. |
| `test_ai_A.py`, `test_ai_B.py` | 중복 이름, 빈 줄, 잘못된 행, 경계값과 명령행 실행 결과를 추가로 테스트한다. |
| `scores.csv`, `empty.csv` | 성적 읽기와 헤더만 있는 파일을 확인하는 입력 예시이다. |

## ⑥ 만든 사람 · AI를 어디에 썼는지

- 만든 사람 : 2026100334_장준호
- AI를 쓴 곳 : 성적 읽기 테스트 코드 작성·수정, 테스트 결과 해석, README 사용법 정리에 활용
- 내가 직접 판단한 것 : README와 테스트 내용을 확인하고 실행 결과를 점검함

## 라이선스

MIT License

Copyright (c) 2026 장준호

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
