# python-resize-image

### change the size (height, width or size in kb) of all images in a folder and subfolders

```
PS C:\Users\nogw> python .\resize.py

+------------------+-------+--------+-------+-----------+
|       name       |  size | height | width | adjusted? |
+------------------+-------+--------+-------+-----------+
| frog'-resize.jpg | 278kb |  1000  |  1000 |    yes    |
| frog-resize.jpg  | 283kb |  1000  |  1000 |    yes    |
+------------------+-------+--------+-------+-----------+
```
<div style="display: flex; justify-content: space-evenly">
  <h1>original (541kb, 1500x1101)</h1>
  <h1>resized (283kb, 1000x1000)</h1>
</div>
<img src="./images/frog.jpg" alt="frog" height="200px"/>

<img src="./frog-resize.jpg" alt="frog" height="200px"/>