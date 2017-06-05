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
  
# Additional link: http://blog.sigopt.com/post/130275376068/sigopt-fundamentals-intuition-behind-gaussian

Trích đoạn: 
"At SigOpt, we focus on a slightly different problem than simply understanding what our process looks like: we want to find the location at which this process is maximized. When drilling for oil this can consist of finding the latitude/longitude/depth where the most profitable well is expected. When implementing a machine learning algorithm, this can consist of optimizing the learning strategy so as to make the best recommendations for your customers; our client Sonica uses this to more accurately make song predictions for their users. When developing physical products, this can consist of choosing the chemical quantities which produce the desired product at the minimum cost; our client Advent Lab Group Northwest has used this strategy to better design shaving cream.

In each of these situations, expert knowledge is required to build the underlying system we are attempting to optimize, whether that is an oil rig, machine learning model, or cosmetic product. Once the system is built, finding the best variation of that system is often a non-intuitive process that is commonly performed inefficiently via brute force trial and error. In contrast, SigOpt leverages techniques like Gaussian Processes to provide a guided search through the complex space of possible parameters. This allows experts to build the next great model and apply their domain expertise instead of searching in the dark for the best experiment to run next. With SigOpt you can conquer this tedious, but necessary, element of development and unleash your experts on designing better products with less trial and error."

Thì ra GP có ứng dụng rộng rãi và quan trọng khủng khiếp như thế, thảo nào bác Kevin P. Murphy dành hẳn một chương trong sách về nó.
  
  
(ML 19.5) Positive semidefinite kernels (Covariance functions) 

- k(x, y) = f(x - y): "stationary kernel" => (x, y) and (x+a, y+a) has the same k
- k(x, y) = f(|x - y|): "isotrophic" 

(ML 19.6) Inner products and PSD kernels 

Mercers' theorem: under "fairly general" conditions, any positive semidefinite kernel can be represented in some Hilber space.


# GP for Regression
Xét bài toán con sau đây: Cho một mô hình Z ~ N(muy, K) in R^n và epsilon ~ N(0, sigma^2 * I) in R^n indepedent, và biến phụ thuộc
    Y = Z + epsilon
    
Ta được cho m (m > 0) giá trị (Z1, Y1), (Z2, Y2), ..., (Zm, Ym). Khi có một giá trị mới Z' thì Y' tương ứng thuộc phân phối như 
thế nào?

Dễ thấy là Y ~ N(muy, K + sigma^2 * I). Chứng minh được là phân phối có điều kiện (Y'|Z_1..m, Y_1..m) là phân phối chuẩn N(m, D)
trong đó m, D đều tính được ngay (công thức quá phức tạp, xem trong video 19.10)

Áp dụng sang GP: Chọn mean function và covariance function muy(x) và K(x), ta được một GP với Z(x) đóng vai trò hệt như Z ở trên.
Từ đó ta có một phân phối xác suất của Y'. Để làm inference thì ta chọn hàm loss (ví dụ như log likelihood) và dùng phân phối xác suất
vừa tìm được để cực tiểu hóa hàm loss tương ứng.
