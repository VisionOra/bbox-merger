# Bounding Box Merger

This code will help you out in merging your Boundingbox

## Example Usage

```python
boxes = [[0, 0, 2, 2], [1, 1, 3, 3], [4, 4, 6, 6]]
merged_boxes = merge_boxes(boxes)
print(merged_boxes)
```

Output:

```
[[0.0, 0.0, 3.0, 3.0], [4.0, 4.0, 6.0, 6.0]]
```

# Example

1. Before Merging Bounding Boxes
   ![Image1](attachments/Image1.png)
2. After Merging Bounding Boxes
   ![Image1](attachments/merged.png)

---

## Thing To cover

- Add support for polygons
