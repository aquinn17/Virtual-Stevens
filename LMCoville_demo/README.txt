9:37 AM 8/6/2015

VIRTUAL LOCKHEED MARTIN - LMCOVILLE

LMCOville uses browser-based WebGL to render 3D images using JavaScript. The Three.js library is used to make the
coding much simpler.

The .html file should run fine in most updated browsers. 

Use https://get.webgl.org/ to check your browser's compatibility. Updating the browser should allow WebGL. Otherwise
look for how to enable WebGL in your preferred browser.

All style sheets are built into the headers of the main LMCOville html files.

LMCOvilleV1.7.html is the most recent. LMCOville.html is the workspace used for editing and, as of the last edits,
identical to LMCOvilleV1.7.html

//SEARCHBAR//

The current search in version 1.6 is crude and undeveloped. LMCOvilledatagenerator.py was used to randomly assign
names random specialties into the flat LMCOdata.txt file, which was used for very basic dictionary searches.
Flask was installed to display the search results. In order to get any search results, you must run
'LMCOvillesearch.py' to act as a back-end database within your computer. Searches must either be a name or
specialty.

This search is a poor placeholder that deserves the most attention to improve functionality.


//FILTER BUTTONS//

Filter buttons work through true/false properties designated as subunit.active (ie. Aeronautics.active). Depending
on the current state of the neighborhood, the switch will remove or add the items to BOTH the scene and various
target lists of the raycaster functions. Future goals include having the search results trigger these filters to
highlite the floor(s) of the person(s) and remove non-affiliated neighborhoods.

Suppliers, customers, and partners have a seperate filter function at the moment of V1.6 because they do not have
the property .floors. Future updates will require some sort of clickability, be it floors or generic outline.


//BASIC THREE.JS CONTROLS//

Scripts imported from three,js. Basic scene/camera/renderers implemented.
Controls: various adjustments to basic controls. Removed panning for less complicated use. Max/min distance to
keep user in controled zone. min/maxPolarAngle also to keep user in controled zone. It's important that
controls.target.copy(Vector) and camera.lookAt(Vector) are the same.


//BASIC GRASS/SKY/LIGHTS/PLATFORMS//

Grass generated as a plane. Skybox is a large BackSided box to give the appearance of a sky. There is both a
directed light near the center of the scene and ambient light. Center platforms are just the concentric circles/rings
that show the user they are moving away from core LM. They use rad, rad2,..., rad5.


//GLOBAL VARIABLES//

Since data was so difficult to find and not provided, basic building heights were decided and used as standards
to the buildings. Small, medium, and large for buildings. verylarge for F35 (largest unit).

rad, rad2, rad3, rad4, rad5 were radii for the concentric circles/rings.

width as standard width of buildings.

floorheight for height of floors in generateFloors()

mouseActive starts true. Turns false when certain callback functions are called to prevent clicking on scene when div
is open.


!!LMCOville PRIMARY BUILDINGS!!

Because of the concentric circle design, the actual building blocks ('new THREE.Mesh' for buildings) are entirely
hardcoded. It is possible to create a function that detects collisions and properly space and rotate the units, so
a data-driven building constructor is possible but would have been very time consuming for this demo. Positioning after
rotation was also troublesome since rotating the object did not rotate the object's own xyz-axis. I'd suggest looking
for a  function online that alter's the object's matrix so that it's xyz position adjusts with the rotation (if such
a function exists). CHECK THIS THREE.JS DOCUMENTATION: http://threejs.org/docs/#Manual/Introduction/Matrix_transformations
I did not know it was possible to adjust the matrix so easily. Using this and a loop would let you generate the subunit
buildings around the arch very easily with a list or hash-table(?) input.


-Building Texture: Mostly taken from online demo (http://learningthreejs.com/blog/2013/08/02/how-to-do-a-procedural-city-in-100lines/)

-NEIGHBORHOOD TEXT: Convoluted. Used while still new to JS and Three.js. Creates the general Neighborhood
labels. Very difficult to reposition the labels! Would need to be generated like the buildings in future.

-TEXT SPRITES: generated from makeTextSprite function. Could have been created recursively with data by first assigning buildings
names in the form building.name = 'buildingname' then looping makeTextSprite function with colors designated.

-Enteprise Operations and LM International - not given labels due to lack of information about sectors and lack of 
significance to the demo.


//BUILDING FLOORS//
Floors are created for a building with the 'createFloors(building)' function. 
Floors are created for every building using the function 'generateFloors(listOfBuildings)' and array 'allBuildings'.


//LM RESOURCES//

Generated from function with no paramaters. cylinder above the 4 buildings to give it 'distinct' appearance. Unclear of
what it's future use will be so placeholder 'video' div pops up on click.


//Partners, Customers and Suppliers//

Generated by using the hardcoded building positions and looping every third building so many units away. They do not have floors


//IMPORTANT ARRAYS AND PROPERTIES//

'allBuildings' contains all SUBUNIT buildings, and the 'subunits' contain the subunit arrays ([Aeronautics, MFC, ...]).
In future implementation of generating the city from data, these arrays would be necessary and gathered from the database.

building.floors is the array of all the building's floors (ie. F35.floors = [Mesh, ..., Mesh], F35.floors[0] = first floor mesh).

floorslist contains all floor meshes of the subunits. Does NOT include LMResources floors

subunit.floors is the array of all building.floors within the neighborhood (Aeronautics.floors = [F35.floors, SkunkWorks.floors, ...]

subunit.floors[i].number is the 'floor number'. F35.floors[0] is the first floor mesh and is at the bottom of the building.
Therefore F35.floors[0].number is 1.

Partners/Suppliers/Customers are the arrayss of subcontractor/supplier building meshes.

targetList: all floors. Used for onDocumentMouseOver

targetList2: all floors. Used for onDocumentMouseDown. In latest version lists ended up being the same. Continue
keeping them seperate for updates.



//CLICKABILITY//

assignCalls(building, divName) assigns each floor of the building the same callback function to open divName. Used
for basic demo.


//onDocumentMouseDown/Move//
onDocumentMouseDown uses targetList2 as the list of objects to detect hits. It triggers object.callback on the first object in
targetList2 that is hit. NOTE: onDocumentMouseDown is disabled when (1) mouse moves above 0.77 y (top ~12% of screen),
or (2) when specific calls are made that cause mouseActive to be turned false. (1) allows the user to click on the search bar
without running into errors, (2) disables the user from calling other object callbacks while a textbox is open.


onDocumentMouseMove uses targetList1 as the list of objects applies to. Saves the objects' colors then turns them
white. Upon moving off object, returns original color that was saved.


!!ROOMS!!
Only rooms that currently exist are in folders Floors -> F35. Rooms consist of employees (2 hard coded each), static chat-box,
same search bar located in LMCOville, updating clock, and a Current Project Wiki link. Lack of data and search engine leaves a
fairly static and bland room design. (NOTE: Update onDocumentMouseMove is VERY static; it does not save the
object's color, just sets it directly to the orange/yellow and returns to the grey. Can easily be updated when
needs change)


The star.name variables are real names from 'LMCOvilledata.txt'. They can be used in the search bar to find their
specializations.

'people' is the array of stars; people[0] = star1
star.name is the employee's name
star.role is the employee's role or position
star.Sname is the employee's sprite for their name
star.Srole is the employee's sprite for their role or position

Room 1 has been updated to have star.Sname and star.Srole, the others have not.

Room 1 has been updated to show project timeline and storyboards. Images were generated by running them into an image to Base64 string converter
and then in a seperate .js file, the image was defined (var image = new Image()) and the src was the Base64 string (image.src = "...").
The file was imported and then the variable image could be used freely. (This had to be done due to cross-origin error intentionally
blocked by three.js creators).


Questions? Contact me at:
akubis18@gmail.com