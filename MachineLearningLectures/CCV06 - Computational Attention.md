Link: Cognitive Computer Vision, mincommsy

# Mở đầu
## Lợi ích của Attention:

3 lợi ích chính:

- Process một fraction của input => efficient, suitable for real-time processing
- Support decision making under limited physical components
- Human effect: joint/shared attention

Attention là một hành vi tự nhiên của con người, ai cũng chỉ nhìn vào 1 chỗ trong 1 lúc và tạm thời ko để ý tới chỗ khác. Nghiên cứu attention là đề ra các mô hình tính toán, các giả thuyết về những yếu tố gây ra sự chú ý của mắt người.

## Attention in Computer Vision

- Thường là để giảm computational complexity
- Hai bước chính:
  + Pre-process image by a attention system and find region of interest
  + Process the interested region (e.g object recognition)
  
## Hai loại Attention cơ bản:
- Bottom-up: loại này là kiểu "nhìn một phát để ý ngay": dựa vào color contrast, unique features,...
- Top-down: loại này là kiểu "quan sát": chú ý vào từng phần theo task, motivation, expectation

# Attention và Saliency

## Định nghĩa Saliency

Saliency is "the saliency of an item is the state or quality by which it stands out relative to its neighbors."

Như vậy, saliency tương ứng với bottom-up attention, bởi vì khi nhìn vu vơ thì nói chung là người ta tập trung vào những thứ nổi bật đập vào mắt.

*Thế saliency với attention có phải là một không? Không, bởi vì attention bao gồm cả quá trình xử lý region of interest nữa. Saliency chỉ là một bước trong (bottom-up) attention mà thôi.*

## Saliency Detection

Phần này nhấn mạnh tới hai đối tượng nghiên cứu có sức ảnh hưởng lớn nhất tới computational attention systems: Feature Integration Theory và Guided Search.

*Ý tưởng chính: một region trong ảnh là salient nếu nó sở hữu một tập features (màu sắc, tương phản, orientation, semantic information, objectness...). Không chỉ vậy, các features này là độc lập: ta có thể tính toán chúng song song với nhau và kết quả của feature này không ảnh hưởng tới kết quả của feature khác. Khi ta "ghép" một đống feature này lại với nhau thì được một số thực biểu diễn độ saliency của region đó. Với mỗi feature, tập hợp tất cả feature values của các region trong ảnh được một feature map. Tập hợp độ saliency của các region trong ảnh được một activation map.*

## Lịch sử của Saliency Detection

Lịch sử luôn luôn thú vị. Các mốc chính của saliency detection là:

- 1980: xuất hiện Feature Integration Theory
- 1985: mô hình computational attention đầu tiên, dc gọi là Koch-Ullman model
- 1989-1995: xuất hiện neural network based attention system. Lưu ý rằng 3 năm trước, năm 1986, nhóm nghiên cứu của Geoffrey Hinton đã chứng minh là backpropagation chạy tốt cho neural nets. 
- 1998: open source model đầu tiên: Itti-Koch.
- 2002-2005: cô gái trẻ người Đức S. Frintrop hoàn thành luận văn PhD với VOCUS system.
- 2005: saliency computation trở nên phổ biến trong cộng đồng khoa học
- 2005-2015: thời kỳ nở rộ của giới khoa học, nhà nhà người người tham gia làm saliency với hướng nghiên cứu chính là contrast computation. Một loạt các phương pháp khủng bố được đề xuất: information theory, Bayesian surprise, learning saliency
- 2014: chỉ 2 năm sau khi Google nhận dạng được chó và mèo, cộng đồng deep learning nhảy vào cuộc chiến saliency, với vị thiếu hiệp Convolutional Neural Networks (CNN) võ công cái thế, trấn áp quần hùng.
- 2015: S. Frintrop, lúc này đã là giáo sư tại DH Bonn, cho ra đời VOCUS2
- 2017: xu hướng bây giờ là kết hợp cả deep learning và contrast computation.

Như vậy, trải qua 36 năm (1980-2017), nghiên cứu saliency đã trải qua nhiều thăng trầm. Điều đáng chú ý là theory ra đời từ những ngày đầu cho tới tận bây giờ vẫn còn nguyên giá trị, không có bất cứ nghiên cứu nào của neorosience chối bỏ nó. Mốc lịch sử tiếp theo của saliency sẽ phụ thuộc vào representation learning trong deep neural nets.

# Mô hình Koch-Ullman

# Mô hình Itti-Koch

# Mô hình VOCUS và VOCUS2

# Evaluation
