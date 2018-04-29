# Dragonfly: A Plugin for Climate Modeling (GPL) started by Chris Mackey <chris@ladybug.tools> 
# This file is part of Dragonfly.
#
# You should have received a copy of the GNU General Public License
# along with Dragonfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Use this component to generate boundary layer parameters that can be plugged into the "Dragonfly_Run Urban Weather Generator" component.  This component is mostly for climatologists, meteorologists and urban weather experts and probably does not have to be used for most simulations.
-
Provided by Dragonfly 0.0.02
    Args:
        dayBndLayerHeight_: A number that represents the height in meters of the urban boundary layer during the daytime. This is the height to which the urban meterorological conditions are stable and representative of the overall urban area. Typically, this boundary layer height increases with the height of the buildings.  The default is set to 700 meters.
        nightBndLayerHeight_: A number that represents the height in meters of the urban boundary layer during the nighttime. This is the height to which the urban meterorological conditions are stable and representative of the overall urban area. Typically, this boundary layer height increases with the height of the buildings.  The default is set to 800 meters.
        referenceHeight_: A number that represents the reference height at which the vertical profile of potential temperature is vertical. It is the height at which the profile of air temperature becomes stable. Can be determined by flying helium balloons equipped with temperature sensors and recording the air temperatures at different heights.  The default is set to 150 meters.
    Returns:
        boundLayerPar: A list of refernce EPW site parameters that can be plugged into the "Dragonfly_Run Urban Weather Generator" component.
"""

ghenv.Component.Name = "Dragonfly_Boundary Layer Parameters"
ghenv.Component.NickName = 'boundaryLayerPar'
ghenv.Component.Message = 'VER 0.0.02\nAPR_29_2018'
ghenv.Component.Category = "Dragonfly"
ghenv.Component.SubCategory = "01::UWG"
ghenv.Component.AdditionalHelpFromDocStrings = "5"

