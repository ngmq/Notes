[Springer Link](https://link.springer.com/chapter/10.1007/978-3-319-46493-0_50)

# Abstract:

What is "saliency prior knowledge" mean?

What is "pre-training with semantic segmentation data"?

What is "strong supervision of segmentation tasks"? Is there any "weak supervision"?

# 1. Introduction

Ok so this paper is about bottom-up saliency detection.

Still, what is "saliency priors" that are shown to be effective?

One point worth considered: "the supervision of binary labels is relatively weak to effectively train a deep CNN". So if the 
problem that the network is trying to solve has complex structure (so that CNN is needed) but simple answers (binary classification) then it might
be harder to train the network? Is this always true?

So the predicted saliency map at one time step becomes the "saliency prior" to another. The question now is, how does the CNN use this saliency prior in each
time step? And what kind of information that can only be extracted through time steps and not feed foward pass?

This paper has 03 main contributions:

+) Propose a new RFCN for saliency detection. This new model can refine the previous predictions.
+) Propose a general method for using saliency priors. Previous CNN models do not use this saliency priors.
+) Design a pre-training method for RFCN that can somehow make use of "multiple object categories" and "capture the intrinsic representation of generic objects". 
This helps addressing the point above: weak supervision. 

Also, the model outperforms state-of-the-art approaches.

# 2. Related Work

This paper is most closely realted to [17]. In [17], a FCN is trained under multi-task learning framework. Differences are:

+) [17] does not use saliency priors.
+) [17] use FCN, not Recurrent FCN.
+) This paper's pre-training method allows to learn "both "class-specific-features" and "generic-object-representations" suing segmentation data.
[17] pre-trains the network on object categories classification, essentially different from the task of saliency object detection.


# 3. Saliency Prediction by Recurrent Networks

Different CNN model: this RFCN actually use Deconvolution layers, and learn the parameters of these layers to upsample the image.

Input: image h * w * 3 (3 for RGB)
Output: image h * w * 2 (2 for Foreground and Background)

## 3.1 Funlly CN for Saliency Detection
====== About the FCN in [22]: (this one has no recurrent connections) =====

In general, the formulas of one forward pass are constructed from two main processes of the system: Input => Conv layers => Deconv layers

The paper uses negative log-likelihood loss function.

Loss = -( sum_all_over_pixels_in_all_over_images 1(Ci,j = fg)log(p(li,j=fg)) + 1(Ci,j = bg)log(p(li,j=bg)) ).

It should be maximize, not minimize. Plus, why isn't the loss function binary entropy?

Two main drawbacks of this FCN without any recurrent:

- no priors
- cannot fix the errors itself

## 3.2 Recurrent Network for Saliency Detection

====== Main RFCN model =====

Saliency Prior Map is computed as follow:

step 1: Oversegmentation to M superpixels
step 2: compute central distance prior, color contrast prior, intensity contrast prior and orientation contrast prior
step 3: compute saliency prior from those 04 values. Done.


Subsequent correction step: use foreground as prior. 

If using RFCN (d): at every step both Conv and Deconv process have new input and thus have to be re-computed forward => inefficient
If using RFCN (e): at every step > 1, the Conv process have the same input being the original image I => can be reused, and only the Deconv process has to be re-computed forward.

However: the RFCN (e) does not work very well, only achieve similar performance to non-recurrent FCN. The reason is because the prior map has to be downsampled to the size of
the last layer in Conv process => less information about the prior in every Deconv forward pass.

Therefore: the RFCN (d) is chosen.

## 3.3 Training RFCN for Saliency Detection

One notable argument: "saliency detection and semantic segmentation are highly correlated but essentially different in that saliency detection aims at 
separating generic salient objects from background, whereas semantic segmentation focuses on distinguishing objects of different categories."

Pre-train on PASCAL VOC 2010 "enjoys strong supervision from segmentation data and also enables the network to learn general representation of foreground objects."

----- In the pre-training stage: ----

Deconv process has C+3 final layers: 1 for Foreground, 1 for Background, C+1 for semantic class label of each pixel (i,j) from the PASCAL VOC 2010 dataset

----- In the fine-tuning state: ----

Keep the Foreground and Background output layers. Remove the C+1 layers of semantic object segmentation.

## 3.4 Post-processing

Aims: the binary output of foreground and background layers can be noisy at the boundaries of objects i.e. the edges are not straight or disconnected. Post-processing should
focus on this aspect and smooth the foreground and background.

Start from the foreground map H:

step 1: calculate the average saliency score of H, call it muy
step 2: binary thresholding H with threshold muy. Now white pixels are foreground and black pixels are background.
step 3: compute the center of the foreground region and the number of foreground pixels.
step 4: compute spatial confidence and color confidence: SC_{i,j} and CC_{i,j}.
step 5: Hnew_{i,j} = SC_{i,j} * CC_{i,j} * H

Then perform an edge-aware erosion [4] on Hnew to obtain the final saliency map

# 4. Experiments

## 4.1 Experimental Setup
- Implemented on Caffe with MATLAB interface
- Pre-train RFCN on PASCAL VOC 2010 semantic segmentation dataset with > 10000 images belong to 20 classes, done after 200k iterations
- Fine-tune for saliency detection on the THUS10K data set for 100k iterations.

Test: apply the network in 03 different scales and then fuse all to the final map

## 4.2 Results:
- Ablation studies proved that the proposed approach is effective: prior, recurrent and pre-train strategy

- Interesting results in comparision of RFCN-B and RFCN: RFCN-B always slightly outperforms RFCN in F-measure, but far behind in AUC.

# References

- [4]. Gastal, E.S., Oliveira, M.M.: Domain transform for edge-aware image and video
processing. ACM Trans. Graph. (TOG) 30, 69 (2011)

- [17]. Li, X., Zhao, L., Wei, L., Yang, M., Wu, F., Zhuang, Y., Ling, H., Wang, J.:
Deepsaliency: multi-task deep neural network model for salient object detection.
arXiv preprint arXiv:1510.05484 (2015)

- [22]. Long, J., Shelhamer, E., Darrell, T.: Fully convolutional networks for semantic
segmentation. In: CVPR, pp. 3431–3440 (2015)
