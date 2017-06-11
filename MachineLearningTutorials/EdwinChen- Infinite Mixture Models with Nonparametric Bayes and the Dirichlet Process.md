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

Từ kinh nghiệm làm K-means và từ những bài giảng khác như [Dirichlet Process Mixture Models and Gibbs Sampling by Jordan Boyd-Graber](https://www.youtube.com/watch?v=UTW530-QVxo&t=1216s), ta biết cách làm là bắt đầu từ một cái random assignment và sau đó dùng unsupervised learning technique nào đó để cái assignment đó hội tụ (một random assignment tương ứng với việc gán randomly các giá trị cho các latent variables, với GMM thì các latent variables là các mean và variance của các Gaussian). Trong phần sau ta thử nghiên cứu kỹ về Gibbs Sampling là một technique xử lý việc hội tụ này theo paper 6 trang của MIT: *Bayesian Inference: Gibbs Sampling* của tác giả *Ilker Yildirim* (http://www.mit.edu/~ilkery/papers/GibbsSampling.pdf)

## Gibbs Sampling in general form

Việc đi tìm phân phối posterior của các latent variables như mean và variance của các Gaussian trong GMM được gọi là [Bayes inference](https://en.wikipedia.org/wiki/Bayesian_inference). Vấn đề kinh điển của Bayes Inference lại vẫn là computational complexity của cái posterior. Công thức Bayes tính posterior là:
    p(latent_vars | observed_data) = p(observed_data | latent_vars) * p(latent_vars) / p(observed_data)
    
Trong đó, cái p(observed_data) = tích phân qua tất cả các possible values của latent_vars. Cái tích phân này không bao giờ tính được. Vậy làm sao để tính được cái posterior đây? 

Câu trả lời: không cần tính mà chỉ cần xấp xỉ cái posterior là được. 

Vì phần trên đã nói tới "hội tụ", ta làm rõ luôn sự "hội tụ" ở đây là hội tụ của distribution. Paper viết ở trang 2: *"However, the theory of MCMC guarantees that the stationary distribution of the samples generated under Algorithm 1 is the target joint posterior that we are interested in (Gilks et al., 1996; also see the Computational Cognition Cheat Sheet on Metropolis-Hastings sampling). For this reason, MCMC algorithms are typically run for a large number of iterations (in the hope that convergence to the target posterior will be achieved)"*

Như vậy, Gibbs sampling cung cấp một phương pháp xấp xỉ cái posterior trong Bayes Inference bằng cách tạo ra các posterior conditional distribution với từng latent variable một, khi làm tới variable nào thì tạm thời coi đống còn lại là constant. Lý thuyết đảm bảo rằng khi sample một số lần đủ lớn thì tất cả đống posterior conditional distributions ấy sẽ trở nên không thay đổi (hội tụ về stationary), và nếu tiến hành sampling lần lượt trên đống conditional distributions ấy, mỗi lần sampling lấy ra một latent variable, thì samples thu được sẽ tương tự như việc sample một lần trên cái posterior. Rất ảo diệu :))

Tuy nhiên đến đây lại có một vấn đề phát sinh: làm sao chắc chắn là cái đống conditional distributions đấy có dạng closed form (i.e well known) để mà sample từ nó? 

Conjugate priors come to the rescue!

Ta lại nhớ lại các bài học về các cặp conjugate priors: khi likelihood là một loại hàm và prior là một loại hàm khác sao cho cặp hai hàm này đặc biệt thì cái posterior nó sẽ có dạng trùng với hàm prior. Như vậy, nếu hàm prior của mỗi latent variable là hàm well known thì nó sẽ làm cho hàm posterior conditional distribution đấy cũng sẽ là hàm well known, và như vậy thì sẽ dễ dàng draw samples từ đó. Kể cả nếu cái hàm posterior conditional distribution mà không well known, nhưng biến latent đang xét là rời rạc và khoảng giá trị không lớn lắm, thì ta có thể tính trực tiếp p(var_rời_rạc_đó | những cái khác) và cho nó thành multinomial distribution, như paper đã làm với biến n ở equation 10.

Full code của ví dụ trong paper (có thể download tại [đây](http://www2.bcs.rochester.edu/sites/jacobslab/cheat_sheet/GibbsSampling.code.py)) :
```python
# Gibbs sampler for the change-point model described in a Cognition cheat sheet titled "Gibbs sampling."
# This is a Python implementation of the procedure at http://www.cmpe.boun.edu.tr/courses/cmpe58n/fall2009/
# Written by Ilker Yildirim, September 2012.

from scipy.stats import uniform, gamma, poisson
import matplotlib.pyplot as plt
import numpy
from numpy import log,exp
from numpy.random import multinomial

# fix the random seed for replicability.
numpy.random.seed(123456789)

# Generate data

# Hyperparameters
N=50
a=2
b=1

# Change-point: where the intensity parameter changes.
n=int(round(uniform.rvs()*N))
print str(n)

# Intensity values
lambda1=gamma.rvs(a,scale=1./b) # We use 1/b instead of b because of the way Gamma distribution is parametrized in the package random.
lambda2=gamma.rvs(a,scale=1./b)

lambdas=[lambda1]*n
lambdas[n:N-1]=[lambda2]*(N-n)

# Observations, x_1 ... x_N
x=poisson.rvs(lambdas)

# make one big subplots and put everything in it.
f, (ax1,ax2,ax3,ax4,ax5)=plt.subplots(5,1)
# Plot the data
ax1.stem(range(N),x,linefmt='b-', markerfmt='bo')
ax1.plot(range(N),lambdas,'r--')
ax1.set_ylabel('Counts')

# Gibbs sampler
E=5200
BURN_IN=200

# Initialize the chain
n=int(round(uniform.rvs()*N))
lambda1=gamma.rvs(a,scale=1./b)
lambda2=gamma.rvs(a,scale=1./b)

# Store the samples
chain_n=numpy.array([0.]*(E-BURN_IN))
chain_lambda1=numpy.array([0.]*(E-BURN_IN))
chain_lambda2=numpy.array([0.]*(E-BURN_IN))

for e in range(E):
    print "At iteration "+str(e)
    # sample lambda1 and lambda2 from their posterior conditionals, Equation 8 and Equation 9, respectively.
    lambda1=gamma.rvs(a+sum(x[0:n]), scale=1./(n+b))
    lambda2=gamma.rvs(a+sum(x[n:N]), scale=1./(N-n+b))

    # sample n, Equation 10
    mult_n=numpy.array([0]*N)
    for i in range(N):
        mult_n[i]=sum(x[0:i])*log(lambda1)-i*lambda1+sum(x[i:N])*log(lambda2)-(N-i)*lambda2
    mult_n=exp(mult_n-max(mult_n))
    # mult_n=exp(mult_n) # still works!
    n=numpy.where(multinomial(1,mult_n/sum(mult_n),size=1)==1)[1][0]

    # store
    if e>=BURN_IN:
        chain_n[e-BURN_IN]=n
        chain_lambda1[e-BURN_IN]=lambda1
        chain_lambda2[e-BURN_IN]=lambda2


ax2.plot(chain_lambda1,'b',chain_lambda2,'g')
ax2.set_ylabel('$\lambda$')
ax3.hist(chain_lambda1,20)
ax3.set_xlabel('$\lambda_1$')
ax3.set_xlim([0,12])
ax4.hist(chain_lambda2,20,color='g')
ax4.set_xlim([0,12])
ax4.set_xlabel('$\lambda_2$')
ax5.hist(chain_n,50)
ax5.set_xlabel('n')
ax5.set_xlim([1,50])
plt.show()
```

Xong, sau khi có (xấp xỉ của) posterior rồi thì làm gì tiếp? Hiển nhiên là có thể làm maximum likelihood để tìm ra bộ giá trị hợp lý nhất cho các latent variables. Với ví dụ trong paper, nhìn vào hình vẽ histogram xấp xỉ distribution ở trang cuối ta thấy là nên chọn lambda1 khoảng 2.98 (giá trị ground truth là 3.074), lambda2 khoảng 8.9 (ground truth là 9.8), n khoảng 26.9 (ground truth là 27)

## Gibbs sampling with Dirichlet Process distributed prior

Note của phần này sẽ combine nội dung từ [Jacob Labs - Computational Cognition Cheat Sheets - Bayesian Statistics: Dirichlet Processes](http://www2.bcs.rochester.edu/sites/jacobslab/cheat_sheet/dpmm.pdf), [Xiaodong Yu - Gibbs Sampling Methods for Dirichlet Process
Mixture Model:  Technical Details](https://pdfs.semanticscholar.org/9ece/0336316d78837076ef048f3d07e953e38072.pdf) và hai PhD Theses giải thích Gibbs sampling cho Dirichlet Processes mà paper đó đề cập là [Nonparametric Bayesian Discrete Latent Variable Models for Unsupervised Learning](http://www.gatsby.ucl.ac.uk/~dilan/papers/gorurDilan_thesis.pdf) và [Graphical models for visual object recognition and tracking](https://dspace.mit.edu/handle/1721.1/34023).

### Probabilistic model of DP
Quay lại cơ bản chút về cơ chế sinh data gồm *n* points của DP: gồm 3 bước. 

- Bước 0: chọn alpha, một số thực, và H, một joint distribution bình thường của các latent variables. Ví dụ với GMM thì H sẽ là joint distribution của mean và variance (hoặc std dev hoặc precision = 1.0 / variance, ko quan trọng).
- Bước 1: Sample một cái *countably infinite discrete multinomial distribution* G từ DP(alpha, G0) (cũng có thể viết là DP(alpha, H), nói chung ký hiệu base distribution là G0 hay H đều ok. Chắc từ đây viết là H cho dễ). 
- Bước 2: Sample *n* điểm gốc (atoms) theta. Trong mô hình GMM, mỗi điểm gốc này tương ứng với một giá trị mean và variance (hoặc precision) của một Gaussian. Dễ thấy là trong *n* điểm gốc này sẽ có những điểm trùng nhau do G là discrete.
- Bước 3: data point thứ *i* được sinh ra từ điểm gốc thứ *i* bằng cách sampling. Hàm F(theta_i) lúc này là hàm Gaussian.

Anw, a picture says a thousand words:
<img src="https://lh6.googleusercontent.com/4oYD0Z_s3zeP0NNAVf6roywiTPQOtrWmt5i2Vh3LIogfn5tL662xyc73y57V7iHlDj9tE93jBGtIHMo=w1599-h700">
(hình cắt từ paper "Computational Cognition Cheat Sheets - Bayesian Statistics: Dirichlet Processes")

Điểm tinh tế ở đây là hàm H có thể chọn đơn giản là tích của phân phối mean và phân phối variance (coi như mean và variance là độc lập). Khi đó ta có thể chọn mean là Uniform còn Variance là  Gamma để đảm bảo conjugate prior. Như vậy thì khi làm sampling tạo ra G, có thể sample độc lập các mean từ Uniform và các variance từ Gamma, miễn sao đảm bảo số lượng mean bằng số lượng variance là được.

Đến đây, ta cũng đã có thể trả lời một cách tổng quát tất cả các câu hỏi dẫn dắt: *1) GP giải quyết vấn đề không chọn trước số clusters hoặc số maximal clusters nhưng trong Bayesian finite Mixture Model (BFMM) bằng cách sử dụng hàm phân phối multinomal G với K tiến tới +oo là prior cho số lượng clusters. 2) Việc ưu tiên tạo ra clusters mới dựa trên hàm distance được thực hiện thông qua việc update hàm posterior cho latent variables: number_clusters, means và variances tương ứng. Lúc quyết định xem nên có bao nhiêu clusters thì chỉ việc làm maximum likelihood trên posterior là xong.*

### Gibbs sampling for DPGMM
