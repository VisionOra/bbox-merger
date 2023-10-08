# ==============================================================================
# Example script
# ==============================================================================

# Open JSON file
import json
with open('examples\example_001.json', 'r') as f:
    data = json.load(f)
bboxes = [d['bounding_box'].values() for d in data['detections']]

# ==============================================================================

# Draw boxes (before bbox_merger)
import cv2
image = cv2.imread("examples\example_001.jpg")
height, width, _ = image.shape
bboxes = [[x_min * width, y_min * height, x_max * width, y_max * height] for x_min, y_min, x_max, y_max in bboxes]
for bbox in bboxes:
    x_min, y_min, x_max, y_max = map(int, bbox)
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
cv2.imwrite("examples\example_001_before.jpg", image)

# ==============================================================================

# Merge bounding boxes
import sys, os
sys.path.append(os.getcwd())
from bbox_merger import merge_boxes
merged_bboxes = merge_boxes(bboxes, overlap=0.1)

# ==============================================================================

# Draw boxes (after bbox_merger)
image = cv2.imread("examples\example_001.jpg")
height, width, _ = image.shape
for bbox in merged_bboxes:
    x_min, y_min, x_max, y_max = map(int, bbox)
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
cv2.imwrite("examples\example_001_after_threshold_50_percent.jpg", image)

# ==============================================================================

# Merge bounding boxes
import sys, os
sys.path.append(os.getcwd())
from bbox_merger import merge_boxes
merged_bboxes = merge_boxes(bboxes, overlap=0.5)

# ==============================================================================

# Draw boxes (after bbox_merger)
image = cv2.imread("examples\example_001.jpg")
height, width, _ = image.shape
for bbox in merged_bboxes:
    x_min, y_min, x_max, y_max = map(int, bbox)
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
cv2.imwrite("examples\example_001_after_threshold_90_percent.jpg", image)

# ==============================================================================
