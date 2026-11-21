# VisionPort dataset audit

Annotation file : data\audit\annotations\instances.json
Image folder    : data\audit\images

## 1. Overview
Images: 100 | Annotations: 408 | Categories: 6
Images with no annotation: 5 [90, 91, 92, 93, 94]
Image sizes in the JSON: 640x360 (100)

## 2. Class distribution
 id  class          count   share
  1  car              200   49.1%  #########################
  2  motorcycle       102   25.1%  #############
  3  pedestrian        49   12.0%  ######
  4  bus               23    5.7%  ###
  5  truck             28    6.9%  ###
  6  autorickshaw       5    1.2%  #
Imbalance ratio (largest / smallest class): 40.0 : 1
Rare classes (under 5% of annotations): ['autorickshaw']

## 3. Annotation validation
- area differs from width x height: 1  e.g. annotation ids [408]
- box outside the image: 3  e.g. annotation ids [400, 401, 402]
- duplicate box: 2  e.g. annotation ids [285, 405]
- points to a missing image: 1  e.g. annotation ids [407]
- points to an unknown category: 1  e.g. annotation ids [406]
- tiny box (side under 10 px): 2  e.g. annotation ids [403, 404]
- zero or negative width/height: 2  e.g. annotation ids [398, 399]

## 4. Image files and quality
- file missing: 2  e.g. image ids [40, 41]

## 5. Object size mix (COCO definition by pixel area)
small (under 32x32): 2 | medium (under 96x96): 306 | large: 98

## 6. Summary
Annotations with at least one problem: 12 of 408
Images with at least one problem     : 12 of 100
Suggested actions: remove or repair the flagged annotations, replace missing or corrupt images, review dark and blurry images by eye, and collect more examples of rare classes before training.
- file cannot be opened (corrupt): 2  e.g. image ids [30, 31]

## 5. Object size mix (COCO definition by pixel area)
small (under 32x32): 2 | medium (under 96x96): 306 | large: 98

## 6. Summary
Annotations with at least one problem: 12 of 408
Images with at least one problem     : 12 of 100
Suggested actions: remove or repair the flagged annotations, replace missing or corrupt images, review dark and blurry images by eye, and collect more examples of rare classes before training.
- size differs from the JSON: 1  e.g. image ids [50]

## 5. Object size mix (COCO definition by pixel area)
small (under 32x32): 2 | medium (under 96x96): 306 | large: 98

## 6. Summary
Annotations with at least one problem: 12 of 408
Images with at least one problem     : 12 of 100
Suggested actions: remove or repair the flagged annotations, replace missing or corrupt images, review dark and blurry images by eye, and collect more examples of rare classes before training.
- too dark (mean brightness under 50): 3  e.g. image ids [10, 11, 12]

## 5. Object size mix (COCO definition by pixel area)
small (under 32x32): 2 | medium (under 96x96): 306 | large: 98

## 6. Summary
Annotations with at least one problem: 12 of 408
Images with at least one problem     : 12 of 100
Suggested actions: remove or repair the flagged annotations, replace missing or corrupt images, review dark and blurry images by eye, and collect more examples of rare classes before training.
- blurry (sharpness under 100): 4  e.g. image ids [20, 21, 22, 23]

## 5. Object size mix (COCO definition by pixel area)
small (under 32x32): 2 | medium (under 96x96): 306 | large: 98

## 6. Summary
Annotations with at least one problem: 12 of 408
Images with at least one problem     : 12 of 100
Suggested actions: remove or repair the flagged annotations, replace missing or corrupt images, review dark and blurry images by eye, and collect more examples of rare classes before training.
