# 목회자 AI 스킬 (Pastor AI Skills, 한글판)

> **이것은 [tkcostello/pastor-ai-skills](https://github.com/tkcostello/pastor-ai-skills)의 한글 번역본입니다.**
> 원저자: Thomas Costello (MIT License). 한글 번역: guysaint.
> 한국 교회 맥락(용어, 성경 번역본, 신학 가드레일 등)에 맞춰 의역·각색되었습니다.

목회자를 위해 만들어진 AI 워크플로우 도구 13개. 단순 프롬프트가 아닙니다. 매주 반복되는 업무를 처리해 주는 다단계 스킬로, 사역에 집중할 수 있도록 돕습니다.

[Claude Code](https://claude.ai/code)용으로 제작되었습니다. Claude.ai Projects에서도 동작합니다.

---

## 소개

원저자 Thomas Costello는 20년 넘게 목회 사역에 몸담아 왔으며, 교회 마케팅 에이전시 [REACHRIGHT](https://reachrightstudios.com)를 운영합니다. 매주 같은 종류의 글을 처음부터 다시 쓰는 데 지쳐 자신을 위해 이 스킬들을 만들었고, 실제로 매주 사용하는 도구라고 합니다.

목회자에게는 일반적인 AI 프롬프트보다 더 나은 것이 필요하다는 신념으로 이 도구들이 공개되었습니다. 무겁게 다시 써야 하는 템플릿이 아니라, 목회적 감수성이 내장된 워크플로우 도구입니다.

이 한글판은 한국 교회의 용어·문화·신학적 맥락에 맞춰 다시 작성되었습니다.

---

## 스킬 목록

| 스킬 | 하는 일 | 사용 빈도 |
|---|---|---|
| **설교 준비** | | |
| `/sermon-research` | 본문에 대한 깊이 있는 조사: 주석, 역사적 배경, 단어 연구, 사고 촉진 질문. 포맷된 PDF 출력. | 주간 |
| `/sermon-brainstorm` | 명확한 설교 개요를 산출하는 대화식 브레인스토밍 | 주간 |
| `/sermon-series` | 제목, 본문, 핵심 메시지로 구성된 다주간 시리즈 기획 | 월간 |
| **글 작성** | | |
| `/church-email` | 주간 교회 이메일 작성: 제목, 미리보기 텍스트, 본문 | 주간 |
| `/announcement-script` | 주일 광고용 60~90초 스피치 원고 | 주간 |
| `/church-letter` | 다양한 상황의 편지: 이임, 근황, 축하, 어려운 소식 | 필요 시 |
| **설교 재활용** | | |
| `/small-group-questions` | 주일 설교 기반 순/목장 토론 질문: 관찰·해석·적용 | 주간 |
| `/sermon-to-blog` | 설교를 800~1,200자 분량의 블로그 글로 (녹취록이 아님) | 주간 |
| `/sermon-to-youtube` | 유튜브 제목, 설명, 태그, 썸네일 컨셉, 숏폼 클립 추천 | 주간 |
| **소셜미디어** | | |
| `/church-social-post` | 페이스북·인스타그램·트위터용 플랫폼별 포스트 | 주 3~5회 |
| `/social-media-calendar` | 한 주 또는 한 달치 콘텐츠 캘린더 (날짜·플랫폼별) | 주간 |
| **목회 리듬** | | |
| `/midweek-devotional` | 이메일·앱용 200~300자 묵상글: 목회적·개인적·간결 | 주간 |
| `/meeting-agenda` | 시간 블록과 토의 질문이 있는 구조화된 회의 안건 | 주간 |

---

## 시작하기

### 옵션 1: Claude Code (가장 쉬움)

Claude Code를 열고 다음을 붙여넣으세요:

> https://github.com/guysaint/pastor-ai-skills 에서 목회자 AI 스킬을 설치해 줘. 전부 다 원해.

이게 전부입니다. Claude가 레포를 클론하고, 파운데이션과 모든 스킬을 설치해 줍니다. 특정 스킬만 원하면 어떤 스킬을 원하는지 말해 주세요.

설치 후에는 `/sermon-research`, `/church-email` 등을 입력해 사용합니다.

### 옵션 2: 수동 설치 (Claude Code CLI)

직접 설치하고 싶다면:

```bash
# 레포 클론
git clone https://github.com/guysaint/pastor-ai-skills.git

# 파운데이션 복사 (모든 스킬에 필수)
cp -r pastor-ai-skills/foundation/pastor-foundation ~/.claude/skills/

# 사용할 스킬 복사
cp -r pastor-ai-skills/sermon-prep/sermon-research ~/.claude/skills/
cp -r pastor-ai-skills/written-communication/church-email ~/.claude/skills/
cp -r pastor-ai-skills/sermon-repurposing/small-group-questions ~/.claude/skills/
# ... 필요한 만큼 추가
```

### 옵션 3: Claude.ai Projects

1. Claude.ai에서 새 Project 생성
2. 사용하려는 스킬의 `SKILL.md` 파일을 엽니다 (GitHub에서 바로 보기 가능)
3. 전체 내용을 Project의 커스텀 인스트럭션에 복사
4. 더 나은 결과를 위해 `pastor-foundation/SKILL.md` 내용도 먼저 복사

---

## 파운데이션 설정

어떤 스킬을 처음 사용할 때, 파운데이션이 교회에 대한 몇 가지 정보를 묻습니다:

- **교회 이름**
- **이름 및 호칭** (예: 김OO 목사)
- **교단** (선택사항, 기본값: 장로교 고신)
- **주일 평균 출석 인원**
- **지역** (시/도 및 구/군)
- **선호 성경 번역본** (기본값: 개역개정)

한 번 입력하면 모든 스킬이 이 정보를 사용해 출력물을 개인화하므로, 외부 AI가 아니라 사역 동역자가 쓴 것처럼 느껴집니다.

---

## 의존성

대부분의 스킬은 의존성이 없습니다. 다음 스킬만 일회성 설치가 필요합니다:

| 스킬 | 의존성 | 설치 |
|---|---|---|
| `/sermon-research` | reportlab (Python) | `pip install reportlab` |

Claude Code가 처음 사용 시 자동으로 설치합니다. 수동 설치를 원하면 위 명령어를 실행하세요.

---

## 철학

**이것들은 프롬프트 템플릿이 아니라 워크플로우 도구입니다.** 각 스킬에는 정의된 프로세스, 형식 규칙, 품질 기준이 내장되어 있습니다. 이메일 마케팅 모범 사례나 유튜브 SEO를 알 필요가 없습니다. 스킬이 알고 있습니다.

**파운데이션 레이어가 모든 것을 일관되게 유지합니다.** 어조, 신학적 감수성, 교회 정보가 모든 스킬에 자동으로 적용됩니다.

**설교 준비 도구는 조사와 사고를 돕습니다. 설교 자체를 쓰지 않습니다.** 그 일은 당신과 성령 사이의 일입니다. 조사 스킬은 주석과 배경을 파고듭니다. 브레인스토밍 스킬은 질문을 던집니다. 어느 쪽도 원고를 건네주지 않습니다.

**모든 출력물은 바로 사용 가능하도록 설계되었습니다.** 다시 써야 할 거친 초안이 아닙니다. 복사·붙여넣기·전송. 받은 것의 20% 이상을 다시 쓰고 있다면, 스킬이 제 일을 못한 것입니다.

---

## 원저자 (Original Author)

**Thomas Costello** is the founder and CEO of [REACHRIGHT](https://reachrightstudios.com) and Executive Pastor at New Hope Hawaii Kai. He's been in ministry for 20+ years, planted a church, led a church through a merger, grew a church from 30 to 150, and built a marketing agency that serves churches across the country.

- [LinkedIn](https://www.linkedin.com/in/tkcostello/)
- [Twitter/X](https://x.com/tkcostello)
- [REACHRIGHT](https://reachrightstudios.com)

## 한글판 (Korean Edition)

한글 번역 및 한국 교회 맥락 각색: [guysaint](https://github.com/guysaint)

---

## 라이선스

MIT. 자유롭게 사용하세요.
