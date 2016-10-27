# Raspberry Pi Microscope
#### Team 11: House of Pies - Katelin Cherry & Melody Tan

#### Brainstorm
We will set up a USB microscope controlled by a Raspberry Pi and a sample platform driven by a single-axis motor that will move the specimen to different distances below the objective. We will then use focus stacking to take images at increments below the objective and composite the in-focus portions of those images into a single, beautiful image. 

#### Abstract
Focus stacking is an image processing technique where a series of images is captured at different focal distances. The in-focus portions of each image are then combined to form a single, completely in-focus image. We are using a USB microscope to image samples mounted on a Cognisys Stackshot, a photo stacking platform. The stackshot increments the distance between the sample and microscope objective by XXmm per shot, with the distances ranging from XX-XXmm.  The images are then processed on the Raspberry Pi using an open-source focus stacking program we have modified. Composite images are displayed on the Raspberry Pi screen.
