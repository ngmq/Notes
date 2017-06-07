[Applying Deep Learning to real world projects](https://medium.com/merantix/applying-deep-learning-to-real-world-problems-ba2d86ac5837)

Tut này đề cập tới các vấn đề:

- Dùng pre-trained models để dùng trên bộ dữ liệu có labels đắt đỏ
- Xử lý imbalanced dataset
- Nêu ra 3 điều kiện để một model có thể chạy trong môi trường thực tế:
  - Understand why and how a model can make wrong predictions,
  - Give some intuition why our model can perform better than any previous solution,
  - Make sure that the model cannot be tricked.
  
Tut viết: "This becomes an important challenge in real-world applications as deep neural networks are rapidly entering many areas of our lives: autonomous driving, medical diagnostics, financial decision-making, and many more. Most of these applications directly lead to outcomes that significantly affect our lives, assets or sensitive information. Therefore, wrong decisions by algorithms can hurt people or cause financial damage."

"In real life, generally, you want to understand the reason why your system doesn’t behave as it should."

=> Phần filter visualization là rất quan trọng.

- Công cụ [Picasso](https://medium.com/merantix/picasso-a-free-open-source-visualizer-for-cnns-d8ed3a35cfc5):
  - Trông có vẻ rất ảo, được giới thiệu là để visualize CNN.

Best Kalman Filter explantion: www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/

Anscombe quartet (correlation + outliner): https://en.wikipedia.org/wiki/Anscombe%27s_quartet
