# Bài 7: Cảm biến dò line TCRT5000 với Arduino Nano

## Mục tiêu bài học

Sau bài này, bạn có thể:

- Đọc năm kênh digital của module dò line.
- Xác định mức logic trên line/nền.
- Tính vị trí line trước khi ghép điều khiển motor.

**Trước khi bắt đầu:** Đọc khoảng cách HC-SR04 — [mở bài trước](06-hc-sr04.md). Mỗi mã chạy thử là một sketch độc lập; Upload sẽ thay chương trình đang chạy. Giữ bản mã robot gốc để nạp lại sau khi học.

## 1. Nguyên lý và kiến thức cần biết

TCRT5000 gồm LED hồng ngoại và phần thu phản xạ. Module dò line thường bổ sung mạch so sánh để tạo đầu ra digital; cần phân biệt cảm biến rời với module 5 kênh của robot. Độ phản xạ phụ thuộc nền, line, độ cao và ánh sáng. Xem [datasheet cảm biến Vishay](https://www.vishay.com/docs/83760/tcrt5000.pdf).

Bộ mã robot nhận LOW là thấy line. Không kết luận mọi module đều cùng mức: đo trên nền/line và xác nhận trước.

## 2. Chuẩn bị, bảng chân và đấu nối

| Module | Chân | Vị trí theo mã robot |
| --- | --- | --- |
| OUT1 | 8 | Trái ngoài |
| OUT2 | 9 | Trái trong |
| OUT3 | 10 | Giữa |
| OUT4 | 11 | Phải trong |
| OUT5 | 12 | Phải ngoài |

Cấp VCC theo module, nối GND chung, đặt đúng chiều trái/phải. Tháo đường IN1/IN2 của driver khỏi D0/D1 trong các bài dùng Serial. Chỉ ngắt nguồn động cơ chưa loại bỏ xung đột tín hiệu trên D0/D1. Ngắt motor trong bài đọc tín hiệu; không để xe tự chạy khi hiệu chỉnh module.

## 3. Mã chạy thử hoàn chỉnh

Tạo sketch riêng có tên thư mục trùng tên tệp `.ino`, chép toàn bộ mã sau, chọn đúng board/COM rồi Verify và Upload:

```cpp
const int S[5] = {8, 9, 10, 11, 12};
const int W[5] = {-2, -1, 0, 1, 2};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) pinMode(S[i], INPUT);
}

void loop() {
  int tong = 0, soKenh = 0;
  for (int i = 0; i < 5; i++) {
    bool thayLine = digitalRead(S[i]) == LOW;
    Serial.print(thayLine ? 1 : 0);
    Serial.print(' ');
    if (thayLine) { tong += W[i]; soKenh++; }
  }
  if (soKenh == 0) Serial.println("| mat line");
  else if (soKenh == 5) Serial.println("| toan bo tren line / giao lo");
  else {
    Serial.print("| vi tri: ");
    Serial.println((float)tong / soKenh);
  }
  delay(100);
}
```

## 4. Giải thích chương trình

Mỗi kênh được in 1 khi thấy line; đây là giá trị đã chuyển từ mức LOW, không phải điện áp logic gốc. Trọng số -2…2 biểu diễn trái tới phải, trung bình các kênh cho vị trí gần đúng. Không có kênh và cả năm kênh cần xử lý riêng; không coi giao lộ là luôn phải đi thẳng.

## 5. Chạy thử và kết quả mong đợi

Monitor 9600 baud: đưa line dưới từng mắt, chỉ vị trí tương ứng đổi thành 1; line ở giữa cho vị trí gần 0, phía trái âm, phía phải dương. Nếu hướng ngược, kiểm tra hướng module/bảng chân. Tài liệu bàn giao mô tả đèn kênh tắt trên line, sáng ngoài line; kiểm tra module thật.

## 6. Lỗi thường gặp

| Hiện tượng | Cách kiểm tra |
| --- | --- |
| Luôn cùng giá trị | Độ cao, nguồn, ngưỡng so sánh, line/nền |
| Thứ tự ngược | Hướng lắp và đầu OUT |
| Nhận sai màu | Kiểm tra LOW/HIGH bằng đo thực tế |
| ESP32 bị lỗi | Mức logic đầu ra module, GPIO34 không có kéo lên nội |

## 7. Bài tập thực hành

1. Ghi năm giá trị trên nền, line, giao lộ.
2. Viết luật: vị trí âm/dương/0 thì cần chỉnh hai nhóm motor thế nào; chưa cấp nguồn motor.
3. Khi ghép motor, thêm xử lý mất line và giới hạn thời gian thử; so với bộ mã bàn giao.

**Điều kiện học tiếp:** thực hiện được mục tiêu của bài và giải thích được kết quả quan sát.

[Bài trước](06-hc-sr04.md) · [Lộ trình](../index.md) · [Bài tiếp: Encoder](08-encoder.md)
