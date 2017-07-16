Link Gabor Filter: CCV 03, mincommsy
Link Human Attention: CCV 05, mincommsy

# Gabor Filter

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


