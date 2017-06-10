Link: http://blog.echen.me/2012/03/20/infinite-mixture-models-with-nonparametric-bayes-and-the-dirichlet-process/

# Chinese Restaurant Process:

```python
import numpy as np

def chinese_restaurant_process(no_customers, alpha):
    if no_customers <= 0:
        return []
        
    current_cluster = 0
    res = list()
    cnt = list()
    cnt.append(0)
    
    for i in range(no_customers):
        x = np.random.rand()
        print( "x = ", x )
        if x <= alpha / (alpha + i):
            # new cluster
            current_cluster += 1
            res.append(current_cluster)
            cnt.append(1)
        else:
            # x -= alpha / (alpha + i)
            # for k in range(1, current_cluster + 1):
                # if x <= 1.0 * cnt[k] / (0.0 + cnt[k] + i):
                    # res.append(k)
                    # cnt[k] += 1
                    # break
                # else:
                    # x -= 1.0 * cnt[k] / (0.0 + cnt[k] + i)
                    
            y = np.random.randint(0, len(res))
            k = res[y]
            res.append(k)
            
    return res
    
print( chinese_restaurant_process(10, 1.0) )
# Run 1: [1, 2, 2, 1, 3, 4, 5, 6, 6, 4]
# Run 2: [1, 2, 3, 1, 3, 4, 4, 3, 3, 2]
```

**Nhận xét 1:** Để ý là việc generate cluster mới được thực hiện deterministic (current_cluster += 1). Trong mô hình Bayes ta muốn có một cái prior distribution để generate ra cluster mới tùy thích mới sướng. Điều này dẫn tới Polya Urn Model trong đó cluster mới được sinh ra từ một hàm color_distribution.

# Polya Urn Model: 

```python
import numpy as np
# import matplotlib.pyplot as plt

def uniform_color_distribution():
    return 1.0 * np.random.randint(100) / 100.0
    
def polya_urn_model(color_distribution, no_balls, alpha):
    colors = list()
    
    for i in range(no_balls):
        x = np.random.rand()
        if x <= alpha / (alpha + len(colors)):
            new_color = color_distribution()
            colors.append(new_color)
        else:
            y = np.random.randint(len(colors))
            k = colors[y]
            colors.append(k)
        
    return colors
    
    
print( polya_urn_model(uniform_color_distribution, 10, 3.2) )
# Run 1: [0.4, 0.1, 0.94, 0.94, 0.71, 0.71, 0.71, 0.57, 0.74, 0.94]
# Run 2: [0.14, 0.17, 0.73, 0.73, 0.17, 0.17, 0.17, 0.17, 0.35, 0.17]

```
**Nhận xét 2:** Để ý rằng sự khác biệt giữa Chinese Restaurant Process và Polya Urn Model là CRP chỉ quyết định distribution của clusters thôi (hàm random trả về index của colors, còn cluster mới lúc nào cũng là cluster cũ cộng 1), còn PUM thì quyết định cả distribution của cluster (uniform) và parameters của clusters (ở đây chính là các số 0.14, 0.55 random từ công thức randomint(0, 100) / 100.0).

**Nhận xét 3:** Giả sử ta cho CRP hoặc PUM chạy liên tục không nghỉ. Tới một lúc nào đó khi có quá nhiều bóng trong mỗi cluster rồi và kích cỡ của res trong CRP hoặc colors trong PUM trở nên vô cùng lớn, thì giá trị threshold *alpha / (alpha * len(colors))* sẽ xấp xỉ 0. Điều này có nghĩa là sẽ không có thêm bất cứ clusters mới nào được tạo thành nữa và ta có một sự *hội tụ*, mỗi cluster sẽ có một weight riêng (bằng *nk / (len(colors) + alpha)*) indicate xác suất mà một quả bóng mới sẽ thuộc về cluster đó. Có cách nào randomly sinh ra thẳng được những cái weight này mà không cần phải chạy CRP hoặc PUM liên tục ngày đêm hay không? Câu trả lời là có, chính là **Stick-Breaking Process**.

# Stick-Breaking Process
```python
import numpy as np
# import matplotlib.pyplot as plt

def stick_breaking_process(no_sticks, alpha):
    betas = np.random.beta(1, alpha, no_sticks - 1)
    weights = list()
    last = 1.0
    for beta in betas:
        w = last * beta
        weights.append(w)
        last = last * (1.0 - beta)
    
    w = last
    weights.append(w)
    return weights
    
weights = stick_breaking_process(5, 0.9)
print(np.sum(weights)) # should be 1.0 no matter what
print(weights)
# Run 1: [0.11519179905627835, 0.043693851100807479, 0.27923691462392553, 0.24671585739138038, 0.31516157782760829]
# Run 2: [0.51627208407975589, 0.15467214315560243, 0.065677280324127035, 0.0016998670346014386, 0.26167862540591313]
# Run 3: [0.91932155608029531, 0.019377813599789476, 0.0019257903047440459, 0.033467049442477158, 0.025907790572694014]
```

**Nhận xét 4:** SBP, cũng giống như CRP, chỉ trả về probabilities của distributions (dưới dạng weights) của partitions mà không xác định thông số cụ thể (parameters) của từng partition như là PUM. Tuy nhiên, trong khi CPR là sequential process (từng customer một, người trước người sau) thì SBP có thể được tiến hành in parallel (cứ sample hết mấy giá trị beta cùng lúc là được). 

**Nhận xét 5:** Output của cả 3 tiến trình ở trên đều là random instances of distributions. Khi có thêm base distribution G0 cho SBP và CRP thì ta có một Dirichlet Process hoàn chỉnh. Định nghĩa: Dirichlet Process là distribution of distributions. DP có thể được biểu diễn bởi một trong ba process con ở trên, cái nào không quan trọng, vì với G0 và alpha là đủ để sinh ra cả weights lẫn parameters của các partitions rồi. Thêm vào đó, với cùng một input là số lượng điểm data point (trong các hàm trên là no_balls) thì số partition (số lượng điểm phân biệt trong output) của DP là biến đổi liên tục. Kể từ sau đây, thay vì dùng từ "partition" ta sử dụng từ "cluster" để nói về thuật toán phân cụm (clustering) với Gaussian Mixture Model (GMM) và DP.

# Dirichlet Process for GMM clustering
*Câu hỏi dẫn dắt:* DP với GMM "mang tiếng" là có thể giúp giải quyết vấn đề không cần xác định trước số lượng clusters. DP làm việc đó như thế nào? Trong ba tiến trình đề cập ở trên thì threshold cho việc tạo mới cluster chỉ được quyết định bởi alpha mà thôi. Khi làm thuật toán phân cụm thì ta thấy là chỉ nên tạo cluster mới khi điểm data đang xét cách xa tất cả các điểm còn lại. Vậy, DP mô phỏng tư tưởng cách xa thì nên tạo mới như thế nào?

Từ những bài giảng khác như [Dirichlet Process Mixture Models and Gibbs Sampling by Jordan Boyd-Graber](https://www.youtube.com/watch?v=UTW530-QVxo&t=1216s), ta biết cách làm là bắt đầu từ một cái random assignment và sau đó dùng unsupervised learning technique nào đó để cái assignment đó hội tụ. Trong phần sau ta thử nghiên cứu kỹ về Gibbs Sampling là một technique xử lý việc hội tụ này theo paper 6 trang của MIT: *Bayesian Inference: Gibbs Sampling* của tác giả *Ilker Yildirim* (http://www.mit.edu/~ilkery/papers/GibbsSampling.pdf)

## Gibss Sampling
