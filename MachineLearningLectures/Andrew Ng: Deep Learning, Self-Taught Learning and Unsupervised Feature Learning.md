Lecture: https://www.youtube.com/watch?v=n1ViNeWhC24

Live note:

[4:53]  Ý nghĩa của các số trong lớp "Sum up edge strength in each quadrant", ví dụ số 0.7 được giảng là "density" của vertical tương ứng trong nửa phần tư ở góc top-right của bức ảnh xe máy.

[6:00 - 10:00] Hand-crafted features đòi hỏi expert knowledge và nói chung là time-consuming. Trong NLP có vị trí của Noun Phrase, trong Vision có SIFT, trong Speech có MFCC. Mà chính vì đòi hỏi expert knowledge và time consuming nên muốn có đột phá về performance thì mất nhiều thời gian để cải tiến hoặc nghĩ ra cái mới.

[22:11] Sparse coding: vào thời điểm sparse coding ra đời, nó chỉ là một theoretical model trong neuroscience. Các tác giả (Olhausen and Field) không hề nghĩ là sparse coding sẽ được sử dụng cho machine learning. Mô hình sparse coding là:

- Input: có $m$ ảnh images đánh số từ $1...m$ là $x^1, x^2, ..., x^m$ có kích cỡ $R^{n x n}$
- Learn: bộ não sẽ tự học một bộ "từ điển" chứa $k$ các thành tố cơ bản (cùng kích cỡ $R^{n x n}$) \phi_1, \phi_2,...\phi_k của các bức ảnh sao cho mỗi bức ảnh ban đầu có thể được xấp xỉ như là linear combination của các thành tố này:
    $x^i = \sum_j a_j * phi_j
    mà với mọi $i$, hầu hết các a_j bằng 0 (sparse)
