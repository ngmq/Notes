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
Right eye and left eye each has its own visual field too. Image how one-eyed people see the world. Let's call them right visual field and left  visual field.
Then each of the left and right visual field is divided further into two halves that are called **hemifield**.

So the left hemifield of each eye is viewed by the right hemisphere of the brain, and vice-versa. It's not hard to see why if we look at the picture at page 18.

Remember the optic chiasm: it distributes (in VNese: "chia") the optic signals from the eyes to different parts of the brain. That signals go all the way to the primary visual cortex, also known as V1, in the back of the brain.

## Neurons

We are all familiar with neurons - IAS students should have seen them at least three times: in Bio-inspired AI lectures, in Knowledge Engineering lectures and in Neural Networks lectures. Each neuron is connected to other neurons via its axon. The connecting part between one axon and one neuron is synapses. How they encode information? many ways, could be rate coding, activation coding, timing coding.

## The human eye

The diagram in page 25 shows components of an eye. Our question is, how are the visual signals encoded in our eyes? Which components of the eye should we focus on to answer that question?

Answer: we don't have time to learn all of them, but we should definitely learn about the retina and the visual cortex (V1 and all the other Vs)

## The Retina

- What is it?
  + A light-sensitive surface ("bề mặt") at the back of the eye
  + That surface is covered with photo-receptors (sensory neurons). We know light has photons, so probably the name comes from photo(n)-receptors.
  + Sensory neurons consist of Rods and Cones (R-C, like Ross and Chandler). Rods are light sensitive, not color sensitive. Cones are color sensitives. There are about 120 million rods, but only 7 million cones. I guess that's because light sensitivity is much more important than color sensitivity: black and white TVs were made much earlier than colored TVs.
  + So what do the little guys R and C do? "Task of photoreceptors: change the electromagnetic energy ("năng lượng điện từ") of photons into visual activity as need by neurons." A ha! So these guys do all the hard work.
  + Are they uniformly distributed over the retina? No, and that's when things get interesting. Distribution of R and C is showed in page 27. The area with no Rods and densely packed Cones is the **Fovea** ("điểm tiêu cự"). We all know very well from high school physics that the fovea is where all the incoming light rays end up after reflected on the lens. Therefore,  the fovea is responsbile for "sharp central vision".
  + What that means is when we focus on different visual field around us, we are changing the input to the fovea. Since we only have one fovea, we can only gaze at one region at one time.
  
 - The Cones: we are trying to make sense of the color channels (RGB) and what the cones actually do here
  + 03 types of cones: long-wavelength (Red), middle-wavelength (Green) and short-wavelength (Blue)
  + They are the source of trichromatic theory of color vision: all colors are made of only 3 types of cells.
  + How they transform colors to neural signals? It's their ganglion cells that produce spike discharges and transform analog signal to discrete one. Information is coded by frequencies.
  
 - Receptive field and Ganglion cells:
  + Receptive field (of a cell) is the region that affects the cell's output. So remember that a cell reacts to a region, quite magical. How big is that region, measured in cm and visual degrees? From 0.5 to 2 degree for V1. When the viewing distance is 57 cm, one visual degree equals 1 cm. So each cell in our eye generally reacts to a region of 0.5cm to 2cm in width and length.
  + On center - off surround cells: excite when light focuses on the center
  + Off center - on surround cells: inhibit when light focuses on the center
  
