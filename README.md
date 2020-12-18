# Group 48 Final Project Report

Reid Chen and Jijie Zhang 

Introduction and Background
===========================

As a college student, great note-taking skill is the path to success.
Nowadays, many students decide to use the iPad or Microsoft Surface to
take handwritten notes electronically due to their convenience. One of
the benefits of taking notes in this manner is that electronic
note-taking applications can recognize handwritten texts so that
students can search through their notes and find what they need
instantly. Although notes can be converted to searchable texts
successfully. Note-taking apps usually fail to recognize mathematical
formulas or expressions that are pervasive in the notes of a science or
engineering student's note. Nevertheless, this might be something
note-taking app's users are requiring. So, we initially wanted to find a
way so that mathematical formulas among notes, usually in PDF format,
can be recognized.

Although note-taking apps do not have the feature of recognizing math
symbols globally, i.e., these apps cannot detect where the formulas are,
some of them have the ability to recognize math formulas given that the
user tells the application where the math formulas are. For example,
Notability [@notability_2020] recently announced a math conversion
feature that converts a selected region of handwritten math into
typewritten math. This shows that a mathematical recognizer exists. In
fact, handwritten mathematical formula recognizers like
[@zhang2018multi] outperforms the state-of-the-art accuracy in the
Competition on Recognition of Online Handwritten Mathematical
Expressions (CROHME). We also found a commercial mathematical recognizer
called Mathpix [@mathpix_snip], which provides mathematical recognizer
API. These existing recognizers only work well on an image containing a
single formula. They cannot be used directly because the input should be
a PDF file or images of each page from notes. Therefore, retrieving the
mathematical expressions or finding where the mathematical symbols are
from inputs is essential.

Researches in object detection provide methods of solving the detection
problem. Fast R-CNN [@girshick2015fast] and Faster R-CNN
[@ren2015faster] can both enable formula detection, but these methods
require a long computational power and time. Since we wish to deploy our
model on mobile devices, which do not have huge computational power,
one-shot detectors like YOLO [@redmon2016you] and Single Shot MultiBox
Detector [@liu2016ssd] are more suitable for the project.

We decided to use ScanSSD [@mali2020scanssd] as our formula detection
architecture. ScanSSD is a typesetting formula detector proposed by Mali
et al. It has a precision of 0.848 on typesetting inputs, which is high
enough for our purpose. The acronym SSD stands for Single Shot MultiBox
Detector, which is an object detector that achieves high accuracy and
can be computed quickly. The idea of SSD and ScanSSD is that they use
structures called multi-box detectors. The multi-box detectors try to
detect formulas at each location of the image, and the results are
stitched together. The pooling process, at last, selects the best
bounding box as the network's output.

The reason we choose a SSD-based detector is that it consists of
multi-box detectors of various sizes, which follow the nature of the
shape of formulas. Mathematical formulas are various in their aspect
ratio. Sliding detectors with different shapes capture this nature well,
which could contribute to better results.

We think the precision rate is more important because the network's
purpose is to provide output to existing state-of-the-art formula
recognizers like Mathpix, which will generate corresponding latex code.
The false positives that are sent to these recognizers do not result in
generating harmful latex code.