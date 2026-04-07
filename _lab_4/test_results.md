# Lab 4 - Xây dựng AI Agent đầu tiên với Langgraph

- **Student Name**: Nguyen Thi Thu Hien
- **Student ID**: 2A202600212
- **Date**: April 7, 2026

---

# Test 1 - Direct Answer (Không cần tool)
- User: "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu"
- Kỳ vọng: Agent chào hỏi, hỏi thêm về sở thích/ngân sách/thời gian. Không gọi tool nào.

> Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu

TravelBuddy đang suy nghĩ...

>TravelBuddy: Xin chào! Rất vui được đồng hành cùng bạn trong kế hoạch du lịch lần này.

Để mình có thể tư vấn tốt hơn, bạn có thể chia sẻ một chút về sở thích của mình không? Bạn thích biển, núi hay khám phá văn hóa? Và ngân sách hoặc khoảng thời gian bạn dự định đi là bao nhiêu? 

---

# Test 2 - Single Tool Call
- User: "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"
- Kỳ vọng: Gọi search_flights("Hà Nội", "Đà Nẵng"), liệt kê 4 chuyến bay

> Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...

Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})

> TravelBuddy: Dưới đây là danh sách các chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines**
   - Thời gian: 06:00 - 07:20
   - Hạng: Economy
   - Giá: **1.450.000đ**

2. **Vietnam Airlines**
   - Thời gian: 14:00 - 15:20
   - Hạng: Business
   - Giá: **2.800.000đ**

3. **VietJet Air**
   - Thời gian: 08:30 - 09:50
   - Hạng: Economy
   - Giá: **890.000đ**

4. **Bamboo Airways**
   - Thời gian: 11:00 - 12:20
   - Hạng: Economy
   - Giá: **1.200.000đ**

Nếu bạn cần thêm thông tin hoặc muốn đặt vé, hãy cho mình biết nhé!
---

# Test 3 - Multi-Step Tool Chaining
- User: "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp tôi!"
- Kỳ vọng: Agent phải tự chuỗi nhiều bước:
1. search_flights -> tìm giá vé rẻ nhất
2. search_hotels -> gợi ý trong tầm giá
3. calculate_budget(5000000, "vé_bay:1100000, khách_sạn:...") -> tính còn lại
- Rồi tổng hợp thành gợi ý hoàn chỉnh với bảng chi phí.

> Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp tôi!

TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})

> TravelBuddy: Dưới đây là kế hoạch du lịch của bạn từ Hà Nội đi Phú Quốc trong 2 đêm với ngân sách 5 triệu đồng:

### 1. Vé máy bay
- **Vietnam Airlines**
  - Thời gian: 07:00 - 09:15
  - Hạng: Economy
  - Giá: **2.100.000đ**

- **VietJet Air**
  - Thời gian: 10:00 - 12:15
  - Hạng: Economy
  - Giá: **1.350.000đ**

- **VietJet Air**
  - Thời gian: 16:00 - 18:15
  - Hạng: Economy
  - Giá: **1.100.000đ**

### 2. Khách sạn tại Phú Quốc
- **9Station Hostel (2 sao)**
  - Khu vực: Dương Đông
  - Rating: 4.5
  - Giá: **200.000đ/đêm**

- **Sol by Meliá (4 sao)**
  - Khu vực: Bãi Trường
  - Rating: 4.2
  - Giá: **1.500.000đ/đêm**

- **Lahana Resort (3 sao)**
  - Khu vực: Dương Đông
  - Rating: 4.0
  - Giá: **800.000đ/đêm**

### Tính toán ngân sách
- **Chi phí vé máy bay (từ Hà Nội đến Phú Quốc)**:
  - Chọn chuyến bay **VietJet Air** (1.100.000đ - để tiết kiệm).
- **Chi phí khách sạn**:
  - Chọn 9Station Hostel (200.000đ/đêm), tổng 2 đêm là 400.000đ.

### Tổng chi phí
- **Vé máy bay**: 1.100.000đ
- **Khách sạn**: 400.000đ
- **Tổng chi phí**: 1.500.000đ

### Ngân sách còn lại
- **Ngân sách ban đầu**: 5.000.000đ
- **Chi phí**: 1.500.000đ
- **Số tiền còn lại**: 3.500.000đ

Bạn còn dư 3.500.000đ để chi tiêu cho ăn uống, hoạt động vui chơi trong chuyến đi. Nếu bạn quyết định chuyến bay và khách sạn nào, hãy cho mình biết để giúp bạn đặt nhé!

---

# Test 4 - Missing Info / Clasification
- User: "Tôi muốn đặt khách sạn"
- Kỳ vọng: Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu?
- Không gọi tool vội

> Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...

> TravelBuddy: Chào bạn! Để giúp bạn tìm được khách sạn phù hợp, mình cần biết thêm một chút thông tin:

1. Bạn muốn đặt khách sạn ở thành phố nào?
2. Số đêm bạn dự định lưu trú là bao nhiêu?
3. Ngân sách mỗi đêm của bạn là khoảng bao nhiêu?

Hãy cho mình biết nhé!

---

# Test 5 - Guardrail / Refusual
- User: "giải giúp tôi bài tập lập trình Python về linked list"
- Kỳ vọng: Từ chối lịch sự, nói rằng chỉ hỗ trợ về du lịch.

>Bạn: giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...

> TravelBuddy: Xin lỗi, nhưng mình chỉ hỗ trợ các vấn đề liên quan đến du lịch như đặt phòng, vé máy bay hay lên kế hoạch du lịch. Nếu bạn cần thông tin hay hỗ trợ về du lịch, hãy cho mình biết nhé!

---

# Test 6 - Multi-turn Memory
- User: "Tôi muốn đi Đà Nẵng"
- Kỳ vọng: Agent phải hỏi lại

> Bạn: tôi muốn đi Đà Nẵng 

TravelBuddy đang suy nghĩ...

> TravelBuddy: Chào bạn!

Bạn có dự định đi Đà Nẵng vào thời gian nào? Bạn có ngân sách cụ thể và sở thích gì về hoạt động hay chỗ ở không? Như thế mình sẽ tìm được kế hoạch tốt nhất cho bạn!

> Bạn: tôi đi vào tháng 7, budget 10 triệu cho 2 người, tôi thích du lịch biển. Xuất phát từ Hà Nội

Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})

Gọi tool: search_hotels({'city': 'Đà Nẵng', 'max_price_per_night': 1500000})

Gọi tool: calculate_budget({'total_budget': 10000000, 'expenses': 'vé_máy_bay:1780000,khách_sạn:3500000'})

> TravelBuddy: Dưới đây là kế hoạch chi tiết cho chuyến đi Đà Nẵng của bạn:

### 1. Vé máy bay:
- **Vietnam Airlines**
  - Giờ bay: 06:00 - 07:20
  - Hạng: Economy
  - **Giá: 1.450.000đ** (chuyến đi)
- Hoặc bạn có thể chọn **VietJet Air**
  - Giá: 890.000đ (chuyến đi)

### 2. Khách sạn:
Mình đã tìm được một số khách sạn phù hợp với ngân sách:
- **Christina's Homestay** (2 sao) - An Thượng
  - Giá: 350.000đ/đêm
  - Rating: 4.7
- **Sala Danang Beach** (4 sao) - Mỹ Khê
  - Giá: 1.200.000đ/đêm
  - Rating: 4.3

### 3. Ngân sách tổng thể:
- **Tổng chi phí:**
  - Vé máy bay: 1.780.000đ (2 vé máy bay khứ hồi)
  - Khách sạn (5 đêm ở Christina's Homestay): 3.500.000đ
  - **Tổng chi: 5.280.000đ**

### 4. Ngân sách còn lại:
- **Ngân sách còn lại: 4.720.000đ**

Với số tiền còn lại, bạn có thể thưởng thức các món ăn hải sản tươi ngon, tham gia các hoạt động vui chơi tại bãi biển, thuê xe máy để khám phá Đà Nẵng hoặc tận hưởng các dịch vụ khác.

Bạn có muốn đặt vé máy bay hoặc khách sạn không? Hay cần thêm thông tin gì khác?

---

# Test 7 - Budget quá thấp
- User: "Đi Phú Quốc 3 ngày 2 đêm với 1 triệu được không?"
- Kỳ vọng: Không gọi tool ngay

>Bạn: Đi Phú Quốc 3 ngày 2 đêm với 1 triệu được không?                                       

TravelBuddy đang suy nghĩ...

> TravelBuddy: Với ngân sách 1 triệu đồng cho chuyến đi Phú Quốc 3 ngày 2 đêm, bao gồm vé máy bay, khách sạn và ăn uống, thì khá khó khăn.

Tổng chi phí cho vé máy bay và khách sạn đã rơi vào khoảng 1.500.000đ (vé máy bay khoảng 1.100.000đ và khách sạn 400.000đ). Chưa kể đến chi phí ăn uống và các hoạt động khác, ngân sách 1 triệu đồng sẽ không đủ.

Nếu bạn có thể tăng thêm ngân sách hoặc chấp nhận giảm thời gian lưu trú, có thể cân nhắc thuê phòng ở một số nơi khác hoặc tìm kiếm vé máy bay rẻ hơn.

Nếu bạn cần tư vấn thêm hoặc muốn tìm kiếm lựa chọn khác, hãy cho mình biết nhé!