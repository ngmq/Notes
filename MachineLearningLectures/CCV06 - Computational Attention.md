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

# Các mô hình tính toán

Ba mô hình được đề cập trong slide: Koch-Ullman (lý thuyết chính), Itti-Koch (code, thêm phần top-down), VOCUS và VOCUS2 (cải tiến, lắp ráp thêm)

## Mô hình Koch-Ullman
Ngược dòng thời gian về năm 1985 để tìm hiểu xem Koch và Ullman (lúc đó 2 bác này đang làm ở MIT) đã đề xuất mô hình như thế nào để áp dụng Feature Integration theory. Paper: https://cseweb.ucsd.edu/classes/fa09/cse258a/papers/koch-ullman-1985.pdf.

<Hình vẽ slide số 15>

Bên cạnh feature integration, điểm đáng chú ý nữa trong mô hình kể trên là Winner-Take-All selection. WTA cố gắng giải bài toán *tìm phần tử lớn nhất với locally connected architecture*.

<Hình vẽ slide số 73>

**Bài toán: cho mảng a[], tìm vị trí của phần tử lớn nhất bằng mạng neuron locally connected kiểu pyramid, mỗi neuron chỉ lưu được 2 trạng thái 0 và 1. Độ phức tạp cần thiết là O(logn), vì mảng a thay đổi liên tục.**

**Lời giải của WTA network**

Dùng 2 mạng neuron: mạng màu vàng lưu trạng thái của a[i], mạng màu xanh lưu trạng thái của index i.

Neuron màu vàng sẽ activated (trạng thái 1) nếu giá trị của nó lớn hơn giá trị của neuron connect với nó.

Neuron màu xanh sẽ activated, nếu neuron vàng gắn với nó activated và neuron xanh ở trên nó activated.

Dễ thấy là về cơ bản mỗi mạng xanh và vàng là một cây nhị phân cân bằng, độ phức tạp của forward pass tìm phần tử lớn nhất và backward pass tìm vị trí của phần tử đó đều bằng chiều cao cây, cho nên độ phức tạp sẽ là O(logn).

WTA của Koch-Ullman đúng là rất đơn giản nhưng cũng rất thú vị. Về sau VOCUS model cũng làm WTA và có thay đổi một chút.

Lưu ý là Koch-Ullman hồi ấy chỉ nêu thuật toán chứ không có code.

## Mô hình Itti-Koch

<Hình vẽ slide số 16>

Là bản cài đặt của Koch-Ullman, ra đời mãi tận 13 năm sau (chắc cụ Koch mải chọn ngôn ngữ để cài đặt, điều thú vị là C++ cũng ra đời năm 1985). Trong model có cài đặt cụ thể central-surround contrast, intensity, orientation, colors...và có cả top-down attentional bias, đây chính là điểm mới so với Koch-Ullman là chưa có tín hiệu top-down. 

## Mô hình Attention chung

<Hình vẽ slide số 19>

Gồm 7 bước chính, được rút ra từ Itti-Koch model:

1. Tính các feature channels
2. Scale representation
3. **Center-surround contrast (most important!)**
4. Fusion
5. Maximum Finder
6. Inhibition of Return
7. Top-down influence

## Mô hình VOCUS và VOCUS2

Saliency systems: bước từ 1 tới 4 của attention system.

Khác biệt với Itti: 

- Bước số 1: dùng color space khác.
- Bước số 2 và 3: nhiều scale hơn nhiều. Lý do có thể áp dụng nhiều scale là bởi vì VOCUS system trừ Gauss của hai pyramid khác nhau, còn Itti trừ Gauss của cùng một pyramid.
- Bước số 4: fusion khác (e.g. uniqueness...)

Khác biệt giữa VOCUS2 và VOCUS:

VOCUS2 có thêm bước 3.5 là tính map cho orientation và motion. Thực ra VOCUS cũng có motion nhưng ko hiệu quả, làm giảm performance nên ko dc cho vào.

### Cách tính center-surround contrast cho L, a, b
### Cách tính motion
### Cách làm trajectory inference

# Evaluation

Nội dung giống hệt như exercise. Dataset phổ biến là MSRA, MIT, PASCAL VOC,... Cách làm vẫn là generate ra saliency map rồi cho threshold chạy, sau đó tính Precision và Recall. Khi tính precision và recall thì "positive" data chính là salient pixel. Tất nhiên là tính cả F1, rồi thì AUC,...
