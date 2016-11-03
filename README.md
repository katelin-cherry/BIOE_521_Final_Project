# Raspberry Pi Microscope
#### Team 11: House of Pies - Katelin Cherry & Melody Tan

#### Brainstorm
We will set up a USB microscope controlled by a Raspberry Pi and a sample platform driven by a single-axis motor that will move the specimen to different distances below the objective. We will then use focus stacking to take images at increments below the objective and composite the in-focus portions of those images into a single, beautiful image. 

#### Abstract
Microscopy is limited by a trade off between numerical aperture and magnification against depth of field. This results in images that have certain portions that are in-focus and other portions that are out-of-focus, depending on the distance at which they were taken. Focus stacking is an image processing technique where a series of images is captured at different focal distances. The in-focus portions of each image are then combined to form a single, completely in-focus image.

We are creating a low-cost focus stacking system. We use a USB microscope to image samples mounted on a Cognisys Stackshot photo stacking platform. The Stackshot increments the distance between the sample and microscope objective by 10 um per shot over a range of XX-XX mm.  The USB microscope takes a timelapse of images, which are then processed on the Raspberry Pi using an open-source focus stacking program that we have adapted for our application. Composite images are displayed on the Raspberry Pi screen.
