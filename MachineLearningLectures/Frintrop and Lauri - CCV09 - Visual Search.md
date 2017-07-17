Link: CCV 09, mincommsy

# General ideas

The guiding for search (topdown signals) happens constantly until the search stops - humans constantly think about the features of the object that are being looked for.

The most important questions are:

*1. Given a attention system in FIT - liked (Koch-Ullman, Itti-Ullman, VOCUS2), where should we put the top down cues into?*

Answer: after across scale addition, so that every possible feature channels can be taken into account, e.g "Red is better than Blue" or "Color is better than Orientation"

*2. How to encode the topdown signals?*

Answer: When fusing channels maps (On-Off, Off-on, orientation 0, 45, 90, 135,...) and conspicuity maps: the topdown signals is basically a vector of size N by 1 where N equals number of channels maps and conspicuity maps. Each element indicates the weight of the corresponding map. For example, in page 21 the table on the right with green and red text is an expected feature vector. 

In general, the topdown signals tells the system that "the saliency value indicated by the channels map of 90 degree is important, let's take more from that map. And also, the intensity map is not very important since normally all surrounding objects have similar intensity, so let's not count on intensity too much".

The same principle can be observed by humans: if the task is to guess the time period in which a picture is taken, most of us will think "the facial features of people are not very important, but their clothes are".

*3. How to integrate that signals to the system? Excitation or Inhibition? <- interesting here, how to do inhibition? Should the top down cues repeatedly inject to the system?*

The answer for seond question also answered this one. Excitation means positive weights or weights > 1, inhibition means vice-versa. The exact condition depends on how the topdown signal vector is constructed. For neural networks, that condition is positive. For VOCUS system, that condition is greater than 1.0.

Page 14 wrote

"Several research findings indicate that both, excitation and inhibition are important in human visual attention."

# How VOCUS did visual search

In VOCUS, an explicit saliency map for top down cues is computed. Recall that the saliency map in previous lectures with Laplacian pyramids and stuff is the bottom up saliency map. Suppose that the top down map has been calculated, the final global saliency map is just a weighted average of the top down and bottom up map:

Final_saliency_map = (1 - t) * BU_map + t * TD_map

Next, we discuss the calculation of the TD_map in VOCUS, especially the learning mode and testing mode. 

## VOCUS learning mode

* Training set: images with region of interest (ROI) of each object (number of possible objects is limited).
* Output: feature vector for each object.

Step 1: compute the bottom up saliency map of the ROI
Step 2: detect most salient point in ROI
Step 3: Extract most salient region (MSR) by region growing

**Question 1: What if there are multiple most salient points?**
**Question 2: What if the most salient region does not overlap with the target object?**

Step 4: For each map X_i in the saliency system (not only conspicuity map but also other channel maps like each angle, each color space,... In total there could be 13 such maps: 2 Intensity (On-Off and Off-on) + 4 angles (0, 45, 90, 135) + 4 colors (G, B, Y, R) + 3 Conspicuity map), compute the mean value of MSR in that map and mean value of the rest of other pixels in that map.

Step 5: the importance, or weight, or "feature" of that map is the ratio v_i = m_{i, MSR) / m_{i, the rest}

Step 6: because different training images have different v_i, we then combine them together by a geometric mean:

v_i_final = nth_root_of (v_i_1 * v_i_2 * ... * v_i_K) where K is number of training images. i runs from 1 to 13.

Done! Now save the feature vector for each object for later testing.

## VOCUS testing mode (calculation of TD_map)

Testing mode is simple. We use the same saliency system for bottom up map to compute the top down map with one modification: we construct two additional map: excitation map and inhibition map. Excitation map is the output of that system with weighted average when fusing the channel maps and conspicuity maps with v_i > 1 (weights are v_i). The Inhibition map is the output of that system with weighted average when fusing the channel maps and conspicuity maps with v_i < 1 (weights are 1/v_i). Ignore v_i = 1. Finally, the formula for the top down saliency map is **TD_map = Emap - Imap.**

# Evaluation

Simple. Just find the sequence of FOAs, calculate the number of first_hit_correct.

# Summary

This lecture is mainly about how top down cues can be integrated into a system such as VOCUS2. It is clear that there does not exist a general representation for the top down cues, and different saliency system needs different ways to represent top down cues. For VOCUS2, that way is feature vector of importances of each maps. 

**Answer to Question 1 and 2 between step 3 and 4 above: in that case we have to choose the ROI such as the object is also contained in the most salient region. Otherwise the feature vector does not belong to the target object.**
