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



# Evaluation

Find the sequence of FOAs, calculate the number of first_hit_correct.
