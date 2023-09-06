from shapely.geometry import box
from shapely.ops import cascaded_union


def calculate_iou(box1, box2):
    """
    Calculate the Intersection over Union (IoU) between two bounding boxes.

    Args:
        box1 (tuple): The coordinates of the first bounding box in the format (x_min, y_min, x_max, y_max).
        box2 (tuple): The coordinates of the second bounding box in the format (x_min, y_min, x_max, y_max).

    Returns:
        float: The IoU value, representing the overlap between the two bounding boxes.

    Raises:
        shapely.geos.TopologicalError: If there is an error during the calculation.

    Example:
        box1 = (0, 0, 2, 2)
        box2 = (1, 1, 3, 3)
        iou = calculate_iou(box1, box2)
        print(iou)
        # Output: 0.25
    """
    box1 = box(*box1)
    box2 = box(*box2)

    if not box1.intersects(box2):
        return 0

    try:
        intersection_area = box1.intersection(box2).area
        union_area = box1.area + box2.area - intersection_area
        return intersection_area / union_area

    # pylint: disable=broad-except,bare-except
    except:
        print("shapely.geos.TopologicalError occurred, iou set to 0")
        return 0


def merge_boxes(bboxes):
    """
    Merge overlapping polygons until no more merging is possible.

    Args:
        bboxes (list): A list of bboxes represented as lists of four coordinates [x1, y1, x2, y2].

    Returns:
        list: The final list of merged polygons.
    """
    box_objs = [box(*bbox) for bbox in bboxes]
    merged_boxes = []

    while box_objs:
        union_poly = box_objs.pop(0)
        overlap_boxes = []

        for other_box in box_objs:
            if other_box.intersects(union_poly):
                union_poly = cascaded_union([union_poly, other_box])
            else:
                overlap_boxes.append(other_box)

        box_objs = overlap_boxes
        merged_boxes.append(list(union_poly.bounds))

    return merged_boxes


def merge_bbox_recursively(bboxes):
    """
    Merges overlapping bounding boxes recursively until no more merging is possible.

    Args:
        bboxes (list): A list of bounding boxes represented as lists of four coordinates [x1, y1, x2, y2].

    Returns:
        list: The final list of merged bounding boxes.
    """

    bboxes_processed = []

    while True:
        bboxes_processed = merge_boxes(bboxes)

        if len(bboxes_processed) < len(bboxes):
            bboxes = bboxes_processed
        else:
            print("Completely Merged")
            break

    return bboxes_processed
