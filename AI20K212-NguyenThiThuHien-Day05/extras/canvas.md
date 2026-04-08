# AI Product Canvas — Trợ thủ MoMo AI Moni

**Học viên:** Nguyễn Thị Thu Hiền

**Mã học viên:** 2A202600212

**Sản phẩm:** MoMo — Trợ thủ AI Moni

---



|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Trả lời** | **- User:** Người dùng MoMo thường xuyên chuyển khoản cá nhân (P2P), quét QR.<br>**- Pain point:** Lười ghi chép chi tiêu thủ công, cuối tháng không biết "tiền đi về đâu".<br>**- AI giải quyết gì:** Tự động nhận diện ngữ cảnh và phân loại giao dịch (Auto-categorization) realtime ngay khi tiền vừa trừ, không bắt user tự nhập tay như các app truyền thống (MoneyLover, Sổ Thu Chi). | **- Khi AI sai ảnh hưởng gì:** Báo cáo tài chính cuối tháng sai bét (gom tiền "trả nợ" vào "mua sắm"), user hoang mang, mất niềm tin vào app.<br>**- User biết AI sai bằng cách nào:** Nhìn icon danh mục gắn kèm ngay trên lịch sử giao dịch vừa thực hiện, hoặc xem biểu đồ tổng kết cuối tháng thấy vô lý.<br>**- User sửa bằng cách nào:** Chạm nhanh vào icon sai ở màn hình chính -> Chọn lại danh mục đúng từ Pop-up "Top 3 AI gợi ý" (áp dụng luồng Quick Edit đề xuất). | **- Cost:** Rất thấp (~$0.0001 - $0.0005/request) do chỉ cần dùng mô hình Classification/NLP nhỏ đã fine-tune, không cần gọi LLM lớn cho mọi giao dịch.<br>**- Latency:** Yêu cầu < 500ms (Phải realtime ngay khi giao dịch thành công để user thấy tag ngay).<br>**- Risk chính:** <br>1. *Data Privacy:* Rủi ro khi đọc/phân tích lời nhắn chuyển khoản nhạy cảm.<br>2. *Data Drift:* Ngôn ngữ lóng, teencode của người dùng thay đổi liên tục khiến model bị out-date. |

---

## Automation hay augmentation?

☐ Automation — AI làm thay, user không can thiệp
☑ Augmentation — AI gợi ý, user quyết định cuối cùng

**Justify:**
Ngữ cảnh chi tiêu mang tính cá nhân hóa cực cao (Cùng chữ "cf", người này là đi uống Cà phê, người kia là chuyển tiền mua Cổ phiếu). Nếu dùng Automation 100%, AI tự quyết định sai mà không báo, user sẽ không phát hiện ra cho đến cuối tháng -> Hậu quả dữ liệu hỏng nghiêm trọng.
Vì vậy, Moni phải là **Augmentation**: AI phân loại trước (Gợi ý), nhưng thiết kế UX phải cho phép user cực kỳ dễ dàng sửa đổi (Quyết định cuối cùng).

---

## Learning signal

| # | Câu hỏi | Trả lời |
|---|---------|---------|
| 1 | User correction đi vào đâu? | Đi thẳng vào Data Pipeline làm nhãn (Labelled Data) để Fine-tune lại mô hình định kỳ, hoặc đưa vào bộ nhớ User Profile (RAG context) để AI "nhớ" thói quen cho lần giao dịch sau. |
| 2 | Product thu signal gì để biết tốt lên hay tệ đi? | - **Độ chính xác (Tốt lên):** Tỷ lệ user chấp nhận (không sửa) tag của AI tăng; Tỷ lệ user bấm chọn đúng "Top 3 gợi ý" khi sửa lỗi tăng.<br>- **Ma sát (Tệ đi):** Tỷ lệ giao dịch user bấm "Sửa" nhưng bỏ ngang (Exit/Bailout) tăng. |
| 3 | Data thuộc loại nào? | ☑ User-specific <br>☐ Domain-specific <br>☐ Real-time <br>☑ Human-judgment <br>☐ Khác: ___ |

**Có marginal value không?**
**CÓ.** Rất lớn. Các model foundational (như Gemini) dù thông minh đến đâu cũng không thể biết được ông "Hùng" trong lịch sử chuyển khoản là chủ nhà hay bạn nhậu của user. Chỉ có MoMo, thông qua việc thu thập **User-specific Data** (từ thao tác user tự sửa lỗi AI), mới có được lớp dữ liệu thói quen này. Đây chính là lợi thế cạnh tranh độc quyền (Moat) mà các đối thủ không thể có được.

