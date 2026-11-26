# Bài 7. Kết nối máy tính với robot

Trước khi xem dữ liệu LiDAR hoặc gửi lệnh cho robot, chúng ta cần một đường kết nối giữa robot và máy Ubuntu. Việc máy tính đã chọn được Wi-Fi mới là một phần của quá trình này, đặc biệt khi Ubuntu đang chạy trong VMware.

Trong bài, chúng ta sẽ lần theo đường kết nối, tìm địa chỉ IP của Ubuntu và dùng `ping` để kiểm tra liên lạc mạng trước khi chạy phần mềm robot.

**Mục tiêu:** biết Ubuntu có liên lạc được với robot hay chưa, trước khi chạy phần mềm điều khiển.

**Chuẩn bị:** robot ESP32 LiDAR/SLAM, Ubuntu đã mở và đã biết dùng Terminal. Bài này chỉ kiểm tra kết nối, chưa gửi lệnh chuyển động.

## 1. Wi-Fi và địa chỉ IP khác nhau thế nào?

Khi mở danh sách mạng, chúng ta dùng **tên Wi-Fi** để chọn mạng cần tham gia. Sau khi kết nối, các thiết bị sử dụng **địa chỉ IP** để tìm đến nhau trong mạng. Vì vậy, chọn đúng Wi-Fi và kiểm tra đúng IP là hai bước có liên quan nhưng cần thực hiện riêng.

Ví dụ của bộ robot hiện tại:

| Thông tin | Giá trị mặc định trong tài liệu ROBOVIS |
| --- | --- |
| Tên Wi-Fi robot | `ESP32_SLAM` hoặc `ESP SLAM`, tùy phiên bản |
| Mật khẩu Wi-Fi | `12345678` |
| Địa chỉ robot | `192.168.4.1` |
| Địa chỉ Ubuntu dùng với robot | `192.168.4.99` |

Đây là cấu hình của **bộ robot này**, không phải giá trị mặc định của mọi robot ESP32. Nếu thiết bị đã được cấu hình lại, dùng thông tin cấu hình hiện tại.

## 2. Hiểu đường kết nối trên máy Windows

Nếu dùng Windows và VMware, tín hiệu từ robot đi qua card Wi-Fi của máy thật rồi mới đến card mạng ảo trong Ubuntu. Sơ đồ dưới đây giúp chúng ta nhận ra từng phần cần kiểm tra khi Windows đã kết nối nhưng Ubuntu chưa liên lạc được với robot.

```mermaid
flowchart TD
    R["Robot phát Wi-Fi"] <-->|"Kết nối không dây"| W["Card Wi-Fi của máy Windows"]
    W --> B["VMware Bridged"]
    B --> U["Card Wired trong Ubuntu máy ảo"]
    U --> T["Terminal Ubuntu kiểm tra robot"]
    W --> H["Windows cũng có địa chỉ IP riêng"]
```

Trong chế độ **Bridged**, máy ảo tham gia mạng thông qua card mạng của máy thật. Ubuntu vẫn có cấu hình và địa chỉ IP riêng, nên chúng ta cần kiểm tra bên trong Ubuntu ngay cả khi Windows đã báo kết nối Wi-Fi thành công.

Ubuntu cài trực tiếp thì kết nối Wi-Fi ngay trong Ubuntu, bỏ qua nhánh Windows và VMware.

## 3. Kết nối Wi-Fi robot

Chúng ta bắt đầu bằng mạng do robot phát ra trong cấu hình mặc định. Hãy thực hiện bước chọn Wi-Fi ở hệ điều hành đang quản lý card không dây của máy tính:

1. Bật nguồn robot theo hướng dẫn sản phẩm.
2. Nếu dùng máy ảo, mở danh sách Wi-Fi **trên Windows**. Nếu cài Ubuntu trực tiếp, mở Wi-Fi **trong Ubuntu**.
3. Chọn `ESP32_SLAM` hoặc `ESP SLAM` đúng với robot.
4. Nhập mật khẩu `12345678` nếu robot vẫn dùng cấu hình mặc định.
5. Giữ kết nối dù máy tính báo **No Internet**.

Wi-Fi robot dùng cho liên lạc nội bộ nên có thể không cung cấp Internet. Trong lúc này, không dùng việc mở được Google hay không làm tiêu chí kiểm tra robot.

## 4. Kiểm tra địa chỉ bên trong Ubuntu

Sau khi kết nối Wi-Fi, chúng ta xem Ubuntu đang nhận địa chỉ nào. Mở Terminal Ubuntu và chạy:

```bash
ip -br -4 addr
```

**Ví dụ kết quả:**

```text
lo               UNKNOWN        127.0.0.1/8
ens33            UP             192.168.4.99/24
```

Tên `ens33` có thể khác, ví dụ `ens160` hoặc `wlp2s0`. Hãy nhìn vào địa chỉ, không yêu cầu tên card giống hệt ví dụ.

- `127.0.0.1` là địa chỉ của chính máy Ubuntu, không phải kết nối đến robot.
- `192.168.4.99/24` là địa chỉ Ubuntu mong đợi trong cấu hình này.
- `/24` mô tả kích thước mạng; khi điền trong giao diện, thường tương ứng với netmask `255.255.255.0`.

Địa chỉ IP còn được dùng làm đích gửi dữ liệu. Chẳng hạn, một địa chỉ khác trong cùng mạng **có thể vẫn ping được robot**, trong khi robot vẫn gửi dữ liệu đến `192.168.4.99` theo cấu hình đã lưu. Vì vậy, chúng ta cần đối chiếu địa chỉ Ubuntu với cấu hình robot, kể cả khi đã nhận được phản hồi ping.

### Nếu Ubuntu chưa có IP đúng

Với máy ảo ROBOVIS, trước tiên kiểm tra Windows còn kết nối đúng Wi-Fi, sau đó kiểm tra **VMware → Settings → Network Adapter → Bridged** và trạng thái kết nối của card ảo. Nếu máy có nhiều card mạng, chế độ Automatic có thể chọn sai card; cần chọn đúng card Wi-Fi đang kết nối robot trong thiết lập bridge.

Nếu vẫn chưa đúng, xem mục cấu hình thủ công bên dưới hoặc gửi ảnh cài đặt mạng để kiểm tra.

??? info "Đặt IP thủ công cho kết nối robot khi cần"
    Chỉ áp dụng khi robot vẫn dùng mạng mặc định `192.168.4.0/24` và chưa có thiết bị khác dùng `192.168.4.99`. Chụp lại cấu hình cũ trước khi thay đổi.

    Trong Ubuntu, mở **Settings → Network → Wired → biểu tượng bánh răng** nếu dùng máy ảo. Nếu Ubuntu nối Wi-Fi trực tiếp, mở phần cài đặt mạng Wi-Fi robot tương ứng.

    Chọn **IPv4 → Manual**. Điền **Address: `192.168.4.99`**, **Netmask: `255.255.255.0`**. Với kết nối nội bộ chỉ dùng trao đổi robot cùng mạng, có thể để trống Gateway và DNS nếu giao diện cho phép; đây không phải cấu hình Internet.

    Chọn **Apply**, ngắt rồi kết nối lại card mạng. Chạy lại `ip -br -4 addr`. Nếu đây là card Wired ảo đang đặt IP thủ công, khi đổi Windows về Wi-Fi có Internet bạn có thể cần chuyển IPv4 của card này về **Automatic (DHCP)**, rồi kết nối lại. Khi quay về robot, khôi phục cấu hình robot.

    Tham khảo thao tác giao diện tại [hướng dẫn đặt mạng thủ công của Ubuntu](https://help.ubuntu.com/stable/ubuntu-help/net-manual.html.en).

## 5. Kiểm tra robot bằng `ping`

Trong Terminal Ubuntu, chạy:

<!-- tutorial-figure:mang-robot-ubuntu -->
<figure class="tutorial-figure" markdown>

[![Ubuntu kết nối tới Wi-Fi robot; máy ảo cần bridge đúng card, robot và Ubuntu có IP riêng.](../assets/illustrations/mang-robot-ubuntu.svg)](../assets/illustrations/mang-robot-ubuntu.svg)

<figcaption>Sơ đồ kết nối với robot LiDAR ở chế độ AP mặc định. Với Wi-Fi ngoài, dùng IP thực tế theo cấu hình của mạng đó. Nhấp hình để xem lớn.</figcaption>
</figure>
<!-- /tutorial-figure:mang-robot-ubuntu -->

```bash
ping -c 4 192.168.4.1
```

Trong lệnh trên, `-c 4` yêu cầu `ping` gửi bốn lần rồi tự kết thúc. Chúng ta có thể chờ phần thống kê xuất hiện để đọc kết quả, không cần nhấn Ctrl + C như khi chạy `ping` liên tục.

**Kết quả ví dụ khi kết nối tốt:**

```text
64 bytes from 192.168.4.1: icmp_seq=1 ttl=255 time=3.2 ms
...
4 packets transmitted, 4 received, 0% packet loss
```

Thời gian và `ttl` có thể khác. Điều cần quan sát là có phản hồi từ đúng địa chỉ và tỷ lệ mất gói.

| Kết quả | Hiểu thế nào? | Bước tiếp theo |
| --- | --- | --- |
| Có phản hồi, `0% packet loss` | Phép thử mạng cơ bản thành công | Kiểm tra IP đích dữ liệu rồi sang bài khởi động robot |
| Có phản hồi nhưng mất một số gói | Kết nối có thể chập chờn | Đưa máy gần robot hơn và kiểm tra lại |
| `100% packet loss` | Chưa nhận phản hồi ping | Kiểm tra nguồn robot, Wi-Fi, IP và bridge |
| `Network is unreachable` | Ubuntu chưa có đường mạng phù hợp | Xem card mạng và IP trước |

**Ping thành công chưa xác nhận ROS 2 hoạt động.** Đây là bước kiểm tra kết nối mạng; phần mềm robot còn cần môi trường và chương trình giao tiếp chạy đúng.

## 6. Nếu robot dùng Wi-Fi ngoài

Nếu robot và máy tính cùng tham gia mạng của nhà hoặc phòng lab, chúng ta vẫn kiểm tra theo trình tự Wi-Fi, IP rồi liên lạc mạng. Tuy nhiên, địa chỉ thường khác `192.168.4.x`, nên cần dùng thông tin thực tế của mạng đó thay cho cặp IP mặc định ở trên.

Bạn cần biết IP hiện tại của robot và IP Ubuntu mà robot gửi dữ liệu tới. Nếu router tự cấp địa chỉ, IP máy tính có thể thay đổi sau lần kết nối khác. Khi đó cần đặt IP cố định/đặt chỗ DHCP phù hợp hoặc cấu hình lại địa chỉ máy tính trong robot theo bài Wi-Fi ngoài của sản phẩm.

Với máy ảo, địa chỉ cần kiểm tra là **IP Ubuntu**, không mặc nhiên là IP Windows.

## 7. Kiểm tra USB nếu bài hướng dẫn yêu cầu

Một số bước trong tài liệu sản phẩm có thể yêu cầu kết nối thiết bị qua USB. Khi đó, chúng ta kiểm tra thiết bị theo cách dưới đây. Phép thử này tách biệt với kết nối Wi-Fi vừa thực hiện; bạn không cần cắm USB chỉ để kiểm tra ping robot.

Chạy trước và sau khi cắm thiết bị:

```bash
lsusb
```

Quan sát dòng mới xuất hiện. Nếu dùng VMware, có thể cần chọn **VM → Removable Devices → thiết bị → Connect (Disconnect from host)** để chuyển thiết bị từ Windows sang Ubuntu.

Việc thấy thiết bị trong `lsusb` chưa đảm bảo chương trình đã có quyền mở cổng serial. Khi có lỗi quyền, ghi lại chính xác thông báo và tên cổng để xử lý theo tài liệu sản phẩm. Bài này không yêu cầu nạp firmware.

**Bạn đã hoàn thành bài này khi:** xác định đúng Wi-Fi, tìm được IP Ubuntu và đọc được kết quả ping robot.

## Tổng kết

Chúng ta đã phân biệt tên Wi-Fi với địa chỉ IP và kiểm tra đường liên lạc từ Ubuntu đến robot. Ping thành công là bằng chứng cho phép thử mạng cơ bản; dữ liệu ROS 2 còn phụ thuộc chương trình kết nối và cấu hình đích gửi. Bài cuối sẽ kết hợp những thao tác Ubuntu đã học thành một bài thực hành hoàn chỉnh.

[← Bài 6](06-cai-va-chay-phan-mem.md) · [Bài 8: Thực hành và xử lý lỗi →](08-thuc-hanh-va-loi.md)
