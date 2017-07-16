Link: CCV lectures, mincommsy

# General ideas

- Vision is not as easy as we think.
  + Page 7: Is "the whole" the summary of the parts? [Image: R. Magritte, LeBlanc-Seing, 1965]
  + Page 8: How many chairs are in this image? [Image: Bülthoff, http://www.kyb.tuebingen.mpg.de/de/forschung/abt/bu/recat.html]
  + Page 9: scary skull-liked Santa
- Vision is task dependent.
  + Picture with lots of objects and humans: where should we look at?
- Visual perception needs context and possibilities
  + Well-structured buildings or not? [Images: M.C.Escher, left: Waterfall, 1961, right: Belvedere, 1958]
  + The famous Ames room
  
# The HVS
  
## Visual field
  
(Page 18)
The whole area that we see is called *visual field*.
Right eye and left eye each has its own visual field too. Imagine how one-eyed people see the world. Let's call them right visual field and left  visual field.
Then each of the left and right visual field is divided further into two halves that are called **hemifield**.

So the left hemifield of each eye is viewed by the right hemisphere of the brain, and vice-versa. It's not hard to see why by looking at the picture at page 18.

Remember the optic chiasm: it distributes (in VNese: "chia") the optic signals from the eyes to different parts of the brain. That signals go all the way to the primary visual cortex, also known as V1, in the back of the brain.

## Neurons

We are all familiar with neurons - IAS students should have seen them at least three times: in Bio-inspired AI lectures, in Knowledge Engineering lectures and in Neural Networks lectures. Each neuron is connected to other neurons via its axon. The connecting part between one axon and one neuron is synapses. How they encode information? many ways, could be rate coding, activation coding, timing coding.

## The human eye

The diagram in page 25 shows components of an eye. Our question is, how are the visual signals encoded in our eyes? Which components of the eye should we focus on to answer that question?

Answer: we don't have time to learn all of them, but we should definitely learn about the retina, the LGN and the visual cortex (V1 and all the other Vs)

## The Retina

- What is it?
  + A light-sensitive surface ("bề mặt") at the back of the eye
  + That surface is covered with photo-receptors (sensory neurons). We know light has photons, so probably the name comes from photo(n)-receptors.
  + Sensory neurons consist of Rods and Cones (R-C, like Ross and Chandler). Rods are light sensitive, not color sensitive. Cones are color sensitives. There are about 120 million rods, but only 7 million cones. I guess that's because light sensitivity is much more important than color sensitivity: black and white TVs were made much earlier than colored TVs.
  + So what do the little guys R and C do? "Task of photoreceptors: change the electromagnetic energy ("năng lượng điện từ") of photons into visual activity as need by neurons." A ha! So these guys do all the hard work.
  + Are they uniformly distributed over the retina? No, and that's where things get interesting. Distribution of R and C is showed in page 27. The area with no Rods and densely packed Cones is the **Fovea** ("điểm tiêu cự"). We all know very well from high school physics that the fovea is where all the incoming light rays end up after reflecting on the lens. Therefore,  the fovea is responsbile for "sharp central vision".
  + What that means is when we focus on different visual field around us, we are changing the input to the fovea. Since we only have one fovea, we can only gaze at one region at one time.
  
 - The Cones: we are trying to make sense of the color channels (RGB) and what the cones actually do here
  + 03 types of cones: long-wavelength (Red), middle-wavelength (Green) and short-wavelength (Blue)
  + They are the source of trichromatic theory of color vision: all colors are made of only 3 types of colors (cells).
  + How they transform colors to neural signals? It's their ganglion cells that produce spike discharges and transform analog signal to discrete one. Information is coded by frequencies.
  
 - Receptive field and Ganglion cells:
  + Receptive field (of a cell) is the region that affects the cell's output. So remember that a cell reacts to a region, quite magical. How big is that region, measured in cm and visual degrees? From 0.5 to 2 degree for V1. When the viewing distance is 57 cm, one visual degree equals 1 cm. So each cell in our eye generally reacts to a region of 0.5cm to 2cm in width and length.
  + Receptive field's shape actually resembles a cone, with the ganglion cells at the top.
  + On center - off surround cells: excite when light focuses on the center
  + Off center - on surround cells: inhibit when light focuses on the center
  + There seem to be a certain proportion of center / surround that maximizes the excitation of neurons. Image on page 39 shows maximum response belongs to the middle state.
  + No light => no response
  + Each receptive field has at least 6 ganglion cells at its top: **Blue-Yellow x 2 (On-off and Off-on), Red-Green x 2, Black-White x 2.**
  + These pairs of opponent colors are called *oponent channels*.
  + **Question:** How is the output of the three-cone system transformed into the color-opponent system of ganglion cells?
  + **Answer:** Mỗi ganglion cell sẽ chỉ phản ứng với một trong 6 kiểu opponency và nó sẽ cố gắng tổng hợp màu từ input ở receptive field. Nhìn vào hình vẽ trang 52: với cùng một input R, G, B mỗi ganglion cell sẽ tự đóng / mở các khóa tương ứng với các màu để tạo ra màu ở center và ở surround mà nó mong muốn. Ví dụ cái ganglion cell đầu tiên (OnBlue - OffYellow) sẽ chạy như sau:
    B1. Cones ở Retina phân tách coming light thành 3 luồng tín hiệu tương ứng ba bước sóng long, middle, short là R, G, B.
    B2. Tín hiệu R và G được gộp vào nhau (cộng đại số) được tín hiệu Y (Yellow), tín hiệu B giữ nguyên.
    B3. Giữ lại tín hiệu B cho phần Center, tín hiệu Y cho phần surround.
    B4. Tính độ chênh lệch giữa B và Y là B - Y. Lưu ý cả B và Y đều là số lớn hơn 0.
    B5. Fire spikes dựa vào độ chênh lệch. Chênh lệch này càng lớn, response càng mạnh.
    
Xong nội dung về Retina. Giờ ta biết là Retina tính contrast thế nào. Vấn đề là, dùng cái contrast đấy để làm gì? Ta tìm hiểu tiếp Lateral Geniculate Nucleus (LGN). 

## The Lateral Geniculate Nucleus

Nhìn vào hình vẽ trang 56 ta thấy ngay là LGN nằm ngay sau Retina trong HVS. Tín hiệu hình ảnh sẽ đi từ Retina qua LGN rồi đi vào các V1, V2, ... rồi đi tới Parietal Cortex và Inferotemporal Cortex. Như vậy LGN là nơi trích xuất các thông tin cơ bản nhất để đưa tới các trung khu thần kinh khác. LGN có những loại cell ("tế bào") gì mà làm được việc ấy?

Page 57: LGN có 6 layers of cells. Mỗi cell trong 6 lớp này cũng có receptive field của riêng nó, chỉ có cái là những cái receptive field này không phải là hình tròn nữa mà đủ các thể loại hình. RFs này cũng to hơn và "have a stronger surround" (no idea what that means, perhaps it means these cells will only fire upon highly discriminative center-surround input?)

Mặc dù có 6 lớp, cells trong LGN chỉ có 2 loại: P-cell và M-cell (not gonna remember their Greek or Latin names). P-M is just like Phoebe and Monica (I love Friends!). *Phoebe perceives color & form whilst Monica perceives motion & depth.*

## Visual Cortex

Visual Cortex (VC) có khoảng 5 tỷ neurons và chiếm 20% vỏ não. Thành phần "primary" nhất gọi là V1. Đây là nơi lưu giữ các thông tin tối mật, à quên, tối quan trọng. Mỗi một nhóm (collection) cells lại lưu giữ một phần thông tin (spatial information) của visual field. Mỗi nhóm này được gọi là một **visual field map**. Mặc dù ta không rõ chính xác là mỗi vs map ở các vùng khác nhau (LGN, V1, V2, ...) lưu cái gì, điểm nhấn quan trọng là đống vf maps này có thể được biểu diễn bằng hình ảnh (images).

### Primary VC (V1)

V1 là nơi chứa Simple cells, Complex cells và Hyper complex cells. Đây chính là nguồn cảm hứng của mạng CNN đầu tiên. Hình vẽ trang 67 giải thích cơ chế gộp nhiều receptive fields của cells ở lớp trước thành một receptive field của lớp sau. Điều thú vị là simple cells và complex cells sẽ chỉ phản ứng với một vài orientations nhất định. Ví dụ cell nào chỉ phản ứng với input đến từ góc 45 độ thì chỉ fire nếu ánh sáng đi đúng theo góc đấy. Outlook: dùng Gabor filter để mô phỏng góc nghiêng.

### Phân biệt simple cells, complex cells, hypercomplex cells và cells in extrastriate cortex

- Simple cells: response to oriented edges/bars.
- Complex cells: cũng như simple cells nhưng ngoài orientation thì phải đang di chuyển (moving) (xem trang 79). Lưu ý là complex cells chỉ cần đối tượng đang di chuyển là nó đã phản ứng rồi, ko cần biết hướng nào hoặc nhanh chậm ra sao.
- Hypercomplex cells: respond chọn lọc theo từng hướng (orientation), độ dài (length), tỷ lệ sáng tối (ratio of lit surface to dark surface). Hypercomplex cells tinh tế hơn rất nhiều so với 2 loại kia.
- Cells in extrastriate cortex: phản ứng với màu sắc (V4), quỹ đạo nhất định (V3 và MT), mỗi thứ một ít (V2) và tất cả các thể loại dao động nén, ép, xuôi ngược kim đồng hồ (MST)

### Two pathways: ventral and dorsal

Sự phong phú của các loại cells ở Retina (Ross and Chanler), LGN (Phoebe and Monica) và Visual cortex (Simple, Complex, Hypercomplex, extrastriate cells) cho phép con người phân xây dựng một bức tranh sinh động về thế giới xung quanh. Ngay từ đầu ta thấy là có một sự chia tách khá rõ ràng về chức năng màu sắc / hình khối và chức năng độ sâu / quỹ đạo. Hiện nay khoa học nhất trí là có 2 con đường (pathway) mà tín hiệu hình ảnh sẽ đi: "what" pathway và "where" pathway.

- *What pathway gồm Cones -> P-cells -> V1 -> V2, V4, IT*: trả lời câu hỏi input là cái gì, có ăn được không.
- *Where pathway gồm  Rods -> M-cells -> V1 -> V2, V3, V5, PP*: trả lời câu hỏi input cách bao xa, có đang di chuyển không.

Dễ thấy trước V1 thì xử lý hầu hết là serial, sau V1 là bắt đầu xử lý song song.

Tuy nhiên, 2 pathway này không hoàn toàn chia cắt mà có sự trao đổi thông tin qua lại giữa neurons của path này với neurons của path kia.

# Kết thúc

Mặc dù slide vẫn còn 1 phần nữa về phương pháp nghiên cứu bộ não (fMRI, brain lesion) nhưng phần đó ko hứng thú và cũng ko cần thiết lắm, ta kết thúc tại đây. 

Đây là một bài thực sự thú vị, trải dài qua slide 100 trang. Trong bài này ta đã học về các thành phần cơ bản của HVS, từ Retina qua LGN tới Visual Cortex. Retina có 3 thành phần chính: Rods, Cones và Ganglion cells, thực hiện chức năng tính contrast của Receptive Field. Thông tin về contrast này được truyền tới LGN. Vì receptive field của P-cells của LGN rộng lớn hơn và không bị bó hẹp vào hình tròn, LGN cung cấp thông tin màu sắc, hình khối, đường nét của một cơ số đa dạng các thể loại input. Ngoài ra LGN còn có M-cells để thu thập toàn bộ thông tin về depth và motion. Hai khối thông tin từ P-cells và M-cells của LGN đi tới V1. Ba loại cells Simple, Complex và Hypercomplex của V1 là nguồn cảm hứng chính cho mạng CNN. Thông tin từ hypercomplex cells của V1 đi tới khắp nơi trong não bộ, mỗi vùng não bộ lại giữ lại một thông tin hữu ích cho riêng nó. Cuối cùng ta có extrastriate cortex là nơi tiến hành parallel computing với đủ loại cells khủng bố để nhận diện các loại hình khối và quỹ đạo phức tạp.
