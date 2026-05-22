import streamlit as st

# 웹 페이지 제목 설정
st.title("🚚 배송비 및 총 결제금액 계산기")
st.write("회원 상태와 주문 금액을 입력하시면 총 결제금액을 계산해 드립니다.")

st.divider()  # 구분선

# 1. 사용자 입력 받기
# 정기 회원 여부를 라디오 버튼으로 선택 (기본값 '아니오')
member_status = st.radio("정기 회원입니까?", ["예 (y)", "아니오 (n)"], index=1)

# 주문 금액 입력 (기본값 0원, 100원 단위로 조절 가능)
total_price = st.number_input("주문 금액은 얼마입니까? (원)", min_value=0, step=100, value=0)

st.divider()  # 구분선

# 2. 배송비 계산 및 결과 출력 조건문
if st.button("결제금액 계산하기"):
    shipping_fee = 0
    
    if member_status == "예 (y)":
        st.info("💡 정기 회원으로 배송비가 면제됩니다.")
    else:
        st.warning("ℹ️ 배송비 3,000원이 부과됩니다.")
        shipping_fee = 3000
    
    # 최종 금액 계산
    final_total = total_price + shipping_fee
    
    # 결과 보여주기
    st.success(f"### 💰 총 결제금액은 **{final_total:,}원** 입니다.")