# Bài tập UX: phân tích sản phẩm AI thật

**Thời gian:** 40 phút | **Cá nhân** | **Output:** sketch giấy, nộp cuối bài

---

**Học viên:** Nguyễn Thị Thu Hiền

**Mã học viên:** 2A202600212

**Sản phẩm:** MoMo — Trợ thủ AI Moni

---

## PHẦN 1 — KHÁM PHÁ (Marketing vs. Thực tế)

* **Marketing hứa hẹn (Kỳ vọng):** Truyền thông MoMo định vị Moni là "Trợ lý tài chính cá nhân thấu hiểu bạn", quảng cáo tính năng "Tự động phân loại chi tiêu cực chuẩn không cần nhập tay", giúp quản lý ngân sách rảnh rang.
* **Trải nghiệm thực tế (Thực trạng):**
    * *Mượt ở đâu?* Rất mượt khi thanh toán hóa đơn đối tác tích hợp (Điện, Nước, CGV, Grab) -> AI tự động nhận diện chính xác 100% nhờ ID đối tác rõ ràng.
    * *Gãy ở đâu?* Cực kỳ bối rối với giao dịch chuyển khoản cá nhân (P2P). Với các nội dung mập mờ như "tien an", "ck", AI thường xuyên đoán bừa hoặc đẩy hết vào rổ "Chi tiêu khác", làm sai lệch hoàn toàn biểu đồ báo cáo tài chính cuối tháng.

---

## PHẦN 2 — PHÂN TÍCH 4 PATHS

Dùng framework 4 paths để mổ xẻ sản phẩm:

| Path (Tình huống) | Phân tích UX Hệ thống |
| :--- | :--- |
| **1. Khi AI Đúng (Happy)** | **User thấy gì:** Giao dịch trừ tiền xong sẽ lập tức hiện icon danh mục chuẩn (vd: Ăn uống). Biểu đồ ngân sách tự động nhích lên. <br>**Hệ thống confirm:** Bằng feedback thị giác (icon) tự động, không phiền user. |
| **2. Khi AI Không chắc (Uncertain)** | **Hệ thống xử lý (Clarification Path):** Khi user nhắn tin thiếu ngữ cảnh (VD: *"Moni ơi, ghi nhận khoản 500k lúc nãy nhé"* - không rõ giao dịch nào, tiền ra/vào), AI bắt buộc phải nhận diện được sự thiếu hụt thông tin này. Thay vì đoán bừa (Error) hay báo lỗi (Exit), AI chủ động hỏi lại để làm rõ: *"Bạn muốn ghi chép khoản 500k vừa chuyển cho Nguyễn Văn A lúc 14:00 đúng không? Thuộc danh mục gì nhỉ?"*. |
| **3. Khi AI Sai (Recovery)** | **User biết bằng cách nào:** Cuối tháng nhìn Báo cáo thấy mục "Mua sắm" tăng vọt do AI gom nhầm tiền "Trả nợ" vào. <br>**Sửa bằng cách nào:** UX hiện tại rất cồng kềnh. Bấm vào GD sai -> Mở chi tiết -> Bấm sửa -> Cuộn mỏi tay tìm danh mục đúng trong 1 list dài. |
| **4. Khi Mất tin (Exit/Bailout)** | **Có Exit không:** Có. Khi AI báo cáo sai bét hoặc chat mãi bot không hiểu lệnh, user có thể vào Cài đặt tắt tính năng "Tự động phân loại", hoặc thoát hẳn khung chat và bỏ luôn việc dùng AI để quản lý chi tiêu. |

**Nhận xét tự phân tích (Gap Marketing):**
* **Path tốt nhất:** Happy Path với dịch vụ tích hợp sẵn.
* **Path yếu nhất:** Path 3 (Sai/Recovery). UX sửa lỗi quá cồng kềnh tạo ra "ma sát" cao, khiến người dùng lười sửa. Điều này trực tiếp giết chết *Data Flywheel* vì AI không nhận được data feedback để khôn lên.
* **Gap Marketing vs Thực tế:** Marketing hứa hẹn một sự "thấu hiểu", nhưng thực tế AI chưa hiểu lóng tiếng Việt và thiếu cơ hội để học (do UX thiết kế thiếu vòng lặp phản hồi tốt).
