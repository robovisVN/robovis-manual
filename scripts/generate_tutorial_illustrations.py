"""Build SVG illustrations and place them beside relevant tutorial sections.

Run with the project's Python. Images are conceptual diagrams, not screenshots.
Only marked figure blocks are replaced on later runs.
"""
from pathlib import Path
from html import escape
import math
import os
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/assets/illustrations'
OUT.mkdir(parents=True, exist_ok=True)
FIGURES = []

class SVG:
    def __init__(self, name, title, description, height=520):
        self.name, self.height = name, height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>', '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#3672a4"/></marker></defs>', '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#183b56;font-size:22px}.title{font-size:29px;font-weight:700}.small{font-size:20px}.bold{font-weight:700}.mono{font-family:Consolas,monospace}.muted{fill:#53697d}.white{fill:white}.accent{fill:#1765b0}</style>']
        self.rect(0,0,1120,height,'#f4f7fb',16)
        self.text(36,48,title,'title')
        self.text(36,82,'SƠ ĐỒ MINH HỌA • Đọc cùng các bước và cấu hình trong bài.','small muted')
    def rect(self,x,y,w,h,fill='#fff',rx=10,stroke='#c8d8e7'):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>')
    def text(self,x,y,value,cls='',size=None):
        self.parts.append(f'<text x="{x}" y="{y}" class="{cls}"'+(f' style="font-size:{size}px"' if size else '')+f'>{escape(value)}</text>')
    def line(self,x1,y1,x2,y2,arrow=False,color='#3672a4'):
        self.parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="3" fill="none"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
    def path(self,d,color='#1765b0',width=4):
        self.parts.append(f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="none"/>')
    def circle(self,x,y,r,fill='#e7f0fb'):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#3672a4" stroke-width="2"/>')
    def box(self,x,y,w,title,lines,number=None,h=160):
        self.rect(x,y,w,h)
        if number: self.text(x+18,y+31,number,'small accent bold')
        self.text(x+18,y+66,title,'bold',min(23, (w-36)/max(1,len(title))/.58))
        for i,line in enumerate(lines): self.text(x+18,y+104+30*i,line,'small',min(20,(w-36)/max(1,len(line))/.57))
    def note(self,lines):
        y=self.height-48-30*(len(lines)-1)
        for i,line in enumerate(lines): self.text(36,y+30*i,line,'small muted')
    def save(self):
        self.parts.append('</svg>')
        (OUT/(self.name+'.svg')).write_text('\n'.join(self.parts)+'\n',encoding='utf-8')

def flow(name,title,steps,notes):
    s=SVG(name,title,' → '.join([x[0] for x in steps])+'. '+' '.join(notes),450)
    gap=28; w=(1048-gap*(len(steps)-1))/len(steps)
    for i,(label,lines) in enumerate(steps):
        x=36+i*(w+gap); s.box(x,135,w,label,lines,f'{i+1:02}')
        if i<len(steps)-1: s.line(x+w+3,218,x+w+gap-5,218,True)
    s.note(notes); s.save()

def attach(path,name,heading,alt,caption):
    FIGURES.append((path,name,heading,alt,caption))

s=SVG('ubuntu-trong-windows','Windows, máy ảo Ubuntu và phần mềm robot','Windows chứa VMware, VMware chứa Ubuntu. Terminal và ROS 2 chạy bên trong Ubuntu. ESP32 không chạy Ubuntu.',580)
s.rect(36,117,1048,360,'#e5edf6'); s.text(58,154,'Máy tính Windows','bold')
s.rect(82,177,970,272,'#fff'); s.text(104,214,'VMware — máy ảo Ubuntu','bold')
s.box(125,240,400,'Terminal Ubuntu',['Nhập lệnh trong Ubuntu'],h=165)
s.box(605,240,400,'Phần mềm ROS 2',['Nhận dữ liệu, điều khiển robot'],h=165); s.line(536,320,590,320,True)
s.note(['Tệp tải trong Windows không tự xuất hiện trong Home của Ubuntu.','Nếu cài Ubuntu trực tiếp, bạn không cần lớp VMware.']); s.save()
for p in ['ubuntu-co-ban/01-ubuntu-la-gi.md','robot-esp32-lidar/02-chuan-bi/04-windows-may-ao-ubuntu.md']:
 attach(p,s.name,'## 3. Dùng Windows' if p.startswith('ubuntu') else None,'Windows chứa VMware và Ubuntu; Terminal chạy phần mềm ROS 2 bên trong Ubuntu.','Phân biệt nơi chạy phần mềm: nhập lệnh ROS 2 trong Terminal Ubuntu, không nhập vào PowerShell của Windows.')

flow('mo-may-ao','Mở đúng bộ máy ảo Ubuntu', [('Giải nén toàn bộ',['robovis.zip','Giữ các tệp cùng nhau']),('Mở bằng VMware',['Chọn tệp .vmx','.vmdk là dữ liệu ổ đĩa']),('Bật và đăng nhập',['Power on','Đến màn hình Ubuntu'])],['Không tách riêng .vmx khỏi các tệp của máy ảo.'])
attach('ubuntu-co-ban/02-chuan-bi-moi-truong.md','mo-may-ao','## 3. Mở máy ảo','Giải nén robovis.zip, chọn .vmx bằng VMware, bật máy và đăng nhập Ubuntu.','Ba bước mở máy ảo; tệp .vmx và dữ liệu .vmdk cần được giữ trong bộ máy ảo đầy đủ.')
flow('cai-nap-chay','Cài phần mềm, nạp môi trường và chạy lệnh', [('Cài khi còn thiếu',['sudo apt install nano','Cần Internet để tải gói']),('Nạp môi trường ROS 2',['source setup.bash','Dùng đúng đường dẫn']),('Chạy khi cần dùng',['nano ghi_chu.txt','hoặc ros2 topic list'])],['Đây là ba loại thao tác khác nhau, không phải ba lệnh phải chạy liên tiếp.','Phần mềm đã cài không cần cài lại mỗi lần mở Terminal.'])
attach('ubuntu-co-ban/06-cai-va-chay-phan-mem.md','cai-nap-chay','## 1. Cài và chạy','So sánh cài phần mềm, source môi trường và chạy chương trình.','Phân biệt ba công việc thường gặp. Với ROS 2, dùng nguyên đường dẫn source được ghi trong bài.')
flow('mang-robot-ubuntu','Kiểm tra mạng từ Ubuntu tới robot', [('Ubuntu',['IP trên card đang dùng','Khác IP của Windows']),('Đường kết nối',['Wi-Fi robot','VMware: kiểm tra Bridged']),('Robot LiDAR',['192.168.4.1','Cấu hình AP mặc định'])],['Ví dụ AP mặc định: IP Ubuntu 192.168.4.99, robot 192.168.4.1; không đặt trùng IP.','Ping thành công mới xác nhận kết nối mạng, chưa xác nhận ROS 2 hoạt động.'])
for p,h in [('ubuntu-co-ban/07-ket-noi-robot.md','## 5. Kiểm tra'),('robot-esp32-lidar/02-chuan-bi/03-cau-hinh-wifi.md','## 3. Kiểm tra')]:
 attach(p,'mang-robot-ubuntu',h,'Ubuntu kết nối tới Wi-Fi robot; máy ảo cần bridge đúng card, robot và Ubuntu có IP riêng.','Sơ đồ kết nối với robot LiDAR ở chế độ AP mặc định. Với Wi-Fi ngoài, dùng IP thực tế theo cấu hình của mạng đó.')
flow('kiem-tra-tung-lop','Tìm lỗi theo từng lớp', [('Mạng',['Đúng Wi-Fi và IP?','ping có phản hồi?']),('Môi trường',['Đúng Terminal Ubuntu?','Đã source ROS 2?']),('Dữ liệu và hiển thị',['Node, topic có dữ liệu?','RViz đúng frame?'])],['Dừng ở lớp đang lỗi và đọc thông báo trước khi thay đổi cấu hình.'])
for p,h in [('ubuntu-co-ban/08-thuc-hanh-va-loi.md',None),('robot-esp32-lidar/06-xu-ly-su-co/01-loi-ket-noi-va-ros2.md',None)]:
 attach(p,'kiem-tra-tung-lop',h,'Ba lớp kiểm tra: mạng, môi trường ROS 2, dữ liệu và hiển thị.','Kiểm tra từ kết nối mạng tới môi trường và dữ liệu. Ghi lại lệnh đã chạy cùng thông báo lỗi ở lớp gặp vấn đề.')

flow('quy-trinh-nap','Từ mã nguồn đến chương trình trên bo mạch', [('Chọn đúng',['Bo và cổng USB','Theo cấu hình của bài']),('Verify',['Kiểm tra biên dịch','Sửa lỗi nếu có']),('Upload',['Nạp xuống bo','Chờ thông báo hoàn tất']),('Quan sát',['Serial Monitor / LED','Đối chiếu baud rate'])],['Chương trình biên dịch được chưa có nghĩa đã nạp thành công xuống bo.'])
for group in ['robot-arduino','robot-esp32']:
 for filename in ['03-cai-arduino-ide.md','bai-giang/02-lap-trinh.md']:
  attach(f'{group}/{filename}','quy-trinh-nap',None,'Quy trình chọn bo và cổng USB, Verify, Upload rồi quan sát Serial Monitor hoặc LED.','Quy trình nạp chương trình. Tên bo, cổng và tốc độ Serial cần theo đúng phần hướng dẫn của từng bo.')
attach('robot-esp32-camera/03-nap-code/02-chon-board-va-nap-code.md','quy-trinh-nap',None,'Chọn đúng bo và cổng, biên dịch, nạp chương trình rồi kiểm tra kết quả.','Làm lần lượt các bước nạp, giữ đúng cấu hình ESP32-S3 và chương trình tương ứng trong bài.')
flow('goi-board-va-thu-vien','Phân biệt gói hỗ trợ bo và thư viện', [('Boards Manager',['Cài nền tảng của bo','Ví dụ: esp32 / Espressif']),('Chọn bo trong IDE',['Dùng đúng loại phần cứng','Không suy ra từ tên robot']),('Library Manager',['Cài thư viện theo mã nguồn','Đúng tên và phiên bản'])],['Gói hỗ trợ bo giúp IDE biên dịch cho phần cứng; thư viện bổ sung các chức năng.'])
for p in ['robot-esp32/04-cai-thu-vien.md','robot-arduino/04-cai-thu-vien.md','robot-esp32-camera/02-cai-dat-arduino/02-cai-board-esp32.md','robot-esp32-camera/02-cai-dat-arduino/03-cai-thu-vien.md']:
 attach(p,'goi-board-va-thu-vien',None,'Boards Manager cài nền tảng bo; chọn đúng bo; Library Manager cài thư viện theo chương trình.','Gói hỗ trợ bo và thư viện có nhiệm vụ khác nhau. Cài đúng thành phần được yêu cầu trong bài, không thay thế hai loại cho nhau.')

s=SVG('led-high-low','LED bật và tắt theo thời gian','Sơ đồ LED active-high: HIGH bật, LOW tắt. Trục ngang là thời gian. LED active-low có trạng thái ngược lại.',440)
s.text(45,171,'HIGH','mono'); s.text(45,272,'LOW','mono'); s.line(155,298,1055,298,True); s.text(922,334,'Thời gian','small')
s.path('M170 270V170H385V270H600V170H815V270H1035'); s.text(220,145,'Bật'); s.text(435,248,'Tắt'); s.text(650,145,'Bật'); s.text(865,248,'Tắt')
s.note(['Minh họa cho LED active-high; LED active-low có trạng thái sáng/tắt ngược lại.']); s.save()
for g in ['robot-arduino','robot-esp32']:
 attach(f'{g}/bai-giang/03-led.md',s.name,None,'Xung HIGH LOW thay đổi theo thời gian, tương ứng bật và tắt đối với LED active-high.','Sơ đồ thời gian giúp đọc trình tự bật/tắt. Kiểm tra loại LED thực tế và mức kích hoạt trong bài.')

s=SVG('servo-goc-quay','Servo vị trí: lệnh góc và vị trí trục','Ba vị trí minh họa 0, 90, 180 độ. Giới hạn cơ khí và góc thực tế phụ thuộc servo.',450)
for x,angle,label in [(195,180,'0°'),(560,90,'90°'),(925,0,'180°')]:
 s.circle(x,245,72); s.circle(x,245,13,'#1765b0'); rad=math.radians(angle); s.line(x,245,x+84*math.cos(rad),245-84*math.sin(rad),True); s.text(x-22,355,label,'bold')
s.note(['Góc chỉ là minh họa; kiểm tra hành trình thực tế và không ép servo qua giới hạn cơ khí.']); s.save()
for g in ['robot-arduino','robot-esp32']:
 attach(f'{g}/bai-giang/04-servo.md',s.name,None,'Ba vị trí trục servo được minh họa với lệnh 0, 90 và 180 độ.','Servo vị trí di chuyển tới góc yêu cầu. Ba góc minh họa không thay cho thông số hành trình của servo đang sử dụng.')

s=SVG('sieu-am-khoang-cach','HC-SR04: sóng đi và sóng phản xạ','Cảm biến phát sóng đến vật cản, nhận sóng quay lại. Khoảng cách bằng vận tốc âm nhân thời gian khứ hồi chia hai.',490)
s.rect(60,155,245,180,'#dfeef5'); s.text(105,192,'HC-SR04','bold'); s.circle(132,263,36,'#fff'); s.circle(232,263,36,'#fff')
s.rect(895,140,145,230,'#d6dce4'); s.text(917,265,'Vật cản','bold')
s.line(325,208,871,208,True); s.text(465,184,'Sóng phát đi'); s.line(871,309,325,309,True); s.text(455,349,'Sóng phản xạ')
s.text(350,401,'d = vận tốc âm × thời gian khứ hồi / 2','bold')
s.note(['Sơ đồ nguyên lý, không phải sơ đồ đấu dây. Mức điện áp Echo phải theo đúng bài của bo.']); s.save()
for g in ['robot-arduino','robot-esp32']:
 attach(f'{g}/bai-giang/06-hc-sr04.md',s.name,'## 4. Nguyên lý' if g=='robot-esp32' else None,'HC-SR04 phát siêu âm tới vật cản rồi nhận phản xạ; khoảng cách bằng nửa quãng đường khứ hồi.','Vì tín hiệu đi tới vật cản rồi quay lại, phép tính khoảng cách phải chia thời gian khứ hồi cho hai.')

s=SVG('do-line-5-mat','Năm mắt dò line và vị trí vạch','Năm mắt cảm biến quan sát bề mặt; vạch dưới mắt giữa giúp xác định line đang ở giữa. Mức 0/1 phụ thuộc cảm biến, cần hiệu chuẩn.',470)
s.rect(95,145,930,175,'#fff'); s.rect(502,145,116,175,'#292c35',0)
for x,label in [(200,'L2'),(380,'L1'),(560,'M'),(740,'R1'),(920,'R2')]:
 s.circle(x,224,28,'#72c5dd'); s.text(x-16,125,label,'bold'); s.line(x,261,x,307)
s.text(72,364,'Nhìn từ trên xuống: vạch nằm dưới mắt M (giữa).','bold')
s.note(['Xác định lại thứ tự trái/phải khi lắp. Không mặc định 0 hoặc 1 luôn là màu đen.']); s.save()
for g in ['robot-arduino','robot-esp32']:
 attach(f'{g}/bai-giang/07-do-line.md',s.name,None,'Mảng năm cảm biến L2 L1 M R1 R2 nhìn từ trên xuống với vạch nằm dưới mắt giữa.','Ví dụ nhận biết vị trí vạch bằng năm mắt cảm biến. Thứ tự kênh và mức 0/1 cần đối chiếu kết quả đo thực tế.')

s=SVG('encoder-xung-rpm','Encoder: từ xung đến tốc độ bánh xe','Đếm N xung trong T giây. RPM bằng N nhân 60 chia PPR và T; PPR phải tính theo một vòng bánh và phương pháp đếm thực tế.',500)
s.text(44,152,'Tín hiệu encoder','bold'); s.path('M65 269V199H120V269H175V199H230V269H285V199H340V269H395V199H450V269')
s.line(65,312,450,312); s.line(65,299,65,325); s.line(450,299,450,325); s.text(155,352,'Cửa sổ đo T giây','small')
s.box(535,143,505,'Đếm N xung trong T giây',['RPM = N × 60 / (PPR × T)','PPR: xung / một vòng bánh'],h=215)
s.note(['Hiệu chuẩn PPR theo đúng trục bánh và chế độ đếm; không lấy số xung ví dụ làm mặc định.']); s.save()
for g in ['robot-arduino','robot-esp32']:
 attach(f'{g}/bai-giang/08-encoder.md',s.name,None,'Dạng xung encoder và công thức RPM bằng N nhân 60 chia cho PPR nhân T.','Đếm số xung trong một khoảng thời gian để suy ra tốc độ. PPR phải phù hợp với bánh xe và cách đếm đang dùng.')

s=SVG('pid-vong-kin','Điều khiển tốc độ có phản hồi','Tốc độ đặt được so sánh với tốc độ encoder. Sai số đi vào PID, đầu ra PWM tới động cơ; encoder đo tốc độ đưa về so sánh.',490)
for x,w,t,lines in [(36,225,'So sánh',['Đặt − tốc độ đo','Sai số e']),(307,225,'PID',['Tính điều khiển','Giới hạn đầu ra']),(578,225,'Driver + động cơ',['Nhận PWM','Bánh xe quay']),(849,235,'Encoder',['Đo tốc độ','Phản hồi'])]: s.box(x,145,w,t,lines,h=170)
for a,b in [(261,307),(532,578),(803,849)]:s.line(a+4,225,b-8,225,True)
s.line(964,315,964,369); s.line(964,369,148,369); s.line(148,369,148,321,True); s.text(404,400,'Tốc độ đo quay về điểm so sánh','small')
s.note(['Sơ đồ nguyên lý vòng kín; hệ số PID và giới hạn PWM phải theo thử nghiệm trong bài.']); s.save()
for g in ['robot-arduino','robot-esp32']:
 attach(f'{g}/bai-giang/10-pid.md',s.name,None,'Vòng kín tốc độ đặt, so sánh, PID, driver động cơ, encoder và đường phản hồi.','Encoder cung cấp tốc độ thực tế để bộ điều khiển liên tục tính lại sai số và điều chỉnh PWM.')

flow('wifi-trinh-duyet','Điều khiển ESP32 từ trình duyệt', [('Kết nối Wi-Fi',['Chọn mạng robot phát','Giữ kết nối nội bộ']),('Mở đúng địa chỉ',['Nhập IP ở thanh địa chỉ','Theo Serial / cấu hình']),('Gửi lệnh điều khiển',['Nhấn nút trên trang','Quan sát phản hồi'])],['Wi-Fi robot có thể không có Internet. Không tìm địa chỉ IP bằng Google.'])
attach('robot-esp32/bai-giang/09-wifi.md','wifi-trinh-duyet','## 9. Kết nối','Kết nối Wi-Fi do ESP32 phát, mở địa chỉ trong trình duyệt, gửi lệnh từ trang điều khiển.','Ba bước sử dụng giao diện web. Dùng địa chỉ thực tế của chương trình; không mặc định mọi robot đều có cùng cấu hình.')

s=SVG('camera-hai-cau-hinh','Robot Camera: chọn đúng một cấu hình','Hai chương trình Camera có SSID và cổng khác nhau. YOLO dùng ESP32-Car-01, trang cổng 82, WebSocket cổng 82; kiểm tra cảm biến dùng ESP32-Car, trang và WebSocket cổng mặc định.',610)
for x,t,ssid,page,ws in [(36,'Camera + motor / YOLO','ESP32-Car-01','http://192.168.4.1:82','ws://192.168.4.1:82/ws'),(575,'Kiểm tra camera + cảm biến','ESP32-Car','http://192.168.4.1','ws://192.168.4.1/ws')]:
 s.rect(x,125,509,295); s.text(x+20,165,t,'bold'); s.text(x+20,218,'Wi-Fi: '+ssid,'mono',21); s.text(x+20,266,'Trang:','small muted'); s.text(x+20,299,page,'mono',22); s.text(x+20,345,'WebSocket:','small muted'); s.text(x+20,378,ws,'mono',21)
s.rect(36,447,1048,60,'#e7f0fb'); s.text(57,485,'Luồng camera của cả hai: http://192.168.4.1:81/stream','mono',23)
s.note(['Không trộn SSID, cổng hay sơ đồ GPIO giữa hai chương trình.','Bảng mật khẩu và cấu hình phần cứng tương ứng nằm trong bài.']); s.save()
for p in ['robot-esp32-camera/01-bat-dau/03-phan-biet-hai-chuong-trinh.md','robot-esp32-camera/04-dieu-khien-web/01-ket-noi-va-mo-giao-dien.md']:
 attach(p,s.name,'## Chọn đúng chương trình' if '03-phan-biet' in p else '## 4. Mở giao diện','Hai cấu hình ESP32 Camera: YOLO dùng Wi-Fi ESP32-Car-01 và cổng 82; kiểm tra cảm biến dùng ESP32-Car và cổng mặc định.','Chọn trọn một cấu hình tương ứng với firmware đang chạy. Luồng camera dùng cổng 81, nhưng cổng điều khiển khác nhau.')
s=SVG('yolo-luong-du-lieu','YOLO chạy ở đâu trong hệ thống Camera?','Robot gửi ảnh qua cổng 81 về máy Windows chạy YOLO và giao diện. Lệnh điều khiển đi từ giao diện trở lại robot qua WebSocket cổng 82.',530)
for x,title,lines in [(36,'Robot ESP32 Camera',['Gửi hình ảnh qua Wi-Fi','Nhận lệnh motor']),(395,'Máy tính Windows',['Python + model YOLO','Nhận diện trên máy tính']),(754,'Giao diện người dùng',['Xem khung nhận diện','Gửi lệnh qua WebSocket'])]:
 s.box(x,140,330,title,lines,h=160)
s.line(372,215,383,215,True); s.line(731,215,742,215,True)
s.line(918,300,918,352); s.line(918,352,201,352); s.line(201,352,201,306,True)
s.text(300,391,'Lệnh điều khiển quay lại robot qua WebSocket','small bold')
s.note(['Luồng ảnh: cổng 81 /stream. Điều khiển của firmware YOLO: WebSocket cổng 82.','Model YOLO chạy trên máy tính Windows, không chạy trong ESP32.']); s.save()
for p in ['robot-esp32-camera/05-yolo-windows/02-chay-chuong-trinh-yolo.md','robot-esp32-camera/05-yolo-windows/03-su-dung-phan-mem-yolo.md']:
 attach(p,'yolo-luong-du-lieu',None,'Robot gửi hình về máy Windows chạy YOLO; giao diện hiển thị nhận diện, điều khiển gửi qua WebSocket.','Nhận diện YOLO chạy trên Windows. Kênh ảnh và kênh điều khiển robot có URL riêng; kiểm tra đúng cả hai.')

s=SVG('workspace-build-source','Workspace: mã nguồn, build và môi trường','src chứa mã nguồn, colcon build tạo build, install, log. Source install/setup.bash để Terminal tìm thấy package đã build.',500)
s.box(36,140,280,'src/',['Mã nguồn và package','Nơi chỉnh sửa'],h=175); s.box(375,140,280,'colcon build',['Chạy ở gốc workspace','Đọc thông báo build'],h=175); s.box(714,140,370,'build/  install/  log/',['install: môi trường và tệp cài','log: nhật ký build'],h=175)
s.line(322,225,363,225,True); s.line(661,225,702,225,True)
s.rect(36,345,1048,60,'#e7f0fb'); s.text(58,383,'Sau khi build: source install/setup.bash trong Terminal dùng workspace.','small bold')
s.note(['Nạp ROS 2 nền trước overlay của workspace, theo đúng thứ tự và đường dẫn trong bài.']);s.save()
for p,h in [('kien-thuc-nen/robot-ros2/06-workspace-va-node-python.md','## 2. Workspace'),('robot-esp32-lidar/02-chuan-bi/02-cai-dat-workspace.md','## 2. Build')]:
 attach(p,s.name,h,'src chứa mã nguồn; colcon build tạo build, install và log; source install/setup.bash nạp môi trường workspace.','Quan hệ giữa mã nguồn, kết quả build và môi trường Terminal. Bài LiDAR có hai workspace: giữ đúng thứ tự build/source được hướng dẫn.')
flow('ros2-topic','Node, topic và message trong ROS 2', [('Node phát',['Publisher','Tạo dữ liệu']),('Topic',['Tên kênh dữ liệu','Message có kiểu xác định']),('Node nhận',['Subscriber','Xử lý dữ liệu nhận'])],['Một node có thể vừa phát vừa nhận trên các topic khác nhau.','Có tên topic chưa chứng minh đang có message; kiểm tra thêm info, echo và hz.'])
for p,h in [('kien-thuc-nen/robot-ros2/00-robot-va-ros2.md',None),('kien-thuc-nen/robot-ros2/01-node-topic-va-lenh.md','## 3. Topic'),('robot-esp32-lidar/03-van-hanh/02-khoi-dong-va-kiem-tra.md','## Bước 3.')]:
 attach(p,'ros2-topic',h,'Publisher phát message có kiểu xác định qua topic tới subscriber.','Topic là kênh, message là dữ liệu truyền trên kênh. Kiểm tra dữ liệu thật thay vì chỉ dựa vào tên topic trong danh sách.')

flow('tf-chuoi-frame','Cây TF: quan hệ giữa các hệ tọa độ', [('map',['Tham chiếu toàn cục','SLAM / định vị']),('odom',['Liên tục cục bộ','Có thể trôi theo thời gian']),('base_link',['Gắn với thân robot','Động theo odometry']),('Frame LiDAR',['Gắn với cảm biến','Tên tùy mô hình'])],['Mũi tên biểu diễn quan hệ cha → con; một số robot có thêm frame trung gian.','TF cần đúng cả quan hệ không gian và thời điểm dữ liệu.'])
for p,h in [('kien-thuc-nen/robot-ros2/he-toa-do-va-tf.md','## 4. Ghép'),('kien-thuc-nen/robot-ros2/03-rviz-va-tf.md',None)]:
 attach(p,'tf-chuoi-frame',h,'Ví dụ cây TF từ map tới odom, base_link và frame LiDAR.','Chuỗi frame thường gặp để đưa dữ liệu cảm biến vào bản đồ. Đối chiếu tên frame và các nhánh thực tế của robot đang chạy.')

flow('slam-dau-vao','SLAM kết hợp cảm biến và chuyển động', [('LiDAR + odometry',['Quét môi trường','Ước lượng chuyển động']),('SLAM + TF',['Ghép các lần quan sát','Ước lượng vị trí robot']),('Bản đồ trong RViz',['Quan sát vùng đã quét','Kiểm tra trước khi lưu'])],['Di chuyển chậm theo bài thực hành; kiểm tra scan, odometry và TF trước khi quét.'])
attach('robot-esp32-lidar/05-lidar-slam-navigation/02-tao-ban-do-slam.md','slam-dau-vao',None,'LiDAR và odometry cung cấp dữ liệu cho SLAM, kết quả là bản đồ và vị trí robot được quan sát trong RViz.','Các thành phần tham gia tạo bản đồ. Đây là sơ đồ nguyên lý, không thay cho các lệnh khởi chạy trong bài.')
s=SVG('ban-do-yaml-pgm','Bản đồ cần cả YAML và ảnh PGM','m_map.yaml tham chiếu image: m_map.pgm. YAML chứa thông tin bản đồ, PGM chứa ảnh lưới chiếm chỗ. Sao lưu cả hai tệp.',460)
s.box(36,140,450,'m_map.yaml',['Thông tin độ phân giải, gốc tọa độ','image: m_map.pgm'],h=185); s.box(632,140,450,'m_map.pgm',['Ảnh lưới chiếm chỗ','Dữ liệu hình học của bản đồ'],h=185); s.line(500,235,615,235,True); s.text(511,209,'image','small')
s.note(['Sao lưu cả hai tệp. Nếu đổi tên hoặc chuyển ảnh, kiểm tra lại đường dẫn image trong YAML.']); s.save()
attach('robot-esp32-lidar/05-lidar-slam-navigation/03-luu-va-quan-ly-ban-do.md',s.name,'## Kiểm tra file','Tệp m_map.yaml tham chiếu tới ảnh m_map.pgm; cần lưu và sao lưu cả hai.','Hai tệp làm việc cùng nhau. Chỉ sao chép YAML hoặc PGM sẽ không tạo thành bộ bản đồ đầy đủ.')
flow('nav2-quy-trinh','Từ bản đồ đã lưu đến mục tiêu điều hướng', [('Chuẩn bị',['Đủ YAML + PGM','Bringup và dữ liệu chạy']),('Đặt pose ban đầu',['2D Pose Estimate','Đúng vị trí và hướng']),('Gửi mục tiêu',['Nav2 Goal / 2D Nav Goal','Chọn điểm thử gần']),('Giám sát',['Quan sát robot thực','Sẵn sàng dừng'])],['Dừng SLAM trước khi chạy Navigation2 theo bài; đặt tốc độ thấp, khu vực thử thông thoáng.'])
attach('robot-esp32-lidar/05-lidar-slam-navigation/04-dieu-huong-nav2.md','nav2-quy-trinh','## 2. Đặt vị trí','Chuẩn bị bản đồ, đặt pose ban đầu trong RViz, gửi Nav2 Goal và giám sát chuyển động.','Đặt vị trí ban đầu trước khi gửi mục tiêu. Mũi tên pose và mục tiêu đều cần đúng hướng, không chỉ đúng vị trí.')

s=SVG('digital-adc-pwm','Digital, ADC và PWM có nhiệm vụ khác nhau','Digital dùng HIGH LOW; ADC chuyển điện áp analog đầu vào thành số; PWM là xung số với tỷ lệ thời gian HIGH thay đổi, không phải DAC.',570)
for y,title,desc in [(142,'Digital','Đọc / xuất HIGH hoặc LOW'),(266,'ADC','Điện áp đầu vào → giá trị số'),(390,'PWM','Thay đổi tỷ lệ thời gian HIGH')]:
 s.rect(36,y-28,1048,108); s.text(58,y+7,title,'bold'); s.text(58,y+43,desc,'small')
s.path('M580 185V135H705V185H830V135H1025');s.path('M580 305L640 285L700 302L760 255L820 270L880 240L950 260L1020 235')
s.path('M580 432V382H610V432H700V382H760V432H820V382H910V432H1025')
s.note(['PWM vẫn là xung HIGH/LOW. Độ phân giải ADC và cách tạo PWM phụ thuộc từng bo.']);s.save()
attach('kien-thuc-nen/vi-dieu-khien/02-digital-adc-pwm.md',s.name,'## Ba khái niệm','So sánh tín hiệu số, đầu vào analog được ADC số hóa và chuỗi xung PWM.','Ba dạng minh họa có nhiệm vụ khác nhau. Không coi PWM là điện áp analog liên tục hoặc dùng thang ADC của Nano cho mọi bo.')

s=SVG('gnd-tham-chieu','GND chung tạo mốc cho đường tín hiệu','Hai mạch giao tiếp trực tiếp có đường tín hiệu và đường GND làm mốc chung; không nối tùy tiện hai cực dương nguồn.',460)
s.box(60,142,350,'Mạch phát',['Chân tín hiệu','GND'],h=180); s.box(710,142,350,'Mạch nhận',['Chân vào','GND'],h=180)
s.line(422,240,697,240,True); s.text(468,213,'Tín hiệu','bold'); s.line(422,294,697,294,color='#68727e');s.text(457,350,'GND: mốc chung','bold')
s.note(['Sơ đồ nguyên lý giao tiếp trực tiếp. Không đồng nghĩa nối chung mọi cực dương nguồn.']);s.save()
attach('kien-thuc-nen/dien-dien-tu/02-gnd-va-noi-chung-mass.md',s.name,'## Khi hai mạch','Hai mạch nối tín hiệu và nối GND tham chiếu chung; không có đường nối các cực dương nguồn.','Bên nhận cần mốc GND phù hợp để hiểu mức điện áp tín hiệu. Với mạch cách ly hoặc nguồn đặc biệt, làm theo sơ đồ thiết kế.')

# Insert after a section's introductory paragraph, keeping existing content intact.
for relative,name,heading,alt,caption in FIGURES:
    page=ROOT/'docs'/relative
    content=page.read_text(encoding='utf-8-sig')
    marker=f'<!-- tutorial-figure:{name} -->'
    end=f'<!-- /tutorial-figure:{name} -->'
    image=os.path.relpath(OUT/(name+'.svg'),page.parent).replace(os.sep,'/')
    block=f'{marker}\n<figure class="tutorial-figure" markdown>\n\n[![{alt}]({image})]({image})\n\n<figcaption>{caption} Nhấp hình để xem lớn.</figcaption>\n</figure>\n{end}'
    if marker in content:
        content=re.sub(re.escape(marker)+r'.*?'+re.escape(end),lambda _:block,content,flags=re.S)
    else:
        if heading:
            match=re.search(r'^'+re.escape(heading)+r'.*$',content,re.M)
            if not match: raise ValueError(f'Missing section {heading} in {relative}')
        else:
            match=re.search(r'^## .+$',content,re.M)
            if not match: raise ValueError(f'Missing section in {relative}')
        start=match.end()
        # Place after the first complete prose paragraph, before lists/code/tables.
        tail=content[start:].lstrip('\n')
        paragraph=tail.split('\n\n',1)[0]
        if paragraph.startswith(('#','```','|','1.','- ','<')):
            pos=start
        else:
            pos=content.index(paragraph,start)+len(paragraph)
        content=content[:pos].rstrip()+'\n\n'+block+'\n\n'+content[pos:].lstrip('\n')
    page.write_text(content,encoding='utf-8')
print(f'Generated {len(list(OUT.glob("*.svg")))} diagrams; placed {len(FIGURES)} figures in {len(set(x[0] for x in FIGURES))} articles.')
