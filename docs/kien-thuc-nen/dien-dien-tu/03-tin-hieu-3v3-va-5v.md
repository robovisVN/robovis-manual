# Tín hiệu 3,3 V và 5 V: những điều cần biết khi đấu nối

**Mục tiêu:** quyết định một đường tín hiệu có thể nối trực tiếp hay cần chuyển mức điện áp.

**Cần biết trước:** [GND và nối chung mass](02-gnd-va-noi-chung-mass.md). Bài tập làm trên giấy, chưa cần cắm cảm biến.

## Điện áp nguồn khác điện áp tín hiệu

Một module cấp 5 V không có nghĩa tất cả chân tín hiệu đều chịu được 5 V. Bo có USB 5 V vẫn có thể dùng GPIO 3,3 V vì nguồn đi qua bộ ổn áp.

| Bo đang nói đến | Mức logic danh định | Điều cần nhớ |
| --- | --- | --- |
| Arduino Nano **classic ATmega328P chạy 5 V** | 5 V | Không suy ra cho Nano ESP32 hay toàn bộ họ Nano |
| ESP32 **classic** trong tài liệu ESP32 CH340 Type-C | 3,3 V | Không đưa trực tiếp tín hiệu 5 V vào GPIO |

**HIGH/LOW** là trạng thái logic cao/thấp. Chân vào nhận diện chúng theo ngưỡng trong datasheet (bảng thông số), không yêu cầu điện áp đúng tuyệt đối 0 V hoặc điện áp nguồn. Vùng giữa các ngưỡng có thể không được xác định chắc chắn.

## Kiểm tra cả hai chiều

1. **5 V → 3,3 V:** kiểm tra điện áp đầu ra lớn nhất và giới hạn đầu vào. GPIO ESP32 classic không phải đầu vào chịu 5 V; cần mạch chuyển mức phù hợp.
2. **3,3 V → 5 V:** không tự coi là luôn hoạt động. Điện áp đầu ra HIGH thấp nhất phải đáp ứng ngưỡng HIGH tối thiểu của bên nhận, với cùng tham chiếu GND.
3. **Đường hai chiều:** chọn bộ chuyển mức theo kiểu giao tiếp và tốc độ; mạch dùng cho I2C không mặc nhiên phù hợp tín hiệu push-pull. *Push-pull* là đầu ra chủ động kéo lên và kéo xuống; I2C là giao tiếp thường dùng các đường được kéo lên bằng điện trở.

`VIH` là ngưỡng vào mức cao tối thiểu; `VIL` là ngưỡng vào mức thấp tối đa. Giới hạn điện áp chịu được và ngưỡng nhận logic là hai kiểm tra riêng. Xem [hướng dẫn chuyển mức của Texas Instruments](https://www.ti.com/lit/ml/scyb018h/scyb018h.pdf).

## Ví dụ tính cầu chia áp một chiều

Cầu chia áp gồm hai điện trở nối tiếp. Khi đầu nhận có trở kháng cao (ít lấy dòng), điện áp tại điểm giữa xấp xỉ:

`Vout = Vin × R2 / (R1 + R2)`.

```text
Tín hiệu vào -- R1 --+-- Tín hiệu ra tới đầu vào
                    |
                    R2
                    |
                   GND
```

Giả sử tín hiệu vào được giới hạn **tối đa 5,0 V**, R1 = 10 kΩ và R2 = 15 kΩ, kết quả lý tưởng là `5 × 15 / 25 = 3,0 V`. Đây là ví dụ tính; thiết kế thật phải kiểm tra sai số điện trở, dải điện áp đầu vào, ngưỡng HIGH bên nhận và tốc độ tín hiệu. Cặp điện trở này không phải lựa chọn mặc định cho mọi giao tiếp.

Cầu chia áp **không phải nguồn 3,3 V để cấp cho bo**, không nâng điện áp và không thay bộ chuyển mức hai chiều. Với cảm biến cụ thể, theo mạch giao tiếp trong tài liệu sản phẩm, chẳng hạn [HC-SR04 với ESP32](../../robot-esp32/bai-giang/06-hc-sr04.md).

## Thực hành nhỏ

Phân loại ba trường hợp:

- Cảm biến có đầu ra push-pull 5 V → GPIO ESP32 classic: cần chuyển mức, không nối trực tiếp.
- Đầu ra 3,3 V → thiết bị nguồn 5 V, chưa biết `VIH`: chưa đủ thông tin để quyết định.
- Module I2C có điện trở kéo lên 5 V → ESP32: cần xử lý cả mức kéo lên và chuyển mức theo sơ đồ; không chỉ đổi dây VCC rồi giữ mọi kết nối khác.

**Kết quả mong đợi:** hỏi về kiểu đầu ra, ngưỡng logic và GND trước khi nối dây, thay vì chỉ nhìn nhãn nguồn.

## Lỗi thường gặp

- Dùng một điện trở nối tiếp và coi đó là bộ chuyển 5 V xuống 3,3 V cho mọi trường hợp.
- Tín hiệu “vẫn đọc được” rồi kết luận không vượt giới hạn điện: mạch vẫn có thể bị hỏng.
- Áp dụng sơ đồ Nano classic 5 V sang bo ESP32 có tên chân tương tự.

Thông số bo: [Arduino Nano classic](https://docs.arduino.cc/hardware/nano/) và [ESP32 datasheet, mục DC Characteristics](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf).

[← GND và nối chung mass](02-gnd-va-noi-chung-mass.md) · [Tiếp: Biến, kiểu dữ liệu và toán tử →](../lap-trinh/01-bien-kieu-du-lieu-toan-tu.md)
