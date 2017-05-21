Lecture: https://www.youtube.com/watch?v=n1ViNeWhC24

Live note:

[4:53]  Ý nghĩa của các số trong lớp "Sum up edge strength in each quadrant", ví dụ số 0.7 được giảng là "density" của vertical tương ứng trong nửa phần tư ở góc top-right của bức ảnh xe máy.

[6:00 - 10:00] Hand-crafted features đòi hỏi expert knowledge và nói chung là time-consuming. Trong NLP có vị trí của Noun Phrase, trong Vision có SIFT, trong Speech có MFCC. Mà chính vì đòi hỏi expert knowledge và time consuming nên muốn có đột phá về performance thì mất nhiều thời gian để cải tiến hoặc nghĩ ra cái mới.

[] Prof. Ng nói rằng hướng phát triển tiếp theo sẽ là Unsupervised learning.Tuy thầy chưa nói tới model nào cụ thể nhưng ai cũng biết là unsupervised learning được dùng rất nhiều để initialize các layer trong một mạng DNN. Trong phần sau nói về sparse coding nên có thể dự đoán các phương pháp dimensionality reduction sẽ được nhắc tới rất nhiều.

[22:11] Sparse coding: vào thời điểm sparse coding ra đời, nó chỉ là một theoretical model trong neuroscience. Các tác giả (Olhausen and Field) không hề nghĩ là sparse coding sẽ được sử dụng cho machine learning. Mô hình sparse coding là:

- Input: có $m$ ảnh images đánh số từ $1...m$ là $x^1, x^2, ..., x^m$ có kích cỡ $R^{n x n}$
- Learn: bộ não sẽ tự học một bộ "từ điển" chứa $k$ các thành tố cơ bản (cùng kích cỡ $R^{n x n}$) \phi_1, \phi_2,...\phi_k của các bức ảnh sao cho mỗi bức ảnh ban đầu có thể được xấp xỉ như là linear combination của các thành tố này:
    $x^i ~ \sum_j a_j * phi_j
    mà với mọi $i$, hầu hết các a_j bằng 0 (sparse)

[] "Được xấp xỉ" là một cụm từ quan trọng. Tại sao không tìm đống bases mà có thể khôi phục cả bức ảnh thay vì chỉ "xấp xỉ"? Ý nghĩa ở đây là mỗi bức ảnh chỉ chứa một cụm các features quan trọng mà thôi, cho nên ANN chỉ cần học được đống bases đấy là đủ rồi (một chút liên tưởng tới Overfit và Underfit0

[] Sparse coding in ANN: ANN đã học được edge filter giống như bộ não con người trong neuroscience.

[30:00] Brief mention about Independent Component Analysis. 

[31:14] Hierarrchical representation. Ở trên ta đã có ANN học edges từ image, ta tiếp tục cho nó học objects từ edges.

[35:13] Spectra of audio signal (Phổ của tín hiệu âm thanh). Một câu hỏi rất quan trọng sau khi đã code ra một hệ thống ML là: ừ thì performance của nó là 60-70-80-90% đấy, nhưng thực sự thì nó đã học cái gì? Muốn trả lời câu hỏi ấy thì phải trả lời câu hỏi: bases là gì? Ta đã biết rằng với ảnh thì ta có thể kiểm tra xem có neurons nào học được edges filter không, thế với tín hiệu âm thanh thì sao? Slide ở 35:13 trả lời câu hỏi này: bases là dải tần số, có thể tạm coi là một đoạn nhạc cơ bản (giống như edge là một hình vẽ cơ bản). Ta lại refer đến bài viết cực hay về áp dụng CNN lên music của tác giả Sander Dieleman ở đây http://benanne.github.io/2014/08/05/spotify-cnns.html. Slide ở 35:34 nói thêm "Many bases seems to correspond to phonemes".

Đến đây ta có thêm 1 suy nghĩ là việc học cách nhìn vào từng neuron một (ví dụ ở mạng CNN) xem nó học cái gì không chỉ có ý nghĩa trong việc debugging: kiểm tra xem nó có học features có ý nghĩa không hay là chỉ học noise, mà còn có ý nghĩa giúp người phát triển hệ thống học ngược lại từ nó để xem features nào quan trọng mà con người chưa nghĩ đến. Ví dụ ở trên con người đã biết về edges và phonemes là những thành tố cơ bản cấu tạo nên bức ảnh và âm thanh. Thế nếu có những thành tố cơ bản khác mà con người chưa điểm mặt đặt tên được nhưng ANN đã tự phát hiện ra thì sao? Rõ ràng là rất ý nghĩa.

[Cuối video] Bác Ng có nói là "I'll take credits for bringing GPU into deep learning world" -> không ngờ bác Ng chính là người trùm sò vụ này :))
