Tut link (slide): https://www.cs.cmu.edu/afs/cs/academic/class/15782-f06/slides/hebbpca.pdf

Phần này chủ yếu giải thích, làm rõ và chứng minh nhận định được nêu ra trong page 2 của file pdf trên, góc trên bên phải (trang 8):

"In this case, the weight vector will ultimately align itself with the *direction of greatest variance* in the data".

## Hebbian Learning là gì?

Hebbian Learning là thứ đầu tiên về Neural Networks trong môn Bio-inspired Artificial Intelligence mà ai cũng học :)) Trong khóa IAS môn Bio-inspired AI thì nó nằm ở slide số 03: Spiking Neural Networks, trang 29: 

"Hebb rule (1949): Cells that fire together, wire together"

Công thức của nó được viết ở trang 31:

*Hebb rule formalized:* delta_W_ij = x_j * y_i

*Update:* W_ij = W_ij + alpha * delta_W_ij

trong đó *alpha* là một số thực nằm trong đoạn [0, 1]. 

Một cách tổng quát, Hebb rule cho ta biết rằng độ mạnh của synapse kết nối giữa hai neurons sẽ được gia cố hoặc giảm đi một lượng bằng với sự tương đồng của tín hiệu điện đi ra từ hai neurons đó. Nếu hai tín hiệu đó là tương đồng nhau thì độ mạnh kết nối được gia cố, ngược lại thì bị giảm đi.

Đối với artificial neural networks khi cái độ mạnh của synapse được mô phỏng bằng weight, thì sự tương đồng là tích của output của 2 neuron, cùng dấu thì mạnh lên, khác dấu thì yếu đi. Tóm lại Hebb rule rất đơn giản.

## Mối liên hệ giữa Hebb rule và PCA

Trong quá trình tìm hiểu về lý thuyết ẩn sau Deep Learning, một câu hỏi đặt ra là DL học sự độc lập giữa các neuron kiểu gì? Sự độc lập đó là độc lập như thế nào, PCA hay ICA? Phải chăng là mỗi neuron chứa một component của PCA của cái không gian nhiều chiều mà CNN học được? Nếu google tài liệu liên quan giữa neural nets và PCA một lúc, sẽ ra tài liệu như ở phần đầu, trong đó tác giả viết rằng áp dụng Hebb rule đủ lâu lên trên một bộ data đã được centrelized về mean 0 thì cái weight nó sẽ biến thành 1st component của PCA, tức là chiều của weight sẽ trùng với chiều giải thích dc nhiều variance nhất. Đây là một sự liên kết bất ngờ mà mình chưa bao giờ được học.

Hình minh họa từ tài liệu ở trên

## Từ nghi ngờ tới chứng minh
Vì nghi ngờ kết quả này đúng sai thế nào chưa rõ nên ta quyết định là code một cái thí nghiệm nhỏ trong 2D xem có đúng không. Vì tài liệu nói là cuối cùng cái weight nó hội tụ, nên ta mạnh dạn dự đoán là cái variance nó sẽ giảm dần hoặc tăng dần tới một giá trị nào đấy thì không thay đổi nữa. Dĩ nhiên ở mỗi bước ta phải normalize cái weight lại cho nó thành unit vector (i.e norm bằng 1). Code như sau:

```python
# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
 
np.random.seed(1991)

""" Generate randomly 33 data points in 2D and centrelize them (i.e. mean = 0) """
n = 33
x1 = np.random.rand(n)
x2 = -5*(x1) + 3 + 1.5*np.random.rand(n)

print(x1)
print(x2)

X = np.array([x1, x2])
X = X.T
X = X - np.mean(X, axis=0) 

## print(X.shape)

""" Randomly assign weights. No biases is used """
w = np.random.rand(2, 1)
nw = np.linalg.norm(w)
w = w / (nw + 1e-15)

""" Set learning rate and number of iteration """
lr = 0.001
niter = 6905

sumy = []
last_var = 0 ## Variable to check if variance is increasing

for iter in range(niter):
    y = np.dot(X, w) ## [n, 2] * [2, 1] = [n, 1]
    delta = np.dot(y.T, X) ## [1, n] * [n, 2] = [1, 2]
    delta /= n
    delta = delta.reshape(w.shape)
    assert delta.shape == w.shape # For mistake 1
    
    w = w + lr * delta
    nw = np.linalg.norm(w)
    w = w / (nw + 1e-15)
    
    y2 = np.dot(X, w)
    var = np.sum(y2**2) / n
    sumy.append(var)
    if(var < last_var):
        print(iter, "WEIRD!") # For mistake 2. Now I realized the whole thing is just gradient descent
    last_var = var
    
print(np.sum(y2**2) / n)
pca = PCA(n_components=1)
pca.fit(X)
print(pca.explained_variance_[0])


plt.plot(range(niter), sumy, 'b-')
plt.show()

# plt.plot(x1, x2, 'ro')
# plt.show()
```
Output: 
```python
2.17262642904
2.17262642904
```

Hình biểu diễn variance over time:


A ha, đồ thị rất mượt mà trơn tru. Đến đây ta có 2 lưu ý về 2 điểm debug đã giúp ta nhận ra 2 vấn đề:

 - Vấn đề 1: coi chừng dimension broadcasting của numpy
 - Vấn đề 2: nhận ra Hebbian Learning thực ra là gradient descent giải bài toán first component của PCA

Thí nghiệm trên cộng với thói quen viết alpha là learning rate giúp ta nhanh chóng nhận ra Hebbian Learning có dạng giống hệt như một tiến trình gradient descent (GD). Mà đã là GD thì nó phải giải bài toán tối ưu nào đó. Hàm tối ưu là gì? Vì đã biết trước Hebb learning hội tụ về PCA, ta chỉ cần chứng minh hàm tối ưu chính là minimum hàm khoảng cách từ các data points tới đường thẳng của vector W là xong.

Minh họa khoảng cách từ bài viết hướng dẫn SVD của jeremykun (https://jeremykun.files.wordpress.com/2016/02/vectormax.png)

Công thức khoảng cách cho một data point là:

Công thức khoảng cách từ ch18.pdf của cmu (http://www.stat.cmu.edu/~cshalizi/uADA/12/lectures/ch18.pdf)

Viết cho tất cả data point ta có ngay:

**L = -1/n * SUM_over_i_to_n (x_i^T * x_i - (x_i^T * W)^2)**

Đạo hàm theo w:

**dL/dW = -1/n * 2 * SUM_over_i_to_n ( (x_i^T * W ) * x_i )**

**dL/dW = -2/n * SUM_over_i_to_n (y_i * x_i)**

Như vậy Hebbian learning có thể viết lại hàm update là

**W = W - alpha * dL/dW**

Rõ ràng Hebbian learning chẳng qua chính là quá trình gradient descent để tìm first component trong PCA! Chứng minh hoàn tất.

Không thể ngờ là một insight trong biology lại có mối quan hệ toán học đẹp đẽ như vậy với hình học :)
