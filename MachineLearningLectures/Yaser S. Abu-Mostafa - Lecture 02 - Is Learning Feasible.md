Lecture: https://www.youtube.com/watch?v=MEG35RDD7RA

Phong thái của Prof. Abu-Mostafa gây nhiều thiện cảm cho người học. Cách tổ chức lecture và dẫn dắt, giải thích vấn đề của thầy 
rất chặt chẽ, chu đáo, thể hiện một nhà nghiên cứu say mê lĩnh vực của ông ta và một nội công cửu âm chân kinh cuồn cuộn như sóng biển
của một trong những người sáng lập NIPS.

Quay trở lại với lecture, đây chắc là lecture sinh động nhất về Hoeffding's inequality từ trước đến nay. Tuy nhiên, cách dùng bin topology
với mình cảm thấy không thuyết phục lắm, vì mỗi bin đại diện cho một hypothesis trong cả một rừng hypotheses. Mà cảm giác hypothesis là
"vật sống", có nhiều tính chất toán học phong phú trong khi cái "bin" thì chỉ là một vật hơi đơn giản. Có lẽ cách dạy thẳng vào biểu thức
toán học như lecture note của thầy Ng phù hợp hơn với những người đã từng học qua rồi.

Phần nội dung chính của lecture có nhiều điểm quan trọng với người mới học ML, đặc biệt là phần phân biệt verification và learning ability.
Tuy nhiên như đã nói ở trên, thầy muốn chia Learning Theory thành nhiều buổi cho Bias vs Variance rồi Train and Test nên dừng lại ở 
đấy thì cảm giác vừa thừa vừa thiếu. Điểm tóm gọn lại là công thức cuối cùng của Hoeffding's inequality 

  P( |E_in(x) - E_out(x)| > epsilon) < 2*M*exp(-2*epsilon*N)
  
 Công thức quan trọng này đặt một cận trên cho "bad event" là khoảng cách giữa expected value của in và out lớn hơn epsilon là hữu hạn.
 Tại sao điều này lại chứng minh learning is feasible? Vì cái E_out(x) sẽ đo khả năng "learn" còn E_in(x) sẽ đo khả năng "memorize".
 Xác suất để bad event xảy ra bị chặn có nghĩa là có khả năng là bad event không xảy ra. Mà bad event không xảy ra tức là có hi vọng 
 làm cho E_out gần với E_in. Mà E_out gần với E_in thì có nghĩa là model có khả năng làm việc trên những cái ngoài những thức nó đã nhìn
 thấy, tức là có khả năng học. Vậy kết luận là learning is feasible.
