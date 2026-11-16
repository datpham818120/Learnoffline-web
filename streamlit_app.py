import streamlit as st
from datetime import datetime

st.set_page_config(page_title="LearnOffline", page_icon="📚")
QUESTIONS = [
 {"subject":"Toán","topic":"Phương trình","q":"Nếu 3x = 15 thì x bằng bao nhiêu?","options":["3","5","12","45"],"answer":1,"explain":"Chia hai vế cho 3, ta được x = 5."},
 {"subject":"Vật lí","topic":"Chuyển động","q":"Tốc độ trung bình được tính bằng công thức nào?","options":["Quãng đường chia thời gian","Thời gian chia quãng đường","Vận tốc nhân thời gian","Khối lượng chia thể tích"],"answer":0,"explain":"Tốc độ trung bình = tổng quãng đường / tổng thời gian."},
 {"subject":"Hóa học","topic":"Nguyên tố","q":"Kí hiệu hóa học của sắt là gì?","options":["Ag","Fe","F","S"],"answer":1,"explain":"Sắt có kí hiệu hóa học là Fe."},
 {"subject":"Tiếng Anh","topic":"Từ vựng","q":"Từ 'attend' thường có nghĩa là gì?","options":["Tham dự","Từ chối","Xây dựng","Làm khô"],"answer":0,"explain":"'Attend' thường có nghĩa là tham dự hoặc có mặt."},
 {"subject":"Sinh học","topic":"Tế bào","q":"Đơn vị cấu tạo cơ bản của cơ thể sống là gì?","options":["Nguyên tử","Mô","Tế bào","Cơ quan"],"answer":2,"explain":"Tế bào là đơn vị cấu trúc và chức năng cơ bản của cơ thể sống."}
]
if "history" not in st.session_state: st.session_state.history=[]
if "feedback" not in st.session_state: st.session_state.feedback={}
st.title("📚 LearnOffline")
st.caption("Bản web thử nghiệm học tập và luyện trắc nghiệm.")
st.warning("Bản demo lưu lịch sử trong phiên hiện tại; chưa có lưu trữ bền vững hoặc tài khoản. Không nhập thông tin cá nhân thật.")
page=st.sidebar.radio("Điều hướng",["Trang chủ","Luyện tập","Thống kê","Về dự án"])
if page=="Trang chủ":
    st.header("Học tập và ôn tập")
    st.write("LearnOffline hướng tới học liệu, luyện tập trắc nghiệm và gợi ý nội dung cần ôn dựa trên lịch sử làm bài.")
    st.metric("Câu hỏi mẫu",len(QUESTIONS))
    st.write("Đây là bản thử nghiệm; nội dung câu hỏi cần được rà soát trước khi dùng trong nghiên cứu.")
elif page=="Luyện tập":
    subjects=["Tất cả môn"]+sorted({q["subject"] for q in QUESTIONS})
    subject=st.selectbox("Chọn môn",subjects)
    qs=[(i,q) for i,q in enumerate(QUESTIONS) if subject=="Tất cả môn" or q["subject"]==subject]
    if "qpos" not in st.session_state: st.session_state.qpos=0
    st.session_state.qpos=min(st.session_state.qpos,len(qs)-1)
    idx,q=qs[st.session_state.qpos]
    st.caption(f"{q['subject']} · {q['topic']} · Câu {st.session_state.qpos+1}/{len(qs)}")
    st.subheader(q["q"])
    choice=st.radio("Chọn đáp án",q["options"],key=f"choice_{subject}_{st.session_state.qpos}")
    if st.button("Kiểm tra đáp án"):
        correct=q["options"].index(choice)==q["answer"]
        st.session_state.history.append({"subject":q["subject"],"topic":q["topic"],"correct":correct,"at":datetime.now().isoformat()})
        st.session_state.feedback[idx]={"correct":correct,"explain":q["explain"],"answer":q["options"][q["answer"]]}
    fb=st.session_state.feedback.get(idx)
    if fb:
        st.success("Chính xác! "+fb["explain"]) if fb["correct"] else st.error("Chưa đúng. Đáp án: "+fb["answer"]+". "+fb["explain"])
    c1,c2=st.columns(2)
    if c1.button("← Câu trước",disabled=st.session_state.qpos==0):
        st.session_state.qpos-=1; st.rerun()
    if c2.button("Câu tiếp →",disabled=st.session_state.qpos>=len(qs)-1):
        st.session_state.qpos+=1; st.rerun()
elif page=="Thống kê":
    h=st.session_state.history
    n=len(h); right=sum(x["correct"] for x in h)
    a,b,c=st.columns(3)
    a.metric("Lượt trả lời",n); b.metric("Lượt đúng",right); c.metric("Tỉ lệ đúng",f"{right/n*100:.1f}%" if n else "0%")
    for subject in sorted({x["subject"] for x in h}):
        rows=[x for x in h if x["subject"]==subject]
        st.write(f"- {subject}: {sum(x['correct'] for x in rows)}/{len(rows)} lượt đúng")
    if st.button("Xóa lịch sử phiên"):
        st.session_state.history=[]; st.rerun()
else:
    st.header("Mục tiêu nghiên cứu")
    st.write("Nghiên cứu liệu thuật toán ưu tiên câu từng trả lời sai hoặc lâu chưa ôn có hỗ trợ ghi nhớ tốt hơn chọn câu ngẫu nhiên hay không.")
    st.write("Bản web được triển khai trên mạng cần Internet để truy cập. Muốn dùng khi mất mạng cần phát triển thêm PWA/offline cache hoặc dùng bản Windows cục bộ.")
 print("Đạt dzai vaiz")

 
