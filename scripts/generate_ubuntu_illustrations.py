"""Generate standalone SVG teaching diagrams; no third-party packages required."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'docs/ubuntu-co-ban/images'
OUT.mkdir(parents=True, exist_ok=True)

class Diagram:
    def __init__(self, name, title, desc, height=660):
        self.name, self.height = name, height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>', '<style>text{font-family:Segoe UI,Arial,sans-serif;font-size:22px;fill:#17334e}.title{font-size:30px;font-weight:700}.small{font-size:20px}.mono{font-family:Consolas,monospace;font-size:23px}.white{fill:#fff}.muted{fill:#53697d}.green{fill:#8ae59c}.orange{fill:#ffbc8c}.bold{font-weight:700}</style>']
        self.rect(0,0,1120,height,'#f4f7fb',16)
        self.text(36,48,title,'title')
        self.text(36,82,'MINH HỌA • Tên tài khoản và giao diện thực tế có thể khác.','small muted')
    def rect(self,x,y,w,h,fill,rx=0,stroke=None):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+'/>')
    def text(self,x,y,value,cls='',fill=None):
        self.parts.append(f'<text x="{x}" y="{y}" class="{cls}"'+(f' style="fill:{fill}"' if fill else '')+f'>{escape(value)}</text>')
    def line(self,x1,y1,x2,y2,color='#7193b3',width=3):
        self.parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    def badge(self,x,y,n):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="17" fill="#1765b0" stroke="#fff" stroke-width="2"/>')
        self.text(x-6,y+7,str(n),'small white bold')
    def folder(self,x,y,label,selected=False):
        if selected: self.rect(x-12,y-12,170,116,'#e6f0ff',10,'#5c8fd0')
        self.rect(x,y,47,22,'#d99038',4); self.rect(x,y+12,95,56,'#edb25c',6)
        self.text(x,y+95,label,'small')
    def terminal(self,x=36,y=115,w=1048,h=300,title='robovis@ubuntu: ~'):
        self.rect(x,y,w,h,'#2d1230',10)
        self.rect(x,y,w,42,'#34313a',10)
        self.rect(x,y+25,w,17,'#34313a')
        self.text(x+20,y+29,title,'small white')
        self.text(x+w-31,y+29,'×','white')
    def save(self):
        self.parts.append('</svg>')
        (OUT/self.name).write_text('\n'.join(self.parts)+'\n',encoding='utf-8')

s=Diagram('03-man-hinh-ubuntu.svg','Nhận biết màn hình Ubuntu Desktop 22.04','Sơ đồ màn hình: Activities góc trái trên; Dock bên trái; ngày giờ ở giữa thanh trên; menu hệ thống ở góc phải trên; Show Applications ở cuối Dock.',720)
s.rect(36,110,1048,400,'#4b2154',10)
s.rect(36,110,1048,40,'#26242a',8)
s.text(57,138,'Activities','small white'); s.text(480,138,'May 12  09:41','small white'); s.text(943,138,'Mạng  •  Âm','small white')
s.rect(36,150,74,360,'#302734')
for y,label in [(180,'Web'),(245,'Files'),(310,'Term'),(375,'Cài')]:
 s.rect(48,y,50,46,'#56515d',8); s.text(52,y+29,label,'small white')
for x in [54,71,88]:
 for y in [459,476,493]: s.rect(x,y,6,6,'#fff',1)
s.text(325,295,'Không gian làm việc của bạn','title white')
s.text(325,335,'Mở ứng dụng từ Activities hoặc Dock.','white')
s.badge(196,130,1); s.badge(119,272,2); s.badge(688,130,3); s.badge(1064,166,4); s.badge(118,476,5)
for x,y,n,label in [(40,555,1,'Activities: tìm ứng dụng'),(580,555,2,'Dock: mở nhanh ứng dụng'),(40,605,3,'Ngày giờ: lịch, thông báo'),(580,605,4,'Menu hệ thống: mạng, tắt máy'),(40,655,5,'Show Applications: danh sách ứng dụng')]:
 s.badge(x+14,y-6,n); s.text(x+42,y,label)
s.save()

s=Diagram('03-files-home.svg','Tìm thư mục thực hành trong Files','Cửa sổ Files ở Home với Downloads và hoc_ubuntu. Chọn Home ở thanh bên, rồi nhấp đúp hoc_ubuntu. Ctrl+Shift+N tạo thư mục mới.',620)
s.rect(36,115,1048,350,'#fff',10,'#d3dde8'); s.rect(36,115,1048,48,'#e9e8e6',10); s.text(64,147,'Files   ‹   ›','bold'); s.text(370,147,'Home','bold'); s.text(1039,147,'×')
s.rect(36,163,220,302,'#f0f2f4'); s.rect(48,194,196,42,'#dbe9fb',5)
for y,label in [(224,'Home'),(276,'Documents'),(328,'Downloads'),(380,'Other Locations')]: s.text(66,y,label,'small')
s.folder(308,207,'Documents'); s.folder(548,207,'Downloads'); s.folder(788,207,'hoc_ubuntu',True)
s.badge(234,212,1); s.badge(957,216,2)
s.text(65,510,'1. Chọn Home.'); s.text(395,510,'2. Nhấp đúp hoc_ubuntu.')
s.rect(60,538,998,49,'#eaf2fc',8); s.text(80,570,'Chưa có thư mục? Nhấn Ctrl + Shift + N → nhập hoc_ubuntu → Create.','small')
s.save()

s=Diagram('04-doc-terminal.svg','Đọc một lệnh trong Terminal','Ví dụ robovis@ubuntu:~$ pwd. Phần trước pwd là dấu nhắc, pwd là lệnh cần nhập, /home/robovis là kết quả, dấu nhắc mới cho biết lệnh đã kết thúc.',650)
s.terminal(h=287)
s.text(68,209,'robovis@ubuntu:~$','mono green'); s.text(321,209,'pwd','mono white'); s.badge(589,202,1)
s.text(68,264,'/home/robovis','mono white'); s.badge(589,257,2)
s.text(68,319,'robovis@ubuntu:~$','mono green'); s.rect(323,298,12,26,'#fff'); s.badge(589,312,3)
s.text(639,208,'Nhập pwd rồi nhấn Enter.','white'); s.text(639,263,'Đây là kết quả trả về.','white'); s.text(639,318,'Đã xong, có thể nhập tiếp.','white')
s.text(58,450,'Phân biệt các phần của dấu nhắc','bold')
for x,w,label,detail in [(58,230,'robovis','Tên tài khoản'),(304,210,'ubuntu','Tên máy'),(530,220,'~','Thư mục Home'),(766,288,'$','Đang chờ lệnh')]:
 s.rect(x,474,w,112,'#fff',8,'#d3dde8'); s.text(x+18,514,label,'mono bold'); s.text(x+18,552,detail,'small')
s.text(58,625,'Chỉ nhập pwd. Không gõ lại robovis@ubuntu:~$ và không dán phần kết quả.','small muted')
s.save()

s=Diagram('04-dung-ping.svg','Dừng lệnh đang chạy bằng Ctrl + C','Terminal chạy ping 127.0.0.1, xuất hiện các dòng phản hồi liên tiếp. Nhấn Ctrl+C sẽ in thống kê và trả về dấu nhắc. Đây là kiểm tra chính máy Ubuntu, không phải Internet hay robot.',680)
s.terminal(h=407)
lines=[('robovis@ubuntu:~$ ping 127.0.0.1','green'),('PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.','white'),('64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.040 ms','white'),('64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.035 ms','white'),('^C','orange'),('--- 127.0.0.1 ping statistics ---','white'),('2 packets transmitted, 2 received, 0% packet loss','white'),('robovis@ubuntu:~$','green')]
for i,(line,color) in enumerate(lines): s.text(62,195+i*40,line,'mono '+color)
s.rect(58,555,1004,74,'#eaf2fc',8); s.text(78,585,'Ctrl + C: yêu cầu dừng chương trình đang chạy.','bold'); s.text(78,614,'Dấu nhắc quay lại: bạn có thể nhập lệnh mới. Thời gian phản hồi chỉ là ví dụ.','small')
s.save()

s=Diagram('05-cay-thu-muc.svg','Hiểu đường dẫn bằng cây thư mục','Cây /home/robovis chứa Downloads và hoc_ubuntu. Trong hoc_ubuntu có bai_05, bên trong chứa ghi_chu.txt. Ký hiệu ~ là /home/robovis; cd .. đi từ bai_05 lên hoc_ubuntu.',680)
for x,y,w,label,fill in [(60,126,340,'/','#fff'),(105,193,295,'home','#fff'),(150,260,250,'robovis  (= ~)','#eaf2fc'),(205,327,245,'Downloads','#fff'),(205,394,245,'hoc_ubuntu','#fff'),(260,461,250,'bai_05','#eaf2fc'),(315,528,280,'ghi_chu.txt','#fff')]:
 s.rect(x,y,w,48,fill,7,'#b9cddd'); s.text(x+16,y+32,label,'mono')
for points in [(80,174,80,217),(80,217,105,217),(125,241,125,284),(125,284,150,284),(175,308,175,418),(175,351,205,351),(175,418,205,418),(230,442,230,485),(230,485,260,485),(285,509,285,552),(285,552,315,552)]: s.line(*points)
s.rect(565,136,493,133,'#122b44',10); s.text(587,173,'HAI CÁCH VIẾT CÙNG MỘT VỊ TRÍ','small white bold'); s.text(587,215,'/home/robovis/hoc_ubuntu','mono white'); s.text(587,250,'~/hoc_ubuntu','mono green')
s.rect(565,300,493,150,'#fff',10,'#b9cddd'); s.text(587,339,'Nếu Terminal đang ở bai_05:','bold'); s.text(587,382,'cd ..','mono'); s.text(587,423,'→ trở về hoc_ubuntu','small')
s.text(60,625,'Tệp ví dụ: ~/hoc_ubuntu/bai_05/ghi_chu.txt','mono bold')
s.save()

s=Diagram('05-nano-luu-tep.svg','Nhập, lưu và thoát tệp trong nano','Nano đang sửa ghi_chu.txt với hai dòng ghi chú. Thanh dưới có ^O Write Out và ^X Exit. Thao tác lưu: Ctrl+O, Enter xác nhận tên, Ctrl+X thoát.',650)
s.terminal(h=306,title='nano ghi_chu.txt')
s.rect(52,170,1016,34,'#c7c9ca'); s.text(66,195,'GNU nano                         ghi_chu.txt','mono')
s.text(66,246,'Toi dang hoc Ubuntu.','mono white'); s.text(66,285,'Toi biet mo Terminal va tim thu muc Home.','mono white')
s.text(66,360,'^G Help       ^O Write Out       ^W Where Is','mono white'); s.text(66,397,'^X Exit       ^R Read File       ^K Cut','mono white')
for x,n,key,desc in [(50,1,'Ctrl + O','Yêu cầu lưu'),(400,2,'Enter','Xác nhận tên tệp'),(750,3,'Ctrl + X','Thoát nano')]:
 s.rect(x,458,320,103,'#fff',10,'#c7d7e6'); s.badge(x+28,487,n); s.text(x+61,496,key,'mono bold'); s.text(x+22,537,desc,'small')
s.text(58,610,'Dấu ^ trong ^O và ^X có nghĩa là giữ phím Ctrl, không phải gõ ký tự ^.','small muted')
s.save()
print('Generated 6 Ubuntu SVG illustrations.')
