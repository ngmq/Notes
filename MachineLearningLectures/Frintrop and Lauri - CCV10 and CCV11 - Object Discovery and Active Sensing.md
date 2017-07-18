# Object discovery

Link: CCV10, mincommsy

## Gestalt Principles

Một tập hợp rules cho appearance của object.

- Proximity
- Similarity
- Symmetry
- Parallelism
- Closure/Compactness
- Continuity
- Common fate
- Past experience

## Graph-based segmentation

Đồ thị (V, E) với V là tất cả các pixel, mỗi pixel kề cạnh với 4 pixel xung quanh. Tiến hành clustering thành nhiều cụm. Trong quá trình chạy, hai cụm nhỏ sẽ được nối với nhau thành một cụm lớn nếu **Minimum Internal Difference** của *hai* cụm là lớn hơn so với *cạnh nối* hai cụm đang xét tới:

``` python
If edge_{u, v} <= min(ID(C1), ID(C2)):
  merge cluster of u and cluster of v to one cluster
```
Cách tính ID của mỗi cụm C: ID(C) = max(w(e)) + k / |C| với w(e) là cạnh lớn nhất trong minimum spanning tree của C và k là hyperparameter, |C| là kích cỡ của C. Tham số k được dùng để hạn chế kích cỡ của clusters.


## Bio-inspired 2D Object Discovery 

Tư tưởng chính: object sẽ được con người tiếp cận qua 2 mechanism: proto-objects generation và attention to group coherent proto-objects.

Proto-objects generation: thực ra là một cách segmentation của cái ảnh input image, trong paper của Frintrop thì dùng cái graph-based segmentation của Felzenzwalb and Huttenlocher (phần 1 của bài này). Lý do dùng phương pháp này là bởi vì pp này phản ánh 2 Gestalts principles: similarity and proximity.

Attention: thực ra là generate một cái saliency map cho cũng cái input image đấy bằng CoDi như ở bài 7. Dùng CoDi để dễ bề thay đổi tham số :)) khoảng cách giữa 2 Gaussian distribution được tính bằng Wasserstein metric hoặc đơn giản là khoảng cách giữa hai mean.

**Cải tiến (paper T. Werner, G. Martín-García, and S. Frintrop. ): ** cải tiến bước proto-objects generation cho ăn khớp hơn với cái saliency map (more consistent) bằng cách dùng luôn saliency map làm guide cho bước object generation. Ý tưởng là sự tương đồng (similarity) giữa 2 pixels bây giờ tính luôn bằng độ chênh lệch saliency. Vì càng salient thì càng gần nhau nên thay vì làm Minimum Spanning Tree thì giờ dùng Maximum Spanning Tree. Tiếp theo đó, sau khi đã có đống object proposals rồi thì làm tiếp ranking theo Gestalt principles. Phương pháp ranking là Support Vector Regression.

# Active Sensing

Link: CCV11, mincommsy

Phần này chỉ mang tính giới thiệu sơ lược lý thuyết xác suất cơ bản nhất của Active Sensing chứ không có gì đặc biệt. Nhìn chung bài toán Active Sensing cố gắng trả lời câu hỏi: làm sao để thu thập nhiều thông tin hữu ích về môi trường xung quanh một cách nhanh nhất và tốn ít chi phí nhất.

Khi robot hoạt động thì môi trường làm POMDP, cho nên bài toán Active Sensing có mối quan hệ mật thiết với Reinforcement Learning. Từ đầu slide cho tới Decision Processes chỉ nói về MDP và POMDP. Phần Decision theory for active sensing thì dùng Belief Complex để minh họa một cách nhìn về việc update trạng thái của robot, trong đó nhấn mạnh vào việc giảm uncertainty của cái distribution over all possible states. Độ uncertainty được tính bằng công thức entropy quen thuộc. Về mặt hình học, khi entropy giảm thì cũng có nghĩa là vị trí của belief state nằm gần cạnh của cái belief simplex. Nếu take action mang tính exploration nào đó mà làm cho entroy giảm, nghĩa là vị trí của belief chạy về gần cạnh, thì là ổn.
