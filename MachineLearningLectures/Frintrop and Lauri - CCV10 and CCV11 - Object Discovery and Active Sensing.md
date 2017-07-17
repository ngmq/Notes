# Object discovery

## Gestalt Principle

## Graph-based segmentation

## Bio-inspired 2D Object Discovery 

# Active Sensing

Link: CCV11, mincommsy

Phần này chỉ mang tính giới thiệu sơ lược lý thuyết xác suất cơ bản nhất của Active Sensing chứ không có gì đặc biệt. Nhìn chung bài toán Active Sensing cố gắng trả lời câu hỏi: làm sao để thu thập nhiều thông tin hữu ích về môi trường xung quanh một cách nhanh nhất và tốn ít chi phí nhất.

Khi robot hoạt động thì môi trường làm POMDP, cho nên bài toán Active Sensing có mối quan hệ mật thiết với Reinforcement Learning. Từ đầu slide cho tới Decision Processes chỉ nói về MDP và POMDP. Phần Decision theory for active sensing thì dùng Belief Complex để minh họa một cách nhìn về việc update trạng thái của robot, trong đó nhấn mạnh vào việc giảm uncertainty của cái distribution over all possible states. Độ uncertainty được tính bằng công thức entropy quen thuộc. Về mặt hình học, khi entropy giảm thì cũng có nghĩa là vị trí của belief state nằm gần cạnh của cái belief simplex. Nếu take action mang tính exploration nào đó mà làm cho entroy giảm, nghĩa là vị trí của belief chạy về gần cạnh, thì là ổn.
