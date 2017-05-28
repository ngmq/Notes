Link: Machine Learning playlist và Probability Primer playlist của mathematicalmonk

# Một chút căn bản về (multivariate) Gaussian:

- Định nghĩa 1: biến NN n-dimensional X thuộc Gau nếu mọi linear combination bất kỳ của các thành phần của X (x_1, x_2, ...., x_n) thuộc
univariate Gau.
- Định nghĩa 2: biến NN n-dimensional X thuộc Gau nếu ma trận covariance C không suy biến (det(C) # 0) và density của X có dạng
    f(x) = 1/ sqrt(2 * pi * det(C)) * exp(-1/2 * (x - muy).T * C^-1 * (x-muy))
    
- Tính chất 1: nếu X thuộc Gau và x_i, x_j là 2 thành phần bất kỳ của X thì: x_i, x_j độc lập <=> cov(x_i, x_j) = 0

- Tính chất 2 (affine space): nếu X thuộc Gau thì mọi affine transformation của X cũng thuộc Gau. Cụ thể là: gọi A là ma trận [m, n]
bất kỳ và b là vector trong R^m, thế thì A * X + b cũng thuộc Gau (A * muy + b, A * C * A.T). 

- Lưu ý 1: khi m > n hoặc m < n thì tính chất 2 cho phép xây dựng một Gau mới ở chiều lớn hơn / nhỏ hơn n. Khi n = 1 và m > 1 thì 
ta đang đi từ univariate Gau ra multivariate Gau

- Lưu ý 2:  tính chất 2 chính là một trong những thành phần quan trọng làm nên tên tuổi của Kalman Filter.

# Gau Process (GP):
Matlab code: 

% Choose a kernel (covariance function)  
kernel = 6;  
switch kernel     
  case 1; k =@(x,y) 1*x'*y; % Linear      
  case 2; k =@(x,y) 1*min(x,y); % Brownian     
  case 3; k =@(x,y) exp(-1013*(x-y)'*(x-y)) % Squared exponential     
  case 4; k =@(x,y) exp(-1*sqrt((x-y)'*(x-y)))     
  case 5; k =@(x,y) exp(-1*sin(50*pi*(x-y))^2) % Periodic     
  case 6; k =@(x,y) exp(-100*min(abs(x-y), abs(x+y))^2) 
end            
  
  % Choose points at which to sample
  x= (0:.05:1);  n = length(x);  
  
  % Construct the covariance matrix  
  C = zeros(n,n); 
  for i = 1:n      
    for j = 1:n          
      C(i,j)= k(x(i),x(j));     
    end 
  end 
  
  % Sample from the Gaussian process at these  
  u = randn(n,1); % sample u ~ N(0, I) 
  [A,S, B] = svd(C); % factor C = ASB' 
  z = A*sqrt(S)*u; % z = A S^.5 u  
  
  % Plot  
  figure(2); hold on; clf 
  plot(x,z,'.-') 
  axis([0, 1, -2, 2])
