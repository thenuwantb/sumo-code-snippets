import subprocess
import os

os.chdir('D:\\Thenuwan\\Coding\\SUMO_Python\\sumo_python\\4_Bus_priority_lane\\5_Real_Network_Cross_Junc_Dehiwala\\5_0_Wife_laptop_bus_flows')

command_sumo = 'sumo -c osm.sumocfg --vehroute-output 1_vehroutes_random_trips_galle_road.xml'

command_route_sampler = 'routeSampler.py -r 1_vehroutes_random_trips_galle_road.xml --edgedata-files rda_counts_2019_dehiwala.xml ' \
          ' -o 1_random_routes_match_rda_counts.rou.xml '
subprocess.run(command_sumo, shell=True)
subprocess.run(command_route_sampler, shell=True)