# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Output so sánh phản hồi của GPT-4o và GPT-4o-mini. **(KẾT QUẢ ĐƯỢC CHẠY TỪ TERMINAL)**

                                                === COMPARING MODELS ===
> gpt4o_response: Temperature controls the randomness of the output by adjusting the probability distribution, while top_p (nucleus sampling) narrows the output by selecting from the smallest set of tokens whose cumulative probability meets a threshold.

> mini_response: Temperature controls the randomness of the model's output by scaling the probabilities of different options, while top_p (nucleus sampling) limits the selection to a subset of the most probable options whose cumulative probability meets a specified threshold, ensuring a balance between creativity and coherence.

> gpt4o_latency: 2.7730590000282973

> mini_latency: 1.8598494000034407

> gpt4o_cost_estimate: 0.00043999999999999996

                                                === STREAMING CHATBOT ===
[Chatbot] Type 'quit' to end.

You: hello
AI: Hello! How can I assist you today?

You: what is the AI?
AI: AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are programmed to think, learn, and solve problems. AI systems can perform tasks that typically require human intelligence, such as understanding natural language, recognizing patterns, making decisions, and adapting to new information.

There are different types of AI, including:

1. **Narrow AI**: Also known as weak AI, this type is designed for a specific task, such as virtual assistants (like Siri or Alexa), recommendation systems, and image recognition.

2. **General AI**: Also referred to as strong AI, this is a theoretical form of AI that possesses the capability to understand, learn, and apply intelligence across a wide range of tasks, similar to a human being. As of now, general AI has not yet been achieved.

3. **Machine Learning**: This is a subset of AI that involves the use of algorithms and statistical models that enable computers to improve their performance on a task through experience.

4. **Deep Learning**: A more advanced subset of machine learning, deep learning uses neural networks with many layers to analyze various forms of data, such as images and audio.

AI is used in many applications today, including healthcare, finance, transportation, and entertainment, and continues to evolve rapidly. If you have any specific questions about AI or its applications, feel free to ask!

You: AI in SmartHome
AI: AI plays a significant role in the development and functionality of smart home technologies. Smart homes utilize interconnected devices and appliances that can be controlled remotely or programmed to automate tasks, often using AI to enhance their capabilities. Here are some key ways AI is applied in smart home environments:

1. **Smart Assistants**: Virtual assistants like Amazon's Alexa, Google Assistant, and Apple's Siri use AI to interpret voice commands, control smart devices, manage schedules, set reminders, and provide information. They can learn from user interactions to improve their responses and functionality over time.

2. **Home Automation**: AI allows for the automation of various household tasks. For example, smart thermostats (like Nest) can learn a user’s schedule and preferences to optimize heating and cooling, resulting in energy savings and increased comfort.

3. **Security Systems**: AI-powered security cameras and systems can recognize familiar faces, detect unusual activity, and send alerts to homeowners. They can distinguish between routine events (such as pets moving in and out of view) and potentially suspicious activity.

4. **Smart Lighting**: AI can be used to control smart lighting systems, adjusting brightness and color based on the time of day or user preferences. Some systems can learn user behaviors to automate lighting based on when rooms are occupied.

5. **Energy Management**: AI can help monitor and manage energy consumption in smart homes, identifying patterns and providing recommendations for energy savings. This can include controlling appliances and systems to operate during off-peak hours.

6. **Health Monitoring**: AI-enabled devices can monitor health metrics, such as heart rate and activity levels, and can be integrated with home systems to alert users or caregivers in case of emergencies.

7. **Smart Appliances**: Appliances like refrigerators, ovens, and washing machines can be equipped with AI to optimize their functions, such as adjusting cooking times, suggesting recipes, or running energy-efficient cycles based on usage patterns.

8. **Interconnectivity**: AI enhances the ability of different smart home devices to communicate with each other. For example, a smart security system can trigger lights to turn on when an intruder is detected, or the thermostat can adjust based on the presence of occupants detected by smart sensors.

9. **Personalization**: AI can analyze data from users' behaviors and preferences to offer personalized experiences, such as customizing music playlists, suggesting activities, or adjusting home settings according to the user's mood or needs.

10. **Predictive Maintenance**: Smart home devices can use AI to analyze performance data and predict when maintenance might be needed, alerting homeowners before issues become severe.

Overall, AI in smart homes enhances convenience, efficiency, security, and personalization, contributing to a more connected and responsive living environment. As technology continues to advance, we can expect even more innovative applications of AI in smart home solutions.

You: quit

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

When tem = 0.0
=> [Chatbot] Type 'quit' to end.

You: Tell me an interesting fact about Vietnam.
AI: One interesting fact about Vietnam is that it is home to the world's largest cave, Sơn Đoòng. Discovered in 2009 in Phong Nha-Kẻ Bàng National Park, this cave is over 5.5 miles (9 kilometers) long and features its own ecosystems, rivers, and even a localized weather system. The cave's massive chambers are large enough to house entire Boeing 747 airplanes, and it's thought to be millions of years old. Sơn Đoòng is a remarkable natural wonder that attracts explorers and adventure seekers from around the globe.

When tem = 0.5
=> [Chatbot] Type 'quit' to end.

You: Tell me an interesting fact about Vietnam.
AI: One interesting fact about Vietnam is that it is home to the world's largest cave, Sơn Đoòng. Discovered in 1991 and fully explored in 2009, this massive cave is located in Phong Nha-Kẻ Bàng National Park, and it features a unique ecosystem, including its own weather system, complete with clouds and vegetation. Sơn Đoòng is so large that it could fit a 40-story skyscraper inside, making it a remarkable natural wonder and a popular destination for adventure travelers.

When tem = 1.0
=> [Chatbot] Type 'quit' to end.

You: Tell me an interesting fact about Vietnam.
AI: One interesting fact about Vietnam is that it is home to the world's largest cave, Son Doong. Discovered in 2009, Son Doong is located in Phong Nha-Kẻ Bàng National Park. The cave is so vast that it has its own ecosystem, including a river, unique flora and fauna, and even a localized weather system. In some places, the cave is big enough to fit an entire skyscraper! Its stunning beauty and scale make it a remarkable natural wonder and a popular destination for adventurous travelers.

When tem = 1.5
=> [Chatbot] Type 'quit' to end.

You: Tell me an interesting fact about Vietnam.
AI: One interesting fact about Vietnam is that it is home to the world's largest cave, Sơn Đoòng, which is located in Phong Nha-Kẻ Bàng National Park. Discovered in 2009, Sơn Đoòng measures over 5.5 miles (9 kilometers) in length and features its own ecosystem, complete with a river and a jungle. The cave's unique climate and geography have created a variety of stalagmites, stalactites, and even a large opening that allows sunlight to pour in, supporting the growth of vegetation inside the cave. This remarkable natural wonder draws adventurers and explorers from around the globe.

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Theo như phần test 4 Tem trong các trường hợp, nhận được các câu trả lời, nhận thấy rằng Temperature thấp (0.0 - 0.5) cho câu trả lời ổn định, chính xác, ngắn gọn. Temperature cao (1.0 - 1.5) khiến AI dùng từ lạ và dễ nói sai (hallucination).

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Chọn 0.1 đến 0.2. Vì cần sự chính xác và đồng nhất; không được phép để AI tự ý "sáng tạo" thông tin sai lệch cho khách

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.
COST_PER_1K_OUTPUT_TOKENS = {
    "gpt-4o": 0.010,
    "gpt-4o-mini": 0.0006,
}

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> So token moi ngay   = 10.000 x 3 x 350 = 10.500.000 tokens
> Chi phi GPT-4o      = (10.500.000 / 1000) * 0.01 = 105
> Chi phi GPT-4o-mini = (10.500.000 / 1000) * 0.0006 = 6.3

[=>]GPT-4o gap 16.67 lan GPT-4o-mini

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> GPT-4o xứng đáng khi: Cần giải quyết các tác vụ đòi hỏi khả năng lập luận logic phức tạp, viết code chuyên sâu, hoặc phân tích các tài liệu học thuật có tính chất đa tầng nghĩa mà các model nhỏ không xử lý được.

> GPT-4o-mini tốt hơn khi: Thực hiện các tác vụ quy mô lớn nhưng đơn giản như phân loại ý định người dùng, tóm tắt các đoạn văn bản ngắn, hoặc đóng vai trò là tầng lọc dữ liệu thô ban đầu để tối ưu hóa chi phí vận hành.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming (Phục vụ Con Người):
Quan trọng nhất khi làm Chatbot tương tác trực tiếp. Nó giải quyết vấn đề tâm lý: người dùng thà thấy AI tạo từng chữ còn hơn là ngồi nhìn màn hình trắng xóa 10 giây. Nó biến sự chờ đợi thành trải nghiệm quan sát.

> Non-streaming (Phục vụ Hệ Thống):
Phù hợp nhất cho xử lý Backend hoặc trích xuất JSON. Máy móc không biết sốt ruột; nó cần nhận một cục dữ liệu hoàn chỉnh, sạch sẽ để lưu vào Database hoặc chạy logic tiếp theo. Nhận từng mảnh vụn (streaming) lúc này chỉ làm code thêm rối và dễ lỗi cấu trúc.


## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
