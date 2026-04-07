## Context: Tôi là ai?

Tôi là **Hiền**, 23 tuổi, Sinh viên ngành Công nghệ thông tin ứng dụng, hiện đang thực hiện một số dự án nghiên cứu. Mỗi tuần tôi phải:

- Nghiên cứu & Thực nghiệm: Trực tiếp thiết kế hệ thống phần cứng (ESP32/Arduino) và thu thập dữ liệu từ các cảm biến (DHT11, MQ2, Gia tốc kế) cho dự án phát hiện té ngã.

- Xử lý dữ liệu & AI: Đọc và tổng hợp kiến thức từ các paper kỹ thuật để tối ưu hóa thuật toán Machine Learning, phục vụ cho việc làm đồ án và khóa luận tốt nghiệp.

- Báo cáo & Định hướng: Cập nhật tiến độ nghiên cứu kỹ thuật định kỳ

Bài toán tôi mang vào lab hôm nay đến từ chính công việc hàng ngày.

**Vì sao context này tốt cho lab?**
- Có actor rõ
- Có workflow thật
- Có pain lặp lại
- Có metric đo được
- Không quá rộng

# Phase 1 — SCAN (Cá nhân)



### List của tôi

| # | Lens | Bài toán |
|---|------|----------|
| 1 | Lặp lại | Mỗi sáng viết báo cáo tiến độ (Stand-up) trên Discord: Hôm qua đã hàn mạch/code gì, hôm nay làm gì tiếp theo. |
| 2 | Lặp lại | Viết Commit Message trên GitHub cho các thay đổi nhỏ khi fix lỗi sensor/thư viện ESP32 sao cho đúng quy chuẩn nhóm. |
| 3 | Tốn thời gian | Đọc và lọc hàng chục paper kỹ thuật (PDF) để tìm thông số so sánh (Accuracy/Recall) cho dự án Fall Detection. |
| 4 | Tốn thời gian | Tổng hợp thủ công các dòng dữ liệu lỗi từ Serial Monitor (Arduino IDE) sang Excel để phân loại nguyên nhân nhiễu cảm biến. |
| 5 | AI tốt hơn | Gợi ý Task ưu tiên: Tự động nhắc nhở các task sắp đến deadline trên GitHub/Notion để không bị trễ tiến độ đồ án. |
| 6 | AI tốt hơn | Tóm tắt họp nhóm: AI tự ghi lại và tóm tắt các yêu cầu chỉnh sửa phần cứng/thuật toán sau mỗi buổi họp với giảng viên. |
| 7 | Pain từ thành viên | Conflict Code: Hai thành viên cùng sửa cấu hình chân Pin (GPIO) trên GitHub dẫn đến lỗi merge, mất thời gian cấu hình lại. |
| 8 | Pain từ thành viên | Code Review khó hiểu: Thành viên viết code xử lý Signal Processing quá phức tạp, người khác đọc không hiểu phải giải thích lại từ đầu. |
| 9 | Tốn thời gian | Debug môi trường: Khi chạy code báo lỗi thư viện (như ESP32 Core hay thư viện Sensor), phải copy lỗi lên Google tìm cách fix mất 15-20 phút. |
| 10 | Lặp lại | Chuyển đổi định dạng dữ liệu thô từ cảm biến (Raw data) sang định dạng chuẩn để đưa vào model Machine Learning để train. |

**Tổng:** 10 bài toán.


## Bước 1.2 — Nhóm: Quick Share (8 min)

Mỗi người đọc nhanh **top 3** cho nhóm nghe (~1 min/người). Chỉ nghe, không thảo luận sâu.

Ghi nhận: có pain nào trùng nhau giữa các thành viên không?

---

# Phase 2 — QUICK-ASSESS: Round 1 (40 min)

## Mục tiêu
Quick-pass qua top 3 bài toán. Mỗi cái 10 phút — buộc ra quyết định nhanh, không overthink.

## Bước 2.1 — Cá nhân: Viết 3 Quick Problem Cards (30 min)

Chọn **top 3** từ list → với mỗi cái, điền 1 **Quick Problem Card** (10 min/card).


### Quick Problem Card

```
┌─────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #01                     │
│                                             │
│ Bài toán (1 câu): Tự động ghi chú cuộc họp    │
│                                             │
│ Ai đang đau? Thành viên trong nhóm dự án.   │
│                                             │
│ Workflow hiện tại (3-5 bước):               │
│   1. Họp trên Discord → 2. Vừa nghe vừa gõ →   │
│ 3. Tổng hợp lại ý chính → 4. Gửi cho nhóm.   │
│                                             │
│ Bước nào tốn nhất? Tổng hợp & ghi chú  (⏱ 20 min/lần)   │
│                                            
│ AI có thể giúp ở bước nào? AI có thể tham gia voice channel, ghi âm, chuyển text và tự tạo danh sách task cho từng người sau buổi họp           │
│                                            
│ Đo thành công bằng gì? Có Meeting note sau 1ph họp xong     │
│           │
│                                             
│ Quick gut: □ No AI  □ Rule  □ LLM  [x] Agent │
└─────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #02                     │
│                                             │
│ Bài toán (1 câu): Quá tải thông tin từ đa kênh (Discord, Zalo, Mail, Mes,...)   │
│                                             │
│ Ai đang đau? Bản thân và các thành viên trong nhóm │
│                                             │
│ Workflow hiện tại (3-5 bước):               │
│   1. Check Discord → 2. Check Mail → 3. Check Zalo → 4. Check Mes       │
│                                             │
│ Bước nào tốn nhất? Phân loại và ưu tiên thông tin  (⏱ 30-45 min/ngày cho việc lọc thông tin)   │
│                                             │
│ AI có thể giúp ở bước nào? Một Agent tự đọc API ở các kênh, lọc những thông tin quan trọng và ưu tiên, cập nhật các đầu mục công việc lên Notion để dễ lắm bắt            │
│                                             │
│ Đo thành công bằng gì? giảm từ 45ph -> 15ph. giảm thời gian check app 65% │
│   VD: "Giảm từ 90 min → 30 min"            │
│                                             │
│ Quick gut: □ No AI  □ Rule  □ LLM  [x] Agent │
└─────────────────────────────────────────────┘
```
```
┌─────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #03                     │
│                                             │
│ Bài toán (1 câu): Tự động Debug & Cấu hình môi trường |
│                                             │
│ Ai đang đau? Chình tôi (Developer)   │
│                                             │
│ Workflow hiện tại (3-5 bước):               │
│   1. Code báo lỗi (Error Log) → 2. Copy lỗi     │
│ lên Google/Stack Overflow → 3. Thử sửa file   │
│ cấu hình/thư viện → 4. Chạy lại (thất bại) →  │
│ 5. Hỏi bạn bè/giảng viên.
│                                             │
│ Bước nào tốn nhất? Thử sai & Tìm thư viện lỗi  (⏱ 30-60 min/lần)   │
│                                             │
│ AI có thể giúp ở bước nào? Agent có quyền truye cập và File, tự đọc log lỗi, tự đề xuất dòng code cần sửa và tự cài lại thư viện thiếu            │
│                                             │
│ Đo thành công bằng gì? Dưới 5ph cho các lỗi phổ biến       │
│                                             │
│ Quick gut: □ No AI  □ Rule  □ LLM  [x] Agent │
└─────────────────────────────────────────────┘
```

## Bước 2.2 — Nhóm: Gallery Mini (10 min)



# Phase 3 — PITCH-CHALLENGE-VOTE (30 min)



## Bước 3.1 — Pitch + Challenge (20 min)
## Hiền pitch Card #03 cho nhóm

Hiền nói ngắn gọn:
> “Mỗi lần code ESP32 hoặc sensor bị lỗi, tôi mất 30–60 phút chỉ để đọc log, search Google và thử sai. Bước tốn nhất là tìm đúng nguyên nhân và cách fix. Nếu giải được bước này, có thể giảm phần lớn thời gian debug.”

---

## Nhóm challenge

| Câu challenge | Trả lời của Hiền |
|---------------|------------------|
| “Rule/script đủ chưa? Có thật sự cần AI không?” | “Với lỗi đơn giản thì script có thể check được. Nhưng phần lớn lỗi liên quan đến nhiều thư viện, config khác nhau — cần hiểu context và đề xuất cách sửa → cần LLM/Agent.” |
| “Ngoài bạn, ai đau nữa? Bao nhiêu người?” | “Hầu như tất cả sinh viên làm IoT/Embedded đều gặp. Trong nhóm có 3–4 người, ai cũng từng mất hàng chục phút cho 1 lỗi.” |
| “Metric đo được không? Có số cụ thể chưa?” | “Có — từ 30–60 phút/lỗi xuống dưới 5–10 phút cho các lỗi phổ biến.” |

---

## Vote kết quả
Sau khi cả nhóm pitch xong: **4/5 phiếu cho Card #03**.

---

## Cards bị loại

| Card bị loại | Lý do |
|--------------|-------|
| #01 — Tự động ghi chú họp | Bài toán có giá trị nhưng rào cản kỹ thuật cao (speech-to-text, nhận diện người nói), khó làm tốt trong scope lab |
| #02 — Lọc thông tin đa kênh | Phụ thuộc API (Zalo, Messenger), khó triển khai thực tế, scope rộng và thiếu feasibility |

---

## Vì sao phần này quan trọng trong rubric

Đây là phần **NO-AI**, giúp phân biệt rõ:

- ai hiểu bài toán thật
- ai chỉ nghĩ ý tưởng “cho có”

---

**[INDIVIDUAL SIGNAL]**
Một học viên được đánh giá tốt khi:
- pitch rõ: problem → workflow → bottleneck → metric
- trả lời challenge thẳng, không né
- sẵn sàng bỏ card nếu không khả thi

---

## Bước 3.2 — Vote + Kill Round (10 min)


| Card bị loại | Lý do |
|--------------|-------|
| 01| Rào cản kỹ thuật. Việc xử lý âm thanh thời gian thực và phân biệt người nói trên Discord cực kỳ phức tạp, dễ lỗi kết nối hơn là ngồi tự ghi chép. |
| 02| Quyền riêng tư & API. Zalo và Messenger rất khó kết nối API cá nhân. Bạn sẽ mất thời gian "xin quyền" hoặc lách luật hơn là thực sự dùng AI để lọc tin.|
| | |

**Card được chọn:** Tự động Debug & Cấu hình môi trường

**Vì sao chọn:** 
- Trúng "nỗi đau" kinh niên: Giải quyết vấn đề tốn thời gian nhất của dân IoT/Embedded là lỗi thư viện và xung đột môi trường (giảm từ 60 phút xuống 5 phút).

- Nâng tầm kỹ thuật: Thay vì chỉ dùng AI để "hỏi - đáp", việc xây dựng AI Agent có quyền đọc file và sửa code là một bước tiến đột phá, rất ấn tượng cho đồ án CNTT ứng dụng.

- Giá trị thực tế cao: Công cụ này hỗ trợ trực tiếp và lặp lại hàng ngày trong quá trình bạn thực nghiệm với ESP32/Arduino, giúp giữ mạch tập trung cho việc nghiên cứu thuật toán chính.

---