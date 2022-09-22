# SphericalRieszSearch
Minimizes Riesz energy for N point on a d-dimensional sphere using projected gradient descent.


<table>
<tr>
<td>N=4</td><td>N=25</td><td>N=50</td>
</tr>
<tr>
<td><img src="4.gif" height="300" /></td><td><img src="25.gif" height="300" /></td><td><img src="50.gif" height="300" /></td>
</tr></center>
</table>

Dependencies
------------

SphericalRieszSearch involves the following Python libraries:

* Numpy 1.21.5
* Matplotlib 3.5.1
* Pytorch 1.10.2

An option has been included to leverage Pykeops for high N. This has many additional requirements, but can be turned off by setting use_keops to false in Riesz.py

*Pykeops PyKeops 1.5


Licence
-------

This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version.

This program is distributed in the hope that it will be useful, but WITHOUT 
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
this program. If not, see http://www.gnu.org/licenses/.
