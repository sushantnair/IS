Place this folder in your D drive (just IN the D Drive, and not in any subfolder within it)
in order for the reCAPTCHA to work. Alternatively, change the path in the reCAPTCHA program
so that the images are discoverable. The correct configuration is that the three river pics
should be selected. Nothing else should be selected.
Let number of pictures selected be N
Conditions:
Case 1: N < 3
Response: Too few images selected
Case 2: N > 3
Response: Too many images selected
Case 3: N = 3, but not all are river images
Response: reCAPTCHA Authorization Unsuccessful
Case 4: N = 3, all are river images
Response: reCAPTCHA Authorization Successful
