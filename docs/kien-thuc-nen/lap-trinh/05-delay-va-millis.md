# delay() và cách xử lý thời gian bằng millis()

**Mục tiêu:** thực hiện hai công việc theo hai chu kỳ mà không dùng `delay()` để chờ giữa các lượt kiểm tra.

**Cần biết trước:** [điều kiện](02-cau-lenh-dieu-kien.md), [vòng lặp](03-vong-lap.md), [hàm](04-ham-va-chia-chuong-trinh.md). Dùng bo rời Nano classic ATmega328P 5 V hoặc ESP32 classic 3,3 V, chỉ USB, Serial Monitor 9600 baud; chưa đấu cảm biến/động cơ.

## Chờ khác với kiểm tra đã đủ thời gian

`delay(1000)` chờ khoảng 1000 mili giây (1 giây) trước khi chạy lệnh kế tiếp trong luồng thực thi hiện tại. Trong lúc đó code của bạn không quay lại kiểm tra nút hay thực hiện nhánh tiếp theo. Điều này không có nghĩa mọi ngắt, PWM hay tác vụ hệ thống đều dừng. Xem [Arduino: delay()](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Functions/Time/delay.adoc).

`millis()` trả số mili giây từ khi chương trình bắt đầu, kiểu `unsigned long`. Ta ghi lại một mốc, sau đó kiểm tra **thời gian đã trôi qua**; nếu chưa đủ thì để `loop()` tiếp tục công việc khác. Đây là API Arduino, không phải hàm có sẵn của ngôn ngữ C++.

## Thực hành: hai chu kỳ trên Serial

```cpp
#include <Arduino.h>

const unsigned long CHU_KY_NHANH = 500UL;
const unsigned long CHU_KY_CHAM = 2000UL;
unsigned long mocNhanh = 0;
unsigned long mocCham = 0;

void setup() {
  Serial.begin(9600);
  unsigned long lucBatDau = millis();
  mocNhanh = lucBatDau;
  mocCham = lucBatDau;
}

void loop() {
  unsigned long hienTai = millis();

  if (hienTai - mocNhanh >= CHU_KY_NHANH) {
    mocNhanh = hienTai;
    Serial.println("Nhip 500 ms");
  }

  if (hienTai - mocCham >= CHU_KY_CHAM) {
    mocCham = hienTai;
    Serial.println("Nhip 2000 ms");
  }
}
```

Verify/Upload, mở Serial Monitor 9600. **Kết quả mong đợi:** dòng `Nhip 500 ms` xuất hiện khoảng hai lần mỗi giây; `Nhip 2000 ms` khoảng một lần mỗi hai giây. Quanh mốc 2 giây có thể thấy hai dòng gần nhau. Đây là chu kỳ gần đúng, không phải cam kết thời gian thực chính xác.

Hai `if` độc lập để cả hai công việc đều có cơ hội chạy. Nếu dùng `else if`, nhánh đầu đúng có thể khiến nhánh sau bị bỏ qua. `UL` ghi rõ hằng số kiểu `unsigned long`.

## Vì sao dùng phép trừ?

Trên các bo đang xét, bộ đếm `millis()` 32 bit quay về 0 sau khoảng 49,7 ngày. Phép trừ **hai giá trị không dấu cùng kiểu** vẫn tính đúng khoảng thời gian qua lần quay vòng, miễn khoảng cần xét nhỏ hơn một vòng đếm và chương trình kiểm tra đủ thường xuyên, không bỏ lỡ cả vòng. Tránh so sánh với `moc + chuKy` vì phép cộng có thể vượt phạm vi trước thời điểm mong đợi. Xem [Arduino: millis()](https://raw.githubusercontent.com/arduino/reference-en/master/Language/Functions/Time/millis.adoc).

`moc = hienTai` chọn chu kỳ tính từ lần thực hiện gần nhất; nếu code bị chậm, lịch có thể trôi. Bài này không cố chạy bù các lượt đã lỡ.

## Tự thực hành

Đổi `CHU_KY_NHANH` thành `250UL`; giữ nhánh chậm. Kỳ vọng dòng nhanh khoảng bốn lần mỗi giây, nhánh chậm vẫn khoảng hai giây một lần. Không cần chờ 49 ngày để thử bài học này.

## Lỗi thường gặp

- Lưu mốc bằng `int`: có thể mất dữ liệu thời gian.
- Khai báo lại mốc bên trong `loop()` và đặt về 0 mỗi lượt.
- Dùng `hienTai == moc + chuKy`: có thể bỏ lỡ đúng thời điểm bằng nhau.
- Thêm một `delay()` dài vào cuối `loop()`: vẫn làm mất cơ hội kiểm tra thường xuyên.
- Nghĩ dùng `millis()` là mọi thao tác đều không chặn: gửi Serial khi bộ đệm đầy hoặc hàm cảm biến chờ dữ liệu vẫn có thể làm chương trình chậm.

[← Hàm và chia chương trình](04-ham-va-chia-chuong-trinh.md) · [Tiếp: GPIO và điện trở kéo →](../vi-dieu-khien/01-gpio-va-dien-tro-keo.md)
