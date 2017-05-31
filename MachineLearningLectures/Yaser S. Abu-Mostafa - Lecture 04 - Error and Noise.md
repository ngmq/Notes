Link lecture: https://www.youtube.com/watch?v=L_0efNkdGMc&index=4&list=PLD63A284B7615313A

[9:06 - 9:30] His joke about driving and truck analogies cracks me up :)) He seems to be enjoy it very much too :))

[25:50 - 29:20] The "two types of error" is really informative, it underscores the importance of loss function 
and the need for customized loss function in ML systems.

[34:40] Khi loss function không được nhận từ users thì có hai alternatives là:
  - Plausible measures: squared error = Gaussian noise. Cái này có vẻ nhiều người ngại giải thích nhưng thực ra viết ra khá là ngắn. 
  Phần này cũng làm mình nhớ lại lecture trong lớp Non-parametric Statistics khi giải thích ý nghĩa của việc chọn hàm weight function
  cho cái NW estimation. Cụ thể như sau: model của regression là y = m(x) + noise, trong đó noise là white noise (mean = 0, variance = S)
  chẳng hạn. Cực đại hóa likelihood function, ta có:
      Likelihood = Tích các p(y_i | x_i) với i từ 1 đến n, n là tổng số sample
      log(Likelihood) = Tổng các log(p(y_i | x_i))
      Mà p(y_i | x_i) = công thức Gauss = 1/sqrt(2*pi*S) * exp( -1/2 * (y_i - m(x_i))^2 / S )
      nên 
      log(Likelihood) = Tổng của: log( exp( -1/2 * (y_i - m(x_i)) )^2 + N * log(1 / sqrt(2*pi*S))
                      = Tổng của: -1/2 * (y_i - m(x_i))^2 + Constants
                      
      Qua vài dòng biến đổi thì đến đây thấy ngay là muốn có maximum likelihood thì phải minimum cái tổng độ lệch bình phương
      
      
  - Friendly measures: closed-form solution, convex optimization: cái này thì rõ ràng là tiện lợi rồi, nhưng thực tế thì hầu như
  không có. Lý do là để có convex optimization thì phải đặt thêm nhiều constraints, mà giải đống constraints đấy thường cũng là
  intractable
