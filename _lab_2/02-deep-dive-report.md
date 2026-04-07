## Context: Tôi là ai?

Tôi là **Hiền**, 23 tuổi, Sinh viên ngành Công nghệ thông tin ứng dụng, hiện đang thực hiện một số dự án nghiên cứu. Mỗi tuần tôi phải:

- Nghiên cứu & Thực nghiệm: Trực tiếp thiết kế hệ thống phần cứng (ESP32/Arduino) và thu thập dữ liệu từ các cảm biến (DHT11, MQ2, Gia tốc kế) cho dự án phát hiện té ngã.

- Xử lý dữ liệu & AI: Đọc và tổng hợp kiến thức từ các paper kỹ thuật để tối ưu hóa thuật toán Machine Learning, phục vụ cho việc làm đồ án và khóa luận tốt nghiệp.

- Báo cáo & Định hướng: Cập nhật tiến độ nghiên cứu kỹ thuật định kỳ

**Vì sao context này tốt cho lab?**
- Có actor rõ
- Có workflow thật
- Có pain lặp lại
- Có metric đo được
- Không quá rộng


# Phase 4 — DEEP DIVE:

---

## 4.1 — Current-State Workflow

```text
┌──────────────┐     ┌──────────────────┐     ┌───────────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2           │     │ Bước 3            │     │ Bước 4       │
│ Tìm paper    │     │ Mở abstract +    │     │ Đọc method /      │     │ Ghi chú      │
│ theo keyword │ ──→ │ intro để skim    │ ──→ │ experiment để     │ ──→ │ các điểm     │
│              │     │                  │     │ đánh giá hướng    │     │ chính        │
│ Ai: Sinh viên│     │ Ai: Sinh viên    │     │ Ai: Sinh viên     │     │ Ai: Sinh viên│
│ ⏱ 5 min      │     │ ⏱ 10 min [BN]   │     │ ⏱ 15 min [BN]    │     │ ⏱ 10 min     │
│ In: keyword  │     │ In: PDF paper    │     │ In: paper body    │     │ In: skim thô │
│ Out: list URL│     │ Out: ấn tượng ban│     │ Out: đánh giá liên│     │ Out: bullet  │
│              │     │ đầu về paper     │     │ quan sơ bộ        │     │ thô          │
└──────────────┘     └──────────────────┘     └───────────────────┘     └──────────────┘
                                                                                │
                                                                                ▼
                                                                    ┌───────────────────┐
                                                                    │ Bước 5            │
                                                                    │ Quyết định: đọc   │
                                                                    │ sâu hay bỏ qua    │
                                                                    │                   │
                                                                    │ Ai: Sinh viên     │
                                                                    │ ⏱ 5 min           │
                                                                    │ In: ghi chú thô   │
                                                                    │ Out: go/no-go     │
                                                                    └───────────────────┘

[BN] = Bottleneck (Bước 2 + 3)
Tổng thời gian: 45 min/paper — trong đó 25 min là bottleneck (55%)
```

### Ghi chú bottleneck
- Bước 2–3 chiếm **55% tổng thời gian** cho 1 paper
- Hoàn toàn thủ công: phải đọc, hiểu ngữ cảnh, rồi tự suy ra độ liên quan
- Không có tiêu chí nhất quán → mỗi paper mất công như nhau, kể cả paper cuối cùng bị bỏ qua
- Với 5–10 paper/tuần, bottleneck này nhân lên thành **2–4 giờ/tuần thuần overhead**

---

## 4.2 — Problem Statement (6-field)

| Field | Nội dung |
|-------|----------|
| **Actor / Operator** | Sinh viên năm cuối thực hiện đồ án / khóa luận kỹ thuật, cần đọc 5–10 paper/tuần để xây dựng nền tảng lý thuyết và so sánh phương pháp |
| **Current Workflow** | Tìm paper theo keyword → skim abstract + intro → đọc method/experiment để đánh giá độ liên quan → ghi chú → quyết định đọc sâu. 5 bước, ~45 min/paper, hoàn toàn thủ công |
| **Bottleneck** | Bước skim (2–3) mất 20–25 min vì phải tự đọc, tự hiểu contribution, rồi suy ra xem paper này có giải đúng bài toán mình đang làm không — trong khi phần lớn kết quả là “không liên quan đủ để đọc sâu” |
| **Impact** | 25 min/paper × 7 paper/tuần = ~3 giờ/tuần dành cho quick-screening. Trong số đó, ước tính 60–70% paper bị loại sau khi đọc — tức phần lớn thời gian đọc là wasted. Kéo dài khi deadline khóa luận gần |
| **Success Metric** | Giảm thời gian quick-screen 1 paper từ 25 min xuống dưới 8 min. Tỉ lệ “đọc nhầm” (đọc sâu rồi mới biết không liên quan) giảm từ ~40% xuống dưới 10% |
| **Operational Boundary** | AI được phép tóm tắt, phân loại, và chỉ ra phần nên đọc sâu. AI không được kết luận thay người dùng rằng paper “tốt” hay “xấu” cho đề tài — quyết định cuối thuộc về sinh viên. AI không hallucinate nội dung không có trong paper |

### Sub-goals Decomposition

**TRƯỚC khi dùng AI**
- Sinh viên cần có sẵn context: đề tài, câu hỏi nghiên cứu, các keyword chính của project
- Cần chuẩn bị prompt template mô tả đúng bài toán đang làm để AI có thể so sánh

**TRONG khi dùng AI**
- Sinh viên review AI summary để bắt lỗi hoặc bổ sung ngữ cảnh mà AI bỏ qua
- Sinh viên tự quyết định go/no-go sau khi đọc AI output

### Metrics

| Loại | Metric | Ngưỡng |
|------|--------|--------|
| Efficiency | Thời gian quick-screen 1 paper | 25 min → dưới 8 min |
| Precision | Tỉ lệ paper “đọc sâu nhầm” (không liên quan) | 40% → dưới 10% |
| Quality | Sinh viên vẫn tự đánh giá được paper sau khi dùng AI | Không giảm khả năng critical reading |

---

## 4.3 — Research

### Existing Solutions

| Công cụ | Điểm mạnh | Điểm yếu |
|---------|-----------|----------|
| **Semantic Scholar / Connected Papers** | Tìm paper liên quan theo citation graph | Không tóm tắt nội dung theo bài toán cụ thể của người dùng |
| **Elicit.org** | AI extract claim, method, finding từ paper | Không biết context đề tài của người dùng → tóm tắt generic |
| **ChatGPT + paste abstract** | Có thể hỏi theo ngữ cảnh | Giới hạn context window, không đọc full PDF, cần người dùng tự paste |
| **SciSpace / Typeset** | Hỏi đáp trực tiếp trong PDF | Tốt cho đọc sâu, không tối ưu cho quick-screen hàng loạt |
| **Zotero + plugin GPT** | Tích hợp với reference manager | Cần setup phức tạp, không có relevance scoring theo đề tài |

### Khoảng trống quan sát được
- Các tool hiện có tóm tắt **nội dung paper** nhưng không **so sánh paper với bài toán cụ thể của người dùng**
- Không có tool nào cho ra được: “paper này giải vấn đề X, bạn đang làm vấn đề Y, điểm giao nhau là Z, nên đọc phần A trước”
- Tức là: thiếu **context-aware relevance screening**, không phải thiếu summarization

### Case Study tham khảo
- **Elicit.org research workflow**: researcher cung cấp research question → AI extract structured data từ 50+ paper → researcher filter theo dimension cụ thể. Kết quả: giảm 70% thời gian literature review giai đoạn đầu
- **Bài học**: hiệu quả đến từ việc AI biết **câu hỏi của người dùng**, không chỉ tóm tắt paper

### Quick Poll (informal)
- 3/4 sinh viên khóa luận nói bước skim paper là bước “tốn nhất mà ít thấy kết quả nhất”
- 2/4 đã thử dùng ChatGPT paste abstract — giúp được, nhưng phải tự viết prompt lại mỗi lần, không nhất quán

---

## 4.4 — Future-State Flow + AI Fit

### AI Fit Check

Bài toán nằm ở:
**Complexity thấp + Ambiguity trung bình → LLM Feature** (không phải Agent)

- Input có cấu trúc: PDF paper + context đề tài của sinh viên
- Output mong muốn: bản tóm tắt có định hướng, không phải quyết định tự động
- Không cần AI lặp nhiều vòng, không cần planning — chỉ cần 1 lần generate có chất lượng cao

### AI Suitability Check

| Tiêu chí | Phù hợp? | Ghi chú |
|----------|----------|---------|
| Cần hiểu ngôn ngữ tự nhiên (paper viết bằng prose) | Phù hợp | LLM mạnh ở đây |
| Output cần flexible theo từng paper | Phù hợp | Không có template cứng nào đủ |
| Cần nhất quán về format | Một phần | Cần prompt engineering tốt để output có cấu trúc ổn định |
| Có thể verify output dễ không? | Phù hợp | Sinh viên đọc qua abstract là biết AI summary có đúng không |
| Hậu quả nếu AI sai? | Thấp | Tệ nhất là đọc nhầm 1 paper — không nguy hiểm |

### Future-State Flow

```text
┌─────────────────────┐     ┌──────────────────────────────────────┐
│ Bước 1              │     │ Bước 2 🔵 (AI)                       │
│ Sinh viên cung cấp: │ ──→ │ AI đọc paper + so sánh với context   │
│ - PDF paper         │     │ đề tài → output structured summary:  │
│ - Mô tả đề tài /    │     │                                      │
│   câu hỏi NC        │     │  • Contribution chính của paper      │
│                     │     │  • Paper giải bài toán gì?           │
│ Ai: Sinh viên       │     │  • Điểm giao với đề tài của bạn      │
│ ⏱ 2 min             │     │  • Điểm khác biệt / không liên quan  │
│                     │     │  • Phần nên đọc sâu trước (nếu có)  │
│                     │     │                                      │
│                     │     │ Ai: AI (LLM)                         │
│                     │     │ ⏱ 1–2 min                            │
└─────────────────────┘     └──────────────────────────────────────┘
                                            │
                                            ▼
                            ┌──────────────────────────────────────┐
                            │ Bước 3 🟢 (Sinh viên)                │
                            │ Đọc AI summary (~3 min)              │
                            │ → Quyết định go / no-go              │
                            │ → Nếu go: đọc đúng phần AI chỉ ra   │
                            │                                      │
                            │ 🔴 Boundary: sinh viên phải tự       │
                            │ quyết định — AI không được kết luận  │
                            │ “đây là paper tốt cho đề tài bạn”   │
                            │                                      │
                            │ ⏱ 3–5 min                            │
                            └──────────────────────────────────────┘

➡️ Fallback: AI summary quá generic hoặc sai → sinh viên đọc abstract tự skim như cũ
⏱ Tổng thời gian mới: ~7 min/paper (so với 25 min hiện tại)
```

### AI Fit Decision
**Chốt: LLM Feature — không phải Agent**

**Vì sao không phải Agent**
1. Không cần AI tự tìm paper, tự duyệt nhiều bước liên tiếp
2. Input-output rõ ràng: 1 paper + 1 context → 1 structured summary
3. Không cần planning động hay tool-use phức tạp — 1 lần generate là đủ

**Vì sao không phải Rule/Template**
- Nội dung paper quá đa dạng về cách diễn đạt, cấu trúc, domain
- Rule cứng không thể extract “điểm giao với đề tài” mà không có ngữ nghĩa

### Underspecification Check

| Điều chưa rõ | Hậu quả | Cách tìm ra |
|---|---|---|
| “Context đề tài” cần mô tả chi tiết đến đâu? | Prompt quá ngắn → AI summary generic, không khác gì Elicit | Thử nghiệm với 3–5 cách mô tả khác nhau, so sánh chất lượng output |
| AI có đọc được full PDF hay chỉ abstract? | Nếu chỉ đọc abstract → bỏ sót method/experiment quan trọng | Test với các LLM hỗ trợ long-context (Gemini 1.5, Claude) |
| Sinh viên có trust AI summary không? | Nếu không trust → vẫn tự đọc lại → không tiết kiệm thời gian | Pilot 2 tuần, đo xem có thật sự bỏ bước skim hay không |
| Format output nên cố định hay flexible? | Nếu không nhất quán → khó so sánh nhiều paper với nhau | Dùng structured prompt với output schema rõ ràng |

---

# Phase 5 — EVALUATE

## 5.1 — AI Readiness Checklist

| # | Câu hỏi | Kết quả | Ghi chú |
|---|---------|---------|---------|
| 1 | Có data/input đủ chất lượng không? | ✅ Yes | Input là PDF paper thực tế + mô tả đề tài của sinh viên — không cần dataset riêng, LLM đã được huấn luyện trên văn bản học thuật |
| 2 | Có metric đo được rõ ràng không? | ✅ Yes | Metric 1: thời gian quick-screen 1 paper (25 min → dưới 8 min). Metric 2: tỉ lệ “đọc sâu nhầm” (40% → dưới 10%) |
| 3 | Sai thì hậu quả có chấp nhận được không? | ✅ Yes | Tệ nhất là bỏ sót 1 paper liên quan hoặc đọc nhầm 1 paper — không ảnh hưởng đến hệ thống, không mất dữ liệu, sinh viên luôn là người quyết định cuối |
| 4 | User sẵn sàng thay đổi workflow để dùng AI không? | ✅ Yes | Sinh viên đang chủ động tìm cách giảm overhead — động lực cao; workflow mới chỉ thêm bước “mô tả đề tài 1 lần” thay vì thay đổi toàn bộ quy trình |
| 5 | Có thể verify output của AI không? | ✅ Yes | Sinh viên đọc abstract gốc trong 2 min là biết AI summary có đúng không — vòng feedback ngắn, không cần chuyên gia ngoài |
| 6 | Có resource để xây và maintain không? | ⚠️ Not Yet | Chỉ cần API key LLM (Claude/Gemini) + prompt template — không cần dev phức tạp; nhưng cần thời gian để calibrate prompt cho từng domain |

**Tổng kết: 5/6 điều kiện sẵn sàng.** Điều kiện còn thiếu (resource) không phải là blockers lớn — có thể bắt đầu pilot thủ công với Claude/ChatGPT trực tiếp trước khi wrap thành tool.

---

## 5.2 — Assumption Map

Các giả định đang được mang vào quyết định này — nếu giả định sai thì kế hoạch thay đổi:

| Giả định | Rủi ro nếu sai | Cách kiểm tra |
|----------|---------------|---------------|
| LLM có thể đọc full PDF và extract nội dung kỹ thuật chính xác | AI chỉ đọc được metadata / abstract → summary generic, không khác Elicit | Test 5 paper bằng Claude + Gemini 1.5 với PDF dài > 20 trang, so sánh output với tóm tắt tay |
| Sinh viên mô tả được đề tài đủ rõ để AI so sánh | Context quá mơ hồ → AI không xác định được “điểm giao” → kết quả vô nghĩa | Thử 3 cách mô tả context (ngắn / trung bình / chi tiết), đo sự khác biệt chất lượng output |
| Sinh viên trust AI summary đủ để bỏ bước skim thủ công | Nếu vẫn tự đọc lại → không tiết kiệm thời gian — chỉ thêm bước | Pilot 2 tuần, theo dõi xem sinh viên có thật sự skip skim không sau khi đọc AI output |
| Format output nhất quán đủ để so sánh nhiều paper | Nếu mỗi paper ra format khác → không build được mental model so sánh | Dùng structured output schema cứng trong prompt; đo tỉ lệ output conform đúng schema |

---

## 5.3 — Optimization Check

### Lợi ích kỳ vọng

| Loại | Trước | Sau | Delta |
|------|-------|-----|-------|
| Thời gian quick-screen 1 paper | ~25 min | ~7 min | **-72%** |
| Thời gian/tuần (7 paper) | ~175 min | ~50 min | **Tiết kiệm ~2 giờ/tuần** |
| Tỉ lệ “đọc sâu nhầm” | ~40% | < 10% | **-75% lãng phí** |
| Sự nhất quán đánh giá paper | Không nhất quán (phụ thuộc trạng thái người đọc) | Nhất quán theo schema cố định | **Cải thiện so sánh chéo** |

### Rủi ro nếu dùng AI không đúng cách

| Rủi ro | Khả năng xảy ra | Hậu quả | Biện pháp giảm thiểu |
|--------|----------------|---------|----------------------|
| AI hallucinate — thêm nội dung không có trong paper | Trung bình | Sinh viên tin vào claim sai → dùng trong báo cáo/luận văn | Boundary rõ: AI chỉ được paraphrase, không được suy diễn; sinh viên verify claim quan trọng với bản gốc |
| AI summary quá generic vì context đề tài không đủ | Cao (nếu prompt yếu) | Không biết paper có liên quan không → phải tự đọc lại như cũ | Chuẩn bị sẵn prompt template với context rõ; không dùng prompt ad-hoc |
| Sinh viên bỏ hoàn toàn bước đọc tay → mất critical reading | Thấp | Giảm khả năng phân tích — ảnh hưởng đến chất lượng luận văn | AI chỉ là filter, không replace đọc sâu; quy trình yêu cầu sinh viên vẫn đọc sâu paper “go” |
| Over-reliance: bỏ sót paper tốt bị AI đánh giá thấp | Thấp–Trung | Mất paper có giá trị cao | Định kỳ 2 tuần/lần: skim thủ công 3–5 paper AI đã “no-go” để calibrate lại |

---

## 5.4 — Quyết định

### ✅ Go — Pilot thủ công trong 2 tuần

**Scope của pilot:**
- Dùng Claude API / ChatGPT trực tiếp (không wrap thành tool)
- Chuẩn bị 1 prompt template cố định cho bài toán này
- Áp dụng cho **5 paper tiếp theo** mà sinh viên cần đọc trong đồ án
- Đo thời gian thực tế và tỉ lệ summary đúng sau mỗi lần

**Điều cần validate trong pilot:**

| # | Cần kiểm tra | Cách đo |
|---|-------------|---------|
| 1 | AI có đọc được full paper kỹ thuật không (không chỉ abstract)? | So sánh output khi input là abstract only vs full PDF |
| 2 | Prompt template nào cho output tốt nhất? | A/B test 2–3 version prompt, đánh giá bằng mắt |
| 3 | Thời gian thực tế của flow mới là bao nhiêu? | Bấm giờ từng bước trong 5 paper pilot |
| 4 | Sinh viên có trust output không (có bỏ bước skim không)? | Tự theo dõi hành vi trong 2 tuần |

---

## 5.5 — Justify

### Vì sao Go?

**1 — Rủi ro thấp, chi phí thử nghiệm gần bằng 0**
Pilot chỉ cần prompt template + API key — không cần code, không cần deploy. Nếu thất bại, chi phí là 30 phút viết prompt và 2 tuần thử nghiệm.

**2 — Problem đã được validate rõ**
Phase 3–4 đã xác nhận: bottleneck là skim (bước 2–3), chiếm 55% tổng thời gian và gây 40% “đọc nhầm”. Không phải assumption chưa kiểm chứng.

**3 — LLM đã được chứng minh làm tốt bài này**
Elicit.org, SciSpace, và các case study cho thấy LLM hoàn toàn xử lý được summarization + relevance extraction từ paper học thuật. Điểm thiếu duy nhất của các tool hiện có là **context-aware** — và đây là điểm chúng ta thêm vào qua prompt.

**4 — Boundary rõ ràng → AI không thay thế judgment của người dùng**
Quyết định go/no-go vẫn thuộc sinh viên. AI chỉ làm phần thu thập thông tin để sinh viên quyết định nhanh hơn — không vi phạm academic integrity, không có rủi ro nghiêm trọng.

---

## 5.6 — Exit Criteria & Fallback

### Pilot thành công nếu:
- Thời gian quick-screen ≤ 8 min/paper sau 5 lần thử
- Sinh viên bỏ được bước skim tay trong ít nhất 3/5 paper
- Không có trường hợp AI hallucinate claim quan trọng (kiểm tra bằng cách verify 1–2 claim ngẫu nhiên mỗi paper)

### Nếu pilot thất bại → Fallback

| Kịch bản thất bại | Fallback |
|-------------------|---------|
| AI không đọc được full PDF | Dùng text-extracted version (copy-paste section chính) thay vì upload PDF trực tiếp |
| Summary quá generic | Refine prompt — thêm ví dụ output mong muốn (few-shot prompting) |
| Sinh viên vẫn không trust → tự đọc lại | Dùng AI chỉ cho bước extract structured metadata (title, method, dataset, metric) — không yêu cầu relevance judgment |
| Tốn quá nhiều thời gian viết context | Viết sẵn context template 1 lần cho toàn bộ đồ án, reuse cho tất cả paper |

---

**[GROUP SIGNAL]**
Phase 5 tốt không phải khi mọi thứ đều “Yes, Go”. Phase 5 tốt là khi nhóm biết chính xác *điều gì cần kiểm tra* trong pilot, *tại sao* rủi ro hiện tại chấp nhận được, và *khi nào* thì quay lui — không phải lạc quan mù quáng.

---
