Link Gabor Filter: CCV 03, mincommsy
Link Human Attention: CCV 05, mincommsy

# Difference of Gaussian, Gabor Filter và Orientation Pyramid

## Difference of Gaussian

Rất phổ biến, sinh ra không gì khác là để mô phỏng center-surround và surround-center On/Off nổi tiếng. 

Có thể tính nhanh vì là seperable, do đó được ưa chuộng rộng rãi để xấp xỉ Laplacian filter.

Điểm đáng chú ý là biểu thức toán học của DoG không nói gì tới màu sắc, cho nên DoG thuần túy chỉ có thể áp dụng cho ảnh Black-White contrast mà thôi. Muốn áp dụng DoG cho R-G và B-Y thì trước tiên phải convert ảnh sang hệ Lab trước, lúc này L đại diện cho B-W, a đại diện cho R-G và b đại diện cho B-Y.

Lab là hệ màu perceptually uniform, có nghĩa là mắt người cảm nhận sự thay đổi tuyến tính: khoảng cách giữa 2 màu với nhau có ý nghĩa uniform trên toàn bộ hệ màu.

## Gabor filter
Cũng giống như các loại filter khác trong computer vision, khi tìm hiểu Gabor filter thì câu hỏi quan trọng nhất là: pattern gì? Mỗi loại filter sẽ có phản ứng với pattern nhất định. Câu hỏi tiếp theo là: biể thức toán học của pattern đấy là gì? Phải có biểu thức toán học thì mới có thể nghiên cứu được. Câu hỏi tiếp theo và cũng là cuối cùng: tính toán hoặc xấp xỉ biểu thức toán học đấy như thế nào? 

### Pattern gì?

Nếu như Difference of Gaussian (DoG) là để phát hiện pattern center-surround và surround-center kinh điển ("concentric receptive fileds") trong ganglion cells ở Retina, thì Gabor filter được phát triển là để phát hiện pattern về hướng (orientation) ("elongated receptive fields") như trong simple và hypercomplex cells ở V1. Cũng vì thế nên ta phải chuẩn bị cho một biểu thức toán học cũng "hypercomplex" thì mới đáp ứng được nhu cầu. 

Xem hình vẽ ở slide số 28 (trang 23 pdf) để có hình dung về cách loại enlongated receptive fields mà Gabor filter có thể mô phỏng.

### Biểu thức toán học gì?

Slide số 31 cho ta đồ thị của cái filter mà ta mong muốn, và hình vẽ ở bên phải là hình chiếu của cái filter đó lên mặt phẳng Oxy (giả sử chiều cao lồi lên lồi xuống là trục Oz). Lưu ý là filter ta mong muốn có dạng: ...-lõm-lồi-lõm-lồi-lõm-... cứ lồi lõm đan xen nhau, càng ở giữa thì độ lệch lồi lõm càng lớn, khi đi ra tới rìa thì giảm dần và gần như là ko thay đổi. Các đoạn lồi lõm phải smooth (có đạo hàm liên tục) để tiện cho việc tính toán. Các nhà toán học đã tìm ra biểu thức cho hàm số như vậy là:

Gabor(x) = Gauss(x) * Sinusoid(x)

Trong đó hàm Sinusoid có thể là sin, cos hoặc tổng cos + i\*sin. Phép nhân ở trên là phép nhân đại số bình thường.

Nếu lấy hàm sin thì ta sẽ được một hàm lẻ, vì sin(-x) = -sin(x). Ngược lại lấy hàm cos sẽ được hàm chẵn. Vì vậy mà thường thì chỉ dùng một trong 2 loại là đủ để mô phỏng loại pattern ta mong muốn. Nếu pattern đối xứng (symmetric) thì dùng hàm chẵn, ngược lại dùng hàm lẻ. Biểu thức toán học sẽ là:

Gabor_odd(x) = [1/sqrt(2\*pi\*sigma^2) * exp{-x^2 / (2\*sigma^2)}] * [sin(2\*pi\*omega_0\*x)]
Gabor_even(x) = [1/sqrt(2\*pi\*sigma^2) * exp{-x^2 / (2\*sigma^2)}] * [cos(2\*pi\*omega_0\*x)]

Mở rộng sang 2D:

Gabor_odd(x) = [1/(2\*pi\*sigma_x^2\*sigma_y^2) * exp{-x^2 / (2\*sigma_x^2) - y^2/ (2\*sigma_y^2)}] * [sin(2\*pi\*omega_x_0\*x + 2\*pi\*omega_y_0\*y)]

Gabor_even(x) = [1/(2\*pi\*sigma_x^2\*sigma_y^2) * exp{-x^2 / (2\*sigma_x^2) - y^2/ (2\*sigma_y^2)}] * [cos(2\*pi\*omega_x_0\*x + 2\*pi\*omega_y_0\*y)]

Nói chung khi đã viết dc cho 1D thì mở rộng sang 2D đơn giản. Lưu ý khi sang 2D thì phải là sin của tổng chứ không phải là tổng của sin, lý do là x, y thay đổi cùng nhau.

Gabor filter là xấp xỉ linear, theo http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/TRAPP1/filter.html. 

### Tính hoặc xấp xỉ thế nào?

Gabor filter thường được tính trực tiếp và không cần xấp xỉ.

## Orientation Pyramid

Chính là kết quả giống như trong excercise: Gaussian pyramid => Laplacan pyramid => Orientation pyramid.

# Human Attention

## Inattentional blindness

Đây là khái niệm "mù vô ý": bởi vì people chỉ có thể perceive những gì người ta tập trung vào ("pay attention please!") cho nên khi ngta không tập trung một phát thì là "mù" ngay, không thể nhận ra những sự thay đổi (changes) diễn ra ngắn. Ví dụ về những sự thay đổi đó là flashed blank screen, an eye movement, a cut from one view to another in a movie...

## Attentional Beam

"Tia chú ý" - khi bạn "tia" vào cái gì thì bạn sẽ tập trung năng lượng vào nó. Điểm bị tập trung vào được gọi là focus of attention (FOA). Câu hỏi đặt ra là cơ chế nào điều khiển cái tia chú ý này? Rõ ràng là trong cuộc sống thì con người ta không chú ý bừa mà thường thì sẽ nhìn đi nhìn lại một vài điểm nào đó "đáng chú ý". Giả thiết đặt ra là có một cơ chế "pre-attentive" chạy song song với attention. Slide số 8 viết:

**There is a parallel, pre-attentive processing step that guides the attentional beam to regions of interest.**

Dễ thấy là tiến trình pre-attentive này phải chạy song song với tiến trình attention. Lưu ý là bản thân tiến trình attention là một chuỗi (serial) dịch chuyển từ điểm này qua điểm khác.

Đặc điểm của quá trình pre-attentive là:
- không chủ đích (unconsiously)
- tự động (automatically)
- không tốn nhiều sức lực (effortlessly)
- diễn ra ngay khi con người nhìn thấy input mới (early in the perceptual process)
- và tất nhiên, song song (parallel)

Dễ thấy là các điểm FOA phải có gì đó đặc biệt thì nó mới là FOA :)) "Cái gì đó đặc biệt" đó là features. Như vậy để tìm ra FOA thì các features phải được nhận biết một cách tự động, song song và không chủ đích. Nhưng nhận biết features không chưa đủ mà còn phải gộp các features đó lại, tại vì một điểm chỉ đặc biệt khi nó sở hữu một tập features nào đó. Hai cơ chế nhận biết và gộp features này trở thành tiền đề cho thuyết Tích hợp Đặc điểm: Feature Integration Theory (FIT)

# Feature Integration Theory

FIT có 3 điểm chính:
1. **Features are processed independently in parallel in the brain (one brain area for color, one for motion, one for oriented edges, etc.) (pre-attentive stage)**
2. **Attention is required to glue features together**
3. **A “Master map of Locations” collects the discontinuities in each of the feature maps**

Điểm 1 và 2 đã nói ở trên. Điểm 3 nghe có vẻ rất khó hiểu nhưng thực ra ko có gì. Discontinuities của feature maps chính là các vị trí mà feature thay đổi trên cái map đấy. Khi feature thay đổi thì FOA cũng có nhiều khả năng là sẽ thay đổi, nên khi gộp feature thì phải có một cái map. Lấy ví dụ, nếu có một khu vực màu xanh hình vuông rất to kích cỡ 50 x 50 trong map blue, và ở map green có một hình vuông nhỏ kích cỡ 10 x 10 cùng vị trí đấy (ở map green xung quanh hình vuông 10 x 10 là rìa màu đen). Thế thì khi gộp feature, chắc chắn là phải lấy hình vuông cỡ 10 x 10 trên ảnh gốc làm điểm chú ý, bởi vì "discontinuities" xảy ra với 10 x 10 có ý nghĩa hơn là 50 x 50. 

Lý thuyết FIT phù hợp với findings trong neuroscience, như là color processing chủ yếu thực hiện ở V4, motion processing thì ở V5/MT, nói chung là diễn ra song song. 

**Mô hình Koch-Ullman**

Map of location ở trên được chuyển thành saliency map trong mô hình Koch-Ullman. Mô hình này được nói kỹ hơn trong bài số 6.

Điều thú vị là những nghiên cứu gần đây có vẻ chỉ ra là quả thực trong V1 của não người có một cái saliency map :))

## Feature search

Phần này nội dung khá đơn giản, phân biệt search complexity và chia làm 2 loại: Feature search và Conjunction search. Feature search là khi điểm cần search (target) differs from the distractors by a unique feature. Conjunction search is when the target differs from the distractors by a conjunction of features => search is much slower.

# Guided Search model

Slide viết "Wolfe developed his Guided Search model as a response to Treisman’s Feature Integration Theory". Thực sự là không hiểu "response" ở đây có nghĩa là gì, chắc ý là cái model sẽ áp dụng ("apply") cái theory đó?

Về mặt kỹ thuật, GS model khác với K-U model ở nhiều điểm cơ bản. Thứ nhất là về mục đích: K-U model phục vụ cho attention nên có cả Winner Take All, còn GS thì chỉ phục vụ cho saliency thôi nên chỉ có tới activation map là hết. Thứ hai là về kiến trúc: GS model phân tách rạch ròi giữa bottom-up saliency map và top-down commands. Đây có thể xem là một bước tiến về mặt tư tưởng. 

Lưu ý là GS model vẫn nhằm phục vụ mô hình hóa quá trình pre-attentive, chưa có một process gì nặng nề kiểu như object classification hay scene understanding ở đây cả. Process nặng đó thuộc về attention.

Việc tách rạch ròi top-down signal khỏi bottom-up cũng dẫn tới hệ quả nêu ra ở slide số 37: "highly salient regions “capture”
the attention regardless of the task (emergency bell)". Bất kể task là gì, những cái highly salient sẽ liên tục draw attention từ mắt người.

# Inhibition of Return

Lý do ra đời của IoR rất tự nhiên: câu hỏi là nếu cái điểm trước nó đã salient như vậy, thì cơ chế nào để di chuyển sang điểm salient tiếp theo mà tránh liên tục quay trở lại chú ý vào điểm trước? Phải "inhibit" cái điểm mà ta đang nhìn vào, và cơ chế "inhibits the currently fixated region" được gọi là IoR.

Rõ ràng là IoR phải xảy ra sau khi attention, nghĩa là sau khi đã process xong cái đang nhìn vào là cái gì, làm được gì rồi thì mới move sang điểm khác. Tổng cộng là có 3 quá trình diễn ra liên tục, gần như song song: Pre-attention, Attention và IoR. 

# Saccades, Overt attention, Covert attention

Phần này nói chung ko có gì, chủ yếu là học khái niệm. Saccade là hành động di chuyển mắt nhìn vào một điểm gì đó. Điểm đáng nói là cái ta nhìn vào chưa chắc đã là cái ta chú ý tới, vì vậy mới sinh ra hai kiểu overt (mắt trùng attention) và covert (mắt nhìn một nơi, attention một nẻo).

# Summary

Trong bài này ta tìm hiểu chủ yếu về các khía cạnh psychological của attention. Các mô hình computational system hiện nay được xây dựng theo 3 mechanism: pre-attentive bằng bottom-up saliency có thể kết hợp top-down, attention trong đó xử lý input và Inhibition of Return để tính toán điểm tập trung tiếp theo. Quá trình pre-attentive được xây dựng dựa theo lý thuyết Feature Integration Theory trong đó khẳng định não người có các vùng xử lý song song để bóc tách features về colors, motion cùng lúc, sau đó gộp lại thành một cái map. Koch-Ullman model xử lý cụ thể khía cạnh thuật toán để implement FIT. Guided Search model mở rộng Koch-Ullman model trên bằng việc giới thiệu top-down signal cho quá trình saliency. Toàn bộ sơ đồ của việc tích hợp saliency system vào attention system có thể xem ở bài CCV 06.


