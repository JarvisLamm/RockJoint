from PIL import ImageFilter


def pixel_segmentation(image, edge_threshold=50):
    """Segment edges from an input PIL image using a simple threshold."""
    grayscale = image.convert("L")
    edges = grayscale.filter(ImageFilter.FIND_EDGES)
    return edges.point(lambda value: 255 if value >= edge_threshold else 0)


def two_dim_process(edge_image):
    """Stub for MATLAB twoDimProcess.m; kept for 2D cleanup/filtering parity."""
    return edge_image


def segment_link(edge_image, link_size=3):
    """Link nearby edge pixels using a max filter."""
    return edge_image.filter(ImageFilter.MaxFilter(link_size))


def cal_trace_length(image, edge_threshold=50, link_size=3, return_edges=False):
    """Estimate trace length by counting linked edge pixels."""
    segmented = pixel_segmentation(image, edge_threshold=edge_threshold)
    processed = two_dim_process(segmented)
    linked = segment_link(processed, link_size=link_size)
    histogram = linked.histogram()
    length = histogram[255] if len(histogram) > 255 else 0
    if return_edges:
        return length, linked
    return length
