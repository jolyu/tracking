# Tracking library

Files for the tracking library

Add to project and import:

```python
from tracking import *
```
## Tracking.py
Functions for determining what blobs to track, and to construct boxes around blobs for the trackers.

Transform keypoints, to boxes surrounding the keypoints:
```python
KeypointsToBoxes(keypoints)
```
returns list of boxes.

Remove all keypoints that is inside the boxes:
```
removeTrackedBlobs(keypoints, boxes)
```
Returns list of keypoints.

## multitracker.py
A class to gather multiple trackers.

Initialize a multitracker-object:
```python
NewTracker()
```
Returns nothing.

Add a tracker to the NewTracker:
```python
NewTracker.add(tracker)
```
Returns nothing.

Remove tracker from multitracker using index:
```python
NewTracker.pop(num)
```
Returns nothing.

Update all trackers, and remove the ones that has been nonvalid for 5 frames in a row:
```pyton
NewTracker.update(filteredFrame)
```
returns list of boxes around all tracked objects

## Trackerfunc.py
For initializing a single tracker.

Create a tracker of a given type:
```python
createTrackerByName(trackerType)
```
returns nothing

