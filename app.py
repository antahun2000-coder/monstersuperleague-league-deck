import streamlit as st

st.title("🛡️ 몬스터 슈퍼리그 PVP 덱 분석기")
st.write(
    "환영합니다! 여기에 PVP 랭킹 정보와 캐릭터 카운트 통계가 표시됩니다."
)

# 간단한 데이터 입력 테스트용 위젯
nickname = st.text_input("상대 유저 닉네임 입력")
starmon = st.selectbox(
    "등장한 주요 스타몬 선택",
    ["불 라트", "물 세이렌", "나무 발키리", "빛 아서", "암 빅토르"],
)

if st.button("데이터 기록하기"):
  if nickname:
    st.success(
        f"[{nickname}]님의 덱 정보 ({starmon})가 성공적으로 기록되었습니다!"
    )
  else:
    st.warning("닉네임을 입력해주세요.")
