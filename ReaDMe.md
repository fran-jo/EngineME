<p>
<h5>Minimum Dependencies</h5>
<li>Python 2.7.8</li>
<li>matplolib</li>
<li>scipy</li>
<li>numpy</li>
<li>h5py</li
<li>modelicares (0.10)</li>
<h5>Developing the code</h5>
<li> Download the whole project into a desired folder</li>
<li> Open Eclipse and make sure the PyDev Plug-in is installed (one way to check it is if
you can switch to the Python Perspective from Window> Perspective> Other Perspective> Other> PyDev)
<li> On the project explorer, right click and select Import> Existing project into workspace</li>
<h5>Structure of the Eclipse project</h5>
1) ROOT_FOLDER/<br>
2) ROOT_FOLDER/config/<br>
3) ROOT_FOLDER/models/<br>
4) ROOT_FOLDER/src/config/<br>
5) ROOT_FOLDER/src/engines/<br>
6) ROOT_FOLDER/src/scripts/<br>
7) ROOT_FOLDER/src/utilsmee/<br>

Folder 2) stores .properties files with information about:
	a) the models to simulate,
	b) basic configuration for compilers

Folder 3) contains the models to be simulated

Folder 6) contains the three main scripts of the project, among other script for utilities:
	simulationDY.py for simulations using Dymola compiler
	simulationJM.py for simulations using JModelica compiler (does not work - in development)
	simulationOMC.py for simulations using OpenModelica compiler
	
Each script need two input files, where the XX indicates which compilers is being used. 
Indicate the input parameters in this order:
	simResourcesXX.properties
	simConfigurationXX.properties
</p>
