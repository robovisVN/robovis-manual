# Bài 7: Đọc cảm biến dò line 5 kênh

**Mục tiêu:** kiểm tra từng mắt cảm biến và biết đường line nằm dưới mắt nào. Đầu tiên đọc một mắt, sau đó đọc cả năm; bài này chưa cho xe tự chạy.

## Cảm biến dò line nhận biết gì?

Module có năm mắt nhìn xuống sàn. Mỗi mắt phát hồng ngoại và thu phần ánh sáng phản xạ. Nền và đường line phản xạ khác nhau; mạch trên module đổi sự khác nhau đó thành hai mức đầu ra.

TCRT5000 là tên loại phần tử cảm biến thường dùng trong module. Một **kênh** trong bài nghĩa là một mắt cùng một đầu ra OUT. Nano đọc từng OUT, còn chương trình quyết định nên điều chỉnh xe sang đâu.

Bạn cần nền và line có độ tương phản rõ. Ví dụ dễ thử là line tối trên nền sáng. Không đặt module quá cao rồi kết luận nó không phân biệt được màu.

## Trước khi làm

Đã dùng được Serial Monitor. Ngắt nguồn motor và tháo dây driver khỏi D0/D1 khi dùng USB/Serial. Giữ module ở tư thế giống khi gắn dưới xe; chuẩn bị một đoạn line và nền sáng.

## Bước 1. Đối chiếu năm đầu ra

| Đầu ra | Chân Nano | Vị trí mà mã robot coi là |
| --- | --- | --- |
| OUT1 | D8 | Trái ngoài |
| OUT2 | D9 | Trái trong |
| OUT3 | D10 | Giữa |
| OUT4 | D11 | Phải trong |
| OUT5 | D12 | Phải ngoài |

Cấp VCC theo module, nối GND chung Nano. Trái/phải tính theo hướng xe tiến. Khi xoay module hoặc đảo thứ tự dây, bảng vị trí có thể bị ngược; bạn sẽ kiểm tra từng mắt ở bước sau, không chỉ dựa vào nhãn OUT.

## Bước 2. Đọc riêng mắt giữa

Tạo sketch `NanoLineMotMat`, chép:

```cpp
void setup() {
  pinMode(10, INPUT);
  Serial.begin(9600);
}

void loop() {
  int trangThai = digitalRead(10);
  Serial.println(trangThai);
  delay(200);
}
```

Upload, mở Monitor **9600 baud**. `INPUT` cho chân D10 nhận tín hiệu; `digitalRead(10)` đọc HIGH hoặc LOW. Khi in trực tiếp như trên, HIGH hiện là **1**, LOW hiện là **0**.

1. Đưa mắt giữa lên phần nền.
2. Ghi số thường thấy.
3. Đưa mắt giữa lên line.
4. Ghi số và kiểm tra có thay đổi không.

**Kết quả cần thấy:** hai vị trí cho hai trạng thái khác nhau. Với logic của bộ mã bàn giao, **line là LOW/0**. Nếu module của bạn cho mức ngược, ghi nhận mức thật và kiểm tra điều chỉnh/hướng dẫn module trước khi nạp mã dò line.

Đèn trên module chỉ giúp nhìn nhanh; dữ liệu Nano thực sự đọc mới cần khớp với chương trình. Tài liệu gốc mô tả đèn tắt trên line, sáng ngoài line; xác nhận điều này trên module đang dùng.

## Bước 3. Đọc cả năm mắt, chưa dùng công thức

Lưu sketch mới `NanoLineNamMat`, thay toàn bộ mã bằng:

```cpp
void setup() {
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.print(digitalRead(8));
  Serial.print(' ');
  Serial.print(digitalRead(9));
  Serial.print(' ');
  Serial.print(digitalRead(10));
  Serial.print(' ');
  Serial.print(digitalRead(11));
  Serial.print(' ');
  Serial.println(digitalRead(12));
  delay(200);
}
```

`print(' ')` in khoảng trắng để tách các cột. Chỉ lần cuối dùng `println()` để xuống dòng, nên mỗi dòng có năm giá trị theo D8, D9, D10, D11, D12.

Nếu line hẹp chỉ nằm dưới một mắt và LOW là line, ví dụ có thể thấy:

| Dòng hiển thị | Cách đọc |
| --- | --- |
| 1 1 0 1 1 | Mắt giữa thấy line |
| 0 1 1 1 1 | Mắt trái ngoài thấy line |
| 1 1 1 1 0 | Mắt phải ngoài thấy line |
| 1 1 1 1 1 | Chưa mắt nào thấy line |
| 0 0 0 0 0 | Tất cả cùng thấy vùng tối hoặc một vùng tương ứng logic line; chưa đủ để quyết định rẽ |

Đây là mẫu minh họa, không phải mọi line đều chỉ tác động một mắt. Line rộng có thể làm nhiều mắt cùng về 0.

## Bước 4. Xác nhận thứ tự trái/phải

Đưa một đoạn line dưới từng mắt, từ trái sang phải theo hướng xe tiến. Mỗi lần nhìn xem cột nào thay đổi.

**Kết quả cần thấy:** các cột thay đổi theo thứ tự D8 → D12. Nếu trái/phải bị đảo, chỉnh dây/hướng lắp khi đã tắt nguồn và đối chiếu [bảng chân](../08-su-dung-robot.md). Không sửa luật rẽ trước khi xác định đúng đầu vào.

## Bước 5. Từ tín hiệu đến quyết định của xe

Khi đọc đúng năm mắt, bạn có thể nghĩ về điều khiển:

| Vị trí line | Hành động cần xem xét |
| --- | --- |
| Gần giữa | Hai bên motor đi gần bằng nhau |
| Lệch trái | Chỉnh hướng để cụm cảm biến trở về line |
| Lệch phải | Chỉnh theo chiều ngược lại |
| Mất line | Dừng hoặc tìm lại theo luật đã thiết kế |
| Nhiều/tất cả mắt cùng thấy line | Xử lý riêng giao lộ/vùng rộng, không tự coi là lệnh đi thẳng |

Phần tự chạy cần cả mã motor và quy tắc xử lý mất line. Chạy sketch đọc cảm biến ở trên không làm bánh tự quay. Muốn dùng ngay chương trình dò line đã có, xem [hướng dẫn bộ mã bàn giao](../08-su-dung-robot.md).

## Thực hành thêm: biểu diễn line bằng một con số

Chưa cần viết mã mới. Gán vị trí năm mắt là **−2, −1, 0, 1, 2** từ trái sang phải. Khi một mắt thấy line, lấy vị trí của mắt đó. Nếu hai mắt trái trong/giữa thấy line, trung bình là `(−1 + 0) / 2 = −0,5`.

Số âm nghĩa line lệch trái, số dương lệch phải, 0 gần giữa. Chỉ lấy trung bình khi có mắt thấy line và chưa rơi vào trạng thái đặc biệt. Đây là cách chuẩn bị dữ liệu cho điều khiển bám line nâng cao.

## Nếu các cột không đổi

Kiểm tra theo thứ tự: VCC/GND, chân OUT, đúng sketch/COM, độ cao module, độ tương phản nền/line, rồi ngưỡng điều chỉnh nếu module có biến trở. Chỉ đổi một yếu tố rồi thử lại mắt giữa.

## Khi nào hoàn thành?

Bạn đọc được năm cột, xác nhận đúng thứ tự và mô tả được trạng thái ở giữa, lệch và mất line.

**Bài tập:** chụp/ghi ba dòng: line dưới mắt giữa, dưới phía trái, và không có line. Giải thích số 0/1 theo **mã đang in trực tiếp**, không nhầm với ví dụ khác đã đổi 1 thành “thấy line”.

[Bài trước](06-hc-sr04.md) · [Lộ trình](../index.md) · [Bài tiếp: Encoder](08-encoder.md)
