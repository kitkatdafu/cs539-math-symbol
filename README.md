# Group 48 Final Project Report

Reid Chen, Jijie Zhang

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
Notability recently announced a math conversion
feature that converts a selected region of handwritten math into
typewritten math. This shows that a mathematical recognizer exists. In
fact, handwritten mathematical formula recognizers like
outperforms the state-of-the-art accuracy in the
Competition on Recognition of Online Handwritten Mathematical
Expressions (CROHME). We also found a commercial mathematical recognizer
called Mathpix , which provides mathematical recognizer
API. These existing recognizers only work well on an image containing a
single formula. They cannot be used directly because the input should be
a PDF file or images of each page from notes. Therefore, retrieving the
mathematical expressions or finding where the mathematical symbols are
from inputs is essential.

Researches in object detection provide methods of solving the detection
problem. Fast R-CNN and Faster R-CNN
can both enable formula detection, but these methods
require a long computational power and time. Since we wish to deploy our
model on mobile devices, which do not have huge computational power,
one-shot detectors like YOLO and Single Shot MultiBox
Detector are more suitable for the project.

We decided to use ScanSSD as our formula detection
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

Acknowledgements
===========================
1. Notability.  https://www.gingerlabs.com.
2. Jianshu  Zhang,  Jun  Du,  and  Lirong  Dai. Multi-scale  attention  with  dense  encoder  forhandwritten mathematical expression recognition.  In 2018 24th international conferenceon pattern recognition (ICPR), pages 2245–2250. IEEE, 2018.
3. Mathpix.  https://mathpix.com.
4. Ross Girshick.  Fast r-cnn.  In Proceedings of the IEEE international conference on com-puter vision, pages 1440–1448, 2015.
5. Shaoqing Ren,  Kaiming He,  Ross Girshick,  and Jian  Sun.  Faster r-cnn:  Towards real-time object detection with region proposal networks.  In Advances in neural informationprocessing systems, pages 91–99, 2015.
6.  Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali Farhadi.  You only look once:Unified, real-time object detection.  In Proceedings of the IEEE conference on computervision and pattern recognition, pages 779–788, 2016.i
7.  Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed, Cheng-YangFu, and Alexander C Berg.  Ssd:  Single shot multibox detector.  In European conferenceon computer vision, pages 21–37. Springer, 2016.
8.  Parag  Mali,  Puneeth  Kukkadapu,  Mahshad  Mahdavi,  and  Richard  Zanibbi.   Scanssd:Scanning single shot detector for mathematical formulas in pdf document images.arXiv preprint arXiv:2003.08005, 2020.
9.  Hasty.ai.  https://hasty.ai.
10.  Tsung-Yi Lin,  Michael Maire,  Serge Belongie,  Lubomir Bourdev,  Ross Girshick,  JamesHays, Pietro Perona, Deva Ramanan, C. Lawrence Zitnick, and Piotr Doll ́ar.  Microsoft coco:  Common objects in context, 2014.
11.  Visdom.  https://ai.facebook.com/tools/visdom.[12]  Parag Mali, Puneeth Kukkadapu, and Mahshad Madhavi.  Tfd-icdar 2019:  A dataset fortypeset math formula detection, 2019. https://github.com/MaliParag/TFD-ICDAR2019.