Link: Machine Learning playlist và Probability Primer playlist của mathematicalmonk

# Một chút căn bản về (multivariate) Gaussian:

- Định nghĩa 1: biến NN n-dimensional X thuộc Gau nếu mọi linear combination bất kỳ của các thành phần của X (x_1, x_2, ...., x_n) thuộc
univariate Gau.
- Định nghĩa 2: biến NN n-dimensional X thuộc Gau nếu ma trận covariance C không suy biến (det(C) # 0) và density của X có dạng
    f(x) = 1/ sqrt(2*pi*det(C)) * exp(-1/2 * (x - muy).T * C^-1 * (x-muy))
    
- Tính chất 1: nếu X thuộc Gau và x_i, x_j là 2 thành phần bất kỳ của X thì: x_i, x_j độc lập <=> cov(x_i, x_j) = 0
- Tính chất 2 (affine space): nếu X thuộc Gau thì mọi affine transformation của X cũng thuộc Gau
